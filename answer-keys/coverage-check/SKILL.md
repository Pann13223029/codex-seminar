---
name: coverage-check
description: Calculate electricity-generation coverage of Japanese waste incinerators for a fiscal year (and optionally one prefecture) from data/incinerators_fy2005_fy2024.csv. Use when the user asks about generator coverage or the coverage check. Do not use for other analyses.
---

# Coverage check

Reference version. To use it, copy this folder to `.agents/skills/coverage-check/`
in the `99-follow-my-example` folder.

## Inputs

- A fiscal year: 2005 or 2024.
- Optional: one prefecture name, as written in the `prefecture` column.

## Steps

1. Read the definitions in AGENTS.md. Treat blank power values as zero.
2. Filter data/incinerators_fy2005_fy2024.csv to the fiscal year (and
   prefecture, if given). Report the number of records.
3. Calculate:
   - share of records with power_capacity_kw > 0;
   - share of throughput_t_year at records with power_generated_mwh > 0;
   - share of capacity_t_day at records with power_capacity_kw > 0.
4. Save the three percentages, the record count and the filter used to
   outputs/coverage_<year>[_<prefecture>].csv.
5. Report the three percentages rounded to one decimal place, with the
   counts behind the first one (for example "417 of 1,014").
6. Tell the user how to check the first percentage by hand in a spreadsheet.
7. Warn if more than a few power values are blank, because treating blanks
   differently changes the result.

## Rules

- Never change the data file.
- Never claim why plants were built or closed; the data shows records only.
