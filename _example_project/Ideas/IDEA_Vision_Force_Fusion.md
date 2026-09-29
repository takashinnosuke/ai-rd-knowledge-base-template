---
title: Vision-Force Sensor Fusion for Grip Prediction
type: idea
date: 2026-09-20
author: Team brainstorming session
source: Weekly meeting 2026-09-20
---

# Vision-Force Sensor Fusion for Grip Prediction

## Description

Combine force sensor data with vision-based object recognition to **predict required grip force** before contact.

Current approach: grip → measure force → adjust (reactive, ~50ms lag)

Proposed approach: see object → predict required force from vision → pre-set grip force → measure and fine-tune (proactive)

---

## Rationale

Different objects require different grip forces:
- Rigid objects (metal cans): can tolerate high force
- Soft objects (produce bags): need gentle grip
- Fragile objects (eggs): need very gentle grip

Vision system already identifies objects for picking. We could use that classification to look up or predict optimal force, reducing grip-adjust cycles.

---

## Alternatives Considered

1. **Force-only (current)**: Simple but reactive and slow
2. **Vision-only**: Can't adapt to actual object weight variation
3. **Hybrid (this proposal)**: Best of both — prediction + real-time correction

---

## Potential Benefits

- Faster grip stabilization (reduce 50ms lag)
- Fewer adjust cycles → faster operation
- Could learn from grip history (ML opportunity)

---

## Potential Risks

- Adds complexity (vision pipeline integration)
- Vision misclassification → wrong force prediction
- May not improve enough to justify added cost

---

## Status

**Under Investigation**

Linked to [[../Experiments/EXP_20260925_Vision_Force_Correlation|correlation experiment]] to measure if vision-force relationship is strong enough.

---

## Related

- [[../Research/RES_ML_Grasp_Prediction|ML grasp prediction survey]]
- [[../Experiments/EXP_20260925_Vision_Force_Correlation|Vision-force correlation test]]
