# Quick Start Guide

このガイドは5分でKnowledge Baseを使い始めるためのものです。

---

## 1分でセットアップ

```bash
# 1. このディレクトリをあなたのプロジェクトフォルダにコピー
cp -r ai_rd_knowledge_base_template my_project_kb
cd my_project_kb

# 2. Gitリポジトリを初期化
git init
git add .
git commit -m "Initial knowledge base setup"

# 3. プロジェクト情報を記入
# テキストエディタで以下を編集:
#   - Context/Background.md
#   - 00_Meta/Project.md
```

---

## 最初のノートを作る

### 背景を記録

`Context/Background.md` を作成:

```markdown
---
title: Project Background
type: context
date: 2026-09-29
---

# Project Background

## Origin
このプロジェクトは〜から始まった

## Goal
〜を達成する

## Constraints
- 予算: X円
- 期限: Y週間
```

### 現在地を記録

`00_Meta/Project.md` を編集（すでに存在するテンプレートを書き換え）:

```markdown
## Goal
〜を開発する

## Current State
現在は〜の段階

## Next Actions
1. 〜を調査
2. 〜を実験
```

---

## AIエージェントに作業を依頼

**Claude / ChatGPT / Kiroなど、任意のAIエージェントで:**

```
このプロジェクトのKnowledge Baseを読んで、次の作業を手伝ってください:
[あなたの依頼内容]

まず AGENTS.md を読んでから作業してください。
```

エージェントは:
1. `AGENTS.md` で構造を理解
2. `00_Meta/Project.md` で現在地を把握
3. 必要に応じて関連ノートを読む
4. 作業結果を適切なノートに記録

---

## よくある最初の作業

### 実験結果を記録

```
実験結果:
- センサーAの出力電圧: 2.3V (負荷1N時)
- 直線性: R²=0.998
- 再現性: 良好

この結果をKnowledge Baseに記録して、次に何をすべきか提案してください。
```

→ エージェントが `Experiments/EXP_20260929_Sensor_Test.md` を作成し、`00_Meta/Index.md` を更新

### 論文を調査

```
この論文を読んで要約をKnowledge Baseに追加:
https://arxiv.org/abs/XXXX.XXXXX

プロジェクトへの関連性も評価してください。
```

→ エージェントが `Research/RES_Paper_Title.md` を作成

### アイデアを記録

```
アイデア: 視覚センサーと力センサーを組み合わせて、
接触前に必要な把持力を予測できないか？

このアイデアをKnowledge Baseに記録して、
検証のための実験計画を立ててください。
```

→ エージェントが `Ideas/IDEA_Vision_Force_Fusion.md` を作成し、実験を提案

---

## 日々の運用

### 朝: 現在地を確認

```
00_Meta/Project.md を読んで、今日やるべきことを教えてください。
```

### 日中: 情報を渡す

```
[実験結果 / 観測 / 購入品 / 論文URL / 会話内容] を渡す
→ エージェントが分類・整理
```

### 夕方: 状態を更新

```
今日の作業でProject.mdを更新する必要がありますか？
```

---

## 検証とメンテナンス

```bash
# Knowledge Baseの整合性をチェック
python scripts/validate_kb.py

# 問題があれば修正を提案してもらう
# 問題なければ commit
git add .
git commit -m "今日の作業内容の要約"
```

---

## Obsidianで可視化（オプション）

1. [Obsidian](https://obsidian.md) をダウンロード
2. このフォルダを "Open folder as vault" で開く
3. Graph view でノート間の関係を視覚化
4. Backlinks で「このノートがどこから参照されているか」を確認

Obsidianなしでも完全に機能します。

---

## よくある質問

**Q: どのフォルダにノートを入れるか迷う**  
A: エージェントに任せてください。「この情報を記録して」と渡すだけで、エージェントが適切なカテゴリに分類します。

**Q: ノートのファイル名はどうすれば？**  
A: エージェントが決めます。あなたは内容だけ提供してください。

**Q: frontmatterって何？**  
A: ノートの先頭にある `---` で囲まれた部分。エージェントが自動で追加するので、気にしなくて大丈夫です。

**Q: WikiLinkの書き方がわからない**  
A: `[[ノート名]]` です。Obsidianなら自動補完が効きます。エージェントも自動でlinkを張るので、手動で書く必要は少ないです。

**Q: 既存のプロジェクトに適用できる？**  
A: はい。段階的に移行できます:
   1. まず `AGENTS.md` と `00_Meta/Project.md` だけ作成
   2. 既存ドキュメントを少しずつ分類して移動
   3. 新しい知識から構造に従って記録

---

## 次のステップ

1. ✅ `Context/Background.md` を作成 → プロジェクトの背景
2. ✅ `00_Meta/Project.md` を編集 → 現在地とNext Actions
3. ✅ 最初の情報をエージェントに渡す
4. ✅ `scripts/validate_kb.py` で検証
5. ✅ Git commit

**あとは自然に育てていくだけです。**

詳細は `README.md` (英語) または `README_ja.md` (日本語) を参照してください。
