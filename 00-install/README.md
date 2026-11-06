# 00: Install and sign in

Time: about 5 minutes.

## 1. Install the ChatGPT desktop app

Download the app for your system from the
[official quickstart](https://learn.chatgpt.com/docs/quickstart). It is
available for macOS, Windows and Linux (Linux is in preview).

## 2. Sign in

Open the app and sign in with your ChatGPT account. A Free account works;
paid plans allow more Codex use.

## 3. Open a folder

Create an empty folder for this workshop, for example `codex-practice` in
your Documents folder. Then open it in the app: press `⌘ O` (macOS) or
`Ctrl O` (Windows) and choose the folder.

Codex works **inside the folder you choose**. To change anything outside it, it must ask your permission first.

## 4. Switch to Codex

In the ChatGPT dropdown, select **Codex**, then start a **New chat**.

## 5. Choose the model and effort

Below the message box there is a **model control**. Click it to see the
**Power** slider: **Faster** uses less of your allowance, **Smarter** thinks
longer. **Luna High** is one of the Power settings. To choose the model and
the reasoning effort yourself, open **Advanced**.

- **Free and Go plans:** Codex uses **GPT-6 Luna**, OpenAI's most efficient
  model. Choose **Luna High** if you see it; otherwise leave the default.
- **Plus or higher:** you can pick other models. For this workshop, choose
  **GPT-6 Luna** too: it handles these tasks well and uses the least of your
  allowance. Leave the **Astra** model, and the **Max** and **Ultra** effort
  levels, for very hard work.

**Reasoning effort** is how long the model thinks before acting:

| Setting | Use it for |
| --- | --- |
| **Light** (open **Advanced**, then choose Light) | Quick, clear jobs: explain a file, rename things, tidy notes |
| **High** (the **Luna High** setting) | The analysis and slide steps in this workshop (OpenAI's suggested start for Luna) |

More effort uses more of your allowance, so match it to the task.
([Official model guide](https://learn.chatgpt.com/docs/models))

## 6. Check it works

Copy and paste:

```text
What folder are you working in, and what files can you see? Do not change anything.
```

Codex should name your folder and say it is empty.

## Recommended: install Git

Git lets the app show exactly what Codex changed and lets you undo it.

- **macOS:** paste the prompt below. If Git is missing, macOS shows a
  window that offers to install it; click **Install**.
- **Windows:** install [Git for Windows](https://git-scm.com/download/win)
  with the default options.

Ask Codex: `Run git --version to check whether Git is installed. If it is not, tell me how to install it, but do not install anything yourself.`

## Get ready for the data tracks: Python

Tracks 98 and 99 and the data skills use **Python** with two add-ons,
**pandas** and **matplotlib**. Let Codex check for you. Copy and paste:

```text
Check whether Python, pandas and matplotlib are installed on this computer. If Python itself is missing, explain step by step how to install it on my system (Windows or Mac), then stop. If only pandas or matplotlib is missing, ask my permission, then install them with pip for my user account.
```

Installing needs the internet, so Codex will ask permission. Approve it.

- **Windows, if Python is missing:** install it from
  [python.org/downloads](https://www.python.org/downloads/). On the first
  installer screen tick **"Add python.exe to PATH"**. Then close and reopen
  the ChatGPT app and run the prompt again.
- **Mac, if Python is missing:** macOS may offer to install Apple's
  "command line developer tools". Accept, wait for it to finish, then run
  the prompt again.

## Optional: the terminal version (Codex CLI)

If you have a **Plus plan or higher** and are comfortable with a terminal,
Codex also runs there (the Free and Go plans include the desktop app only).
See the [official Codex CLI page](https://learn.chatgpt.com/docs/codex/cli). For
example, on macOS or Linux:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

or, if you use Homebrew or Node.js:

```bash
brew install --cask codex
```

```bash
npm install -g @openai/codex
```

Then run `codex` and choose **Sign in with ChatGPT**. Everything in this
workshop works in the app, so the terminal is not required.

Next: [01: Your first task](../01-first-task/)
