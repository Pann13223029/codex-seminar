# Speaker notes: Codex for Research (45 minutes)

Present from the web version (https://pann13223029.github.io/codex-seminar/slides/)
or open `slides/index.html` in a browser. The PDF (`codex-for-research.pdf`) is
the backup if a browser or projector misbehaves. Arrow keys move; **F** is full
screen; `#N` in the address jumps to slide N.

| # | Slide | Time | Running |
| --: | --- | --: | --: |
| 1 | Title | 1:00 | 1:00 |
| 2 | Chatbot vs agent | 1:30 | 2:30 |
| 3 | What you need | 1:00 | 3:30 |
| 4 | Install in five steps (live demo) | 3:30 | 7:00 |
| 5 | On the Free plan: make your usage last | 1:30 | 8:30 |
| 6 | The way of working | 1:30 | 10:00 |
| 7 | AGENTS.md | 1:30 | 11:30 |
| 8 | A good prompt has six parts | 2:30 | 14:00 |
| 9 | Let a free chatbot write the prompt | 2:00 | 16:00 |
| 10 | Example 1: my thesis | 2:00 | 18:00 |
| 11 | Who did what | 2:30 | 20:30 |
| 12 | Make mistakes hard to miss | 2:00 | 22:30 |
| 13 | Example 2: capstone | 2:00 | 24:30 |
| 14 | Ask who is buying | 2:00 | 26:30 |
| 15 | One rule for blanks | 2:00 | 28:30 |
| 16 | Three example skills | 2:30 | 31:00 |
| 17 | Make your own skill | 2:00 | 33:00 |
| 18 | Slides that do not look AI-generated | 2:00 | 35:00 |
| 19 | Your turn: the guide | 2:00 | 37:00 |
| 20 | Before you use any result | 1:30 | 38:30 |
| 21 | Four ways to get it wrong | 1:00 | 39:30 |
| 22 | Thanks and questions | 5:30 | 45:00 |

## Talking points

**1. Title.** One line: today you leave with Codex installed and a way of
working that keeps you in charge.

**2. Chatbot vs agent.** The difference is that Codex acts in a folder: it
reads, writes and runs files. That is why it is useful, and why you review
what it did.

**3. What you need.** Free account works. Point to the GitHub guide; they can
follow along now or later.

**4. Install (live).** Open the app, sign in, open an empty folder, choose
Codex, New chat. Type: "What folder are you working in, and what files can
you see? Do not change anything." If the demo fails, move on: step 00 of the
guide has it.

**5. Free plan.** Most of you are on Free: Codex runs GPT-6 Luna, the
efficient model, with limited usage. One task per chat, Light effort for
quick jobs, plan first, draft prompts in a regular chat. Plus users: stay on
Luna today.

**6. The loop.** Brief, plan, one small step, check, next. Most bad
experiences come from skipping the plan or the check.

**7. AGENTS.md.** A file of standing instructions Codex reads before every
task. Show the rules: plan first, never change original data, every number
from code you ran, never invent references.

**8. Six parts.** Goal, Context, Task, Output, Checks, Limits. Read one
"vague vs better" pair from the prompting guide aloud. For quick questions
two parts are enough; for anything that changes files, use all six.

**9. Prompt builder.** Paste the prompt builder into a free chatbot; it
interviews you and writes the six-part prompt. Saves Codex usage and forces
you to think. Two cautions: it cannot see your files, so it uses
[placeholders]; never paste private data into it.

**10. Thesis.** The question: 4 in 10 plants generate, is that low? By waste
it is 8 in 10. The work: 20 years of Ministry spreadsheets, 23,593 records
linked into 1,690 plant histories even though the official IDs broke twice.

**11. Who did what.** Be concrete about the split. The AI helped write the
code and drafts; I set the question and definitions, checked the numbers,
and decided what the results mean. The thesis declares this.

**12. Checks.** Tests that run every time, a build that refuses to finish if
a number in the text drifts from the results, and a mock examiner. The point
for them: make your own mistakes hard to miss.

**13. Capstone.** Google Merchandise Store analytics. Three surprises:
employees were 41% of revenue, Google's own teaching model ranked mostly
staff as likely buyers, and one corporate account made Display look good.

**14. Lesson.** Asking "who is actually buying?" mattered more than model
choice. And the honest part: the AI stated facts from memory, twice wrongly;
checking the original source caught it.

**15. Blanks.** The same data, two rules for blanks: 41.1% or 99.5%. Students
meet this in the follow-along track, so it is a preview.

**16. Three example skills.** data-explore for any spreadsheet,
survey-summary for form exports, presentation-page for slides. They chain:
data, checked memo, slides. Installing is one pasted prompt (step 04).

**17. Make your own.** `$skill-creator` with one prompt; Codex asks a few
questions and writes the file. Test with `$meeting-notes`, then improve it
with another prompt. No file editing by hand.

**18. Design.** Three themes so decks differ but never look sloppy. Titles
state the takeaway; one accent per slide; every number from the memo. The
"don't" list is what makes slides look AI-generated.

**19. Your turn.** Walk the table: install, prompting guide, skills, then
your own project or a practice track (98 survey, 99 thesis data).

**20. Verify and disclose.** Read the checklist aloud. Undisclosed AI help
can count as plagiarism, so check your course rules; step 03 has a template.

**21. Pitfalls.** Private data, invented references, trusting confident
answers, handing over the thinking.

**22. Close.** "Let the agent do the work. Keep the judgement." Then
questions.

## Likely questions

- **Is it free?** Yes: the Free plan includes Codex in the desktop app with
  GPT-6 Luna and usage limits. Paid plans add more models and more usage.
- **Do I need to code?** No. You need to read what it did and check results.
  Ask it to explain code in plain English.
- **Is it allowed for assignments?** Check your course rules and disclose the
  use. When unsure, ask the instructor before using it.
- **What about my data?** Only open folders with data you are allowed to
  share with an outside service.
- **Codex or Claude Code?** They work the same way: an agent in a folder with
  a brief and skills. This workshop uses Codex because every student can
  start free.
