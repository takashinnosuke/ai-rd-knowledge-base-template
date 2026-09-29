# AI-First R&D プロジェクト Knowledge Base

**AIエージェントのセッション継続性に最適化された、コンテキスト・推論・証拠を永続化するKnowledge Baseテンプレート**

---

## 目的

これは単なるドキュメント置き場ではありません。**AIエージェント間のセッション継続性**に最適化されたKnowledge Baseです。

Claude、ChatGPT、Codex、Kiro、Cursor、Aider、将来登場するツールのいずれを使っても:
- コンテキストを失わずに作業を再開できる
- 過去の決定とその理由を理解できる
- 関連する実験・研究・リソースを発見できる
- 前回のセッションの続きから進められる

以下のプロジェクトに対応:
- **Physical AIプロジェクト**: ロボティクス、センサー検証、PoC開発
- **研究プロジェクト**: 論文調査、仮説検証、実験追跡
- **AIコンペ**: モデル訓練、データセット管理、リーダーボード追跡
- **Makerプロジェクト**: 反復設計、部品調達、製作ログ

---

## クイックスタート

### 人間向け

1. **このファイルを読む**（概要）
2. [Obsidian](https://obsidian.md)で開くと視覚的なグラフnavigationが使える（オプション）
3. 知識を追加し始める:
   - Context: `Context/Background.md`
   - Ideas: `Ideas/IDEA_*.md`
   - Experiments: `Experiments/EXP_YYYYMMDD_*.md`
   - Resources: `Resources/*.md`
4. プロジェクト状態が変化したら `00_Meta/Project.md` を更新

### AIエージェント向け

**最初に `AGENTS.md` を読んでください。** それがあなたのエントリーポイントです。

---

## 構造

```
/
├── AGENTS.md                  # AIエージェントbootstrap protocol
├── README.md                  # このファイル — 人間向け概要
├── README_ja.md               # 日本語README
├── ARCHITECTURE.md            # 設計判断の詳細ドキュメント
├── .gitignore                 # バージョン管理除外設定
│
├── 00_Meta/                   # プロジェクトに関するメタ知識
│   ├── Project.md             # 現在地、目標、次のアクション
│   ├── Index.md               # ナビゲーションハブ
│   ├── Principles.md          # 設計思想
│   └── Schema.md              # 詳細なフォーマット規則
│
├── Context/                   # 背景、目標、制約
├── Ideas/                     # 出所付きのアイデア
├── Research/                  # 論文、調査、外部知識
├── Experiments/               # 仮説 → 結果 → 解釈
├── Resources/                 # 部品、ツール、データセット、購入品
├── Prototypes/                # 設計、BOM、コードスナップショット
├── Reports/                   # まとめ、最終レポート
│
├── _templates/                # ノートテンプレート
├── _example_project/          # サンプルプロジェクト（参考用）
└── scripts/                   # 検証スクリプト
    └── validate_kb.py         # Knowledge Base整合性チェック
```

---

## 核心原則

1. **結果だけでなく推論を保存** — なぜその決定をしたかを記録
2. **不確実性を保存** — 事実と仮説と解釈を区別
3. **証拠と解釈を分離** — 観測と結論を別々に保つ
4. **出所を保存** — 出典を記録、誰が何を提案したかを記録
5. **Progressive disclosure** — エージェントは必要なものだけ読む
6. **エージェント独立性** — どのAIツール、どのセッションでも動作

---

## 動作原理

### セッション引き継ぎ

新しいAIエージェントが開始する時:
1. `AGENTS.md` を読む（bootstrap）
2. `00_Meta/Project.md` を読む（現在地）
3. 現在のタスクに関連するノートだけを読む

Knowledge Base全体を読む必要はありません。

### 知識フロー

```
人間が提供:                エージェントが整理:
  - 観測              →      カテゴリへ分類
  - URL              →      ノート作成/更新
  - 論文             →      linkとmetadataを追加
  - 測定値           →      provenanceを保持
  - アイデア         →      必要ならProject.md更新
```

エージェントは「どのフォルダ？」「どのファイル名？」を**質問しない** — 自律的に判断します。

---

## ベストプラクティス

### すべきこと:
- ✅ WikiLinkでノートを接続: `[[Experiments/EXP_20260928|Calibration]]`
- ✅ 新しいノートを作ったら `00_Meta/Index.md` を更新
- ✅ `00_Meta/Project.md` を簡潔に保つ（1000 tokens以下）
- ✅ 事実と仮説を明確に区別
- ✅ 出典をURL、DOI、日付付きで引用

### すべきでないこと:
- ❌ 複数のノートにコンテンツを重複させる
- ❌ ノートを孤立させる（どこからもlinkされない）
- ❌ 推測と確認済み事実を混在させる
- ❌ 事前に複雑な分類体系を作る
- ❌ 会話履歴にコンテキストを依存させる

---

## ツール

### Obsidian（オプション）

このKnowledge BaseはプレーンなMarkdownとあらゆるテキストエディタで動作しますが、[Obsidian](https://obsidian.md)は以下を追加します:
- ノート接続のグラフビュー
- WikiLink自動補完
- バックリンクパネル
- タグ検索

### バージョン管理

Gitで変更を追跡:
```bash
git add .
git commit -m "センサー校正実験を追加"
git push
```

### 検証（オプション）

整合性チェックスクリプト:
```bash
python scripts/validate_kb.py
```

チェック内容:
- 全ノートがfrontmatterを持つか
- 全WikiLinkが実在ファイルを指すか
- 孤立ノートがないか
- Indexが最新か

---

## サンプル

以下のサンプルノートを参照:
- `_example_project/` — 架空のロボット把持センサー開発プロジェクト
- Idea → Research → Experiment → Prototype → Result の流れを確認できます

---

## 哲学

このKnowledge Baseは以下を体現:

1. **Markdown = 知識** — プレーンテキスト、バージョン管理可能、将来性
2. **Links = 構造** — WikiLinkと参照による関係性
3. **Obsidian = インターフェース** — 人間向けの視覚的レイヤー（オプション）
4. **Git = 履歴** — 変更追跡、可逆性
5. **AI = メンテナー** — エージェントが整理、人間がコンテンツ提供

目標: **セッション、エージェント、時間を超えてコンテキスト喪失を最小化**

---

## はじめかた

1. このテンプレートをクローンまたはコピー
2. `Context/Background.md` にプロジェクトの背景を記入
3. `00_Meta/Project.md` に目標を記入
4. 作業しながら知識を追加
5. AIエージェントに整理を手伝ってもらう

**あなたの思考を保存してください。未来のあなた（と未来のエージェント）が感謝します。**

---

## 詳細ドキュメント

- **設計判断と運用ガイド**: `ARCHITECTURE.md` を参照
- **エージェント向け**: `AGENTS.md` から開始
- **詳細なルール**: `00_Meta/Principles.md` と `00_Meta/Schema.md`

---

## ライセンス

このテンプレート構造は現状のまま提供されます。必要に応じて適応してください。

あなたのプロジェクトコンテンツについては: 独自のライセンスを選択してください。
