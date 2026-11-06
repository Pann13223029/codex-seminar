[English](README.md) · **日本語**

# 00：インストールとサインイン

時間：約5分。

## 1. ChatGPTデスクトップアプリをインストールする

[公式クイックスタート](https://learn.chatgpt.com/docs/quickstart)から、
自分のシステム用のアプリをダウンロードします。macOS・Windows・Linuxで
使えます（Linuxはプレビュー版です）。

## 2. サインインする

アプリを開き、ChatGPTアカウントでサインインします。無料アカウントで
使えます。有料プランでは、Codexをもっと多く使えます。

## 3. フォルダを開く

このワークショップ用に、空のフォルダを作ります。たとえば、ドキュメント
（書類）フォルダの中に `codex-practice` を作ります。次に、そのフォルダを
アプリで開きます。`⌘ O`（macOS）または `Ctrl O`（Windows）を押して、
フォルダを選びます。

Codexは**あなたが選んだフォルダの中で**作業します。フォルダの外で何かを変えるときは、先にあなたの許可を求めなければなりません。

## 4. Codexに切り替える

ChatGPTのドロップダウンメニューで **Codex** を選び、**New chat**（新しい
チャット）を始めます。

## 5. モデルと推論の強さを選ぶ

メッセージ入力欄の下に、**モデルの設定**（model control）があります。
クリックすると、**Power**（パワー）のスライダーが出ます。**Faster**（速い）
は利用枠の使用が少なく、**Smarter**（賢い）は長く考えます。**Luna High**
は Power の設定の1つです。モデルと推論の強さを自分で選ぶには、
**Advanced**（詳細設定）を開きます。

- **Free と Go のプラン：** Codexは **GPT-6 Luna** を使います。OpenAIで
  いちばん効率のよいモデルです。**Luna High** があれば選んでください。
  なければ、初期設定のままにします。
- **Plus 以上のプラン：** ほかのモデルも選べます。このワークショップでは、
  こちらも **GPT-6 Luna** を選んでください。これらの作業を十分にこなせて、
  利用枠の使用もいちばん少ないからです。**Astra** モデルと、推論の強さの
  **Max**・**Ultra** は、とても難しい作業のためにとっておきます。

**推論の強さ**とは、モデルが動く前にどれだけ長く考えるかです：

| 設定 | 使う場面 |
| --- | --- |
| **Light**（軽め。**Advanced** を開いて Light を選ぶ） | すぐ終わる、はっきりした作業：ファイルの説明、名前の変更、メモの整理 |
| **High**（高め。**Luna High** の設定） | このワークショップの分析とスライドの作業（OpenAIが、Lunaの最初の設定としてすすめているもの） |

推論を強くするほど、利用枠を多く使います。作業に合わせて選んでください。
（[公式のモデルガイド](https://learn.chatgpt.com/docs/models)）

## 6. 動くか確認する

コピーして貼り付けます：

```text
どのフォルダで作業していますか？ また、どんなファイルが見えますか？ 何も変更しないでください。
```

Codexは、フォルダの名前を答えて、フォルダが空だと言うはずです。

<a id="recommended-install-git"></a>
## おすすめ：Gitをインストールする

Gitがあると、Codexが何を変えたかをアプリで正確に見られます。変更を元に
戻すこともできます。

- **macOS：** 下のプロンプトを貼り付けます。Gitがない場合は、macOSが
  インストールをすすめるウィンドウを出します。**インストール** をクリック
  します。
- **Windows：** [Git for Windows](https://git-scm.com/download/win) を、
  初期設定のオプションのままインストールします。

Codexにこう頼みます：`git --version を実行して、Gitがインストールされているか確認してください。インストールされていなければ、インストール方法を教えてください。ただし、あなた自身は何もインストールしないでください。`

<a id="get-ready-for-the-data-tracks-python"></a>
## データを使うコースの準備：Python

コース98・99とデータ用のスキルは、**Python** と、2つの追加機能
**pandas** と **matplotlib** を使います。確認はCodexに任せましょう。
コピーして貼り付けます：

```text
このパソコンに Python・pandas・matplotlib がインストールされているか確認してください。Python そのものがない場合は、私のシステム（Windows または Mac）へのインストール方法を一歩ずつ説明して、そこで止まってください。pandas か matplotlib だけがない場合は、私に許可を求めてから、pip で私のユーザーアカウントにインストールしてください。
```

インストールにはインターネットが必要なので、Codexは許可を求めます。
許可してください。

- **Windowsで、Pythonがない場合：**
  [python.org/downloads](https://www.python.org/downloads/) から
  インストールします。インストーラーの最初の画面で、**"Add python.exe to
  PATH"** にチェックを入れます。そのあと、ChatGPTアプリを閉じて開き直し、
  もう一度プロンプトを実行します。
- **Macで、Pythonがない場合：** macOSが、Appleの「コマンドライン・
  デベロッパ・ツール」のインストールをすすめることがあります。受け入れて、
  終わるまで待ち、もう一度プロンプトを実行します。

## 任意：ターミナル版（Codex CLI）

**Plus 以上のプラン**があり、ターミナルに慣れているなら、Codexは
ターミナルでも動きます（Free と Go のプランで使えるのは、デスクトップ
アプリだけです）。[公式のCodex CLIページ](https://learn.chatgpt.com/docs/codex/cli)を
見てください。たとえば、macOS や Linux では：

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Homebrew か Node.js を使っているなら、次の方法もあります：

```bash
brew install --cask codex
```

```bash
npm install -g @openai/codex
```

そのあと `codex` を実行し、**Sign in with ChatGPT**（ChatGPTでサインイン）
を選びます。このワークショップの内容はすべてアプリでできるので、
ターミナルは必要ありません。

次へ：[01：最初の作業](../01-first-task/README.ja.md)
