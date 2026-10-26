"""Build the follow-along dataset from the thesis panel (run inside the thesis repo).

Source: Ministry of the Environment Japan, General Waste Treatment Survey
(facility workbooks, FY2005 and FY2024), via e-Stat. Records were parsed and
de-duplicated for the author's graduation thesis; this file keeps only the
columns the workshop needs, with English labels.

Usage (from the thesis repo root):
    python /path/to/codex-seminar/tools/build_dataset.py
"""

from pathlib import Path

import pandas as pd

PREFECTURES = [
    ("北海道", "Hokkaido"), ("青森県", "Aomori"), ("岩手県", "Iwate"), ("宮城県", "Miyagi"),
    ("秋田県", "Akita"), ("山形県", "Yamagata"), ("福島県", "Fukushima"), ("茨城県", "Ibaraki"),
    ("栃木県", "Tochigi"), ("群馬県", "Gunma"), ("埼玉県", "Saitama"), ("千葉県", "Chiba"),
    ("東京都", "Tokyo"), ("神奈川県", "Kanagawa"), ("新潟県", "Niigata"), ("富山県", "Toyama"),
    ("石川県", "Ishikawa"), ("福井県", "Fukui"), ("山梨県", "Yamanashi"), ("長野県", "Nagano"),
    ("岐阜県", "Gifu"), ("静岡県", "Shizuoka"), ("愛知県", "Aichi"), ("三重県", "Mie"),
    ("滋賀県", "Shiga"), ("京都府", "Kyoto"), ("大阪府", "Osaka"), ("兵庫県", "Hyogo"),
    ("奈良県", "Nara"), ("和歌山県", "Wakayama"), ("鳥取県", "Tottori"), ("島根県", "Shimane"),
    ("岡山県", "Okayama"), ("広島県", "Hiroshima"), ("山口県", "Yamaguchi"), ("徳島県", "Tokushima"),
    ("香川県", "Kagawa"), ("愛媛県", "Ehime"), ("高知県", "Kochi"), ("福岡県", "Fukuoka"),
    ("佐賀県", "Saga"), ("長崎県", "Nagasaki"), ("熊本県", "Kumamoto"), ("大分県", "Oita"),
    ("宮崎県", "Miyazaki"), ("鹿児島県", "Kagoshima"), ("沖縄県", "Okinawa"),
]
OPERATION = {"全連続運転": "continuous", "准連続運転": "semi-continuous", "バッチ運転": "batch"}
OUT = Path(__file__).resolve().parents[1] / "99-follow-my-example" / "data" / "incinerators_fy2005_fy2024.csv"


def main() -> None:
    panel = pd.read_csv("data/processed/incineration_panel_identified.csv", low_memory=False)
    panel = panel[panel["fiscal_year"].isin([2005, 2024])].copy()
    names = dict(PREFECTURES)
    if set(panel["prefecture"]) - set(names):
        raise SystemExit(f"Unmapped prefectures: {set(panel['prefecture']) - set(names)}")
    out = pd.DataFrame({
        "fiscal_year": panel["fiscal_year"],
        "prefecture": panel["prefecture"].map(names),
        "facility_id": panel["stable_site_id"],
        "year_started": panel["year_started"],
        "capacity_t_day": panel["capacity_t_day"],
        "throughput_t_year": panel["throughput_t_year"],
        "operation_mode": panel["operation_mode"].str.strip().map(OPERATION),
        "power_capacity_kw": panel["power_capacity_kw"],
        "power_generated_mwh": panel["power_generated_mwh"],
    })
    out = out.sort_values(["fiscal_year", "prefecture", "facility_id"]).reset_index(drop=True)
    out.to_csv(OUT, index=False)
    print(f"Wrote {len(out)} rows to {OUT}")


if __name__ == "__main__":
    main()
