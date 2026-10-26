# Project brief

## What this project is
- Topic: electricity recovery at Japan's municipal waste incinerators.
- Question: Japan's headline statistic says only about 4 in 10 incinerators
  generate electricity. Does that understate how much waste is actually
  burned at plants that generate?
- Audience: a seminar class and a policy reader who is not a programmer.

## Files
- data/incinerators_fy2005_fy2024.csv: one row per incinerator record in
  fiscal years 2005 and 2024 (2,332 rows). Source: Ministry of the
  Environment Japan, General Waste Treatment Survey, via e-Stat, processed by
  Pann Phetra. Columns:
  - fiscal_year: 2005 or 2024
  - prefecture: prefecture name
  - facility_id: the same plant has the same id in both years
  - year_started: year the plant started operating
  - capacity_t_day: design capacity, tonnes of waste per day
  - throughput_t_year: waste actually burned that year, tonnes
  - operation_mode: continuous (24 hours), semi-continuous or batch
  - power_capacity_kw: installed generator capacity, kW (blank = not reported)
  - power_generated_mwh: electricity generated that year, MWh (blank = not reported)

## Definitions
- A record "has a generator" when power_capacity_kw is above zero.
- A record "generates" when power_generated_mwh is above zero.
- Treat blank power values as zero (not reported).

## Rules
- Explain what you will do and wait for my OK before changing files.
- Never change the file in data/. Save scripts in scripts/ and results in outputs/.
- Use simple Python (pandas and matplotlib) and explain code in plain English.
- Every number you report must come from a script you ran; say which one.
- Never claim the data shows why plants were built or closed. It only shows records.
- Write in clear English for a reader who is not a programmer.
