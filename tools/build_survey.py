"""Build the synthetic Beppu visitor survey used in track 98.

All responses are made up (fixed random seed), shaped like a Google Forms
export so students can practise survey cleaning without real respondents.

Usage: python tools/build_survey.py
"""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "98-present-your-work" / "data" / "beppu_visitor_survey_SYNTHETIC.csv"
random.seed(20261106)

ORIGINS = [("Japan: Kyushu", 26), ("Japan: other regions", 30), ("South Korea", 18), ("Taiwan", 12),
           ("Mainland China", 8), ("Hong Kong", 6), ("United States", 5), ("Thailand", 5), ("Other", 10)]
PURPOSES = ["Onsen and relaxation", "Sightseeing (Jigoku hells)", "Food", "Visiting friends or family", "Business or study"]
AGES = ["Under 20", "20-29", "30-39", "40-49", "50-59", "60 or older"]
NIGHTS = ["Day trip", "1 night", "2 nights", "3 or more nights"]
ENJOY = {
    "Onsen and relaxation": ["The sand bath was unforgettable.", "So many different onsen in one town.", "Relaxing in the outdoor bath with a view of the bay."],
    "Sightseeing (Jigoku hells)": ["The Jigoku tour, especially the red Chinoike pond.", "Steam rising everywhere around Kannawa.", "Seeing the hells was unique."],
    "Food": ["Jigoku-mushi steamed food in Kannawa.", "Toriten and the local seafood.", "Fresh dango and street snacks."],
    "Visiting friends or family": ["Time with family at a quiet onsen.", "Friendly local people.", "Walking around the old streets together."],
    "Business or study": ["Easy to relax after work in an onsen.", "The view from the ropeway.", "Good food near the station."],
}
IMPROVE_INTL = ["More signs and maps in English, Korean and Chinese.", "Bus timetables were hard to understand.",
                "Hard to know onsen rules before entering.", "More card payment at small shops.", ""]
IMPROVE_DOM = ["Buses between sights are infrequent.", "More parking near the hells.", "Some areas felt crowded on weekends.",
               "Shops close early in the evening.", ""]


def weighted(items):
    names, weights = zip(*items)
    return random.choices(names, weights=weights)[0]


def likert(base):
    return max(1, min(5, round(random.gauss(base, 0.8))))


def main():
    header = ["Timestamp", "Email address", "Name (optional)", "Age group", "Where are you visiting from?",
              "Main purpose of your visit", "How long are you staying in Beppu?",
              "Overall, how satisfied were you with your visit? (1 = very dissatisfied, 5 = very satisfied)",
              "Onsen experience (1-5)", "Ease of getting around (1-5)", "Information available in my language (1-5)",
              "Value for money (1-5)", "How likely are you to recommend Beppu to a friend? (1-5)",
              "What did you enjoy most?", "What could be improved?"]
    rows = []
    start = datetime(2026, 7, 20, 9, 0)
    for n in range(1, 121):
        origin = weighted(ORIGINS)
        domestic = origin.startswith("Japan")
        purpose = random.choice(PURPOSES)
        nights = random.choices(NIGHTS, weights=[3, 4, 3, 2] if domestic else [1, 3, 4, 3])[0]
        lang = likert(4.4 if domestic else 2.7)
        getting = likert(3.6 if domestic else 3.0)
        onsen = likert(4.4)
        value = likert(3.6 if nights != "Day trip" else 3.2)
        overall = likert((onsen + getting + lang + value) / 4 + 0.3)
        recommend = likert(overall + 0.1)
        ts = start + timedelta(minutes=random.randint(0, 60 * 24 * 40))
        row = [ts.strftime("%Y/%m/%d %I:%M:%S %p GMT+9"), f"respondent{n:03d}@example.com",
               random.choice([f"Respondent {n}", "", ""]), random.choice(AGES), origin, purpose, nights,
               overall, onsen, getting, lang, value, recommend,
               random.choice(ENJOY[purpose]), random.choice(IMPROVE_DOM if domestic else IMPROVE_INTL)]
        if random.random() < 0.04:
            row[random.choice([9, 11])] = ""  # skipped question
        rows.append(row)
    rows.sort(key=lambda r: datetime.strptime(r[0][:-6], "%Y/%m/%d %I:%M:%S %p"))
    rows.insert(41, list(rows[40]))  # one duplicate submission, as happens in real forms
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUT}")


if __name__ == "__main__":
    main()
