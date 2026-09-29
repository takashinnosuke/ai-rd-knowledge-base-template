---
title: Knowledge Base Design Principles
type: meta
date: 2026-09-29
updated: 2026-09-29
---

# Knowledge Base Design Principles

**Read this when you need to understand "why" behind the structure.**  
For day-to-day work, the bootstrap in `AGENTS.md` is sufficient.

---

## 1. Preserve Reasoning, Not Just Outcomes

Record **how** decisions were made, not just what was decided.

- Why did you choose sensor A over sensor B?
- What alternatives were considered and rejected?
- What assumptions underpin the current approach?

This lets future work revisit decisions with full context.

---

## 2. Preserve Uncertainty

Do not promote unverified information to facts.

**Distinguish clearly:**
- **Fact**: Measured, observed, documented (e.g., "sensor output was 2.3V at 1N load")
- **Observation**: What you saw (e.g., "the gripper slipped during test 3")
- **Hypothesis**: Proposed explanation (e.g., "slippage may be due to insufficient friction")
- **Interpretation**: Your reading of data (e.g., "the data suggests X")
- **Proposal**: Suggested action (e.g., "we should try material Y")
- **Decision**: Commitment to action (e.g., "we will use material Y")
- **Unknown**: Explicitly unknown (e.g., "temperature effect on adhesive not yet tested")

AI agents must not convert hypotheses into facts when organizing information.

---

## 3. Separate Evidence from Interpretation

Keep raw data, observations, and interpretations in distinct sections.

Example structure for an experiment note:
```
## Setup
## Method
## Results (raw data, measurements)
## Observations (what you saw)
## Interpretation (what it might mean)
## Next Actions
```

This separation allows re-interpretation if new evidence emerges.

---

## 4. Preserve Provenance

For any external information, record:
- **Source**: Who said it / where it came from
- **Author**: If applicable
- **Date**: When it was obtained or published
- **URL / Reference**: Direct link to original

For ideas:
- Distinguish your ideas from others' ideas from AI-generated ideas
- Credit appropriately

This maintains intellectual honesty and enables fact-checking.

---

## 5. Prefer Links Over Duplication

If information exists in one note, link to it from others rather than copying.

- A part's specifications live in `Resources/`, experiments link there
- A paper's findings live in `Research/`, experiments cite them

Duplication leads to inconsistency when one copy is updated and others aren't.

---

## 6. Optimize for Humans AND Machines

This knowledge base serves:
- **Humans** reading in Obsidian or text editors
- **AI agents** resuming work across sessions

Design for both:
- Use plain Markdown (agent-readable)
- Use WikiLinks and frontmatter (Obsidian features, but degradable)
- Keep navigation simple (Index.md + Project.md pattern)
- Avoid agent-specific or tool-specific lock-in

---

## 7. AI Organizes, Humans Decide

**Agent responsibilities:**
- Classify and file information
- Create and update notes
- Maintain links and metadata
- Suggest categorization

**Human responsibilities:**
- Provide information (observations, decisions, URLs, papers)
- Make decisions when asked
- Validate that organization makes sense

Agents should not ask humans trivial organization questions like "which folder?" or "what filename?" unless the meaning is ambiguous.

---

## 8. Minimize Mandatory Structure

Not every note needs every section. Not every experiment needs a formal hypothesis.

**Use structure when it adds value:**
- Complex experiments → formal structure (hypothesis, method, results)
- Quick observations → minimal structure (date, observation, next action)
- Literature review → citation-heavy structure

Forcing unnecessary structure creates friction and slows work.

---

## 9. Progressive Disclosure of Context

New agents should not need to read the entire knowledge base to start.

**Reading order:**
1. `AGENTS.md` (bootstrap, <500 tokens)
2. `00_Meta/Project.md` (current state, <1000 tokens)
3. `00_Meta/Index.md` (only if searching for specific knowledge)
4. Domain notes (only those relevant to current task)

Heavy schemas (this file, `Schema.md`) are read only when the agent needs to understand deeper rules.

---

## 10. Agent and Session Independence

The knowledge base must work with:
- Any AI agent (Claude, GPT, Gemini, Codex, future tools)
- Any session (today, tomorrow, 6 months from now)
- Any human team member (onboarding, handoff)

**Do not rely on:**
- Conversation history in a chat session
- Agent-specific features (e.g., Claude Projects, GPT Custom Instructions)
- Implicit knowledge not written down

If it's not in the knowledge base, it doesn't exist.

---

## Anti-Patterns (Don't Do This)

- **Don't duplicate content** across multiple notes without clear reason
- **Don't let notes become orphans** — always link from Index or a parent note
- **Don't mix unverified speculation with confirmed facts** in the same section
- **Don't create categories preemptively** — add them when actually needed
- **Don't ask humans to organize** — that's the agent's job

---

**Next: If you need detailed formatting rules, read `00_Meta/Schema.md`**
