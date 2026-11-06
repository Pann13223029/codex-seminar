**English** · [日本語](README.ja.md)

# 01: Your first task

Time: about 5 minutes. Goal: see how an agent differs from a chatbot, and
learn to review and undo its changes.

## 1. Give Codex something to work with

In your workshop folder, copy and paste:

```text
Create a file called notes.md with five made-up seminar meeting notes, each with a date, three bullet points and one action item. Then tell me what you created.
```

Codex writes a real file in your folder. Open it to check, or ask Codex:
`Show me notes.md`.

> **No Git?** Skip steps 2 and 5. In step 4, ask Codex what it changed.

## 2. Save a snapshot

A snapshot (Git) lets you see exactly what Codex changes later, and undo it.
It needs Git (see [step 00](../00-install/#recommended-install-git)).

```text
Make this folder a Git repository if it is not one yet, and save a snapshot of all files with the message "notes created".
```

Codex may ask your permission first, because the snapshot folder (`.git`)
is protected. Read the request, then approve.

If Codex says Git needs your name ("Please tell me who you are"), paste:
`Set my Git name to [your name] and email to [your email] for this folder only, then save the snapshot again.`

## 3. Ask it to change the file

```text
Rewrite notes.md so all action items are collected in a table at the top, with columns Date, Action and Owner. Keep the original notes below the table.
```

## 4. Review the change

Look at what changed. Because you saved a snapshot, the app's review pane
can show the lines that were added and removed. The easiest way is to ask:
`Show me exactly what changed since the last snapshot.`

Ask yourself: is this what I asked for? Did it change anything I did not ask
it to change?

## 5. Undo it

```text
Undo your last change to notes.md by restoring it from the last snapshot, then confirm it matches the snapshot.
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

Steps 1 to 5 are short, so one chat is fine. For the next guide, start a
**New chat**: long chats use more of your allowance.

Next: the [prompting guide](../prompt-guide/).
