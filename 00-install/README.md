# 00: Install and sign in

Time: about 5 minutes.

## 1. Install the ChatGPT desktop app

Download the app for your system from the
[official quickstart](https://learn.chatgpt.com/docs/quickstart). It is
available for macOS, Windows and Linux.

<!-- Screenshot to add: ![](../assets/screenshots/00-download.png) -->

## 2. Sign in

Open the app and sign in with your ChatGPT account. A Free account works;
paid plans allow more Codex use.

## 3. Open a folder

Create an empty folder for this workshop, for example `codex-practice` in
your Documents folder. Then open it in the app:

- **macOS:** press `⌘ O`, or use the open-folder option.
- **Windows:** choose **Add new project**, or press `Ctrl O`.

Codex works **inside the folder you choose**. To change anything outside it, it must ask your permission first.

<!-- Screenshot to add: ![](../assets/screenshots/00-open-folder.png) -->

## 4. Switch to Codex

In the ChatGPT dropdown, select **Codex**, then start a **New chat**.

<!-- Screenshot to add: ![](../assets/screenshots/00-select-codex.png) -->

## 5. Choose the model and effort

Below the message box there is a **model and reasoning control**.

- **Free and Go plans:** Codex uses **GPT-6 Luna**, OpenAI's most efficient
  model. You do not need to change anything.
- **Plus or higher:** you can pick other models. For this workshop, choose
  **GPT-6 Luna** too: it handles these tasks well and uses the least of your
  allowance. Leave **Astra**, **Max** and **Ultra** for very hard work.

**Reasoning effort** is how long the model thinks before acting:

| Setting | Use it for |
| --- | --- |
| **Light** | Quick, clear jobs: explain a file, rename things, tidy notes |
| **High** | The analysis and slide steps in this workshop (OpenAI's suggested start for Luna) |

More effort uses more of your allowance, so match it to the task.
([Official model guide](https://learn.chatgpt.com/docs/models))

<!-- Screenshot to add: ![](../assets/screenshots/00-model-control.png) -->

## 6. Check it works

Copy and paste:

```text
What folder are you working in, and what files can you see? Do not change anything.
```

Codex should name your folder and say it is empty.

## Recommended: install Git

Git lets the app show exactly what Codex changed and lets you undo it.

- **macOS:** open Terminal and run `git --version`; if Git is missing, macOS
  offers to install it.
- **Windows:** install [Git for Windows](https://git-scm.com/download/win)
  with the default options.

You can also ask Codex: `Is Git installed on this computer? If not, tell me how to install it, but do not install anything yourself.`

## Get ready for the data tracks: Python

Tracks 98 and 99 and the data skills use **Python** with two add-ons,
**pandas** and **matplotlib**. Let Codex check for you. Copy and paste:

```text
Check whether Python, pandas and matplotlib are installed on this computer. If Python itself is missing, explain step by step how to install it on my system (Windows or Mac), then stop. If only pandas or matplotlib is missing, ask my permission, then install them with pip for my user account.
```

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
