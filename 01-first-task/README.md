# 01: Your first task

Time: about 5 minutes. Goal: see how an agent differs from a chatbot, and
learn to review and undo its changes.

## 1. Give Codex something to work with

In your workshop folder, copy and paste:

```text
Create a file called notes.md with five made-up seminar meeting notes, each with a date, three bullet points and one action item. Then tell me what you created.
```

Codex writes a real file in your folder. Open it to check.

## 2. Ask it to change the file

```text
Rewrite notes.md so all action items are collected in a table at the top, with columns Date, Action and Owner. Keep the original notes below the table.
```

## 3. Review the change

Look at what changed before you accept it. If Git is installed, the app's
review panel shows the lines that were added and removed.

> Screenshot: `assets/screenshots/01-review.png`

Ask yourself: is this what I asked for? Did it change anything I did not ask
it to change?

## 4. Undo it

```text
Undo your last change to notes.md and confirm the file is back to how it was.
```

Then open the file and check for yourself.

## What just happened

| Chatbot | Agent (Codex) |
| --- | --- |
| Answers in the chat | Reads, writes and runs files in your folder |
| You copy results out | Results are saved where you work |
| Easy to forget what it changed | You can review every change and undo it |

## Three habits from day one

1. **One folder per project.** Codex only sees that folder.
2. **Read before you accept.** You are responsible for what is in the folder.
3. **Ask, do not assume.** If you are not sure what Codex did, ask it:
   `What exactly did you change, and why?`

Next: [02: Work on your own project](../02-your-project/), or the
[follow-my-example track](../99-follow-my-example/) if you have no project.
