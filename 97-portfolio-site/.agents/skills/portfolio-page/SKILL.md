---
name: portfolio-page
description: Build a one-page personal portfolio website for job hunting (one HTML file, works offline, ready for GitHub Pages) from the user's own CV, notes or an interview, using the bundled template and writing guide. Use when the user asks for a portfolio site, personal website or online CV. Do not use for slide decks (use presentation-page) or for analysing data.
---

# Portfolio page

Turn facts the user gives you into a clean one-page portfolio site they can
put online for job hunting. The user may not program and may be writing in
their second language; explain each step in plain language and keep them in
charge of every word that goes public. Reply in the language the user writes in (for example Japanese or English).

## Inputs

- Files in `me/`: a CV (PDF, Word or text), notes, or `me/profile.md`.
- The kind of job they want and when they can start. Ask if not given.
- Theme: `editorial`, `bold` or `field`, and whether they want a Japanese
  version as well as English. Ask if not given.

## Steps

1. **Privacy first.** Before anything else, read `me/`. Never copy any of
   these into the profile or the site: phone number, home address, date of
   birth, age, student ID, My Number or other ID numbers, grades unless the
   user asks, photos of other people, names of private clients or classmates
   without their permission. If you find them, say which kinds you found
   (not the values) and that you will leave them out.
2. **Fill `me/profile.md`.** If it does not exist, use
   `references/profile-template.md` from this skill folder as the form.
   Fill it only with facts from the user's files or
   answers. Ask about the empty parts **one question at a time**, in simple
   language, and at most about ten questions: ask only what is missing. For
   every story ask: when it happened, the problem, what the user did
   themselves, and the result. Do not take a story's dates from other
   dates, such as the degree. For every number ask how they know it. If
   there is no number, use plain words; never estimate one. In "Skills
   used", write only skills the user named; never add soft skills such as
   "attention to detail". Mark anything still missing with `[ADD]`. Do not
   ask about the theme or language here. Show the finished profile, ask the
   user to correct it, and save it only when they say OK. Then stop.
3. **Outline.** If `me/profile.md` exists and the user named the theme
   and language, go straight to the outline; do not ask them to confirm the
   profile again. Read `references/writing-guide.md`. Propose the page in a
   short list: the "Looking for" line, the one-sentence pitch, three proof
   stats, which 2-4 stories in which order (the most relevant to the target
   job first), and the theme. Show which line of `me/profile.md` each claim
   comes from. Wait for the user's OK.
4. **Build.** Copy `assets/site-template.html` from this skill folder to
   `site/index.html`. Replace every example text with the approved content.
   Delete parts the user does not need. Set `data-theme`, the `<title>`,
   the meta description and the `og:` lines. Copy only the photos the user
   put in `me/photos/` and approved into `site/`, each under 500 KB.
   - English only: delete every `<span lang="ja">` and the language button.
   - With Japanese: write a natural Japanese version of every English span,
     in polite です・ます style, and tell the user to have a native speaker
     check it.
5. **Check.** Report each item as done or not done:
   - no private information from step 1 anywhere in `site/`;
   - every claim is in `me/profile.md` (list each number with its line);
   - no words from the writing guide's "avoid" list;
   - every link is a full address that starts with `https://` or `mailto:`;
   - the footer has the AI-use note and the month it was updated;
   - nothing loads from the web (no external fonts, scripts or images).
6. **Tell the user what to do next:** double-click `site/index.html` to
   look at it, make the window narrow to see the phone layout, and follow
   the guide's "Go live" step to publish it.

## Rules

- Never invent facts, numbers, job titles, awards, skills or dates. If the
  user asks you to "make it sound better", improve the wording, not the
  facts.
- Write in the first person, in short sentences with plain verbs.
- Keep the template's layout, fonts and colours. No external fonts,
  scripts, trackers, analytics or images from the web.
- One page, one file: `site/index.html` (plus approved photos).
- The user decides what goes public. Ask before adding anything they did
  not give you.
