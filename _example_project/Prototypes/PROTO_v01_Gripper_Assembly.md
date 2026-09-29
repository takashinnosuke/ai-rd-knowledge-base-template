---
title: Prototype v0.1 - Initial Gripper Assembly
type: prototype
date: 2026-09-23
updated: 2026-09-24
---

# Prototype v0.1 - Initial Gripper Assembly

## Purpose

First functional prototype integrating capacitive force sensor into UR5e gripper.

Goals:
- Validate mechanical fit
- Test sensor integration
- Demonstrate basic force feedback

---

## Design

### Overview

Two-finger parallel jaw gripper with force sensor mounted on inner surface of one finger.

```
┌─────────────┐
│   UR5e Arm  │
└──────┬──────┘
       │
  ┌────┴────┐
  │ Adapter │
  └────┬────┘
       │
  ┌────┴────────┐
  │  Actuator   │ ← Existing pneumatic gripper
  └─┬────────┬──┘
    │        │
 ┌──┴──┐  ┌─┴───┐
 │Finger│  │Finger│ ← 3D printed
 │  #1  │  │  #2 │
 │      │  │ [S] │ ← [S] = Force sensor location
 └──────┘  └─────┘
```

### Key Design Decisions

1. **Sensor placement**: Inner surface of one finger (not both) to simplify wiring
2. **Material**: PETG for fingers (strong enough, easy to print, iterate quickly)
3. **Sensor protection**: Recessed pocket to prevent direct impact
4. **Wiring**: Routed through hollow finger, exits at base

---

## Bill of Materials

| Item | Quantity | Source |
|---|---|---|
| PPS CP-15 sensor | 1 | [[../Resources/RES_Parts_List\|Parts List]] |
| Gripper finger (left) | 1 | 3D printed PETG |
| Gripper finger (right) | 1 | 3D printed PETG |
| Sensor circuit board | 1 | Custom PCB |
| Mounting screws M3×10mm | 4 | Lab stock |
| Signal cable | 1m | Lab stock |

---

## Assembly Notes

### Steps

1. Insert sensor into recessed pocket on right finger
2. Apply thin layer of RTV silicone around sensor perimeter (sealing, not bonding)
3. Allow silicone to cure (24 hours)
4. Solder wires to sensor pads
5. Route wires through finger channel
6. Mount fingers to pneumatic actuator
7. Connect sensor cable to control system

### Challenges

- **Fit**: Sensor pocket was 0.2mm too tight. Filed manually to fit.
- **Wiring**: Cable routing required careful bending radius (sensor datasheet: min 10mm radius)
- **Alignment**: Fingers need precise parallel alignment. Used shims to adjust.

---

## Testing

See [[../Experiments/EXP_20260924_Prototype_Grip_Test|grip force control test]].

Summary:
- Mechanical fit: ✅ Good
- Sensor response: ✅ Validated (see calibration experiment)
- Force control: ⚠️ Partial (PID tuning needed)

---

## Issues / Improvements

### Current Issues

1. **Finger flex**: PETG fingers flex under high force (>3N), affecting sensor reading
   - Impact: ~5% error at high force
   - Mitigation: May need stiffer material or ribbed design

2. **Cable strain**: Wire exit point experiences strain during gripper opening
   - Impact: Potential long-term failure
   - Mitigation: Add strain relief grommet (planned for v0.2)

3. **Single-sided sensing**: Only right finger has sensor, can't detect off-center grips
   - Impact: Asymmetric force readings
   - Mitigation: Consider dual sensors in future (cost increase)

### Planned Improvements (v0.2)

- Switch to carbon-fiber reinforced PETG for fingers
- Add strain relief for cable
- Improve sensor pocket tolerance (0.1mm clearance instead of tight fit)

---

## Status

**Built and tested**

Currently in use for control algorithm development. Functional but not production-ready.

---

## Files

- CAD: `mechanical/gripper_v01/`
  - `finger_left_v01.stl`
  - `finger_right_sensor_v01.stl`
- Electronics: `electronics/sensor_circuit/`
  - `amplifier_v01.kicad_sch`
  - `amplifier_v01.kicad_pcb`
- Code: `software/gripper_control/`
  - `force_feedback.py` (PID controller)
  - `sensor_interface.py` (ADC reading)

---

## Related

- Design based on: [[../Research/RES_Force_Sensor_Survey|Force sensor survey]]
- Tested in: [[../Experiments/EXP_20260924_Prototype_Grip_Test|Grip test experiment]]
- Next version: PROTO_v02 (in progress)
