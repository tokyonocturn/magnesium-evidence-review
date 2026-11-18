# Magnesium Supplementation: An Independent Scientific Review

**Version 1.0.1, 18 November 2026**

A source-linked review of magnesium forms, absorption, clinical evidence, dosing,
safety, product quality and cost. Every quantitative claim traces to a reference
identifier (`R01`–`R56`) listed in [the references](../docs/references.md). All
generated tables are built from the datasets in [`data/`](../data/) by
[`analysis/build_tables.py`](../analysis/build_tables.py).

> **This is not medical advice.** Magnesium interacts with several prescription
> drugs and accumulates in kidney disease. People with kidney impairment, people
> taking diuretics or proton pump inhibitors, and anyone treating a medical
> condition should involve a clinician.

---

## 1. Bottom line

Magnesium is an essential mineral with a wide therapeutic margin in healthy
people. The commercial story around it, however, is inflated in predictable ways:
form superiority is oversold, benefits are borrowed from deficiency states and
applied to replete adults, and doses are printed as compound weight to look larger
than they are.

| Question | Answer | Confidence |
| --- | --- | --- |
| Is magnesium deficiency common? | Low **intake** is common (48% of Americans below the EAR), but symptomatic deficiency in healthy people is not. These are different things. | Moderate |
| Which form is best absorbed? | Soluble organic salts (citrate, glycinate, lactate, aspartate) beat oxide. The advantage over citrate is small and not clearly demonstrated between the organic forms. | Moderate |
| Is glycinate worth the premium? | For tolerability, often yes. For absorption, the evidence does not show superiority over citrate in healthy adults. | Low–Moderate |
| Is threonate worth 10–37× the price? | No, for magnesium replacement. Its cognitive case rests on small, mostly industry-funded trials with inconsistent results. | Low |
| Does it help sleep? | Modestly, in some older adults and poor sleepers: about 17 minutes faster sleep onset in a pooled analysis of three small trials. Certainty is low to very low. | Low |
| Does it stop cramps? | No. The pooled effect in older adults is about 0.18 cramps per week, not clinically meaningful. | Moderate |
| Does it prevent migraine? | Modestly, at 600 mg/day of trimagnesium dicitrate, with guideline support (AAN/AHS Level B). The dose exceeds the supplemental upper limit. | Moderate |
| Does it lower blood pressure? | By about 2 mmHg systolic overall; up to about 7.7 mmHg in treated hypertensives and people with low magnesium. Little effect in normotensive people. | Moderate |
| Does it improve cognition? | Not established in healthy adults. Human brain magnesium has never been measured after oral threonate. | Low |
| Is it safe? | Yes in healthy kidneys at recommended doses. High doses cause diarrhoea; kidney impairment risks dangerous hypermagnesemia. | High |
| What should most people take? | 100–200 mg elemental magnesium per dose, once or twice daily, as citrate or bisglycinate, only if intake or risk factors justify it. Total supplemental intake stays at or below 350 mg/day unless supervised. | Moderate |
| What does it cost? | **$0.08 to $2.92 per 400 mg** of elemental magnesium in this sample: a 37-fold spread for a mineral whose absorbed dose differs far less than that. | Price snapshot |

The detailed argument is in the sections below. The generated
[evidence tables](../docs/generated/evidence-tables.md) and
[claim adjudications](../docs/generated/claims-table.md) contain the full row-by-row
record.

---

## 2. Scope and method

This review asks six questions:

1. How do commercially available magnesium forms differ in elemental content,
   solubility, absorption and gastrointestinal tolerance?
2. Which claimed benefits are supported by controlled human evidence, and how
   large are they?
3. Who is actually at risk of inadequacy, and what can blood testing tell us?
4. What doses are effective, what is the upper limit, and where is the safety
   margin?
5. How do products differ in transparency, testing and cost per elemental dose?
6. Who should supplement, who should not, and how should a formulation be chosen?

**Inclusion.** Human trials, systematic reviews, meta-analyses, national intake
recommendations, regulatory safety communications, label records and independent
product testing were included. Animal and in vitro work is used only to explain
mechanism, and is labelled as such. Marketing pages were used for price and label
facts, never as evidence of efficacy.

**Grading.** Each evidence row carries a certainty grade (High, Moderate, Low,
Very low) and a status (Established, Emerging, Mixed, Unsupported). Certainty is a
GRADE-style judgement about the strength and consistency of the evidence; status
describes the state of the claim. A small effect can be established and still be
clinically unimportant; that distinction drives most of the conclusions here.

**Prices.** Sixteen products were priced on 18 November 2026 from the brand store
or a named retailer, excluding tax, shipping, subscription discounts and coupons.
Cost is normalised to 400 mg of **elemental** magnesium. This is the only
comparison that survives differences in salt mass and serving size.

**What this review did not do.** No new laboratory assays were commissioned.
Contaminant and label-accuracy conclusions rely on published independent testing
and peer-reviewed market surveys. The product set is a purposive sample across
forms and price tiers, not a census. Full limitations are in
[the methodology](../docs/methodology.md).

---

## 3. Magnesium in the body

An adult body contains about 25 g of magnesium. Roughly 50–60% is in bone, most of
the rest is intracellular in soft tissue, and **less than 1% is in serum** (R01).
Serum magnesium is held within a narrow range, about 0.75–0.95 mmol/L, and the
kidneys adjust urinary excretion to defend it (R01).

That distribution explains two things that shape the entire supplement market:

- **A blood test cannot see tissue depletion.** Normal serum magnesium can coexist
  with low intracellular magnesium, because the body pulls magnesium from cells to
  keep serum stable (R51, R56).
- **Dietary shortfall is not the same as deficiency.** The body conserves magnesium
  when intake falls, so a low intake can exist for years without clinical signs
  (R01).

Magnesium is a cofactor in more than 600 enzymatic reactions, including ATP
handling, DNA and protein synthesis, ion transport and neuromuscular transmission.
It also modulates calcium entry and NMDA receptor activity, which is the mechanistic
bridge to its proposed effects on sleep, anxiety, vascular tone and migraine (R01,
R52). Those mechanisms are real; the clinical effects built on them are smaller
and less certain than the mechanisms suggest.

---

## 4. Forms: chemistry and elemental content

The first thing to understand about magnesium supplements is that **the number on
the front of the bottle is usually the salt, not the mineral**. Magnesium oxide is
60.3% magnesium; magnesium bisglycinate is 14.1%; magnesium L-threonate is 8.3%
anhydrous and about 7.2% in the commercial hydrate (R10, R37).

### 4.1 Elemental magnesium by form

| Form | Formula | Molar mass (g/mol) | Elemental Mg | Salt needed for 400 mg Mg |
| --- | --- | ---: | ---: | ---: |
| Magnesium oxide | MgO | 40.30 | 60.3% | 0.66 g |
| Magnesium hydroxide | Mg(OH)₂ | 58.32 | 41.7% | 0.96 g |
| Magnesium carbonate | MgCO₃ | 84.31 | 28.8% | 1.39 g |
| Magnesium chloride (anhydrous) | MgCl₂ | 95.21 | 25.5% | 1.57 g |
| Magnesium chloride hexahydrate | MgCl₂·6H₂O | 203.30 | 12.0% | 3.34 g |
| Magnesium citrate (trimagnesium dicitrate) | Mg₃(C₆H₅O₇)₂ | 451.11 | 16.2% | 2.48 g |
| Magnesium hydrogen citrate (1:1) | C₆H₆MgO₇ | 214.41 | 11.3% | 3.53 g |
| Magnesium malate (anhydrous) | MgC₄H₄O₅ | 156.38 | 15.5% | 2.57 g |
| Magnesium malate dihydrate | MgC₄H₄O₅·2H₂O | 192.41 | 12.6% | 3.17 g |
| Magnesium bisglycinate | Mg(C₂H₄NO₂)₂ | 172.42 | 14.1% | 2.84 g |
| Magnesium lactate | Mg(C₃H₅O₃)₂ | 202.45 | 12.0% | 3.33 g |
| Magnesium sulfate (anhydrous) | MgSO₄ | 120.37 | 20.2% | 1.98 g |
| Magnesium sulfate heptahydrate | MgSO₄·7H₂O | 246.48 | 9.9% | 4.06 g |
| Magnesium taurate | Mg(C₂H₆NO₃S)₂ | 272.57 | 8.9% | 4.49 g |
| Magnesium L-threonate | Mg(C₄H₇O₅)₂ | 294.50 | 8.3% | 4.84 g |
| Magnesium aspartate | Mg(C₄H₆NO₄)₂ | 288.49 | 8.4% | 4.75 g |
| Magnesium orotate | Mg(C₅H₃N₂O₄)₂ | 334.48 | 7.3% | 5.51 g |
| Magnesium gluconate | Mg(C₆H₁₁O₇)₂ | 414.60 | 5.9% | 6.83 g |

Calculated in `analysis/build_tables.py` from standard atomic masses; formulas and
molar masses cross-checked against the published comparison in R10. Hydrated forms
are listed separately because labels rarely say which one is in the bottle.

Two practical consequences:

- **A 500 mg capsule is not 500 mg of magnesium.** It cannot be for bulky salts. A
  500 mg magnesium bisglycinate capsule holds about 70 mg of magnesium; a 500 mg
  magnesium oxide tablet holds about 302 mg.
- **Hydration changes the dose by up to 30%.** Magnesium citrate as the anhydrous
  trimagnesium salt is 16.2% magnesium; as the monobasic form it is 11.3%. A label
  that does not specify which is selling meaningfully less magnesium than the
  customer expects.

### 4.2 Form-by-form assessment

| Form | Elemental content | Solubility | Absorption evidence | GI tolerance | Evidence-based use | Verdict |
| --- | ---: | --- | --- | --- | --- | --- |
| **Oxide** | 60.3% | Very poor (0.010 g/100 mL) | ~4% absorbed, versus 9–11% for soluble salts | Laxative at dose; most reported diarrhoea | Constipation; cheapest option; trials in older adults | Effective but poorly absorbed |
| **Citrate** | 11.3–16.2% | High, even in water | Best-documented advantage over oxide; highest serum Mg at 60 days | Osmotic loosening at higher doses | General supplementation, migraine trials, constipation | Best overall evidence-to-cost balance |
| **Bisglycinate** | 11.7–14.1% | Moderate (1.36 g/100 mL) | Equal to oxide overall in the only direct trial; better in malabsorbers | Generally gentle | Sleep, tolerability-sensitive users | Good tolerability, unproven absorption edge |
| **Glycinate chelate (Albion-type)** | ~10–14% | Moderate | No adequate head-to-head data in healthy adults | Gentle | Same as bisglycinate | Marketing outruns evidence |
| **Malate** | 12.6–15.5% | Slightly soluble | No human head-to-head trials | Moderate | Fatigue and soreness marketing | Plausible, unproven |
| **Taurate** | 8.9% | Slightly soluble | No human head-to-head trials | Moderate | Cardiovascular marketing | Unsupported claims |
| **L-threonate** | 7.2–8.3% | Soluble | Animal brain uptake; human brain Mg unmeasured | Moderate | Cognitive marketing | Expensive, unproven |
| **Chloride** | 12.0% (hexahydrate) | Very soluble (54 g/100 mL) | 9–11% absorbed, better than oxide | Salty; osmotic | Liquid forms, some sustained-release products | Absorbed, inconvenient |
| **Sulfate (Epsom salt)** | 9.9% (heptahydrate) | Very soluble | Oral is laxative; transdermal absorption negligible | Laxative | Baths (not a magnesium strategy) | Not a supplement strategy |
| **Lactate** | 10.2–12.0% | Soluble | 9–11% absorbed in comparative work | Moderate | Clinical and paediatric products | Reasonable, less available |
| **Aspartate** | 8.4% | Soluble | 9–11% absorbed | Moderate | Older clinical trials | Reasonable, dated evidence |
| **Orotate** | 7.3% | Slightly soluble | No good comparative data | Moderate | Heart-failure marketing | Unsupported |
| **Gluconate** | 5.9% | Soluble | Absorbed, but bulky | Reported diarrhoea | Clinical use where chloride is unsuitable | Niche |

### 4.3 The "chelate" question

Chelation is a chemical structure: a metal ion bound to a ligand, often an amino
acid. It is not a synonym for "better absorbed". The strongest direct evidence for
glycinate comes from a small trial in patients with ileal resection, where ²⁶Mg
absorption was 23.5% from glycinate and 22.8% from oxide overall (identical), and
better only in the four patients with the worst absorption (23.5% vs 11.8%)
(R07). That is a real finding for malabsorption, not proof for healthy adults.

Several commercial glycinate products are not pure glycinate. ConsumerLab declined
to approve two magnesium products because the form detected did not match the
label (R46), and a peer-reviewed survey found only 41.3% of magnesium supplements
within acceptable deviation of their declared content (R48). "Chelated" on a label
is a claim to verify, not a guarantee.

### 4.4 What threonate actually is

Magnesium L-threonate is a salt of magnesium and L-threonic acid, an ascorbate
metabolite. Animal work shows it raises brain magnesium more than other salts
(R34). Human trials have not measured brain magnesium; they measure cognitive test
scores, and those results are inconsistent (section 6.8). A 2 g dose of the
commercial ingredient supplies about 144 mg of elemental magnesium, roughly a
third of the RDA, so the product is best understood as a low-dose magnesium
supplement with a premium price and a cognitive hypothesis attached.

---

## 5. Absorption and bioavailability

### 5.1 How much is absorbed

At typical dietary intakes, about **30–40% of ingested magnesium is absorbed**
(R01). Absorption is saturable and paracellular at high doses, so fractional
absorption falls as the dose rises; smaller, divided doses deliver more magnesium
per milligram (R08). This is the basis for splitting doses rather than taking
400 mg at once.

### 5.2 Oxide versus the rest

Three lines of evidence converge:

- **Urinary recovery.** After a 25 mmol load, urinary magnesium rose by 0.22 mg/mg
  creatinine with citrate and 0.006 with oxide in the first four hours (R04). Oxide
  was only 43% soluble even at simulated peak gastric acidity.
- **Fractional absorption.** Oxide delivered about 4% of its dose, against 9–11% for chloride, aspartate and lactate (R03, R09).
- **Sixty-day supplementation.** At 300 mg/day, citrate produced the highest serum
  magnesium; oxide did not differ from placebo on 24-hour urinary excretion (R05).

The counterpoint matters: when citrate and oxide were compared after magnesium
saturation, the difference in 24-hour urinary magnesium was 0.565 mmol, about
13.7 mg, against a daily intake above 800 mg. The authors called it statistically
significant but physiologically irrelevant (R06). Both things are true: oxide is
less bioavailable, and the absolute difference is small in a well-fed person.

### 5.3 Does the organic form matter among themselves?

Not demonstrably. Reviews of balance studies find either no difference between
organic and inorganic salts or a small advantage for organic salts under
standardised conditions (R08, R09). There are no adequate head-to-head trials
showing citrate beats glycinate, or glycinate beats malate, in healthy adults. The
confident marketing rankings are extrapolations from chemistry and from oxide
comparisons.

### 5.4 Measurement problem

Bioavailability studies use urinary recovery, serum_area under the curve_, faecal
balance or isotope tracers. Each has weaknesses: serum is homeostatically buffered,
urine reflects recent intake and renal handling, and balance studies are difficult
to run accurately. This is why small studies disagree and why "absorption
percentage" figures should be read as approximate (R08, R09).

### 5.5 Transdermal and bath products

Intact skin is an effective barrier. An ex vivo study found magnesium permeation
across intact skin of 8.3 µg/cm² over 24 hours, not significantly different from
control (3.9 µg/cm²) (R40). A placebo-controlled cream trial found no significant
overall rise in serum magnesium (0.82 to 0.89 mmol/L, p=0.29), with a positive
result only in a non-athlete subgroup (R39). A review of the transdermal literature
concluded the practice is scientifically unsupported (R38). Epsom salt baths may
feel good; they are not a reliable way to correct low magnesium.

---

## 6. Evidence by outcome

### 6.1 Sleep

**What the trials show.** The most-cited trial gave 500 mg/day magnesium oxide to
46 older adults with primary insomnia for eight weeks. Insomnia Severity Index,
sleep onset latency, sleep efficiency, serum renin, melatonin and cortisol all
improved relative to placebo (R15). The trial was small, single-centre and at risk
of bias.

A meta-analysis of three RCTs in 151 older adults found sleep onset latency 17.36
minutes shorter with magnesium (95% CI −27.27 to −7.44) and total sleep time 16.06
minutes longer, but the latter was not significant (R16). The authors graded the
evidence low to very low.

A 2025 placebo-controlled trial of 250 mg elemental magnesium as bisglycinate in
adults with poor sleep found a 1.6-point greater fall in ISI score (p=0.049,
Cohen's d=0.2), with larger effects in participants reporting low dietary magnesium
(R17). A 2026 systematic review found positive results in older adults, poor
sleepers and people with restless legs or nocturnal cramps, but null results in
PCOS, fibromyalgia and cognitive impairment, and null ISI results for threonate and
nano-chloride (R18).

**Interpretation.** There is probably a small sleep benefit in people with low
magnesium status or poor sleep, and little or none in everyone else. The effect is
smaller than the placebo response in most trials. Magnesium is not a treatment for
insomnia disorder, and it is not a substitute for sleep hygiene or CBT-I.

### 6.2 Muscle function and strength

In 139 healthy women aged about 71 attending a mild fitness programme, 300 mg/day
for 12 weeks improved Short Physical Performance Battery score by 0.41 points,
chair-stand time by 1.31 seconds and 4-metre gait speed by 0.14 m/s. Effects were
larger in women whose dietary intake was below the RDA (R29). The trial had no
placebo group, which inflates apparent benefit.

In replete adults, the picture is different. A 2025 randomised crossover gave
magnesium chloride and found VO₂max fell from 44.4 to 41.3 mL/kg/min and 30-second
sprint power from 439 to 415 W, both worse than placebo (R32). A scoping review
concludes that benefits are reported mainly in deficiency states and are
inconsistent in well-nourished athletes (R55).

**Interpretation.** Correcting a deficiency improves function; supplementing a
replete person does not make them stronger or faster. There is no ergogenic case
for magnesium in well-fed athletes.

### 6.3 Muscle cramps

This is the clearest negative finding in the review. The 2020 Cochrane review
pooled five RCTs in 307 adults, mostly older, with idiopathic cramps. Magnesium
reduced cramps by 0.18 per week (95% CI −0.84 to 0.49) and changed the percentage
of cramps from baseline by −9.59% (95% CI −23.14 to 3.97), both null, with
moderate certainty (R11). A separate trial of magnesium oxide in 94 community
adults was stopped early for futility (R14).

Pregnancy cramps are less clear: trials disagree, a meta-analysis of four RCTs in
332 women found no significant reduction (WMD −0.47, 95% CI −1.14 to 0.20), and a
controlled trial found no difference from placebo (R12, R13). A clinician may
still offer a trial because the intervention is low-risk, but the evidence does not
support a general claim.

**Interpretation.** Magnesium is not an effective cramp prophylactic for most
people. Cramps in kidney disease, diuretic use or alcohol misuse are a different
matter and should be investigated rather than self-treated.

### 6.4 Exercise recovery and soreness

A randomised crossover in which participants ran downhill after a week of
magnesium supplementation found lower IL-6 (1.36 vs 2.06 pg/mL), less soreness and
better post-exercise glucose recovery, but no difference in creatine kinase,
maximal force or performance (R30). A 2024 systematic review of four studies found
consistent reductions in soreness but heterogeneous performance results and very
low certainty (R31).

**Interpretation.** Magnesium may modestly reduce perceived soreness after
unaccustomed exercise. It does not accelerate functional recovery or improve
performance.

### 6.5 Anxiety, stress and mood

A systematic review of 18 studies concluded that magnesium may help mild anxiety
and stress, while noting that most studies were small, heterogeneous and of poor
quality (R25). A 2024 review found five of seven anxiety studies positive, with the
two null trials in premenstrual and postpartum populations (R27).

The best-controlled trial enrolled 264 adults with low serum magnesium and high
stress. Both magnesium and magnesium plus vitamin B6 reduced DASS-42 stress scores
by about 42–45%, with no difference between arms overall; in the severe-stress
subgroup, the B6 combination added a modest 24% greater improvement (R26). The
absence of a placebo arm means regression to the mean cannot be excluded.

For depression, pooled trials report an SMD of −0.92 (95% CI −1.443 to −0.396),
but heterogeneity is high and most studies are small or adjunctive (R28).

**Interpretation.** There may be a small benefit in people with low magnesium
status or high stress. Magnesium is not a treatment for an anxiety disorder or
major depression, and it should not displace evidence-based care.

### 6.6 Migraine

A double-blind trial in 81 adults gave 600 mg/day trimagnesium dicitrate for 12
weeks. Attack frequency fell 41.6% with magnesium versus 15.8% with placebo in
weeks 9–12; migraine days and symptomatic drug use also fell. Diarrhoea occurred in
18.6% and gastric irritation in 4.7% (R19).

A systematic review using the AAN scheme graded the evidence C (possibly
effective), noting that one of two Class I trials was positive (R20). The AAN/AHS
give magnesium a Level B recommendation for prevention, and the German guideline
notes conflicting trial results (R21, R53). Efficacy may depend on the salt: the positive trials used
trimagnesium dicitrate (R19, R20).

**Interpretation.** Magnesium has a reasonable, modest, guideline-supported role in
migraine prevention at 600 mg/day, taken in divided doses under supervision. That
dose is above the 350 mg supplemental upper limit and commonly causes loose stools.
It is not a treatment for an acute attack.

### 6.7 Blood pressure and cardiovascular health

Three meta-analyses agree on direction and disagree on magnitude:

| Analysis | Trials / participants | Dose | Systolic | Diastolic | Notes |
| --- | --- | --- | ---: | ---: | --- |
| Zhang 2016 (R22) | 34 / 2028 | median 368 mg/day | −2.00 mmHg | −1.78 mmHg | 95% CI 0.43–3.58 and 0.73–2.82 |
| 2025 meta-analysis (R23) | 38 / 2709 | 82–637 mg/day | −2.81 mmHg | −2.05 mmHg | −7.68 mmHg in treated hypertensives; null in normotensives |
| 2024 umbrella review (R24) | 10 reviews / 8610 | variable | −1.25 mmHg | −1.40 mmHg | −6.38/−3.71 at ≥400 mg/day; heterogeneity 92% |

Observational data are stronger in appearance than in substance. In 14,232
middle-aged adults, the highest quartile of serum magnesium had 38% lower risk of
sudden cardiac death than the lowest, but dietary magnesium was not associated with
risk (R01). A meta-analysis of seven cohorts (241,378 participants) found 8% lower
stroke risk per additional 100 mg/day (R01). These are associations, confounded by
overall diet and health status.

**Interpretation.** Magnesium lowers blood pressure slightly, and meaningfully in
treated hypertensives and people with low magnesium. It does not prevent heart
attacks or strokes, and no adequately powered trial shows that supplements reduce
cardiovascular events. The FDA's 2022 qualified health claim explicitly calls the
evidence inconsistent and inconclusive (R01).

### 6.8 Cognition

Human evidence is thin. A 2024 meta-analysis found three double-blind RCTs and no
consistent cognitive benefit (R33).

- **MMFS-01 (threonate), 44 older adults with impairment:** overall cognition
  improved with a Cohen's d of 0.91, but the trial was small, industry-linked, and
  placebo effects on sleep and anxiety were strong enough that those outcomes could
  not be interpreted (R34).
- **Magtein plus phosphatidylserine, 109 healthy adults:** improved all five memory
  subscales after 30 days, but the formula contained several active ingredients and
  was industry-funded (R35).
- **Magtein 2 g/day, 100 adults with poor sleep:** NIH Total Cognition Composite
  improved (p=0.043), with a reported 7.5-year reduction in "brain age"; most
  secondary outcomes, including sleep disturbance and wellbeing, were null. A
  correction has been published (R36).
- **Low-dose threonate after breast cancer surgery, 88 women:** no improvement at
  91.8 mg/day (R33).

**Interpretation.** There is no established cognitive benefit for healthy adults.
The positive trials are small, short, mostly industry-funded and inconsistent
across endpoints. The "brain age" figure is a derived marketing metric, not a
clinical outcome. Human brain magnesium has not been measured.

### 6.9 Bone, diabetes and other outcomes

Magnesium is involved in bone formation and parathyroid hormone regulation, and
higher intakes are associated with higher bone mineral density. A small study in
postmenopausal women with osteoporosis found that 290 mg/day magnesium citrate for
30 days suppressed bone turnover, suggesting reduced bone loss, but this is a
surrogate endpoint in 20 women (R01). There is no evidence that magnesium
supplements prevent fractures.

Higher magnesium intake is associated with lower type 2 diabetes risk in cohort
studies, with a 15% lower risk per 100 mg/day in one meta-analysis of 286,668
people (R01). Trials of supplementation for glycaemic control are few and
conflicting. Association is not treatment.

---

## 7. Deficiency, intake and testing

### 7.1 How common is low intake?

NHANES 2013–2016 found that **48% of Americans consume less magnesium from food and
beverages than their Estimated Average Requirement** (R01). Adolescent males and
females and men over 71 are most likely to be low. Average intakes from food alone
were 268 mg/day for men and 234 mg/day for women in an earlier survey; with
supplements, 449 mg and 387 mg (R01).

Low intake is not the same as deficiency. The kidneys reduce urinary magnesium
when status falls, and symptomatic deficiency from diet alone is uncommon in
healthy people (R01).

### 7.2 Who is genuinely at risk

| Group | Mechanism | What to do |
| --- | --- | --- |
| Gastrointestinal disease (Crohn's, coeliac, short bowel, ileal resection) | Malabsorption and loss | Investigate and treat; supplementation often needed, sometimes parenterally |
| Type 2 diabetes / insulin resistance | Increased urinary loss | Address glycaemic control; test if symptomatic |
| Alcohol use disorder | Poor intake, vomiting, diarrhoea, renal loss | Clinical assessment; deficiency is common |
| Older adults | Lower intake, reduced absorption, more medications | Review diet and drugs; supplement if intake is low |
| Loop and thiazide diuretics | Increased urinary excretion | Monitor; potassium-sparing diuretics reduce loss |
| Long-term proton pump inhibitors | Reduced intestinal absorption | FDA advises checking magnesium after long-term use (R41) |
| Chronic kidney disease | Reduced excretion (risk of excess, not deficit) | Do not self-supplement; clinician-guided |

### 7.3 Why blood testing is limited

Serum magnesium is the usual test and a poor one. Less than 1% of body magnesium
is extracellular, and serum is defended at the expense of tissue stores (R01, R51).
Other approaches, including red-cell magnesium, ionized magnesium, salivary
magnesium, 24-hour urinary magnesium and the magnesium loading test, all have shortcomings,
and no single method is considered satisfactory (R01, R50).

The practical implication: a normal serum magnesium does not rule out depletion in
a symptomatic patient, and an abnormal result should prompt a search for the cause
(GI loss, diuretics, PPIs, alcohol, diabetes, kidney disease) rather than
open-ended supplementation. Magnesium is not part of routine electrolyte panels in
most hospitals and has not been measured in NHANES since 1974 (R01).

---

## 8. Dosing

### 8.1 Recommended intake and upper limit

| Life stage | Male | Female | Pregnancy | Lactation |
| --- | ---: | ---: | ---: | ---: |
| 19–30 years | 400 mg | 310 mg | 350 mg | 310 mg |
| 31–50 years | 420 mg | 320 mg | 360 mg | 320 mg |
| 51+ years | 420 mg | 320 mg | n/a | n/a |

These are RDAs for **total** intake from food, water, supplements and medications
(R01, R02). The tolerable upper intake level for **supplemental and medicinal**
magnesium is **350 mg/day for adults**; it does not include food magnesium, because
healthy kidneys excrete the excess (R01). For children the UL ranges from 65 mg at
1–3 years to 350 mg at 9–13 years.

The apparent paradox of a UL below the RDA is explained by the different scopes:
the RDA covers all sources, the UL only supplements and drugs.

### 8.2 Effective doses by indication

| Indication | Dose used in trials | Evidence | Notes |
| --- | --- | --- | --- |
| General adequacy | 100–200 mg/day supplemental | Moderate | Enough to close a modest dietary gap; stay under 350 mg total supplemental |
| Sleep | 250–500 mg in the evening | Low | Trials used oxide, bisglycinate and citrate; effect small |
| Anxiety / stress | 200–300 mg/day | Very low | Best in low-magnesium or high-stress adults |
| Blood pressure | 300–370 mg/day for 8–12 weeks | Moderate | Larger effect in treated hypertensives |
| Migraine prevention | 600 mg/day, divided | Moderate | Above the UL; clinician supervision; expect loose stools |
| Constipation | 200–400 mg oxide or citrate | Moderate | Osmotic effect; not a magnesium-repletion strategy |
| Cramps | Not indicated | Moderate (null) | Investigate causes instead |

### 8.3 Practical protocol

1. **Estimate intake first.** A food diary or a rough count of nuts, seeds,
   legumes, whole grains and leafy greens is more informative than a blood test in
   a healthy person.
2. **Split the dose.** 100–200 mg elemental magnesium per dose, once or twice daily,
   absorbs better than a single large dose (R08).
3. **Take with food** if it upsets the stomach; take separately from interacting
   drugs (section 9.4).
4. **Start low.** 100–200 mg/day for a week, then adjust. Loose stools are the
   dose-limiting side effect, not a sign of "detox".
5. **Reassess at 4–8 weeks.** If there is no clear benefit and intake is adequate,
   stop. Magnesium is not a drug that must be continued indefinitely.
6. **Do not stack products.** Multivitamins, antacids, laxatives and sleep blends
   often contain magnesium; the totals add up.

---

## 9. Safety

### 9.1 Gastrointestinal effects

The most common adverse effect is diarrhoea, nausea and abdominal cramping.
Carbonate, chloride, gluconate and oxide are most often implicated; citrate causes
dose-dependent loosening (R01). The mechanism is osmotic: unabsorbed magnesium
draws water into the bowel. Glycinate is generally gentler but not exempt at high
doses. In the migraine trial, 18.6% of participants on 600 mg/day had diarrhoea
(R19).

### 9.2 Hypermagnesemia and toxicity

Symptoms usually appear when serum magnesium exceeds about 1.74–2.61 mmol/L and
include hypotension, nausea, vomiting, flushing, urinary retention, ileus, lethargy,
muscle weakness, respiratory depression, arrhythmia and cardiac arrest (R01, R45).
Deep tendon reflexes disappear near 5 mmol/L; cardiac arrest can occur above
6–7.5 mmol/L (R45).

Oral supplements rarely cause this in healthy kidneys. Cases cluster in three
settings: kidney impairment, very high doses of laxatives or antacids, and the
combination of the two (R44). A retrospective cohort of 320 patients prescribed
magnesium oxide found that 23% developed some degree of hypermagnesemia; independent
risk factors were eGFR ≤55.4 mL/min (OR 3.1), magnesium oxide ≥1650 mg/day (OR 1.9)
and duration ≥36 days (OR 2.2) (R43).

Documented fatalities include a woman with end-stage renal disease taking 3000 mg/day
of magnesium hydroxide for constipation (serum 9.9 mg/dL, recovered with dialysis)
and a woman with normal renal function who reached 11.0 mg/dL and died (R44).

### 9.3 Kidney disease

This is the main safety issue and it runs opposite to the marketing narrative.
Healthy kidneys excrete excess magnesium; failing kidneys cannot. Patients with
CKD, acute kidney injury or on dialysis should not self-prescribe magnesium, and
dose selection requires clinician involvement and monitoring (R42, R54). Magnesium
is not nephrotoxic to healthy kidneys; the risk is accumulation.

### 9.4 Drug interactions

| Drug class | Interaction | Management |
| --- | --- | --- |
| Tetracycline and quinolone antibiotics (doxycycline, ciprofloxacin, levofloxacin) | Magnesium chelates the drug and reduces absorption | Take magnesium 2 hours before or 4–6 hours after (R01) |
| Oral bisphosphonates (alendronate) | Reduced absorption of the bisphosphonate | Separate by at least 2 hours (R01) |
| Loop and thiazide diuretics | Increased magnesium loss | Monitor magnesium; may need supplementation |
| Potassium-sparing diuretics (amiloride, spironolactone) | Reduced magnesium excretion | Monitor for excess |
| Proton pump inhibitors | Hypomagnesemia with long-term use | FDA advises baseline and periodic magnesium checks (R41) |
| High-dose zinc (142 mg/day) | Interferes with magnesium absorption and balance | Separate or reduce zinc dose (R01) |
| Calcium supplements | Competitive inhibition at high doses | Separate large doses; no fixed ratio is required (R01, R08) |

### 9.5 Pregnancy, children and older adults

Pregnancy increases magnesium requirements (350–360 mg/day total). Oral magnesium
has not been shown to prevent preeclampsia; intravenous magnesium sulfate is a
clinical treatment for seizure prophylaxis and is outside the scope of this review.
Pregnant women should not take high-dose magnesium without obstetric advice.
Children's doses are weight- and age-specific, and the UL is much lower.

Older adults are at higher risk of both low intake and hypermagnesemia, because
kidney function declines with age and polypharmacy is common. The same dose that is
trivial for a 30-year-old can accumulate in an 85-year-old with an eGFR of 40.

---

## 10. Product quality, labelling and contaminants

### 10.1 Labels

Three failure modes recur:

1. **Compound weight presented as dose.** A 483 mg magnesium oxide tablet contains
   about 291 mg of elemental magnesium (R49). Front-of-pack numbers often use the
   larger figure.
2. **Undisclosed hydration.** Anhydrous and hydrated salts differ by up to 30% in
   elemental content (section 4.1).
3. **Blends.** A product listing five salts and one total magnesium number cannot
   be checked against the chemistry, and the contribution of each form is unknown.

A peer-reviewed survey of magnesium supplements found that only 41.3% of samples
were within acceptable deviation of their declared content, and only two samples
matched exactly (R48). ConsumerLab's 2024 review declined to approve two products
because the form found did not match the label (R46).

### 10.2 Third-party certification

Certification programmes verify identity, strength and contaminant limits: lead,
arsenic, cadmium, mercury and, for sport programmes, banned substances (R47). They
do not verify efficacy, and they do not tell you whether the dose is sensible.

- **NSF Certified for Sport** is the strongest signal for athletes: batch-level
  testing for contaminants and prohibited substances.
- **NSF Contents Certified / NSF/ANSI 173** verifies label content and contaminant
  limits for the finished product.
- **USP Verified** verifies identity, strength, purity and manufacturing.
- **Informed Sport / Informed Choice** focus on prohibited-substance testing;
  Informed Choice is retail monitoring rather than batch release.

In this sample, 15 of 16 products had no documented certification. That is a
statement about the sample, not proof that the other products are contaminated
(most magnesium supplements pass independent testing), but certification is the
only cheap way for a consumer to reduce that uncertainty.

### 10.3 Contaminants

Magnesium salts are mined or precipitated and can carry heavy metals, particularly
oxide and carbonate grades. Independent testing has reported lead in some magnesium products,
including brands marketed as "clean". Those results are product- and batch-specific
and are not used here as quantitative evidence. The defensible conclusion is that
contaminant risk is real but product-specific, and certification plus a brand that
publishes certificates of analysis is the practical mitigation.

### 10.4 Forms and formats

- **Powder** is the cheapest per milligram and allows flexible dosing, but it is
  easy to over- or under-measure and flavoured products add sugar or sweeteners.
- **Tablets** are compact but may use oxide as a cheap filler and can be hard to
  swallow at high doses.
- **Capsules** are convenient and usually better labelled, but the capsule shell
  limits how much magnesium a serving can hold, which pushes up the number of
  capsules per dose.
- **Gummies** are the most expensive per milligram and often contain little
  magnesium; they are a poor value format for repletion.

---

## 11. Cost and brand comparison

Prices are one-time US retail snapshots from 18 November 2026. Full tables,
including per-product serving arithmetic, are in the
[generated brand comparison](../docs/generated/brand-comparison.md).

### 11.1 The headline numbers

| Metric | Result |
| --- | --- |
| Products priced | 16 |
| Cost range per 400 mg elemental magnesium | $0.08 – $2.92 |
| Spread | 37× |
| Cheapest overall | Nature's Blend Mag-Oxide, $0.08 per 400 mg |
| Cheapest powder | Nutricost Magnesium Glycinate, $0.31 per 400 mg |
| Cheapest certified | Thorne Magnesium Bisglycinate powder, $1.73 per 400 mg (NSF Certified for Sport) |
| Most expensive | Life Extension Neuro-Mag (threonate), $2.92 per 400 mg |
| Products exceeding the UL per serving | 5 of 16 |
| Products without documented certification | 15 of 16 |

### 11.2 Median cost by form

| Form | Products | Median cost per 400 mg |
| --- | ---: | ---: |
| Oxide | 2 | $0.10 |
| Malate | 2 | $0.40 |
| Citrate | 2 | $0.46 |
| Glycinate chelate | 2 | $0.60 |
| Taurate | 2 | $0.78 |
| Bisglycinate | 4 | $0.88 |
| Chloride | 1 | $1.68 |
| L-threonate | 1 | $2.92 |

The ordering is almost the inverse of the marketing hierarchy. Oxide is cheapest
and worst absorbed; threonate is most expensive and least proven. Citrate sits in
the middle with the best evidence-to-cost ratio. Glycinate costs roughly twice
citrate for tolerability, which may be worth it for people with sensitive guts,
but not for absorption.

### 11.3 Value is not the same as suitability

A $0.08 oxide tablet is poor value if it causes diarrhoea and delivers 4% of its
magnesium. A $2.92 threonate capsule is poor value if the cognitive claim is
unproven. The right metric is **cost per absorbed, tolerated milligram**, which is
why the mid-priced soluble salts usually win in practice:

- **Best value for general use:** NOW Magnesium Citrate at $0.40 per 400 mg, or
  Nutricost glycinate powder at $0.31 if powder suits you.
- **Best value with certification:** Thorne bisglycinate powder at $1.73, the only
  certified product in the sample.
- **Best value for constipation:** oxide, but treat it as a laxative, not a
  repletion strategy.
- **Worst value:** threonate at 7–37× the cost of alternatives, and slow-release
  chloride at $1.68 for a low elemental dose.

### 11.4 What the brands do well and badly

- **NOW, Doctor's Best, Source Naturals, Nutricost** publish clear elemental doses
  and sell mid-priced products with straightforward labels. Doctor's Best and NOW
  use Albion chelates; none in this sample documented certification.
- **Thorne** labels elemental magnesium clearly and carries NSF Certified for
  Sport on one product, but charges a premium ($1.73 per 400 mg for the powder).
- **Life Extension** sells a well-labelled threonate product at a price that only
  makes sense if the cognitive hypothesis is true.
- **Mag-Ox and Nature's Blend** are cheap oxide products that exceed the UL per
  serving and are best treated as laxatives.
- **SlowMag** combines a modest magnesium dose with calcium and a premium price;
  the sustained-release format may suit some people, but the cost per milligram is
  poor.
- **KAL and Jarrow taurate** products add vitamin B6 and herbal "absorption" blends,
  which makes attribution impossible and adds cost.

---

## 12. Who should supplement, and with what

### 12.1 Likely to benefit

- **People with genuinely low intake** who cannot or will not fix it with food
  (nuts, seeds, legumes, whole grains, leafy greens).
- **People with malabsorption** (Crohn's, coeliac, short bowel, ileal resection),
  often needing higher doses and clinical monitoring.
- **People with type 2 diabetes, alcohol use disorder, or long-term PPI use**, in
  whom losses or absorption problems are documented.
- **Older adults with low intake or polypharmacy**, especially diuretics.
- **People with migraine**, at 600 mg/day under clinician supervision.
- **People with constipation** who want an osmotic laxative; oxide or citrate is
  appropriate, but this is a gut treatment, not a magnesium-repletion strategy.

### 12.2 Unlikely to benefit

- **Healthy adults eating a varied diet with adequate intake.** Supplementing a
  replete person does not improve strength, performance or cognition.
- **People with idiopathic muscle cramps.** The evidence is consistently null.
- **Athletes seeking an ergogenic edge.** Trials in replete athletes show no
  benefit, and one showed a small decrement.
- **People seeking cognitive enhancement.** Threonate's human evidence is
  preliminary and inconsistent.
- **Anyone using it for weight loss, "detox", or "adrenal fatigue".** No evidence.

### 12.3 When supplementation is unnecessary

If a person eats nuts, seeds, legumes, whole grains and leafy greens most days, has
no risk factors, no symptoms and normal kidney function, a magnesium supplement is
unlikely to add anything. The 48% "below the EAR" statistic describes intake, not
deficiency, and the body conserves magnesium when intake falls (R01).

### 12.4 Selection algorithm

| If the goal is… | Choose | Dose | Why |
| --- | --- | --- | --- |
| General topping-up | Citrate or bisglycinate | 100–200 mg/day | Soluble, well tolerated, mid-priced, best evidence |
| Sensitive stomach | Bisglycinate | 100–200 mg/day | Gentler than oxide or citrate for most people |
| Lowest cost | Oxide, but split doses and expect looser stools | 200 mg/day | Cheapest per milligram, poorly absorbed |
| Constipation | Oxide or citrate | 200–400 mg as needed | Osmotic effect is the point |
| Sleep | Bisglycinate or citrate in the evening | 200–400 mg | Small evidence base, low risk |
| Migraine prevention | Trimagnesium dicitrate | 600 mg/day divided, clinician-supervised | Only dose with positive trials and guideline support |
| Blood pressure | Citrate or oxide | 300–370 mg/day for 8–12 weeks | Small effect; monitor |
| Cognition | Nothing, or threonate only in a trial | n/a | Unproven and expensive |
| Kidney disease | Nothing without a clinician | n/a | Accumulation risk |

### 12.5 A ten-second label check

1. Find the **elemental magnesium** figure, not the compound weight.
2. Check the **serving size**: is it one capsule or two tablets?
3. Divide the elemental dose by the number of capsules to get mg per capsule.
4. Compare the **cost per 400 mg**, not the pack price.
5. Check whether the **form** is named specifically, including hydration if possible.
6. Look for a **certification** mark if contaminants or sport are a concern.

---

## 13. Uncertainty and how this review could be wrong

- **Publication bias and industry funding.** Many positive trials are small and
  industry-funded, particularly for threonate, glycinate and proprietary blends.
  Negative trials are less likely to be published.
- **Form comparisons are indirect.** Most "best form" claims compare each form with
  oxide, not with each other. A ranking of citrate > glycinate > malate is not
  established.
- **Absorption measurement is imperfect.** Urinary recovery, serum AUC and isotope
  methods answer slightly different questions.
- **Price snapshots age.** The 37× spread is real; the individual prices will change.
- **The product sample is purposive.** Sixteen products illustrate the market; they
  are not a random sample, and the certification rate should not be extrapolated.
- **Guideline recommendations lag evidence.** The AAN/AHS Level B for migraine rests
  on a small evidence base and has not been updated to reflect newer null trials in
  other forms.

Where this review says "unsupported", it means the claim is not supported by
controlled human evidence, not that it has been proven false. Where it says
"established", it means the direction is consistent across studies, not that the
effect is large.

---

## 14. References

Fifty-seven sources are listed in [the references](../docs/references.md), each with a
DOI, PMID/PMC identifier or stable URL. The complete evidence record, with effect
sizes and certainty grades, is in the
[generated evidence tables](../docs/generated/evidence-tables.md). All thirty-one
claim adjudications are in the
[claims table](../docs/generated/claims-table.md).

Key primary sources for the main conclusions:

- **Forms and absorption:** R03, R04, R05, R06, R07, R08, R09, R10
- **Sleep:** R15, R16, R17, R18
- **Muscle, cramps and recovery:** R11, R12, R13, R14, R29, R30, R31, R32
- **Anxiety and mood:** R25, R26, R27, R28
- **Migraine:** R19, R20, R21, R53
- **Blood pressure and cardiovascular:** R22, R23, R24
- **Cognition:** R33, R34, R35, R36, R37
- **Deficiency and testing:** R01, R50, R51, R56
- **Safety and interactions:** R41, R42, R43, R44, R45, R54
- **Quality:** R46, R47, R48, R49

---

## Appendix A: Claim summary

The full table is generated from `data/claims.csv`. Of 31 adjudicated claims:

- **Supported:** 1 (citrate is one of the better-absorbed forms)
- **Partially supported:** 12
- **Unsupported:** 9
- **False:** 9

The pattern is consistent: the chemistry claims are broadly right, the clinical
claims are overstated, and the dosing and safety claims are frequently false.

## Appendix B: What would change the conclusions

- A large, independent, placebo-controlled trial of magnesium for cramps showing a
  meaningful effect.
- A trial measuring brain magnesium in humans after oral threonate, with cognitive
  endpoints.
- A head-to-head RCT of citrate versus bisglycinate versus malate in healthy adults
  using isotope tracers.
- An adequately powered cardiovascular outcome trial of magnesium supplementation.
- Better biomarkers for tissue magnesium status.

Until then, the practical advice is unglamorous: eat magnesium-rich food, test only
when there is a reason, supplement modestly if intake is low or losses are high,
choose a soluble salt at a fair price, and do not expect it to fix sleep, cramps,
memory or heart disease.
