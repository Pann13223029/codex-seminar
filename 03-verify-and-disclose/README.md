**English** · [日本語](README.ja.md)

# 03: Verify and disclose

Codex is fast and usually right. Because of this, its mistakes are easy to
miss. Your name is on the work, so the checking is your job.

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
      `List three ways this result could be wrong, and test the most likely one.`
- [ ] **Check every reference yourself.** Search for each one. AI can invent
      references that look real.
- [ ] **Read every sentence you submit.** If you cannot explain a sentence in
      your own words, rewrite it or remove it.

## What stays your job

- **Your judgement.** The research question, which result matters, and what
  it means are your decisions.
- **Facts you have not checked.** Codex can state things from memory that
  are out of date or wrong. Ask for the source and look at it.
- **Private or restricted data.** See the privacy note in the README.

## Disclose it

Undisclosed AI help can count as plagiarism under university rules,
including APU's. Check your course or supervisor's rules, then say plainly
what the AI did and what you did. A template:

```text
During the preparation of this [thesis/report], the author used [OpenAI Codex] for [writing and running analysis code / organizing notes / language revision / drafting parts of section X]. The author designed the analysis, checked the data and results, reviewed and edited all AI-assisted material, and takes full responsibility for the content.
```

You can ask Codex to draft it, then edit it so it is true. Codex cannot
see what you checked outside the chat, so tell it:

```text
Look at what we did in this project (use outputs/ai-log.md if it exists). Draft a two-sentence AI-use statement saying what you did and what I did. I checked these myself: [what you checked by hand, for example "the main percentage in a spreadsheet"]. Do not exaggerate either part.
```

Next: [04: Skills, Parts B to D](../04-make-a-skill/#part-b-use-a-skill-5-minutes): use a skill and make your own.
