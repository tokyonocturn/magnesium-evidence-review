# Data dictionary

All datasets are UTF-8 CSV with a single header row. They are the source of truth
for the report; the Markdown tables under `docs/generated/` are rendered from them
by `analysis/build_tables.py`.

## `products.csv`

| Column | Type | Meaning |
| --- | --- | --- |
| `id` | slug | Stable identifier used in prose and tables. |
| `brand` | text | Brand name as sold. |
| `product` | text | Product and pack size. |
| `form` | enum | `bisglycinate`, `glycinate_chelate`, `citrate`, `oxide`, `malate`, `threonate`, `chloride`, `taurate`. |
| `format` | enum | `powder`, `tablets`, `capsules`. |
| `magnesium_mg_per_serving` | number | **Elemental** magnesium per label serving, not compound weight. |
| `servings_per_container` | integer | Label servings per pack. |
| `price_usd` | number | One-time retail price in US dollars, excluding tax and shipping. |
| `price_channel` | text | `Brand store` or `Retail listing`. |
| `price_date` | ISO date | Date the price was observed. |
| `price_source_url` | https URL | Page used for the price. |
| `certification` | enum | `NSF Certified for Sport`, `NSF Contents Certified`, `USP Verified`, `Informed Sport`, `None documented`. |
| `single_ingredient` | yes/no | Whether magnesium is the only active ingredient. |
| `other_ingredients` | text | Active co-ingredients, excipients where stated, or `None`. |
| `notes` | text | Provenance and caveats, including serving-size traps. |

### Derived fields (not stored in the CSV)

`analysis/build_tables.py` computes:

- `total_mg` = elemental magnesium per serving x servings per container
- `cost_per_100mg` = price x 100 / total_mg
- `cost_per_200mg` = price x 200 / total_mg
- `cost_per_400mg` = price x 400 / total_mg
- `cost_per_year_400` = cost per 400 mg x 365
- `days_supply_400` = total_mg / 400
- `servings_for_400` = 400 / magnesium per serving
- `exceeds_ul` = elemental magnesium per serving is greater than 350 mg

Cost is expressed per **400 mg of elemental magnesium**, close to the adult RDA
and a common daily dose. Because the metric is elemental magnesium, a 400 mg oxide
tablet is directly comparable with a 200 mg citrate capsule taken twice. This is
the only fair way to compare products that differ in salt mass.

## `evidence.csv`

| Column | Meaning |
| --- | --- |
| `id` | Stable evidence-row identifier. |
| `domain` | `forms`, `sleep`, `muscle`, `cramps`, `recovery`, `anxiety`, `migraine`, `cardiovascular`, `cognition`, `status`, `dosing`, `safety`, `quality`. |
| `question` | The practical question being answered. |
| `outcome` | The measured outcome. |
| `population` | Who was studied. |
| `evidence_type` | Design of the evidence base. |
| `studies_participants` | Number of studies and participants where reported. |
| `pooled_effect` | The estimate, in the units used by the source. |
| `effect_measure` | Unit or scale for the estimate. |
| `ci` | Confidence interval where reported. |
| `certainty` | GRADE-style certainty: `High`, `Moderate`, `Low`, `Very low`, `Not graded`. |
| `status` | `Established`, `Emerging`, `Mixed`, `Unsupported`. |
| `source_ids` | Semicolon-separated reference IDs. |
| `notes` | Caveats. |

## `claims.csv`

| Column | Meaning |
| --- | --- |
| `id` | Stable claim identifier. |
| `claim` | The claim as commonly stated. |
| `category` | `Formulation`, `Performance`, `Safety`, or `Cost`. |
| `verdict` | `Supported`, `Partially supported`, `Unsupported`, `False`. |
| `explanation` | What the evidence actually shows. |
| `source_ids` | Semicolon-separated reference IDs. |

`Partially supported` means a kernel of truth exists but the claim as commonly
stated overstates it. `False` is reserved for claims that are contradicted by the
cited evidence, not merely unproven.

## `references.csv`

| Column | Meaning |
| --- | --- |
| `id` | `R01`-style identifier used in every other dataset. |
| `authors` | Author list as transcribed; `Not transcribed` when the record was checked only by title. |
| `year` | Publication year. |
| `title` | Article or programme title. |
| `journal` | Journal, publisher, or programme. |
| `identifier` | DOI, PMID/PMC, or report number where available. |
| `url` | Stable https link to the record used. |
| `type` | Evidence type. |

## Certainty scheme

Certainty is a judgement, not a statistical output. It combines risk of bias,
inconsistency, indirectness, imprecision and publication bias, following GRADE
logic:

- **High**: further research is unlikely to change confidence in the estimate.
- **Moderate**: further research may change the estimate and could change the conclusion.
- **Low**: further research is likely to change the estimate.
- **Very low**: the estimate is very uncertain.

`Status` is separate and describes the state of the claim, not its certainty:
a small but real effect can be `Established` with `Moderate` certainty, while a
plausible mechanism supported only by pilot data is `Emerging` with `Very low`
certainty.
