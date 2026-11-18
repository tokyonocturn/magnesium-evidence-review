#!/usr/bin/env python3
"""Validate the magnesium review datasets and regenerate every derived table.

The repository treats the CSV files in ``data/`` as the source of truth. This
script performs schema and arithmetic checks, computes cost-per-elemental-dose
metrics, calculates salt chemistry from molar masses, and renders the Markdown
tables used by the documentation.

Usage
-----
    python analysis/build_tables.py           # validate and regenerate
    python analysis/build_tables.py --check   # validate; fail if outputs stale

Only the Python standard library is required (Python 3.10+).
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import sys
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
GEN = ROOT / "docs" / "generated"

MG = 24.305

# Salt chemistry. Hydrated entries are listed separately because the elemental
# fraction of a hydrate is much lower than the anhydrous figure, and labels rarely
# say which one they use.
CHEMISTRY = [
    ("Magnesium oxide", "MgO", 40.304, "anhydrous"),
    ("Magnesium hydroxide", "Mg(OH)2", 58.320, "anhydrous"),
    ("Magnesium carbonate", "MgCO3", 84.314, "anhydrous"),
    ("Magnesium citrate (trimagnesium dicitrate)", "Mg3(C6H5O7)2", 451.11, "anhydrous"),
    ("Magnesium hydrogen citrate (1:1)", "C6H6MgO7", 214.41, "anhydrous"),
    ("Magnesium malate", "MgC4H4O5", 156.38, "anhydrous"),
    ("Magnesium malate dihydrate", "MgC4H4O5.2H2O", 192.41, "dihydrate"),
    ("Magnesium bisglycinate", "Mg(C2H4NO2)2", 172.42, "anhydrous"),
    ("Magnesium chloride", "MgCl2", 95.21, "anhydrous"),
    ("Magnesium chloride hexahydrate", "MgCl2.6H2O", 203.30, "hexahydrate"),
    ("Magnesium sulfate", "MgSO4", 120.37, "anhydrous"),
    ("Magnesium sulfate heptahydrate (Epsom salt)", "MgSO4.7H2O", 246.48, "heptahydrate"),
    ("Magnesium lactate", "Mg(C3H5O3)2", 202.45, "anhydrous"),
    ("Magnesium lactate dihydrate", "Mg(C3H5O3)2.2H2O", 238.48, "dihydrate"),
    ("Magnesium taurate", "Mg(C2H6NO3S)2", 272.57, "anhydrous"),
    ("Magnesium L-threonate", "Mg(C4H7O5)2", 294.50, "anhydrous"),
    ("Magnesium aspartate", "Mg(C4H6NO4)2", 288.49, "bis(hydrogen aspartate)"),
    ("Magnesium orotate", "Mg(C5H3N2O4)2", 334.48, "anhydrous"),
    ("Magnesium gluconate", "Mg(C6H11O7)2", 414.60, "anhydrous"),
]

FORMS = {
    "bisglycinate",
    "glycinate_chelate",
    "citrate",
    "oxide",
    "malate",
    "threonate",
    "chloride",
    "taurate",
}
FORM_ORDER = [
    "oxide",
    "citrate",
    "malate",
    "bisglycinate",
    "glycinate_chelate",
    "taurate",
    "chloride",
    "threonate",
]
FORM_LABELS = {
    "bisglycinate": "Bisglycinate",
    "glycinate_chelate": "Glycinate chelate",
    "citrate": "Citrate",
    "oxide": "Oxide",
    "malate": "Malate",
    "threonate": "L-threonate",
    "chloride": "Chloride",
    "taurate": "Taurate",
}
FORMATS = {"powder", "tablets", "capsules"}
CERTIFICATIONS = {
    "NSF Certified for Sport",
    "NSF Contents Certified",
    "USP Verified",
    "Informed Sport",
    "None documented",
}
DOMAINS = {
    "forms",
    "sleep",
    "muscle",
    "cramps",
    "recovery",
    "anxiety",
    "migraine",
    "cardiovascular",
    "cognition",
    "status",
    "dosing",
    "safety",
    "quality",
}
CERTAINTY = {"High", "Moderate", "Low", "Very low", "Not graded"}
EVIDENCE_STATUS = {"Established", "Emerging", "Mixed", "Unsupported"}
VERDICTS = {"Supported", "Partially supported", "Unsupported", "False"}
CLAIM_CATEGORIES = {"Formulation", "Performance", "Safety", "Cost"}

PRODUCT_COLUMNS = [
    "id",
    "brand",
    "product",
    "form",
    "format",
    "magnesium_mg_per_serving",
    "servings_per_container",
    "price_usd",
    "price_channel",
    "price_date",
    "price_source_url",
    "certification",
    "single_ingredient",
    "other_ingredients",
    "notes",
]
EVIDENCE_COLUMNS = [
    "id",
    "domain",
    "question",
    "outcome",
    "population",
    "evidence_type",
    "studies_participants",
    "pooled_effect",
    "effect_measure",
    "ci",
    "certainty",
    "status",
    "source_ids",
    "notes",
]
CLAIM_COLUMNS = ["id", "claim", "category", "verdict", "explanation", "source_ids"]
REFERENCE_COLUMNS = ["id", "authors", "year", "title", "journal", "identifier", "url", "type"]

URL_RE = re.compile(r"^https://\S+$")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{2,60}$")
REF_ID_RE = re.compile(r"^R\d{2}$")

UL_MG = 350.0
COMPARISON_DOSE_MG = 400.0


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def read_csv(path: Path, columns: list[str], report: Report) -> list[dict[str, str]]:
    if not path.exists():
        report.error(f"{path.relative_to(ROOT)}: file is missing")
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        header = reader.fieldnames or []
        missing = [c for c in columns if c not in header]
        if missing:
            report.error(f"{path.name}: missing columns {missing}")
            return []
        rows = []
        for line, row in enumerate(reader, start=2):
            cleaned = {(k or "").strip(): (v or "").strip() for k, v in row.items()}
            cleaned["_line"] = str(line)
            rows.append(cleaned)
    if not rows:
        report.error(f"{path.name}: no data rows")
    return rows


def as_float(row: dict[str, str], field: str, report: Report) -> float:
    raw = row.get(field, "")
    try:
        return float(raw)
    except (TypeError, ValueError):
        report.error(f"{row.get('id', '?')}: {field} must be numeric, got {raw!r}")
        return float("nan")


def as_int(row: dict[str, str], field: str, report: Report) -> int:
    value = as_float(row, field, report)
    if value != value:
        return 0
    if abs(value - round(value)) > 1e-9:
        report.error(f"{row.get('id', '?')}: {field} must be a whole number")
    return int(round(value))


def load_products(report: Report) -> list[dict[str, object]]:
    rows = read_csv(DATA / "products.csv", PRODUCT_COLUMNS, report)
    seen: set[str] = set()
    products: list[dict[str, object]] = []
    today = dt.date.today()

    for row in rows:
        pid = row["id"]
        if not ID_RE.match(pid):
            report.error(f"{pid or '(blank)'}: id must be lowercase slug text")
        if pid in seen:
            report.error(f"{pid}: duplicate product id")
        seen.add(pid)

        if row["form"] not in FORMS:
            report.error(f"{pid}: form {row['form']!r} not in {sorted(FORMS)}")
        if row["format"] not in FORMATS:
            report.error(f"{pid}: format {row['format']!r} not in {sorted(FORMATS)}")
        if row["certification"] not in CERTIFICATIONS:
            report.error(f"{pid}: certification {row['certification']!r} is not an allowed value")
        if row["single_ingredient"] not in {"yes", "no"}:
            report.error(f"{pid}: single_ingredient must be yes or no")
        if row["price_channel"] not in {"Brand store", "Retail listing"}:
            report.error(f"{pid}: price_channel must be 'Brand store' or 'Retail listing'")
        if not URL_RE.match(row["price_source_url"]):
            report.error(f"{pid}: price_source_url must be an https URL")

        try:
            price_date = dt.date.fromisoformat(row["price_date"])
            if price_date > today:
                report.error(f"{pid}: price_date is in the future")
        except ValueError:
            report.error(f"{pid}: price_date must be ISO YYYY-MM-DD")
            price_date = today

        mg = as_float(row, "magnesium_mg_per_serving", report)
        servings = as_int(row, "servings_per_container", report)
        price = as_float(row, "price_usd", report)

        if mg < 20 or mg > 1_000:
            report.error(f"{pid}: magnesium per serving outside plausible range (20-1000 mg)")
        if servings <= 0:
            report.error(f"{pid}: servings_per_container must be positive")
        if price <= 1:
            report.error(f"{pid}: price_usd must be greater than 1")

        if mg != mg or servings == 0 or price != price or price <= 0 or mg <= 0:
            continue

        total_mg = mg * servings
        cost_per_100 = price * 100 / total_mg
        cost_per_400 = price * COMPARISON_DOSE_MG / total_mg
        products.append(
            {
                **row,
                "mg": mg,
                "servings": servings,
                "price": price,
                "total_mg": total_mg,
                "cost_per_100mg": cost_per_100,
                "cost_per_200mg": cost_per_100 * 2,
                "cost_per_400mg": cost_per_400,
                "cost_per_year_400": cost_per_400 * 365,
                "days_supply_400": total_mg / COMPARISON_DOSE_MG,
                "servings_for_400": COMPARISON_DOSE_MG / mg,
                "exceeds_ul": mg > UL_MG,
                "price_date_value": price_date,
            }
        )

    products.sort(key=lambda p: float(p["cost_per_400mg"]))
    for rank, product in enumerate(products, start=1):
        product["rank"] = rank
    return products


def load_evidence(report: Report, ref_ids: set[str]) -> list[dict[str, str]]:
    rows = read_csv(DATA / "evidence.csv", EVIDENCE_COLUMNS, report)
    seen: set[str] = set()
    for row in rows:
        eid = row["id"]
        if not ID_RE.match(eid):
            report.error(f"{eid or '(blank)'}: evidence id must be lowercase slug text")
        if eid in seen:
            report.error(f"{eid}: duplicate evidence id")
        seen.add(eid)
        if row["domain"] not in DOMAINS:
            report.error(f"{eid}: unknown domain {row['domain']!r}")
        if row["certainty"] not in CERTAINTY:
            report.error(f"{eid}: unknown certainty {row['certainty']!r}")
        if row["status"] not in EVIDENCE_STATUS:
            report.error(f"{eid}: unknown status {row['status']!r}")
        ids = [s for s in row["source_ids"].split(";") if s]
        if not ids:
            report.error(f"{eid}: at least one source id is required")
        for ref in ids:
            if ref not in ref_ids:
                report.error(f"{eid}: source id {ref} is not in references.csv")
    return rows


def load_claims(report: Report, ref_ids: set[str]) -> list[dict[str, str]]:
    rows = read_csv(DATA / "claims.csv", CLAIM_COLUMNS, report)
    seen: set[str] = set()
    for row in rows:
        cid = row["id"]
        if not ID_RE.match(cid):
            report.error(f"{cid or '(blank)'}: claim id must be lowercase slug text")
        if cid in seen:
            report.error(f"{cid}: duplicate claim id")
        seen.add(cid)
        if row["verdict"] not in VERDICTS:
            report.error(f"{cid}: unknown verdict {row['verdict']!r}")
        if row["category"] not in CLAIM_CATEGORIES:
            report.error(f"{cid}: unknown category {row['category']!r}")
        ids = [s for s in row["source_ids"].split(";") if s]
        if not ids:
            report.error(f"{cid}: at least one source id is required")
        for ref in ids:
            if ref not in ref_ids:
                report.error(f"{cid}: source id {ref} is not in references.csv")
    return rows


def load_references(report: Report) -> tuple[list[dict[str, str]], set[str]]:
    rows = read_csv(DATA / "references.csv", REFERENCE_COLUMNS, report)
    seen: set[str] = set()
    for row in rows:
        rid = row["id"]
        if not REF_ID_RE.match(rid):
            report.error(f"{rid or '(blank)'}: reference id must match R00")
        if rid in seen:
            report.error(f"{rid}: duplicate reference id")
        seen.add(rid)
        if not URL_RE.match(row["url"]):
            report.error(f"{rid}: url must be an https URL")
        if not row["title"] or not row["journal"]:
            report.error(f"{rid}: title and journal are required")
        if not row["year"].isdigit() or not (1900 <= int(row["year"]) <= 2100):
            report.error(f"{rid}: year must be a four-digit year")
    return rows, seen


def money(value: object) -> str:
    return f"${float(value):.2f}"


def load_chemistry() -> list[dict[str, object]]:
    table = []
    for name, formula, mass, hydration in CHEMISTRY:
        fraction = MG / mass
        table.append(
            {
                "name": name,
                "formula": formula,
                "mass": mass,
                "hydration": hydration,
                "fraction": fraction,
                "compound_mg_per_100mg": 100 / fraction,
                "compound_g_per_400mg": 400 / fraction / 1000,
            }
        )
    return table


def render_forms(chemistry: list[dict[str, object]], products: list[dict[str, object]]) -> str:
    lines = [
        "<!-- Generated by analysis/build_tables.py. Do not edit by hand. -->",
        "",
        "# Elemental magnesium and salt chemistry",
        "",
        "Every percentage below is calculated from the molecular formula and standard",
        "atomic masses, not copied from a label. The hydrated entries matter: a label",
        "that says only 'magnesium citrate' may be selling the anhydrous salt (16.2% Mg)",
        "or a hydrated or monobasic form (about 11.3% Mg), a 30% difference in what the",
        "dose delivers.",
        "",
        "| Salt | Formula | Molar mass (g/mol) | Hydration | Elemental Mg | Compound for 100 mg Mg | Compound for 400 mg Mg |",
        "| --- | --- | ---: | --- | ---: | ---: | ---: |",
    ]
    for c in chemistry:
        lines.append(
            "| {name} | {formula} | {mass:.2f} | {hydration} | {pct:.1f}% | {per100:.0f} mg | {per400:.2f} g |".format(
                name=c["name"],
                formula=c["formula"],
                mass=c["mass"],
                hydration=c["hydration"],
                pct=c["fraction"] * 100,
                per100=c["compound_mg_per_100mg"],
                per400=c["compound_g_per_400mg"],
            )
        )

    lines += [
        "",
        "## What one capsule actually contains",
        "",
        "A 500 mg capsule of a bulky salt cannot hold 500 mg of magnesium. The table",
        "shows how many 500 mg capsules are needed to reach 200 mg of elemental",
        "magnesium, a typical single dose.",
        "",
        "| Salt | Elemental Mg in a 500 mg capsule | 500 mg capsules for 200 mg Mg |",
        "| --- | ---: | ---: |",
    ]
    for c in chemistry:
        per_cap = 500 * float(c["fraction"])
        caps = 200 / per_cap
        lines.append(f"| {c['name']} | {per_cap:.0f} mg | {caps:.1f} |")

    lines += [
        "",
        "## Label arithmetic traps",
        "",
        "- **Compound weight versus elemental weight.** 1000 mg of magnesium oxide",
        "  contains 603 mg of magnesium; 1000 mg of magnesium bisglycinate contains 141 mg.",
        "  Comparing those two numbers as if they were doses is the single most common",
        "  error in magnesium marketing.",
        "- **Hydration.** Magnesium chloride is 25.5% magnesium anhydrous but 12.0% as the",
        "  hexahydrate. Magnesium sulfate is 20.2% anhydrous but 9.9% as the heptahydrate",
        "  (Epsom salt).",
        "- **Serving size.** A bottle may say '400 mg' on the front and define a serving as",
        "  two tablets, so one tablet is 200 mg.",
        "- **Blends.** When a label lists five salts and one total magnesium figure, the",
        "  contribution of each salt is unknown and cannot be checked against the chemistry.",
        "",
        "## Products in this sample that exceed the supplemental upper limit",
        "",
        f"The tolerable upper intake level for supplemental magnesium is {UL_MG:.0f} mg/day",
        "for adults. The products below exceed it in a single label serving.",
        "",
        "| Product | Form | Elemental Mg per serving |",
        "| --- | --- | ---: |",
    ]
    over = [p for p in products if p["exceeds_ul"]]
    for p in over:
        lines.append(
            f"| {p['brand']} {p['product']} | {FORM_LABELS[str(p['form'])]} | {float(p['mg']):.0f} mg |"
        )
    if not over:
        lines.append("| None | | |")
    lines.append("")
    return "\n".join(lines)


def render_products(products: list[dict[str, object]]) -> str:
    lines = [
        "<!-- Generated by analysis/build_tables.py. Do not edit by hand. -->",
        "",
        "# Brand and product comparison tables",
        "",
        "Prices are US one-time retail snapshots collected on the date in",
        "`data/products.csv`; they exclude tax and shipping and will change. Cost is",
        "normalised to **400 mg of elemental magnesium**, which makes a 400 mg oxide",
        "tablet comparable with two 200 mg citrate capsules.",
        "",
        f"Products: **{len(products)}**. Price snapshot: "
        f"{min(p['price_date_value'] for p in products)}.",
        "",
        "## All products ranked by cost per 400 mg elemental magnesium",
        "",
        "| Rank | Brand | Product | Form | Format | Mg/serving | Servings | Pack price | Cost/400 mg | Cost/year | Days at 400 mg | Certification |",
        "| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for p in products:
        lines.append(
            "| {rank} | {brand} | {product} | {form} | {fmt} | {mg:.0f} mg | {srv} | {price} | {c400} | {cy} | {days:.0f} | {cert} |".format(
                rank=p["rank"],
                brand=p["brand"],
                product=p["product"],
                form=FORM_LABELS[str(p["form"])],
                fmt=p["format"],
                mg=float(p["mg"]),
                srv=p["servings"],
                price=money(p["price"]),
                c400=money(p["cost_per_400mg"]),
                cy=money(p["cost_per_year_400"]),
                days=float(p["days_supply_400"]),
                cert=p["certification"],
            )
        )

    cheapest = products[0]
    priciest = products[-1]
    certified = [p for p in products if p["certification"] != "None documented"]
    powders = [p for p in products if p["format"] == "powder"]

    lines += [
        "",
        "## Value summary",
        "",
        "| Metric | Product | Cost per 400 mg | Cost per year |",
        "| --- | --- | ---: | ---: |",
        f"| Cheapest overall | {cheapest['brand']} {cheapest['product']} | {money(cheapest['cost_per_400mg'])} | {money(cheapest['cost_per_year_400'])} |",
        f"| Most expensive | {priciest['brand']} {priciest['product']} | {money(priciest['cost_per_400mg'])} | {money(priciest['cost_per_year_400'])} |",
    ]
    if powders:
        cheapest_powder = min(powders, key=lambda p: float(p["cost_per_400mg"]))
        lines.append(
            f"| Cheapest powder | {cheapest_powder['brand']} {cheapest_powder['product']} | {money(cheapest_powder['cost_per_400mg'])} | {money(cheapest_powder['cost_per_year_400'])} |"
        )
    if certified:
        certified_sorted = sorted(certified, key=lambda p: float(p["cost_per_400mg"]))
        best = certified_sorted[0]
        lines.append(
            f"| Cheapest certified | {best['brand']} {best['product']} ({best['certification']}) | {money(best['cost_per_400mg'])} | {money(best['cost_per_year_400'])} |"
        )

    multiple = float(priciest["cost_per_400mg"]) / float(cheapest["cost_per_400mg"])
    lines += [
        "",
        f"The price range spans **{multiple:.0f}x**, from {money(cheapest['cost_per_400mg'])}",
        f"to {money(priciest['cost_per_400mg'])} per 400 mg of elemental magnesium.",
        "",
        "## Median cost by form",
        "",
        "| Form | Products | Median cost/400 mg | Range |",
        "| --- | ---: | ---: | --- |",
    ]
    for form in FORM_ORDER:
        group = [p for p in products if p["form"] == form]
        if not group:
            continue
        costs = [float(p["cost_per_400mg"]) for p in group]
        lines.append(
            f"| {FORM_LABELS[form]} | {len(group)} | {money(median(costs))} | {money(min(costs))} - {money(max(costs))} |"
        )

    lines += [
        "",
        "## Cost of a 30-day course at 400 mg/day",
        "",
        "| Product | Servings needed for 400 mg | Cost per day | Cost per 30 days |",
        "| --- | ---: | ---: | ---: |",
    ]
    for p in products:
        lines.append(
            f"| {p['brand']} {p['product']} | {float(p['servings_for_400']):.2f} | {money(p['cost_per_400mg'])} | {money(float(p['cost_per_400mg']) * 30)} |"
        )

    lines += [
        "",
        "## Certification",
        "",
        "Certification verifies identity, strength and contaminant limits; it does not",
        "change the molecule or prove efficacy. Only products with a documented programme",
        "are listed here.",
        "",
        "| Brand | Product | Certification | Cost/400 mg |",
        "| --- | --- | --- | ---: |",
    ]
    for p in sorted(certified, key=lambda x: float(x["cost_per_400mg"])):
        lines.append(
            f"| {p['brand']} | {p['product']} | {p['certification']} | {money(p['cost_per_400mg'])} |"
        )
    if not certified:
        lines.append("| None documented in this sample | | | |")

    lines += [
        "",
        "## Data quality flags",
        "",
    ]
    uncertified = len(products) - len(certified)
    blends = [p for p in products if p["single_ingredient"] == "no"]
    over = [p for p in products if p["exceeds_ul"]]
    lines.append(f"- {uncertified} of {len(products)} products have no documented third-party certification.")
    lines.append(f"- {len(blends)} of {len(products)} products contain active co-ingredients besides magnesium.")
    lines.append(f"- {len(over)} of {len(products)} products exceed the 350 mg supplemental upper limit in one serving.")
    lines.append("- Prices are snapshots, not live quotes; re-check the source URL before buying.")
    lines.append("")
    return "\n".join(lines)


def render_evidence(evidence: list[dict[str, str]]) -> str:
    titles = {
        "forms": "Forms, chemistry and absorption",
        "sleep": "Sleep",
        "muscle": "Muscle function and performance",
        "cramps": "Muscle cramps",
        "recovery": "Exercise recovery and soreness",
        "anxiety": "Anxiety, stress and mood",
        "migraine": "Migraine",
        "cardiovascular": "Blood pressure and cardiovascular health",
        "cognition": "Cognition",
        "status": "Deficiency and status assessment",
        "dosing": "Recommended intake and upper limits",
        "safety": "Safety, toxicity and interactions",
        "quality": "Product quality and labelling",
    }
    lines = [
        "<!-- Generated by analysis/build_tables.py. Do not edit by hand. -->",
        "",
        "# Evidence tables",
        "",
        "Certainty reflects the strength and consistency of the underlying evidence",
        "(GRADE-style judgement), not the size of the effect. `Status` separates",
        "established findings from emerging or unsupported ones. A real but tiny",
        "effect can be established and still be clinically unimportant.",
        "",
    ]
    for domain in titles:
        subset = [e for e in evidence if e["domain"] == domain]
        if not subset:
            continue
        lines += [
            f"## {titles[domain]}",
            "",
            "| Question | Outcome | Evidence base | Result | Certainty | Status | Sources |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
        for e in subset:
            effect = e["pooled_effect"]
            if e["ci"]:
                effect = f"{effect} ({e['ci']})"
            base = e["evidence_type"]
            detail = e["studies_participants"]
            if detail and detail.lower() not in base.lower():
                base = f"{base}; {detail}"
            sources = ", ".join(e["source_ids"].split(";"))
            lines.append(
                f"| {e['question']} | {e['outcome']} | {base} | {effect} | {e['certainty']} | {e['status']} | {sources} |"
            )
        lines.append("")
    return "\n".join(lines)


def render_claims(claims: list[dict[str, str]]) -> str:
    lines = [
        "<!-- Generated by analysis/build_tables.py. Do not edit by hand. -->",
        "",
        "# Claim adjudication table",
        "",
        "Every claim below was checked against the cited evidence. `Partially supported`",
        "means a kernel of truth exists but the claim as commonly stated overstates it.",
        "`False` is reserved for claims the evidence contradicts, not merely claims that",
        "are unproven.",
        "",
        "| # | Claim | Category | Verdict | What the evidence shows | Sources |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for i, c in enumerate(claims, start=1):
        lines.append(
            f"| {i} | {c['claim']} | {c['category']} | **{c['verdict']}** | {c['explanation']} | {', '.join(c['source_ids'].split(';'))} |"
        )
    lines.append("")

    counts = {v: 0 for v in sorted(VERDICTS)}
    for c in claims:
        counts[c["verdict"]] += 1
    lines += [
        "## Verdict summary",
        "",
        "| Verdict | Claims |",
        "| --- | ---: |",
    ]
    for verdict, count in counts.items():
        lines.append(f"| {verdict} | {count} |")
    lines.append("")
    return "\n".join(lines)


def render_references(refs: list[dict[str, str]]) -> str:
    lines = [
        "<!-- Generated by analysis/build_tables.py. Do not edit by hand. -->",
        "",
        "# References",
        "",
        "Identifiers resolve to the publisher record. Where an author list was not",
        "transcribed, `Not transcribed` is shown and the title plus DOI, PMID or stable",
        "URL identifies the record. All records were accessed in November 2026.",
        "",
    ]
    for ref in sorted(refs, key=lambda r: r["id"]):
        authors = ref["authors"].strip()
        prefix = f"{authors} " if authors else ""
        identifier = ref["identifier"].strip()
        ident = f" {identifier}." if identifier else ""
        lines.append(
            f"- **[{ref['id']}]** {prefix}({ref['year']}). *{ref['title']}*. {ref['journal']}.{ident} <{ref['url']}>"
        )
    lines.append("")
    return "\n".join(lines)


def check_doc_links(report: Report) -> None:
    candidates = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "CHANGELOG.md"]
    candidates += sorted((ROOT / "docs").rglob("*.md"))
    candidates += sorted((ROOT / "report").rglob("*.md"))
    for path in candidates:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative = target.split("#", 1)[0]
            if not relative:
                continue
            if not (path.parent / relative).exists():
                report.error(f"{path.relative_to(ROOT)}: broken relative link {target!r}")


def write_outputs(outputs: dict[Path, str]) -> None:
    GEN.mkdir(parents=True, exist_ok=True)
    for path, text in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args()

    report = Report()
    refs, ref_ids = load_references(report)
    products = load_products(report)
    evidence = load_evidence(report, ref_ids)
    claims = load_claims(report, ref_ids)
    chemistry = load_chemistry()
    check_doc_links(report)

    for p in products:
        if p["exceeds_ul"]:
            report.warn(
                f"{p['id']}: {float(p['mg']):.0f} mg per serving exceeds the 350 mg supplemental UL"
            )
    if len(evidence) < 40:
        report.warn("evidence dataset is small; the review is meant to cover every domain")

    outputs = {
        GEN / "brand-comparison.md": render_products(products),
        GEN / "forms-chemistry.md": render_forms(chemistry, products),
        GEN / "evidence-tables.md": render_evidence(evidence),
        GEN / "claims-table.md": render_claims(claims),
        ROOT / "docs" / "references.md": render_references(refs),
    }

    if args.check:
        for path, text in outputs.items():
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                report.error(f"{path.relative_to(ROOT)}: generated output is stale; run python analysis/build_tables.py")
    else:
        write_outputs(outputs)

    print("Magnesium evidence repository validation")
    print(f"  products:   {len(products)}")
    print(f"  evidence:   {len(evidence)} rows")
    print(f"  claims:     {len(claims)} rows")
    print(f"  references: {len(refs)} entries")
    print(f"  warnings:   {len(report.warnings)}")
    print(f"  errors:     {len(report.errors)}")
    for warning in report.warnings:
        print(f"  WARN  {warning}")
    for error in report.errors:
        print(f"  ERROR {error}", file=sys.stderr)
    if report.errors:
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
