---
title: Project Parts List
type: resource
date: 2026-09-16
updated: 2026-09-23
---

# Project Parts List

## Force Sensors

### PPS CP-15 Capacitive Force Sensor

- **Vendor**: Pressure Profile Systems
- **Part Number**: CP-15-10N
- **Quantity**: 3 units
- **Unit Cost**: $175
- **Total**: $525
- **Status**: Received 2026-09-18
- **Location**: Lab, drawer B3
- **Datasheet**: [Link](https://pressureprofile.com/sensors/cp-15) (fictional)
- **Used in**: [[../Prototypes/PROTO_v01_Gripper_Assembly|Prototype v0.1]]

---

## Electronics

### Amplifier Components

- **Op-amp**: Texas Instruments OPA340
  - Vendor: Digi-Key
  - Part Number: OPA340NA/250
  - Quantity: 10
  - Unit Cost: $2.50
  - Status: In stock

- **Capacitors**: 10µF ceramic (0805)
  - Vendor: Mouser
  - Quantity: 50
  - Unit Cost: $0.15
  - Status: In stock

- **Resistors**: Various (kit)
  - Vendor: Amazon
  - Cost: $15
  - Status: In stock

---

## Mechanical

### Gripper Fingers (3D Printed)

- **Material**: PETG
- **Print time**: 4 hours per set
- **Cost**: ~$3 material per set
- **Status**: 5 sets printed
- **Files**: `mechanical/gripper_fingers_v01.stl`

### Mounting Bracket

- **Material**: Aluminum 6061
- **Vendor**: Custom machining (local shop)
- **Cost**: $85
- **Status**: Ordered 2026-09-20, delivery 2026-09-27
- **Drawing**: `mechanical/mounting_bracket.pdf`

---

## Robot Arm Interface

### UR5e End-Effector Adapter

- **Vendor**: Robotiq
- **Part Number**: URE-140-80
- **Cost**: $250
- **Status**: Already owned (from previous project)
- **Documentation**: [[../Context/UR5e_Integration_Notes|Integration notes]]

---

## Consumables

### Test Objects

- Variety of items for grip testing:
  - Metal cans (200g, 400g)
  - Plastic bottles (100g, 250g, 500g)
  - Soft items (foam blocks, produce bags)
  - Fragile items (eggs, thin plastic containers)
- **Cost**: ~$50
- **Status**: Acquired

---

## Budget Summary

| Category | Spent | Remaining (of $5000) |
|---|---|---|
| Sensors | $525 | — |
| Electronics | $150 | — |
| Mechanical | $100 | — |
| Robot Interface | $0 (reused) | — |
| Consumables | $50 | — |
| **Total** | **$825** | **$4,175** |

---

## Notes

Budget is well under target. Remaining funds available for:
- Additional sensors if needed
- Vision system upgrade (if [[../Ideas/IDEA_Vision_Force_Fusion|vision-force fusion]] is pursued)
- Unexpected repairs or replacements
