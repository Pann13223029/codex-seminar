---
name: ai-use-statement
description: Draft an honest AI-use statement (generative-AI disclosure) for a thesis, report, assignment or slide deck from what actually happened in this project, plus a one-line note for the last slide. Use when the user asks for an AI-use statement, AI disclosure, generative-AI declaration or the AI-use note on a slide. Do not use for summarizing results or writing other parts of the work.
---

# AI-use statement

Write a short, true statement of what the AI did and what the student did.
Undisclosed AI help can count as plagiarism, and an exaggerated statement is
as bad as none. Reply in the language the user writes in (for example
Japanese or English).

## Inputs

- The project folder: `AGENTS.md`, `outputs/ai-log.md` if it exists, and the
  files in `scripts/` and `outputs/`.
- What the user tells you: what they did and checked themselves, and their
  course or supervisor's rules on AI use.

## Steps

1. **Collect the evidence.** Read `AGENTS.md` and `outputs/ai-log.md` if
   they exist, and list the files in `scripts/` and `outputs/`. Show the
   user a short list of what the AI did in this project (for example "wrote
   scripts/clean.py", "drafted outputs/findings.md", "built
   outputs/deck/index.html"), each with the file or log line it comes from.
   Do not change any file yet.
2. **Ask, in one short list, and wait for the answers:**
   - What did you check yourself, and how? (For example "counted the main
     percentage in a spreadsheet".)
   - What did you decide or write yourself? (For example the question, the
     definitions, the interpretation.)
   - Where does the statement go, and do your course rules give required
     wording or a length?
   - Which tool and model did you use, and in which month? Suggest "OpenAI
     Codex (GPT-6 Luna)" only if the user confirms it.
3. **Draft two versions.**
   - **For the report:** two or three sentences. Follow the course wording
     if the user gave one; otherwise use this pattern: "During the
     preparation of this [work], the author used [tool, model] in [month
     year] for [what the AI did]. The author [what the student did and
     checked], reviewed and edited all AI-assisted material, and takes full
     responsibility for the content."
   - **For the last slide:** one line, for example "AI use: OpenAI Codex
     wrote the analysis code and drafted these slides; I checked the main
     numbers by hand."
4. **Check every claim.** Under the drafts, list each claim with its
   evidence: a file, a log line, or "you told me". Mark any claim without
   evidence `[CHECK]`.
5. **Save only if asked.** Offer to save both versions to
   `outputs/ai-use-statement.md`. If that file exists, ask before replacing
   it. If the user asks to put the note on a slide, change only the AI-use
   note on the last slide and nothing else.
6. **Remind the user** to rewrite the statement in their own words if they
   want, and to check it against their course rules.

## Rules

- Never claim the user checked, wrote or decided something they did not
  tell you.
- Never play down what the AI did. If the AI wrote code, text or slides,
  say so.
- Never invent course rules, policies or deadlines. If the user does not
  know their rules, tell them to ask their supervisor.
- Keep it short and plain. No promotional or defensive wording.
