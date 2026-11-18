# Methodology

This repository is a structured, source-linked review, not a systematic review
conducted under PRISMA registration. It aims to be reproducible and auditable:
every number in the report comes from a row in `data/`, and every table is
generated from those rows.

## 1. Questions

The review was organised around six questions:

1. How do commercial magnesium forms differ in elemental content, solubility,
   absorption and gastrointestinal tolerance?
2. Which claimed benefits are supported by controlled human evidence, and how large
   are the effects?
3. Who is at risk of magnesium inadequacy, and what can status testing tell us?
4. What doses are effective, what is the upper limit, and where is the safety
   margin?
5. How do products differ in transparency, testing and cost per elemental dose?
6. Who should supplement, who should not, and how should a formulation be chosen?

## 2. Search strategy

Sources were located through targeted searches of PubMed/PMC, Cochrane, the NIH
Office of Dietary Supplements, FDA safety communications, national guideline
documents, and independent product-testing organisations. Search terms combined
`magnesium` with each form (`oxide`, `citrate`, `glycinate`, `bisglycinate`,
`malate`, `taurate`, `threonate`, `chloride`, `sulfate`, `lactate`, `aspartate`,
`orotate`, `gluconate`) and each outcome (`sleep`, `insomnia`, `cramp`, `muscle`,
`strength`, `recovery`, `soreness`, `anxiety`, `stress`, `depression`, `migraine`,
`blood pressure`, `cardiovascular`, `cognition`), plus `bioavailability`,
`deficiency`, `hypomagnesemia`, `hypermagnesemia`, `kidney`, `interaction`,
`labelling`, `contamination` and `certification`.

Searches were run in November 2026. Reference lists of included reviews were checked
for additional trials.

## 3. Inclusion and exclusion

**Included:**

- randomised controlled trials in humans;
- systematic reviews and meta-analyses of RCTs;
- national intake recommendations and upper limits;
- regulatory safety communications and pharmacopoeial standards;
- peer-reviewed label-accuracy and bioavailability studies;
- cohort studies, used only for aetiology and clearly labelled as observational;
- independent product-testing reports and certifier documentation.

**Excluded from efficacy claims:**

- animal and in vitro studies, except to explain mechanism (labelled as such);
- narrative reviews used as evidence rather than as pointers to primary work;
- manufacturer marketing copy, which was used only for price and label facts;
- case reports, except for safety signals;
- conference abstracts without a full record.

**Language:** English.

## 4. Data extraction

Each evidence row records one question and one outcome, the population, the design,
the number of studies and participants, the effect in the units used by the source,
the confidence interval where reported, a certainty grade, a status, and at least
one reference.

Where two syntheses disagree, both are entered as separate rows and the discrepancy
is described in `notes` rather than averaged. The blood-pressure rows (R22, R23,
R24) are an example: three meta-analyses give different point estimates because of
different inclusion criteria and doses, and the review reports the range rather than
picking a favourite.

## 5. Certainty grading

Certainty follows GRADE logic and is a judgement, not a statistical output. It
combines risk of bias, inconsistency, indirectness, imprecision and publication
bias.

| Grade | Meaning |
| --- | --- |
| High | Further research is unlikely to change confidence in the estimate. |
| Moderate | Further research may change the estimate and could change the conclusion. |
| Low | Further research is likely to change the estimate. |
| Very low | The estimate is very uncertain. |

**Status** is separate:

- **Established:** multiple consistent trials or a meta-analysis, plausible
  mechanism, no serious unresolved contradiction.
- **Emerging:** human data exist but are small, inconsistent or very low certainty.
- **Mixed:** the pooled direction is unclear or depends on the outcome or population.
- **Unsupported:** the claim is marketed or repeated but not supported by controlled
  human evidence. This does not mean it has been proven false.

The two axes are deliberately independent. A small effect can be *established* and
still be clinically unimportant; the cramp result is the clearest example.

## 6. Claim adjudication

Claims were selected because they circulate publicly in marketing, retail copy or
popular health writing. Each is classified:

- **Supported:** the evidence supports the claim as stated.
- **Partially supported:** a kernel of truth exists but the claim overstates it.
- **Unsupported:** no controlled human evidence supports it.
- **False:** the evidence contradicts it.

`Partially supported` is not a diplomatic default. It is used only where the
mechanism or a subgroup effect is real but the general claim is too strong.

## 7. Price and product method

**Sampling.** Sixteen products were selected purposively to cover every major form,
both brand-store and retail channels, powder/tablet/capsule formats, and a range of
price points. This is not a random sample and should not be used to estimate market
averages.

**Price rules.**

- One-time retail price in USD, excluding tax, shipping, subscription discounts and
  coupons.
- Price observed on 18 November 2026 from the brand store or a named retailer.
- The source URL resolves to the page used.
- Where a page listed several pack sizes, the pack used is recorded in `notes`.

**Cost model.**

```
total elemental Mg per pack = Mg per serving x servings per container
cost per 100 mg           = price x 100 / total elemental Mg per pack
cost per 400 mg           = price x 400 / total elemental Mg per pack
cost per year at 400 mg   = cost per 400 mg x 365
servings needed for 400 mg = 400 / Mg per serving
```

The 400 mg denominator is close to the adult RDA and is a common daily dose. Using
**elemental** magnesium makes a 400 mg oxide tablet directly comparable with two
200 mg citrate capsules. Comparing pack prices or compound weights would not.

**Certification.** Recorded only when the brand page or the certifier's public
listing documents it. Absence is recorded as `None documented`, not as "uncertified"
in an absolute sense: a product may be certified without saying so on the page
used.

## 8. Salt chemistry

Elemental fractions are calculated in `analysis/build_tables.py` from the molecular
formula and standard atomic masses (Mg = 24.305 g/mol). Hydrated forms are modelled
separately because the elemental fraction of a hydrate is much lower and labels
rarely specify which form is used. Formulas and molar masses were cross-checked
against the published comparison in R10.

The chemistry table is a calculation, not a measurement. Real products may contain
hydrates, excess ligand, or blends that change the effective elemental content. That
is exactly why label-accuracy studies matter (R48).

## 9. Verification

The build script checks:

- required columns and allowed categorical values;
- unique IDs and resolvable cross-references between evidence, claims and
  references;
- plausible elemental dose, serving count and price;
- ISO price dates that are not in the future;
- https source URLs;
- broken relative Markdown links;
- that generated Markdown is byte-identical to what the data produces (`--check`).

The `--check` mode runs in CI on every push.

**What was checked by hand.** Effect sizes and confidence intervals were checked
against the abstract or results section of each cited record. Product prices and
elemental doses were checked against the product page. Chemistry was recalculated
rather than copied.

**What was not checked.** No new laboratory testing was commissioned. Contaminant
conclusions rely on published independent testing. No attempt was made to verify
that a product currently for sale matches the batch tested by a certifier.

## 10. Limitations

- **Not a systematic review.** No PRISMA registration, dual screening or formal
  risk-of-bias scoring. Certainty grades are judgements.
- **Publication and funding bias.** Many positive trials are small and
  industry-funded, especially for threonate and proprietary chelates.
- **Indirect form comparisons.** Most "best form" claims compare a form with oxide,
  not with each other.
- **Absorption measurement.** Urinary, serum and isotope methods answer different
  questions and disagree.
- **Price volatility.** Prices are snapshots. The relative spread is informative;
  the absolute figures will change.
- **Product sample.** Purposive, not random. The certification rate in this sample
  should not be generalised.
- **Guideline lag.** Recommendations such as the AAN/AHS Level B for migraine rest
  on a small evidence base.

## 11. AI-assistance disclosure

This review was assembled with AI assistance under human direction. Every numeric
claim was checked against the cited abstract, table or dataset, and the datasets and
generated tables are machine-validated. It has **not** been peer reviewed. Treat it
as a well-documented starting point, not a substitute for the primary literature or
clinical judgement.

## 12. Corrections

Open an issue with the claim, the source that contradicts it, and the proposed
change. Substantive corrections are recorded in `CHANGELOG.md` with the date and
the affected row. Generated tables are never edited by hand; they are rebuilt from
the CSVs and verified in CI.
