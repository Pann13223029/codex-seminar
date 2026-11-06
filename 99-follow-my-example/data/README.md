# Data

`incinerators_fy2005_fy2024.csv`: 2,332 municipal waste incinerator records
for fiscal years 2005 (1,318 records) and 2024 (1,014 records).

**Source:** Ministry of the Environment Japan, General Waste Treatment Survey
(一般廃棄物処理実態調査), facility workbooks, published via e-Stat
(https://www.e-stat.go.jp/). e-Stat content may be reused and modified with
the source cited, under terms compatible with Creative Commons Attribution
4.0.

**Processing:** parsed and de-duplicated for the graduation thesis of Pann
Phetra (Ritsumeikan Asia Pacific University). `facility_id` links the same
plant across years even though the official facility codes changed. Only the
columns used in this workshop are kept, with English labels. Column
meanings are in `../AGENTS.md`.

Note: in FY2024 the survey leaves generator fields blank for most plants
without a generator, while FY2005 records them as 0. Treat blanks as zero.
