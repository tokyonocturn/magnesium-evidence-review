# Magnesium: An Independent Evidence Review and Product Database

A source-linked review of magnesium supplementation — which forms differ, what the
trials actually show, how to dose it, who should avoid it, and what 16 real products
cost per 400 mg of elemental magnesium. Built as a reproducible repository: every
quantitative claim traces to a reference, and every table is generated from the CSV
datasets in [`data/`](data/).

**No brand funding, affiliate links, or sponsorship.** Prices were collected in
November 2026 and will change.

---

## Bottom line

**Magnesium is essential, cheap to correct, and oversold.** The mineral matters;
most of the marketed benefits are small, limited to deficient or specific
populations, or unproven. Form matters less than dose, tolerance and whether you
actually need it.

| Question | Answer | Confidence |
| --- | --- | --- |
| Is low magnesium common? | **48% of Americans eat less than the EAR**, but symptomatic deficiency in healthy people is uncommon. Intake is not deficiency. | Moderate |
| Best-absorbed form? | Soluble salts (citrate, chloride, lactate, aspartate) beat **oxide** (~4% vs 9–11%). Glycinate matched oxide overall in the only direct trial, though it is gentler and better in malabsorption. Differences among the soluble salts are small and poorly studied. | Moderate |
| Is glycinate worth the premium? | For **tolerability**, often yes. For absorption, the only direct trial found glycinate equal to oxide overall. | Low–Moderate |
| Is threonate worth 10–37× more? | **No**, for magnesium replacement. Its cognitive case rests on small, mostly industry-funded trials. | Low |
| Does it help sleep? | Modestly in some older adults and poor sleepers: about **17 min faster sleep onset** in a pooled analysis of 3 small trials, low certainty. | Low |
| Does it stop cramps? | **No.** About **0.18 cramps/week** difference — not clinically meaningful. | Moderate |
| Does it prevent migraine? | Modestly, at **600 mg/day trimagnesium dicitrate** (AAN/AHS Level B). Above the supplemental UL. | Moderate |
| Does it lower blood pressure? | About **−2 mmHg systolic** overall; up to **−7.7 mmHg** in treated hypertensives. Little effect in normotensive people. | Moderate |
| Does it improve cognition? | **Not established** in healthy adults. Human brain magnesium has never been measured after oral threonate. | Low |
| Is it safe? | Yes with healthy kidneys at recommended doses. High doses cause diarrhoea; **kidney disease risks dangerous hypermagnesemia**. | High |
| How much? | **100–200 mg elemental per dose**, once or twice daily; total supplemental intake **≤350 mg/day** unless supervised. | Moderate |
| What does it cost? | **$0.08–$2.92 per 400 mg** of elemental magnesium — a **37× spread**. | Price snapshot |

The detailed argument, caveats and citations are in the
[full report](report/magnesium-scientific-report.md).

---

## What is in this repository

| Path | Contents |
| --- | --- |
| [`report/magnesium-scientific-report.md`](report/magnesium-scientific-report.md) | Comprehensive report: chemistry, absorption, every major outcome, deficiency, dosing, safety, quality, cost, selection. |
| [`docs/methodology.md`](docs/methodology.md) | Search strategy, inclusion rules, grading scheme, pricing method, verification, limitations, AI disclosure. |
| [`docs/forms-and-quality.md`](docs/forms-and-quality.md) | Form-by-form chemistry and absorption, label reading, certification, contaminants, formats. |
| [`docs/dosage-guide.md`](docs/dosage-guide.md) | RDA and UL tables, protocols by goal, timing, drug spacing, troubleshooting. |
| [`docs/safety-assessment.md`](docs/safety-assessment.md) | Risk-by-risk safety review: GI, hypermagnesemia, kidney, pregnancy, children, interactions, overdose. |
| [`docs/brand-comparison.md`](docs/brand-comparison.md) | How to read the product data, value tiers, serving-size traps, red flags. |
| [`docs/generated/brand-comparison.md`](docs/generated/brand-comparison.md) | Generated 16-product cost table, form medians, 30-day costs, certification. |
| [`docs/generated/forms-chemistry.md`](docs/generated/forms-chemistry.md) | Elemental content, molar masses, capsules needed per dose, UL flags. |
| [`docs/generated/evidence-tables.md`](docs/generated/evidence-tables.md) | 70 graded evidence rows across 13 domains. |
| [`docs/generated/claims-table.md`](docs/generated/claims-table.md) | 31 common claims adjudicated as supported, partial, unsupported or false. |
| [`docs/references.md`](docs/references.md) | 56 references with DOI, PMID/PMC or stable URL. |
| [`data/products.csv`](data/products.csv) | Product database (price, elemental dose, servings, certification, ingredients). |
| [`data/evidence.csv`](data/evidence.csv) | Evidence table with effect sizes, certainty and status. |
| [`data/claims.csv`](data/claims.csv) | Claim adjudication dataset. |
| [`data/references.csv`](data/references.csv) | Reference metadata. |
| [`data/data-dictionary.md`](data/data-dictionary.md) | Column definitions and grading scheme. |
| [`analysis/build_tables.py`](analysis/build_tables.py) | Validates the datasets, computes cost and chemistry, regenerates all tables. |

---

## Reproduce it

Requires Python 3.10+ and no third-party packages.

```bash
python analysis/build_tables.py           # validate + regenerate tables
python analysis/build_tables.py --check   # fail if data or tables are stale
```

The `--check` command runs in CI on every push
([`.github/workflows/validate.yml`](.github/workflows/validate.yml)). It verifies:

- required columns and allowed categorical values;
- unique IDs and resolvable cross-references between evidence, claims and references;
- plausible elemental dose, serving count and price;
- ISO price dates that are not in the future;
- that generated Markdown is byte-identical to what the data produces.

### Derived cost model

```
total elemental Mg per pack = Mg per serving x servings per container
cost per 400 mg             = price x 400 / total elemental Mg per pack
cost per year at 400 mg     = cost per 400 mg x 365
servings needed for 400 mg  = 400 / Mg per serving
```

Salt chemistry (elemental magnesium fraction of each salt, including hydrates) is
calculated in the same script from molar masses, not copied from marketing material.

---

## How the evidence was handled

- **Established** findings have multiple consistent RCTs or a meta-analysis, with a
  plausible mechanism and no serious unresolved contradiction.
- **Emerging** findings have human data but small samples, inconsistency, or very
  low certainty.
- **Mixed** means the pooled direction is unclear or depends on the outcome.
- **Unsupported** means the claim is marketed or repeated but is not supported by
  controlled human evidence.

Certainty is graded High / Moderate / Low / Very low using GRADE logic. The two axes
are deliberately separate: a real but tiny effect can be *established* and still be
clinically unimportant.

Full details, including how contradictions were resolved, are in
[`docs/methodology.md`](docs/methodology.md).

---

## What this review is not

- **Not medical advice.** Magnesium interacts with antibiotics, bisphosphonates,
  diuretics and PPIs, and accumulates in kidney disease. People with kidney
  impairment, who are pregnant or breastfeeding, or who take prescription medication
  should talk to a clinician.
- **Not a primary laboratory study.** Product-quality conclusions come from published
  independent testing (ConsumerLab, peer-reviewed market surveys) and certifier
  documentation; this project did not commission new assays.
- **Not exhaustive.** Sixteen products are a purposive sample across forms, formats
  and price tiers, not a census of the market.
- **Not free of uncertainty.** Much of the magnesium literature is small, short and
  industry-funded. Effect estimates should be read as best current approximations.

### AI-assistance disclosure

This review was assembled with AI assistance under human direction. Every numeric
claim was checked against the cited abstract, table or dataset; the datasets and
generated tables are machine-validated. It has **not** been peer reviewed. Treat it
as a well-documented starting point, not a substitute for the primary literature or
clinical judgement.

Corrections are welcome: open an issue with the claim, the source, and the proposed
change. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Citation and license

Citation metadata is in [`CITATION.cff`](CITATION.cff).

- **Text and data:** CC BY 4.0 — share and adapt with attribution.
- **Code:** MIT.

See [`NOTICE`](NOTICE) for the full content license and medical disclaimer.
