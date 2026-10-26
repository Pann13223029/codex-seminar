# 03: Verify and disclose

Codex is fast and usually right, which is exactly why mistakes slip
through. Your name is on the work, so the checking is yours.

## The checklist

Before you use any result:

- [ ] **Recompute two numbers by hand.** Open the data in Excel or Google
      Sheets, filter, count, divide. Do they match?
- [ ] **Check the definition.** What exactly was counted? ("Has a generator"
      can mean installed capacity above zero, or electricity produced above
      zero. They give different answers.)
- [ ] **Check missing values.** Were blanks treated as zero, dropped or kept?
      Ask: `How did you treat missing values, and how would the result change if you treated them differently?`
- [ ] **Ask what could be wrong.**
      `List three ways this result could be wrong and test each one.`
- [ ] **Check every reference yourself.** Search for each one. AI can invent
      references that look real.
- [ ] **Read every sentence you submit.** If you cannot explain a sentence in
      your own words, rewrite it or remove it.

## What not to hand over

- **Your judgement.** The research question, which result matters, and what
  it means are your decisions.
- **Facts you have not checked.** Codex can state things from memory that
  are out of date or wrong. Ask for the source and look at it.
- **Private or restricted data.** See the privacy note in the README.

## Disclose it

APU treats undisclosed AI assistance as a possible form of plagiarism. Check
your course or supervisor's rules, then say plainly what the AI did and what
you did. A template:

```text
During the preparation of this [thesis/report], the author used [OpenAI Codex] for [writing and running analysis code / organizing notes / language revision / drafting parts of section X]. The author designed the analysis, checked the data and results, reviewed and edited all AI-assisted material, and takes full responsibility for the content.
```

You can ask Codex to draft it, then edit it so it is true:

```text
Look at what we did in this project. Draft a two-sentence AI-use statement saying what you did and what I checked myself. Do not exaggerate either part.
```

Next: [04: Make a skill](../04-make-a-skill/)
