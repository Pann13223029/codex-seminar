---
name: presentation-page
description: Build a clean HTML slide deck (one file, works offline, saves as PDF) from a findings memo, survey summary or the user's notes, using the bundled template and design guide. Use when the user asks for slides, a deck or a presentation of their work. Do not use to analyse data (use data-explore or survey-summary first).
---

# Presentation page

Turn content the user has already written and checked into a slide deck
that looks considered, not generic. The user may not program; explain each
step in plain English.

## Inputs

- A findings memo, survey summary or notes in the project folder. If there
  is none, ask the user for their main points; do not invent content.
- Audience, talk length in minutes, and theme: `editorial`, `bold` or
  `field`. Ask if not given, and suggest one theme in a single sentence.

## Steps

1. **Read the guide.** Read `references/design-guide.md` in this skill
   folder before planning.
2. **Outline first.** Propose a slide list: about one slide per minute,
   each with its layout (title, statement, big number, bar chart, compare,
   points, quote, chart image, table, sources) and its title written as a
   full-sentence takeaway. Show which number from the memo each slide uses.
   Put the most important finding in the first two slides. When a slide
   compares two ways of calculating, its title says which result is correct
   and why, and the accent goes on the correct number. Use the memo's exact
   terms; do not swap similar ones. Wait for the user's OK.
3. **Build.** Copy `assets/deck-template.html` from this skill folder to
   `outputs/deck/index.html`. Set the theme with `data-theme` on `<html>`,
   the `<title>` and the footer text. Replace the example slides with the
   approved slides, using only the template's layouts and classes. Delete
   unused example slides. Copy any chart images into `outputs/deck/`.
4. **Bar charts.** For the bar layout set `--v` on each bar to the value as
   a percentage of the largest value shown, and put the real value in the
   `val` label. Mark the bar that matters with `class="bar key"`.
5. **Check.** Go through the checklist at the end of the design guide and
   report each item as done or not done. Every number must match the memo;
   list each number with where it came from.
6. **Tell the user how to use it:** double-click `outputs/deck/index.html`
   to open it in a browser; arrow keys move; F is full screen; to save a
   PDF, print from Chrome or Edge with Destination "Save as PDF", then
   under "More settings" set Margins to "None" and tick "Background
   graphics".

## Rules

- Never add numbers, quotes, references or claims that are not in the
  user's files. If a slide needs something missing, ask.
- Keep the template's fonts, colours and layouts. No external fonts,
  images or scripts from the internet, so the file works offline.
- Keep the AI-use note on the last slide; the user may edit its wording.
