---
title: Capacitive Force Sensor Calibration
type: experiment
date: 2026-09-22
updated: 2026-09-22
---

# Capacitive Force Sensor Calibration

## Background / Question

Need to verify linearity and accuracy of the capacitive force sensor (Pressure Profile Systems model CP-15) before integrating into gripper prototype.

Datasheet claims 0.01N resolution and linear response 0-10N. Need to validate with our readout circuit.

---

## Hypothesis

Sensor will show linear response (R² > 0.99) across 0-5N range with <0.05N RMS error.

---

## Setup

- **Sensor**: PPS CP-15 capacitive force sensor
- **Readout**: Custom amplifier circuit (design in [[../Prototypes/PROTO_v01_Sensor_Circuit|circuit schematic]])
- **Reference**: Precision scale (0.01g resolution = 0.0001N)
- **Environment**: Lab bench, 23°C

---

## Method

1. Mount sensor on rigid surface
2. Place precision scale on top of sensor
3. Apply known masses: 0g, 50g, 100g, 200g, 300g, 400g, 500g (0-5N)
4. Record sensor voltage output for each mass
5. Repeat 10 times with re-mounting between trials
6. Calculate linear fit and residuals

---

## Results

| Mass (g) | Force (N) | Voltage (V) | Std Dev (V) |
|---|---|---|---|
| 0 | 0.000 | 0.023 | 0.008 |
| 50 | 0.490 | 0.512 | 0.011 |
| 100 | 0.981 | 0.998 | 0.009 |
| 200 | 1.962 | 1.981 | 0.012 |
| 300 | 2.943 | 2.967 | 0.010 |
| 400 | 3.924 | 3.952 | 0.013 |
| 500 | 4.905 | 4.941 | 0.011 |

**Linear fit**: V = 1.003 × F + 0.018  
**R² = 0.9998**  
**RMS error**: 0.032N

---

## Observations

- Extremely linear response across full range
- Zero offset (0.023V at 0N) is stable across trials
- Slight hysteresis (<1%) when unloading vs loading (not shown in table)
- No drift observed over 30-minute test duration

---

## Interpretation

Sensor performance **exceeds specifications**:
- Linearity better than expected (R² = 0.9998 vs 0.99 target)
- RMS error 0.032N well below 0.05N target
- Resolution validated at 0.01N level

The 0.023V zero offset is consistent and can be calibrated out in software.

Minor hysteresis (~1%) is acceptable for our application since we're measuring static grip force, not dynamic impacts.

---

## Conclusions

✅ Sensor validated for gripper integration  
✅ Linearity confirmed  
✅ Resolution meets requirements

No concerns for proceeding to prototype assembly.

---

## Next Actions

1. Implement software calibration (subtract 0.018V offset, apply 1.003 scale factor)
2. Proceed with [[../Prototypes/PROTO_v01_Gripper_Assembly|gripper assembly]]
3. Test sensor under dynamic loading (next experiment)

---

## References

- Sensor datasheet: [[../Resources/RES_PPS_CP15_Datasheet.pdf|PPS CP-15 datasheet]]
- Circuit design: [[../Prototypes/PROTO_v01_Sensor_Circuit|Custom amplifier schematic]]
