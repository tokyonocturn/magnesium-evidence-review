# Changelog

All notable changes to the datasets, generated tables, and report are recorded here.
The format follows Keep a Changelog; versions use semantic versioning.

## [1.0.0] - 2026-11-18

### Added

- Comprehensive scientific report covering body magnesium physiology, form
  chemistry, absorption and bioavailability, sleep, muscle function, cramps,
  recovery, anxiety and mood, migraine, cardiovascular health, cognition, bone and
  diabetes, deficiency and status testing, dosing, safety, drug interactions,
  product quality, certification, cost, and formulation selection.
- `data/products.csv`: 16 products priced on 2026-11-18 and normalised to cost per
  400 mg of elemental magnesium.
- `data/evidence.csv`: 70 graded evidence rows across 13 domains.
- `data/claims.csv`: 31 claims adjudicated as supported, partially supported,
  unsupported, or false.
- `data/references.csv`: 56 references with DOI, PMID/PMC or stable URL.
- `analysis/build_tables.py`: schema validation, cost model, salt chemistry
  including hydrates, generated Markdown, relative-link checking, and a `--check`
  mode for CI.
- GitHub Actions workflow that validates the datasets on every push.
- Practical dosage guide, safety assessment, formulation and quality review, and
  brand comparison.

### Notes

- Prices are US one-time retail snapshots and exclude tax and shipping.
- No new laboratory testing was commissioned; contamination conclusions rely on
  published independent testing and peer-reviewed market surveys.
- The review is AI-assisted and has not been peer reviewed. See
  `docs/methodology.md`.

## Correction policy

Substantive corrections are recorded here with the date, the affected row or claim,
and the source that justified the change. Generated tables are never edited by hand;
they are rebuilt from the CSVs and verified in CI.
