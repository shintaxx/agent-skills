# Agent Skill Repository

このリポジトリは、Claude、Gemini、Codex (GitHub Copilot) で使用する個人の Agent Skill を管理する目的で作られましたが
skillsディレクトリを直接 https://skills.sh/ (npx skill add shintaxx/agent-skills)で取得していただいた方が良さげです

基本、skills/ 以下を更新していく予定です。

## skills
|名前|説明|
|--|--|
|ag-skill-creator|Antigravity用のスキルです。スキルの生成、スキルの解説を行います|
|cc-skill-creator|ClaudeCode用のスキルです。スキルの生成やスキルの解説を行います|
|cp-skill-creator|Copilot用のスキルです。スキルの生成、スキルの解説を行います|

## ディレクトリ構成
```
├── skills/           # スキルをここに配置します (各スキルは独自のディレクトリ内)
│   └── [skill_name]/ # 有効な SKILL.md を含める必要があります
├── bin/              # CLI ツール
│   └── skill-manager # macOS/Linux 用スクリプト
```

## セットアップ

任意のディレクトリから `skill-manager` コマンドを使用できるようにするには、`bin` フォルダを PATH に追加してください。

### macOS (Zsh/Bash)
`~/.zshrc` または `~/.bash_profile` に以下を追加してください（`/path/to/skill-repo` は実際のパスに置き換えてください）:

```bash
export PATH="/path/to/skill-repo/bin:$PATH"
```

その後、`source ~/.zshrc` を実行するか、ターミナルを再起動してください。

## 使用方法

1.  スキルをインストールしたいプロジェクトのディレクトリに移動します。
2.  以下のコマンドを実行します:
    *   **macOS**: `skill-manager`
    *   **Windows**: `skill-manager.ps1`
3.  リストからインストールしたいスキルを選択します。
4.  ターゲット環境（Claude, Antigravity, または Codex）を選択します。

ツールは、適切な隠しディレクトリ（例: `.claude/skills/skill-name`）内に、コピーを行います

## 新しいスキルの追加

1.  `skills/` ディレクトリ内に新しいディレクトリを作成します。
2.  その中に `SKILL.md` ファイルを作成します。
3.  `SKILL.md` に以下の必須 YAML フロントマターが含まれていることを確認してください:

```markdown
---
name: my-new-skill
description: スキルの機能についての説明。
---
# Instructions
...
```
