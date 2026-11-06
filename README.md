# Codex for Research: a Seminar Workshop

Use Codex, OpenAI's coding agent, to do real research work in a folder on your
own laptop: read data, write and run analysis code, make charts and draft
notes, while you stay in charge of every decision and check the results.

Seminar session by Pann Phetra (College of Sustainability and Tourism,
Ritsumeikan Asia Pacific University).

**Slides:** [view as PDF](slides/codex-for-research.pdf) · [open the web version](https://pann13223029.github.io/codex-seminar/slides/) · [all options](slides/)

## What you need

1. A **ChatGPT account**. The **Free plan is enough** for this workshop:
   it includes Codex in the desktop app with **GPT-6 Luna**, OpenAI's most
   efficient model, with usage limits (still rolling out, so a few accounts may not see it yet)
   ([Codex pricing](https://learn.chatgpt.com/docs/pricing),
   [models](https://learn.chatgpt.com/docs/models)). Everything here was
   tested with Luna.
2. A laptop running **macOS, Windows or Linux** with the **ChatGPT desktop
   app** installed ([official quickstart](https://learn.chatgpt.com/docs/quickstart)).
3. Optional but recommended: **Git**. The app uses it to show what Codex
   changed and to undo changes.
4. Either your own seminar project in a folder, or nothing at all: the
   [follow-my-example track](99-follow-my-example/) gives you data and
   copy-and-paste prompts.

> **On the Free plan?** Usage is limited, so keep each chat to one task,
> use the **Light** reasoning setting for quick jobs, and draft long prompts
> in a free chat first. See [make your usage last](prompt-guide/#make-your-usage-last).

> **Privacy:** do not put personal data, interview transcripts, unpublished
> data you are not allowed to share, or passwords into a folder you open with
> Codex. Treat it like sending the files to an outside service.

> **Academic integrity:** undisclosed AI help can count as plagiarism under
> university rules, including APU's. Check your course rules, and if AI helps
> with a thesis or assignment, say so. Step 03 shows how.

> **Stuck on a basic step** (unzipping, hidden folders, opening a CSV,
> counting rows)? See [computer basics](help/computer-basics.md).

## Your route through the workshop

```mermaid
flowchart TD
    A["00 Install and sign in"] --> B["01 First task"]
    B --> PG["Prompting guide<br/>six parts of a good prompt"]
    PG --> C{"Do you have your own project?"}
    C -- "Yes" --> K["04 Part A<br/>Install the example skills"]
    K --> D["02 Work on your project"]
    D --> E["03 Verify and disclose"]
    E --> F["04 Parts B to D<br/>Make your own skill"]
    C -- "No" --> G{"Data or a survey?"}
    G -- "Data" --> G1["99 Follow my example<br/>public incinerator data,<br/>skills included"]
    G -- "Survey" --> G2["98 Present your work<br/>practice survey to slides,<br/>skills included"]
    F --> H(["Finished: a result you checked,<br/>slides and an AI-use statement"])
    G1 --> H
    G2 --> H
```

## How you will work with Codex

Every task follows the same loop. You stay in charge of the two decision
points.

```mermaid
flowchart TD
    B["Brief<br/>AGENTS.md"] --> P["Plan<br/>Codex proposes"]
    P --> OK{"You approve?"}
    OK -- "No, change it" --> P
    OK -- "Yes" --> S["One small step<br/>Codex does it"]
    S --> C{"You check it"}
    C -- "Wrong, undo" --> S
    C -- "Right" --> N["Next step"]
    N --> P
```

## Follow the workshop

| Open | What you will do |
| --- | --- |
| [00: Install and sign in](00-install/) | Install the ChatGPT desktop app, sign in, open Codex. |
| [01: Your first task](01-first-task/) | Open a folder, ask Codex to explain it, review a change and undo it. |
| [Prompting guide](prompt-guide/) | The six parts of a good prompt, before-and-after examples, and a prompt builder for any free chatbot. |
| [02: Work on your own project](02-your-project/) | Write a short brief, ask for a plan first, then work in small steps. |
| [03: Verify and disclose](03-verify-and-disclose/) | Check the results yourself and write an AI-use statement. |
| [04: Skills, step by step](04-make-a-skill/) | Install the example skills, use one, and make your own, all by copy-and-paste prompts. |
| [98: Present your work](98-present-your-work/) | A practice survey → checked summary → slides and PDF, with two example skills. |
| [99: Follow my example](99-follow-my-example/) | Repeat a small version of my thesis analysis with the example skills, then make your own skill. |
| [Example skills](skills/) | `data-explore`, `survey-summary` and `presentation-page`, ready to install. |

Follow **00 → 01 → Prompting guide**, then either your own project
(**04 Part A → 02 → 03 → 04 Parts B to D**) or a practice track: **98**
(survey to slides) or **99** (data analysis). The practice tracks already
include the example skills, so there is nothing to install.

## Words used here

- **Agent:** an AI that can act in your folder (read files, write files, run
  programs) instead of only answering in a chat.
- **Prompt:** the instruction you type.
- **Brief (`AGENTS.md`):** a file of standing instructions Codex reads before
  every task in that folder.
- **Skill:** a saved, reusable workflow (a folder with a `SKILL.md` file) that
  Codex can run again on request.

## About the screenshots

Each step has marked places for screenshots (`assets/screenshots/`). Codex
changes quickly, so if a button looks different from the text, follow the
linked official page.
