# 00: Install and sign in

Time: about 5 minutes.

## 1. Install the ChatGPT desktop app

Download the app for your system from the
[official quickstart](https://learn.chatgpt.com/docs/quickstart). It is
available for macOS, Windows and Linux.

> Screenshot: `assets/screenshots/00-download.png`

## 2. Sign in

Open the app and sign in with your ChatGPT account. A Free account works;
paid plans allow more Codex use.

## 3. Open a folder

Create an empty folder for this workshop, for example `codex-practice` in
your Documents folder. Then open it in the app:

- **macOS:** press `⌘ O`, or use the open-folder option.
- **Windows:** choose **Add new project**, or press `Ctrl O`.

Codex can read and change files **only inside the folder you choose**.

> Screenshot: `assets/screenshots/00-open-folder.png`

## 4. Switch to Codex

In the ChatGPT dropdown, select **Codex**, then start a **New chat**.

> Screenshot: `assets/screenshots/00-select-codex.png`

## 5. Check it works

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

## Optional: the terminal version (Codex CLI)

If you are comfortable with a terminal, Codex also runs there. See the
[official Codex CLI page](https://learn.chatgpt.com/docs/codex/cli). For
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
