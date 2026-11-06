**English** · [日本語](99-follow-my-example.ja.md)

# Answer key

Open this only after you have your own results. All numbers use the
definitions in `AGENTS.md` (blank power values treated as zero). They match
my thesis analysis.

## Step 2: Rows

| Fiscal year | Records |
| --- | --: |
| 2005 | 1,318 |
| 2024 | 1,014 |

## Step 2: The three percentages

| Measure | FY2005 | FY2024 |
| --- | --: | --: |
| Records with a generator (power_capacity_kw > 0) | 21.6% (285 of 1,318) | **41.1%** (417 of 1,014) |
| Waste burned at records that generate (throughput where power_generated_mwh > 0) | 60.5% | **80.1%** |
| Design capacity at records with a generator | 56.0% | **70.5%** |

So yes: about 4 in 10 **plants** have a generator, but about 8 in 10
**tonnes of waste** are burned at plants that generate. The big plants are
the ones that generate, so counting plants understates coverage.

## Step 2: The missing-value trap

In FY2024, `power_capacity_kw` is blank for **595** records, zero for 2 and
positive for 417. In FY2005 there are no blanks: non-generators were
recorded as 0. The reporting format changed.

| How blanks are treated | FY2024 share with a generator |
| --- | --: |
| Blank = zero (correct here) | 41.1% (417 of 1,014) |
| Blanks dropped | 99.5% (417 of 419) |

If your first percentage was 99.5%, this is why. The same question with a
different rule for blanks gives a completely different answer. Always ask
how missing values were treated.

A second definition check: counting records that **generate**
(power_generated_mwh > 0) instead of records **with a generator** gives
40.4% in FY2024 (410 of 1,014). Close, but not the same thing.

## Step 5: Skill test (FY2024, Tokyo)

| Measure | Tokyo FY2024 |
| --- | --: |
| Records with a generator | 66.7% (32 of 48) |
| Waste burned at records that generate | 96.8% |
| Design capacity at records with a generator | 88.5% |

## Stretch: the same plants

732 plants appear in both years.

| Group | Share with a generator |
| --- | --: |
| Same 732 plants, FY2005 | 29.9% |
| Same 732 plants, FY2024 | 32.1% |
| Plants only in FY2005 records | 11.3% |
| Plants only in FY2024 records | 64.5% |

The share among **all records** rose by about 20 points, but among the
**same plants** it rose by only about 2. Most of the rise came from small
plants without generators leaving the records and large plants with
generators joining them. The data shows records, not why plants opened or
closed, so this is "consistent with" Japan's policy of consolidating small
incinerators, not proof of it.

A reference version of the skill is in
[coverage-check/SKILL.md](coverage-check/SKILL.md).
