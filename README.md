# AI-First R&D Project Knowledge Base

**A template for preserving context, reasoning, and evidence across AI agent sessions.**

---

## Purpose

This is not just a document repository. It is a **knowledge base optimized for session continuity** across AI agents.

Whether you use Claude, ChatGPT, Codex, Kiro, Cursor, Aider, or future tools, any agent can:
- Resume work without losing context
- Understand past decisions and reasoning
- Find relevant experiments, research, and resources
- Continue where the last session left off

This structure works for:
- **Physical AI projects**: robotics, sensor validation, PoC prototyping
- **Research projects**: paper surveys, hypothesis testing, experiment tracking
- **AI competitions**: model training, dataset curation, leaderboard tracking
- **Maker projects**: iterative design, parts sourcing, build logs

---

## Quick Start

### For Humans

1. **Read this file** (overview)
2. Open in [Obsidian](https://obsidian.md) for visual graph navigation (optional)
3. Start adding knowledge:
   - Context: `Context/Background.md`
   - Ideas: `Ideas/IDEA_*.md`
   - Experiments: `Experiments/EXP_YYYYMMDD_*.md`
   - Resources: `Resources/*.md`
4. Update `00_Meta/Project.md` when project state changes

### For AI Agents

**Read `AGENTS.md` first.** That file is your entry point.

---

## Structure

```
/
├── AGENTS.md                  # AI agent bootstrap protocol
├── README.md                  # This file — human overview
├── .gitignore                 # Version control exclusions
│
├── 00_Meta/                   # Meta-knowledge about the project
│   ├── Project.md             # Current state, goals, next actions
│   ├── Index.md               # Navigation hub
│   ├── Principles.md          # Design philosophy
│   └── Schema.md              # Detailed formatting rules
│
├── Context/                   # Background, goals, constraints
├── Ideas/                     # Ideas with provenance
├── Research/                  # Papers, surveys, external knowledge
├── Experiments/               # Hypothesis → results → interpretation
├── Resources/                 # Parts, tools, datasets, purchases
├── Prototypes/                # Designs, BOMs, code snapshots
└── Reports/                   # Summaries, final reports
```

---

## Key Principles

1. **Preserve reasoning, not just outcomes** — record why decisions were made
2. **Preserve uncertainty** — distinguish facts from hypotheses from interpretations
3. **Separate evidence from interpretation** — keep observations and conclusions distinct
4. **Preserve provenance** — cite sources, record who suggested what
5. **Progressive disclosure** — agents read only what they need
6. **Agent independence** — works with any AI tool, any session

---

## How This Works

### Session Handoff

When a new AI agent starts:
1. Reads `AGENTS.md` (bootstrap)
2. Reads `00_Meta/Project.md` (current state)
3. Reads only the notes relevant to current task

No need to read the entire knowledge base.

### Knowledge Flow

```
Human provides:           Agent organizes:
  - observations    →       classifies into categories
  - URLs           →       creates/updates notes
  - papers         →       adds links and metadata
  - measurements   →       preserves provenance
  - ideas          →       updates Project.md if needed
```

Agents **do not ask** "which folder?" or "what filename?" — they decide autonomously.

---

## Best Practices

### Do:
- ✅ Link notes with WikiLinks: `[[Experiments/EXP_20260928|Calibration]]`
- ✅ Update `00_Meta/Index.md` when creating new notes
- ✅ Keep `00_Meta/Project.md` concise (under 1000 tokens)
- ✅ Distinguish facts from hypotheses clearly
- ✅ Cite sources with URLs, DOIs, dates

### Don't:
- ❌ Duplicate content across multiple notes
- ❌ Let notes become orphans (not linked anywhere)
- ❌ Mix speculation with confirmed facts
- ❌ Create complex taxonomies preemptively
- ❌ Rely on conversation history for context

---

## Tools

### Obsidian (Optional)

This knowledge base works with plain Markdown and any text editor, but [Obsidian](https://obsidian.md) adds:
- Graph view of note connections
- WikiLink autocomplete
- Backlinks panel
- Tag search

### Version Control

Use Git to track changes:
```bash
git add .
git commit -m "センサー校正実験を追加"
git push
```

### Validation (Optional)

Create a script to check:
- All notes have frontmatter
- All WikiLinks point to real files
- No orphan notes
- Index is up to date

---

## Examples

See the following for example notes:
- `Context/Background.md.example`
- `Ideas/IDEA_Example.md.example`
- `Experiments/EXP_Example.md.example`

These demonstrate the structure in practice.

---

## Philosophy

This knowledge base embodies:

1. **Markdown as knowledge** — plain text, version controlled, future-proof
2. **Links as structure** — relationships via WikiLinks and references
3. **Obsidian as interface** — optional visual layer for humans
4. **Git as history** — changes tracked, reversible
5. **AI as maintainer** — agents organize, humans provide content

The goal: **minimize context loss across sessions, agents, and time.**

---

## License

This template structure is provided as-is. Adapt it to your needs.

For your project content: choose your own license.

---

## Getting Started

1. Clone or copy this template
2. Edit `Context/Background.md` with your project's context
3. Update `00_Meta/Project.md` with your goals
4. Start adding knowledge as you work
5. Let AI agents help you organize

**Preserve your thinking. Future you (and future agents) will thank you.**
