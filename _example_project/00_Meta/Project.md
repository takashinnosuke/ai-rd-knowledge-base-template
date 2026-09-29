---
title: Project State
type: meta
date: 2026-09-15
updated: 2026-09-28
---

# Project State - Force-Sensing Gripper Development

**Current as of 2026-09-28 (Week 2)**

---

## Goal

Develop force-sensing robotic gripper with 0.1N resolution, <10ms response time, <$100 cost, for warehouse automation system. Target: working prototype in 8 weeks, demo in week 12.

Full background: [[../Context/Background|Background]]

---

## Current State

**Phase**: Early prototype validation

**Completed**:
- ✅ Force sensor technology survey complete → selected capacitive sensor
- ✅ Sensor calibration validated (R²=0.9998, 0.032N RMS error)
- ✅ Prototype v0.1 assembled and mechanically validated
- ✅ Basic grip force measurement working

**In Progress**:
- 🔄 PID control algorithm tuning (force control loop)
- 🔄 Durability testing (currently 500 cycles, target 10,000)

**Not Started**:
- ⏸️ Vision-force fusion exploration (optional enhancement)
- ⏸️ Production cost optimization
- ⏸️ Environmental testing (5°C-35°C range)

---

## Open Questions

1. **Can we achieve stable force control with current PID parameters?**
   - Current status: Oscillation at low forces (<0.5N)
   - Hypothesis: Need lower I-gain or add D-term filtering
   
2. **Will PETG fingers survive 10,000 cycles?**
   - Current status: 500 cycles complete, no visible wear
   - Concern: Creep under sustained load not yet tested

3. **Is single-sided sensing sufficient or do we need dual sensors?**
   - Current status: Works for centered grips
   - Concern: Off-center grips show asymmetric readings
   - Decision deferred until PID tuning complete

---

## Recent Work

1. [[../Experiments/EXP_20260922_Sensor_Calibration|Sensor calibration experiment (Sep 22)]]
   - Validated linearity and accuracy of force sensor
   - Result: Exceeds specifications (R²=0.9998)

2. [[../Prototypes/PROTO_v01_Gripper_Assembly|Prototype v0.1 assembly (Sep 23-24)]]
   - First functional gripper with integrated sensor
   - Issues: Finger flex, cable strain, single-sided sensing

3. [[../Ideas/IDEA_Vision_Force_Fusion|Vision-force fusion idea (Sep 20)]]
   - Proposed predictive grip force from vision
   - Status: Deferred until basic force control validated

---

## Next Actions

**Immediate (this week)**:
1. Complete PID tuning for stable force control
2. Run 100-item grip test (varied weights, fragile items)
3. Document PID parameters and control performance

**Next week**:
1. Continue durability testing (target: 5,000 cycles)
2. Test temperature range (5°C-35°C) if chamber available
3. Decide on dual-sensor necessity based on grip test results

**Future**:
1. Iterate to prototype v0.2 with improvements (CF-PETG, strain relief)
2. Explore vision-force fusion if basic system successful
3. Production cost optimization (evaluate bulk sensor pricing)

---

## Blockers

None currently.

Potential future blocker: Mounting bracket delivery delayed to Sep 27 (originally Sep 25). Does not impact current work.

---

## Notes

- Budget status: $825 spent of $5,000 (83% remaining)
- Timeline: On track for week 8 prototype, week 12 demo
- Team availability: Full time through Oct 15, reduced after (needs planning)

---

**Keep this file concise.** Details live in domain notes, not here.
