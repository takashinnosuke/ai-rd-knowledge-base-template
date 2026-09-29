---
title: Knowledge Base Schema and Formatting Rules
type: meta
date: 2026-09-29
updated: 2026-09-29
---

# Knowledge Base Schema and Formatting Rules

**Detailed formatting and metadata rules.**  
Read this only when you need to understand specific conventions.

For most work, `AGENTS.md` and `Principles.md` are sufficient.

---

## 1. Frontmatter (YAML Header)

Every Markdown file should have frontmatter:

```yaml
---
title: Note Title
type: <context|idea|research|experiment|resource|prototype|report|meta>
date: YYYY-MM-DD        # Creation date (never changes)
updated: YYYY-MM-DD     # Last substantial update
source: <optional>      # For external content: URL, paper DOI, etc.
author: <optional>      # For ideas: who originated it
tags: <optional>        # Free-form tags
---
```

**Required fields:** `title`, `type`, `date`  
**Change `updated`** when content changes substantially (not for typo fixes)

---

## 2. WikiLinks

Use WikiLinks for internal references: `[[Note Title]]` or `[[Folder/Note Title|Display Text]]`

**Rules:**
- Prefer explicit paths for clarity: `[[Experiments/EXP_20260928|Calibration Experiment]]`
- Link to notes, not sections (sections may move)
- When creating a note, immediately add it to `00_Meta/Index.md`

---

## 3. File Naming Conventions

### General Notes
- Use descriptive names: `Background.md`, `Parts_List.md`
- Use underscores for spaces: `Force_Sensor_Survey.md`
- Keep it concise

### Dated Notes (Experiments, some Research)
- Format: `TYPE_YYYYMMDD_Description.md`
- Examples:
  - `EXP_20260928_Sensor_Calibration.md`
  - `RES_20260915_Literature_Review.md`
  - `PROTO_v01_Initial_Assembly.md`

### Ideas
- Format: `IDEA_Short_Description.md`
- Example: `IDEA_Sensor_Fusion_Approach.md`

---

## 4. Note Structure by Type

### Context Notes

```markdown
---
title: <Title>
type: context
date: YYYY-MM-DD
---

# <Title>

## Background
<!-- Where did this project come from? -->

## Goals
<!-- What are we trying to achieve? -->

## Constraints
<!-- Budget, time, technical limitations -->

## Stakeholders
<!-- Who cares about this? -->
```

---

### Idea Notes

```markdown
---
title: <Idea Name>
type: idea
date: YYYY-MM-DD
author: <Person or "AI" or "Team brainstorm">
source: <URL or meeting or conversation>
---

# <Idea Name>

## Description
<!-- What is the idea? -->

## Rationale
<!-- Why might this work? -->

## Alternatives Considered
<!-- What else was thought of? -->

## Status
<!-- Untested | Investigating | Validated | Rejected | Implemented -->

## Related
<!-- Links to experiments, research, prototypes -->
```

---

### Research Notes

```markdown
---
title: <Research Topic>
type: research
date: YYYY-MM-DD
source: <DOI, arXiv, URL>
---

# <Research Topic>

## Source
- **Title**: Full paper/article title
- **Authors**: Author list
- **Published**: Journal/Conference, Year
- **Link**: [DOI/URL](https://...)

## Key Findings
<!-- What did they discover? -->

## Relevance to Project
<!-- Why does this matter to us? -->

## Methods
<!-- How did they do it? (if relevant) -->

## Limitations
<!-- What doesn't this cover? -->

## References
<!-- Other papers cited -->
```

---

### Experiment Notes

```markdown
---
title: <Experiment Name>
type: experiment
date: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <Experiment Name>

## Background / Question
<!-- Why are we doing this? What do we want to know? -->

## Hypothesis
<!-- What do we expect to happen? -->

## Falsification Criteria
<!-- What would prove this wrong? -->

## Setup
<!-- Equipment, environment, configuration -->

## Method
<!-- Step-by-step procedure -->

## Results
<!-- Raw data, measurements, observations -->
<!-- Keep facts separate from interpretation -->

## Interpretation
<!-- What do the results mean? -->

## Conclusions
<!-- What can we conclude? What is still uncertain? -->

## Next Actions
<!-- What should be done based on this? -->

## References
<!-- Links to prototypes, resources, related experiments -->
```

**Note:** Not every experiment needs all sections. Quick tests can be minimal.

---

### Resource Notes

```markdown
---
title: <Resource Name>
type: resource
date: YYYY-MM-DD
---

# <Resource Name>

## Description
<!-- What is it? -->

## Specifications
<!-- Technical specs, dimensions, ratings -->

## Source / Vendor
<!-- Where to get it, part number, cost -->

## Status
<!-- Ordered | Received | In Use | Depleted -->

## Related
<!-- Links to experiments or prototypes using this -->
```

---

### Prototype Notes

```markdown
---
title: <Prototype Name>
type: prototype
date: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <Prototype Name>

## Purpose
<!-- What is this prototype for? -->

## Design
<!-- Description, CAD files, diagrams -->

## Bill of Materials (BOM)
<!-- Parts used, link to Resources -->

## Assembly Notes
<!-- How to build it -->

## Code / Configuration
<!-- Link to repo, commit hash, config files -->

## Testing
<!-- Link to experiments validating this prototype -->

## Issues / Improvements
<!-- What works, what doesn't, what to change -->

## Status
<!-- Concept | Built | Tested | Validated | Superseded -->
```

---

### Report Notes

```markdown
---
title: <Report Name>
type: report
date: YYYY-MM-DD
---

# <Report Name>

## Executive Summary
<!-- High-level overview -->

## Background
<!-- Context -->

## Work Done
<!-- What was accomplished -->

## Results
<!-- Key outcomes -->

## Conclusions
<!-- What was learned -->

## Future Work
<!-- What comes next -->

## References
<!-- Links to detailed notes -->
```

---

## 5. Handling References and Citations

For academic papers:
```markdown
- [Paper Title](DOI or arXiv URL) (Author et al., Conference/Journal Year)
```

For web resources:
```markdown
- [Page Title](URL) (accessed YYYY-MM-DD)
```

For internal knowledge:
```markdown
- [[Experiments/EXP_20260928|Calibration Experiment]]
```

---

## 6. Provenance for Ideas and Information

When recording external information:

**From a paper:**
```markdown
According to [Smith et al. 2024](https://doi.org/...), the optimal sampling rate is 100Hz.
```

**From a person:**
```markdown
Dr. Tanaka suggested using a Kalman filter (conversation 2026-09-15).
```

**From AI:**
```markdown
AI-generated idea (Claude, 2026-09-20): combine force and vision sensors for redundancy.
```

**Your own reasoning:**
```markdown
Based on [[Experiments/EXP_20260928]], I propose increasing the threshold to 0.5N.
```

---

## 7. Distinguishing Fact from Interpretation

Use language that signals epistemic status:

| Type | Language |
|---|---|
| **Fact** | "The sensor output was 2.3V" / "Temperature measured at 25°C" |
| **Observation** | "I observed..." / "During test 3, the gripper slipped" |
| **Hypothesis** | "This may be caused by..." / "One possible explanation is..." |
| **Interpretation** | "The data suggests..." / "This implies..." |
| **Proposal** | "We should consider..." / "A potential approach is..." |
| **Decision** | "We decided to..." / "The approach is confirmed as..." |
| **Unknown** | "Not yet tested" / "Effect unknown" / "Requires further investigation" |

---

## 8. Version Control (Git)

- Commit meaningful changes with clear messages
- Do not commit large binary files without good reason (use .gitignore)
- Use Git history as the "change log" — don't duplicate in notes

Suggested `.gitignore`:
```
# Large data files
*.zip
*.tar.gz
*.mp4
*.avi

# Build artifacts
build/
dist/
*.pyc
__pycache__/

# Local config
.env
local_settings.json

# OS files
.DS_Store
Thumbs.db

# Editor files
.vscode/
.idea/
*.swp
```

---

## 9. When to Update `00_Meta/Project.md`

Update `Project.md` when:
- A significant milestone is reached
- The goal or approach changes
- Open questions are answered or new ones arise
- You want to hand off to another agent or human

Do NOT update for:
- Minor edits to notes
- Every single experiment
- Routine organization tasks

Keep `Project.md` concise — aim for under 1000 tokens.

---

## 10. Validation Script (Optional)

Consider writing a lightweight script to check:
- [ ] All notes have frontmatter
- [ ] All WikiLinks point to existing files
- [ ] No orphan notes (not linked from Index or other notes)
- [ ] `00_Meta/Index.md` is up to date

Example: `scripts/validate_kb.py` or similar

---

**You now have all the rules. Return to work.**
