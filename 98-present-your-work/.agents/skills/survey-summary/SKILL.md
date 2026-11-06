---
name: survey-summary
description: Summarize a survey export (Google Forms, Microsoft Forms, Qualtrics CSV) with rating-scale and open-ended questions into tables, charts and themed quotes, after removing personal data. Use when the user asks to analyse, summarize or report survey or questionnaire responses. Do not use for other data files (use data-explore).
---

# Survey summary

Turn a survey export into a checked summary a seminar can present. The user
may not program; explain each step in plain English.

## Inputs

- A survey export (CSV or Excel) in the project folder.
- What the user wants to learn, and which groups to compare (for example
  domestic and international visitors). Ask if this is not clear.

## Steps

0. **Check the tools.** Check that Python with pandas and matplotlib is
   available. If Python itself is missing, explain in plain English how to
   install it on the user's system (Windows or Mac) and stop. If only pandas
   or matplotlib is missing, ask permission, then install them with pip for
   the user's account. Never install anything without their OK.
1. **Protect respondents first.** Before any analysis, find columns with
   personal data (email, name, phone, student ID, free-text that names
   people). Write `scripts/anonymize.py` that saves
   `outputs/responses_anonymous.csv` without them, with a respondent number
   instead. Never print personal data in the chat. Tell the user which
   columns were removed. Never change the original export.
2. **Describe the survey.** List each question, its type (single choice,
   rating 1-5, open text) and its number of answers and blanks. Report
   duplicate submissions (identical rows, or the same respondent twice) and
   ask whether to remove them.
3. **Rating questions.** For each rating question report the number of
   answers, the mean, and the share answering 4 or 5. Show the full
   distribution (how many 1s, 2s, 3s, 4s, 5s), because a mean alone hides it.
   Compare groups only if each group has at least 20 answers; otherwise say
   the group is too small to compare.
4. **Choice questions.** Frequency tables with counts and percentages, and
   cross-tabs against the comparison groups.
5. **Open-ended questions.** Read every answer. Group them into 3-6 themes,
   count how many answers fall in each, and quote 1-2 real answers per theme
   word for word. Never invent or "improve" a quote. Note empty answers.
6. **Charts.** At most four PNG charts in `outputs/`: stacked or grouped
   bars for rating distributions, bars for theme counts. Plain titles, axis
   labels, number of respondents in each caption.
7. **Write the summary.** Save `outputs/survey_summary.md` with: who
   answered (number, groups), 3-5 key findings each with its number, the
   theme table with quotes, the decisions made (duplicates, blanks),
   limitations (who did not answer, sample size, self-reported opinions), and
   a one-line note of what was done with AI assistance.
8. **Hand-check.** Give one number to verify by hand in a spreadsheet, with
   exact steps.

## Rules

- No personal data in outputs, charts or chat.
- Every number must come from a script you ran. Name it.
- Quotes must be exact and must not identify anyone.
- A survey shows what respondents said, not what all visitors think.
  Never generalize beyond the people who answered.
