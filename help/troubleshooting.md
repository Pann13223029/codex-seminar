**English** · [日本語](troubleshooting.ja.md)

# When something goes wrong

Find your problem below. Most fixes are one prompt or one restart. For
unzipping, hidden folders and spreadsheets, see
[computer basics](computer-basics.md).

## Codex is not in my app

Free accounts may not have Codex yet
([pricing](https://learn.chatgpt.com/docs/pricing)). Update the ChatGPT
desktop app, sign out and in again, and check once more. Still missing?
Work with a neighbour today: you can follow every step on their screen and
repeat it later.

## I ran out of usage in the middle of a step

Your files are safe: everything Codex saved is still in your folder. When
your allowance resets (the app shows when), open the same folder, start a
**New chat**, and paste:

```text
Read AGENTS.md and look at the files in outputs/ and scripts/. Tell me which step of the guide I finished last and what the next step is. Do not change any files.
```

Until then, pair with a neighbour. To use less next time, see
[make your usage last](../prompt-guide/#make-your-usage-last).

## Codex says it cannot do something

Codex asks before it writes in a protected folder (`.git`, `.agents`),
writes outside your folder, or uses the internet. If it says it cannot and
did not ask, reply: `Please ask me for permission and try again.`

## A skill is not listed

Close and reopen the ChatGPT app, then type `$` in the message box. Still
missing? It was not installed: repeat
[04, Part A](../04-make-a-skill/#part-a-install-the-example-skills-5-minutes)
and approve the permission request.

## "python not found" (Windows)

- Install Python from [python.org/downloads](https://www.python.org/downloads/)
  and tick **"Add python.exe to PATH"** on the first screen.
- If typing `python` opens the Microsoft Store instead: open **Settings →
  Apps → Advanced app settings → App execution aliases** and turn off the
  two **python** entries.
- Close and reopen the ChatGPT app, then try again.

## "externally-managed-environment" when installing pandas (Mac)

Your Python does not allow installing add-ons for the whole computer. Ask
Codex to make a private copy for this project:

```text
Create a virtual environment in this folder called .venv, install pandas, matplotlib and openpyxl in it, and use it for every script in this project. Ask me for permission first.
```

## I installed Git or Python, but Codex cannot find it

Close the ChatGPT app completely and open it again. It only sees programs
that were installed before it started.

## Japanese text shows as empty boxes in a chart

The chart font has no Japanese letters. Paste:

```text
Remake the charts with a font that shows Japanese: Hiragino Sans on a Mac, Yu Gothic or Meiryo on Windows. Check that no label shows empty boxes.
```

## My Excel file will not open

Reading `.xlsx` files needs one more add-on. Paste:
`Install openpyxl for my user account so you can read Excel files. Ask me for permission first.`

## After unzipping there is a folder inside a folder (Windows)

Windows can make `codex-seminar-main\codex-seminar-main`. Open the inner
one, the folder that contains `README.md`.

## How do I open a `.md` file?

`.md` files (Markdown) are plain text. Open them with TextEdit (Mac) or
Notepad (Windows), or ask Codex: `Show me outputs/findings.md.`

## Codex changed something I did not want

If you saved a snapshot, ask: `Undo your last change and show me what you undid.`
See [step 01](../01-first-task/) for how snapshots work.
