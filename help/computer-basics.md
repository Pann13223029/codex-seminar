**English** · [日本語](computer-basics.ja.md)

# Computer basics for this workshop

Short how-tos for the everyday steps the guides assume. Pick your system.

## Unzip the downloaded repository

- **Mac:** double-click `codex-seminar-main.zip` in Downloads. A folder
  `codex-seminar-main` appears next to it.
- **Windows:** right-click `codex-seminar-main.zip` → **Extract All…** →
  **Extract**. Windows often makes a folder inside a folder:
  `codex-seminar-main\codex-seminar-main`. Open the inner one; that is the
  one with `README.md` in it.

## See hidden folders (like `.agents`)

Folders whose names start with a dot are hidden. You do not need to open
them, but if you want to look:

- **Mac (Finder):** press `⌘ ⇧ .` (Command, Shift, full stop). Press again to
  hide them.
- **Windows (File Explorer):** **View → Show → Hidden items**.

## Open a CSV file in a spreadsheet

- **Excel (Windows or Mac):** open Excel, then **File → Open** and choose
  the `.csv` file. (Double-clicking may open it in another app.)
- **Google Sheets:** open a blank sheet, then **File → Import → Upload**,
  choose the file, and pick **Replace current sheet**.
- **Mac Numbers** also works, but the steps below use Excel or Sheets.

## Count rows without filters: use a formula

The easiest way to check a number by hand is a `COUNTIFS` formula. Click an
empty cell to the right of the data and type the formula, then press Enter.
It works the same in Excel and Google Sheets.

**Track 99** (incinerator data: column A is `fiscal_year`, column H is
`power_capacity_kw`):

| What | Formula | Expected |
| --- | --- | --: |
| FY2024 records | `=COUNTIF(A:A,2024)` | 1014 |
| FY2024 records with a generator | `=COUNTIFS(A:A,2024,H:H,">0")` | 417 |
| The share | `=COUNTIFS(A:A,2024,H:H,">0")/COUNTIF(A:A,2024)` | 0.411 (41.1%) |

**Track 98** (survey: column E is "Where are you visiting from?", column K
is "Information available in my language"):

| What | Formula | Expected |
| --- | --- | --: |
| Domestic answers | `=COUNTIF(E:E,"Japan*")` | 60 |
| Domestic answers rating 4 or 5 | `=COUNTIFS(E:E,"Japan*",K:K,">=4")` | 51 |
| The share | `=COUNTIFS(E:E,"Japan*",K:K,">=4")/COUNTIF(E:E,"Japan*")` | 0.85 (85%) |

`"Japan*"` means "starts with Japan". `">0"` means "greater than zero";
blank cells are not counted.

## Count rows with filters (the other way)

- **Excel:** click any cell in the data, then **Data → Filter**. Click the
  arrow on a column heading, choose **Number Filters → Greater Than…** (or
  **Text Filters → Begins With…**). The count of visible rows appears at
  the bottom left ("x of y records found").
- **Google Sheets:** **Data → Create a filter**, click the filter icon on a
  column heading → **Filter by condition**. Select the column to see the
  **Count** at the bottom right.

## Open a terminal (only for the optional Codex CLI)

- **Mac:** press `⌘ Space`, type **Terminal**, press Enter.
- **Windows:** press the Windows key, type **PowerShell**, press Enter.

You do not need a terminal for anything else in this workshop.
