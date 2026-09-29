# Architecture Documentation

このドキュメントは、Knowledge Baseテンプレートの設計判断と運用ガイドです。

---

## 1. 採用したアーキテクチャ

### Single Source of Truth: Markdown + Filesystem + Git

- **Markdown** = Knowledge（知識の実体）
- **Links / Metadata** = Structure（構造・関係性）
- **Obsidian** = Human Interface（人間向けUI）
- **AI Agent** = Knowledge Maintainer（知識の整理者）
- **Git** = History / Version Control（履歴・変更追跡）

特定のAgent製品やObsidian固有機能への依存を最小化し、プレーンなMarkdownとfilesystemで完結する設計。

---

## 2. 重要な設計判断

### 2.1 Progressive Disclosure（段階的な情報開示）

**問題**: 巨大な規約をセッション開始時に全て読むとcontext予算を圧迫する

**解決**: 読む順序を明確化
1. `AGENTS.md` (< 500 tokens) — bootstrap protocol
2. `00_Meta/Project.md` (< 1000 tokens) — 現在地とNext Action
3. `00_Meta/Index.md` — 必要な知識への navigation
4. Domain notes — タスクに必要なものだけ
5. `Principles.md` / `Schema.md` — 必要な時だけ

新しいAgentは1〜2だけ読めば作業開始できる。

### 2.2 責任分離: AI Organizes, Humans Decide

**問題**: 人間にフォルダ分類・ファイル名・metadata管理を強いると運用負荷が高い

**解決**: 
- **人間の責任**: 情報を提供する（観測、論文URL、実験結果、会話、写真など）
- **Agentの責任**: 分類・整理・link構築・metadata管理

Agentは「どのフォルダ？」「どのファイル名？」を原則質問しない。意味が不明確な場合のみ確認。

### 2.3 Epistemic Integrity（認識論的整合性）

**問題**: AIが情報整理する際、未検証の推論を既成事実に昇格させるリスク

**解決**: Fact / Observation / Hypothesis / Interpretation / Decision / Unknownを明確に区別

- 「センサ出力は2.3Vだった」= Fact
- 「グリッパーが滑った」= Observation
- 「摩擦不足が原因かもしれない」= Hypothesis
- 「データはXを示唆する」= Interpretation
- 「材料Yを使うことにした」= Decision
- 「温度影響は未検証」= Unknown

Agentは推論を事実に、提案を決定に昇格させてはならない。

### 2.4 Provenance First（出所の保持）

**問題**: 後から「なぜそう考えたのか」「どの情報が根拠か」が不明になる

**解決**: あらゆる外部情報に出所を記録
- **論文**: タイトル、著者、DOI/arXiv、アクセス日
- **Web情報**: URL、アクセス日
- **アイデア**: 発案者（自分/他人/AI）、日時、文脈
- **実験**: 使用したプロトタイプ・リソースへのlink

他人の発見を自分たちの発見として扱わない。

### 2.5 Category最小主義

**問題**: 過剰な分類は運用負荷を増やし、どこに何を入れるか迷う

**解決**: 
- 基本7カテゴリに限定: Context / Ideas / Research / Experiments / Resources / Prototypes / Reports
- 明確な必要性がない限り増やさない
- Hypothesis / Observation / Decisionを独立ファイルにせず、Experiment内部構造として扱う

### 2.6 Agent/Session Independence

**問題**: 特定のAgent製品のconversation historyや機能に依存すると、別Agentや別セッションで継続不可

**解決**:
- 会話履歴に依存しない（必要な情報は全てKnowledge Baseに書く）
- Agent固有機能（Claude Projects、GPT Custom Instructions）をSingle Source of Truthにしない
- Markdown + filesystem + Gitを基盤とし、どのAgentでも読める

---

## 3. Agentが新しいセッションで読む順序

```
Session Start
     │
     ├─→ [1] AGENTS.md を読む
     │     ├─ 構造の概要
     │     ├─ Core Principles
     │     └─ Agent責任の理解
     │
     ├─→ [2] 00_Meta/Project.md を読む
     │     ├─ Goal（何を達成したいか）
     │     ├─ Current State（今どこにいるか）
     │     ├─ Open Questions（何が不明か）
     │     └─ Next Actions（次に何をすべきか）
     │
     ├─→ [3] タスクに必要なら 00_Meta/Index.md
     │     └─ 特定の知識への navigation
     │
     ├─→ [4] 必要な domain notes だけ読む
     │     └─ Experiments / Research / Prototypes など
     │
     └─→ [5] 必要な時だけ Principles.md / Schema.md
           └─ 詳細ルールが必要な作業の場合のみ
```

**Token消費の目安**:
- [1] + [2] = 1,500 tokens以下
- [3] = 500 tokens程度
- [4] = タスク依存（通常 2,000〜5,000 tokens）
- [5] = 読まないことが多い（3,000 tokens）

合計: 通常 4,000〜7,000 tokens でコンテキスト復元完了

---

## 4. 人間が普段どのように使うか

### 日常作業フロー

1. **情報を提供する**
   - 実験結果、観測、購入品、論文URL、写真、会話など
   - Agentに渡す（テキスト、ファイル、URL）

2. **Agentが整理**
   - 適切なカテゴリへ分類
   - 新規ノート作成 or 既存ノート更新
   - WikiLinkで関連付け
   - Provenance記録

3. **人間は確認と決定**
   - Agent整理結果をレビュー
   - 必要なら修正・追加
   - 重要な決定は人間が下す

### Obsidianでの閲覧（オプション）

- **Graph View**: ノート間の関係を可視化
- **Backlinks**: このノートがどこから参照されているか
- **Search**: タグ、キーワード検索
- **Daily Notes**: 日々の観察・メモ（オプション機能）

Obsidianなしでも、任意のテキストエディタで全て閲覧・編集可能。

### Git運用

```bash
# 日々の作業後
git add .
git commit -m "Add sensor calibration experiment"
git push

# 他のメンバーと共有
git pull
```

変更履歴はGitが記録するため、ノート内に「変更ログ」を二重管理しない。

---

## 5. 将来的にKnowledge Baseが肥大化した際の拡張方針

### 5.1 スケーリング戦略

#### フェーズ1: 小規模（〜100ノート）
- 現在の構造そのまま
- Project.mdの簡潔性維持が重要
- Index.mdの手動メンテナンスで十分

#### フェーズ2: 中規模（100〜500ノート）
- **サブプロジェクト分離**
  - 大きなプロジェクトは独立リポジトリへ
  - cross-repository linkは慎重に（壊れやすい）
- **Archiveカテゴリ追加**
  - 完了した実験・古いプロトタイプを`Archive/`へ移動
  - Index.mdからは外す（検索では見つかる）
- **Tagging強化**
  - frontmatterのtagsを活用
  - 横断的なテーマ（例: "calibration", "failure-mode"）

#### フェーズ3: 大規模（500ノート以上）
- **Index自動生成**
  - `scripts/generate_index.py` でIndex.mdを自動構築
  - frontmatter metadataから分類
- **Project.mdの分割**
  - 複数プロジェクトがある場合、`00_Meta/Project_A.md`, `Project_B.md`
  - AGENTS.mdからルーティング
- **Full-text search重視**
  - Obsidian search、ripgrep、lunr.js等
  - Index.mdへの依存度を下げる

### 5.2 避けるべき罠

❌ **複雑な階層化**
- 深いフォルダ階層（3階層以上）は避ける
- ファイルの発見が困難になる

❌ **Agent固有の拡張への依存**
- 特定Agentのpluginやworkspaceに依存しない
- Markdown + filesystemで完結を維持

❌ **過度な自動化**
- 全てを自動生成すると、生成スクリプトがSPOFになる
- 手動編集とのハイブリッドを保つ

❌ **重複知識の蓄積**
- 同じ内容を複数ノートに書かない
- Linkで参照する文化を徹底

### 5.3 肥大化の兆候と対策

| 兆候 | 対策 |
|---|---|
| Project.mdが2000 tokens超 | 詳細をdomain notesへ移動、Project.mdは要約のみ |
| Index.mdが巨大で編集困難 | カテゴリ別Indexへ分割（Index_Experiments.md等） |
| 検索しても見つからない | Orphan noteチェック、Tag付与、Archive整理 |
| Agentがcontext予算を使い切る | Progressive Disclosure再確認、不要な全文引用削減 |

---

## 6. PARC2026から学んだこと

このテンプレートはPARC2026プロジェクトのKnowledge Baseを分析・一般化して構築。

### 採用した優れたパターン

✅ **Agent Documentation Guideline**
- 規約をSingle Source of Truthに
- AgentごとのSKILL.mdはコピー（Dual-Sync）

✅ **Experiment Leaderboard Tracker**
- 実験マトリクスによる比較の可視化
- Model/Dataset Cardの統合管理

✅ **Epistemic rigidity**
- Fact/Hypothesis/Interpretationの厳密な分離
- 訂正を消さずに残す（取り消し線+コールアウト）

✅ **Provenance徹底**
- 一次資料へのlink必須
- 査読論文・arXiv・公式技術レポート優先

### 汎用化で改善した点

✅ **カテゴリ単純化**
- PARC2026: 00_Meta / 01_Cookbook / 03_Experiments / 04_Tasks / 05_References
- 汎用版: Context / Ideas / Research / Experiments / Resources / Prototypes / Reports
  - より直感的、専門領域に依存しない

✅ **Project.mdの導入**
- PARC2026: Index.mdに現在地を含めていたが、Index肥大化の原因
- 汎用版: Project.mdを分離し、Session Handoff専用化

✅ **Template提供**
- PARC2026: 暗黙の構造
- 汎用版: `_templates/` で明示的にフォーマット提供

---

## まとめ

このKnowledge Baseは:
- ✅ Agent/Session独立性を達成
- ✅ 人間とAIの両方に最適化
- ✅ Markdown + Git基盤で将来性を確保
- ✅ Epistemic integrityを実装
- ✅ Progressive Disclosureでcontext効率化

「思考・証拠・経緯を永続化し、どのAgentでも最小tokenで継続可能」という目的を実現。
