# GitHub リポジトリセットアップ手順

このテンプレートを新しいGitHubリポジトリにpushする手順です。

---

## 手順

### 1. GitHubで新しいリポジトリを作成

1. https://github.com/new にアクセス
2. リポジトリ情報を入力:
   - **Repository name**: `ai-rd-knowledge-base-template`（または任意の名前）
   - **Description**: AI-First R&D Project Knowledge Base - Session continuity optimized template for AI agents
   - **Visibility**: Public（他の人も使えるように）または Private
   - **Initialize this repository with**: **何もチェックしない**（README, .gitignore, licenseは既に作成済み）

3. **Create repository** をクリック

### 2. リモートリポジトリを追加

GitHubがリポジトリ作成後に表示する "…or push an existing repository from the command line" のコマンドを使用:

```bash
# ai_rd_knowledge_base_template ディレクトリで実行
cd C:\PARC2026\ai_rd_knowledge_base_template

# リモートを追加（URLは実際のリポジトリURLに置き換え）
git remote add origin https://github.com/takashinnosuke/ai-rd-knowledge-base-template.git

# ブランチ名を main に変更（GitHubのデフォルトに合わせる）
git branch -M main

# 初回push
git push -u origin main
```

### 3. 完了

リポジトリページで確認:
- https://github.com/takashinnosuke/ai-rd-knowledge-base-template

---

## 使い方（将来のプロジェクトで）

新しいプロジェクトを始める時:

```bash
# テンプレートをclone
git clone https://github.com/takashinnosuke/ai-rd-knowledge-base-template.git my_new_project

cd my_new_project

# Git履歴をリセット（テンプレートの履歴を引き継がない）
rm -rf .git
git init
git add .
git commit -m "Initial commit from template"

# 新しいプロジェクト用のリポジトリを作成してpush
# （GitHubで新リポジトリ作成後）
git remote add origin https://github.com/takashinnosuke/my_new_project.git
git branch -M main
git push -u origin main

# プロジェクト情報を編集
# - Context/Background.md
# - 00_Meta/Project.md
# などを編集してcommit
```

---

## GitHub Template Repository機能を使う（推奨）

リポジトリ作成後、GitHub上でTemplate repositoryとして設定すると、さらに便利になります:

1. リポジトリページの **Settings** タブへ
2. 上部の **Template repository** にチェック
3. 保存

これで、GitHubのUI上から "Use this template" ボタンで簡単に新しいプロジェクトを作成できます。

---

## 認証について

初回pushで認証を求められた場合:

### HTTPSの場合
- Personal Access Token (PAT) を使用
- https://github.com/settings/tokens でtokenを作成
- パスワードの代わりにtokenを入力

### SSHの場合（推奨）
```bash
# SSH鍵を生成（まだない場合）
ssh-keygen -t ed25519 -C "your_email@example.com"

# 公開鍵をGitHubに追加
# https://github.com/settings/keys

# リモートURLをSSHに変更
git remote set-url origin git@github.com:takashinnosuke/ai-rd-knowledge-base-template.git
git push -u origin main
```

---

## トラブルシューティング

### "remote: Repository not found"
- リポジトリ名が正しいか確認
- リポジトリのVisibilityがPrivateの場合、アクセス権限があるか確認

### "failed to push some refs"
- `git pull origin main --rebase` で最新を取得してから再度push

### 認証エラー
- Personal Access Tokenの期限切れ確認
- SSH鍵が正しく設定されているか確認
