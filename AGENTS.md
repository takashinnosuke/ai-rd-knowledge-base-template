# AI Agent Bootstrap Protocol

**This is the entry point for any AI agent starting work in this repository.**

## Quick Start (Read in Order)

1. **Read this file first** (you are here)
2. **Read `00_Meta/Project.md`** — current project state, goals, open questions, next actions
3. **If needed**, read `00_Meta/Index.md` — navigation to specific knowledge
4. **Only when necessary**, read `00_Meta/Principles.md` and `00_Meta/Schema.md`

## What is This?

This is a **Knowledge Base** for R&D projects involving:
- Physical prototyping, sensor validation, PoC development
- AI competitions, software experiments, robotics research
- Idea exploration → research → experimentation → prototyping → results → reports

The purpose is **session continuity across AI agents**: preserve context so any agent (Claude, Codex, ChatGPT, Kiro, Cursor, Aider, future tools) can resume work without losing reasoning, evidence, or decisions.

## Your Role as an Agent

You are responsible for **organizing knowledge**, not just answering questions.

When the user provides information (observations, URLs, papers, purchases, experiment results, code, files, conversations):

1. **Classify** where it belongs (Context / Ideas / Research / Experiments / Resources / Prototypes / Reports)
2. **Create or update** the appropriate note
3. **Link** related notes with WikiLinks
4. **Preserve provenance**: source, author, date, URL
5. **Update `00_Meta/Project.md`** if project state changed substantially
6. **Do NOT ask** the user which folder, which filename, or which metadata to use — you decide

## Core Principles

- **Preserve reasoning, not just outcomes**
- **Preserve uncertainty** — do not promote hypotheses to facts
- **Separate evidence from interpretation**
- **Prefer links over duplication**
- **Progressive disclosure** — do not load heavy schemas unless the task requires them

## File Structure

```
/
├── AGENTS.md                  # This file — bootstrap for AI agents
├── README.md                  # Human-readable project overview
├── 00_Meta/                   # Project state, index, principles, schema
│   ├── Project.md            # Current state — READ THIS SECOND
│   ├── Index.md              # Navigation hub
│   ├── Principles.md         # Design philosophy (read only when needed)
│   └── Schema.md             # Detailed rules (read only when needed)
├── Context/                   # Background, goals, constraints
├── Ideas/                     # Ideas with provenance
├── Research/                  # Papers, patents, surveys, primary sources
├── Experiments/               # Hypothesis → method → results → interpretation
├── Resources/                 # Parts, sensors, tools, datasets, purchases
├── Prototypes/                # Designs, configurations, BOMs, code snapshots
└── Reports/                   # Summaries, final reports, portfolio artifacts
```

## When You Finish Work

- If project state changed substantially, **update `00_Meta/Project.md`**
- Keep it concise (under 1000 tokens) — detail goes in domain notes, not Project
- Commit your changes to Git with a clear message

---

**Next: Read `00_Meta/Project.md`**
