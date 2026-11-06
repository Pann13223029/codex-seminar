---
name: data-explore
description: Explore, clean and summarize a spreadsheet (CSV or Excel) into checked findings with charts. Use when the user asks to explore, understand, clean, summarize or chart a data file. Do not use for survey exports with free-text answers (use survey-summary) or for making slides (use presentation-page).
---

# Data explore

Turn one data file into a short, checked findings memo. The user is a
student who may not program, so explain every step in plain English.

## Inputs

- A data file (CSV or Excel) in the project folder. If there are several,
  ask which one.
- The question the user wants answered. If it is not clear, ask before
  analysing. Read AGENTS.md first if it exists.

## Steps

0. **Check the tools.** Check that Python with pandas and matplotlib is
   available. If Python itself is missing, explain in plain English how to
   install it on the user's system (Windows or Mac) and stop. If only pandas
   or matplotlib is missing, ask permission, then install them with pip for
   the user's account. Never install anything without their OK.
1. **Describe before touching.** Report rows and columns, what each column
   seems to mean, data types, and for each column the number of blanks,
   zeros and unusual values (negative numbers, impossible dates, typos in
   categories). Do not change any file yet.
2. **Ask about the decisions that change answers.** Before calculating,
   ask the user to confirm, in one short list:
   - how blanks should be treated (as zero, as "not reported", or dropped),
     and say how much the main result would change between these choices;
   - what counts as a duplicate, and how many you found;
   - the exact definition of each measure (for example "has a generator =
     capacity above zero").
   Wait for answers. If AGENTS.md already defines these, use it and say so,
   but still report the result under the other blank rule and explain in
   one sentence why the two differ.
3. **Clean into a new file.** Never change the original. Write a small
   Python script in `scripts/` (pandas, matplotlib) that saves the cleaned
   data to `outputs/clean_<name>.csv` and prints a log of every change
   (rows removed and why, values recoded).
4. **Answer the question.** Calculate only what the question needs. Save the
   numbers to `outputs/results.csv`. Show the key numbers in a small table.
5. **Chart.** Make at most three charts in `outputs/` (PNG), each with a
   plain-language title, labelled axes with units, and the data source in a
   caption. Prefer bar and line charts. No 3D, no pie charts with more than
   four slices.
6. **Hand-check.** Take the number behind the main finding and give a
   `COUNTIFS` formula for Excel or Google Sheets, with the column letters of
   the original file and the expected result.
7. **Write the memo.** Save `outputs/findings.md` with:
   - the question, the data source and the number of rows used;
   - 3-5 findings, each one sentence with its number and the file that
     produced it;
   - the decisions from step 2, and, when a decision changes the answer a
     lot, which result is correct and why;
   - limitations: what the data cannot show (causes, people or places not in
     the data);
   - a one-line note of what was done with AI assistance.

## Rules

- Every number in the memo must come from a script you ran. Name the script.
- Never invent data, sources or explanations. Say "the data does not show
  this" when that is the honest answer.
- Do not claim causes from patterns. Use "is associated with", "is higher
  among".
- Keep the user in charge: plan first, then one step at a time.
