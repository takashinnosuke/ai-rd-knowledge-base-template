---
title: Force Sensor Technology Survey
type: research
date: 2026-09-16
updated: 2026-09-18
source: Various vendor datasheets and academic papers
---

# Force Sensor Technology Survey

## Overview

Surveyed 5 force sensor technologies for robotic gripper application.

---

## Candidates

### 1. Strain Gauge Load Cells

**Source**: HX711-based sensors, various vendors

- **Resolution**: 0.05N typical
- **Range**: 0-5N common
- **Response time**: ~80ms (limited by HX711 ADC)
- **Cost**: $10-20
- **Durability**: Excellent (industrial grade)

**Pros**: Cheap, reliable, well-documented  
**Cons**: Slow response time (80ms > 10ms requirement)

---

### 2. Capacitive Force Sensors

**Source**: [Pressure Profile Systems](https://pressureprofile.com)

- **Resolution**: 0.01N
- **Range**: 0-10N
- **Response time**: 5ms
- **Cost**: $150-200
- **Durability**: Moderate (sensitive to humidity)

**Pros**: Fast, high resolution  
**Cons**: Expensive, environmental sensitivity

---

### 3. FSR (Force-Sensitive Resistor)

**Source**: Interlink FSR402, datasheet from [Adafruit](https://www.adafruit.com/product/166)

- **Resolution**: ~0.2N (poor linearity)
- **Range**: 0.1-10N
- **Response time**: <1ms
- **Cost**: $7
- **Durability**: Good

**Pros**: Very cheap, fast  
**Cons**: Poor linearity, requires calibration, drifts over time

---

### 4. Piezoelectric Sensors

**Source**: [PCB Piezotronics](https://www.pcb.com)

- **Resolution**: 0.001N
- **Range**: 0-50N
- **Response time**: <1ms
- **Cost**: $300+
- **Durability**: Excellent

**Pros**: Extremely fast and precise  
**Cons**: Very expensive, requires charge amplifier

---

### 5. Optical Force Sensors

**Source**: [OptoForce](https://www.optoforce.com) (now OnRobot)

- **Resolution**: 0.02N
- **Range**: 0-30N
- **Response time**: 1ms (1kHz sampling)
- **Cost**: $400+
- **Durability**: Excellent

**Pros**: Fast, robust, industrial-ready  
**Cons**: Exceeds budget significantly

---

## Comparison Table

| Technology | Resolution | Response | Cost | Meets Spec? |
|---|---|---|---|---|
| Strain gauge | 0.05N | 80ms | $15 | ❌ (too slow) |
| Capacitive | 0.01N | 5ms | $175 | ✅ (borderline cost) |
| FSR | 0.2N | <1ms | $7 | ❌ (poor resolution) |
| Piezo | 0.001N | <1ms | $300+ | ❌ (too expensive) |
| Optical | 0.02N | 1ms | $400+ | ❌ (too expensive) |

---

## Relevance to Project

Requirements: 0.1N resolution, <10ms response, <$100 cost

**Shortlist**:
1. **Capacitive sensor** ($175) — only option meeting all specs, but over budget
2. **Strain gauge** ($15) — can we work around 80ms latency?

---

## Decision

Proceed with **capacitive sensor** for prototype. Cost exceeds target but is acceptable for proof-of-concept. If successful, explore bulk pricing or custom design for production.

Alternative: Test if predictive control (see [[../Ideas/IDEA_Vision_Force_Fusion|vision-force fusion idea]]) can compensate for strain gauge latency.

---

## References

- HX711 datasheet: https://www.sparkfun.com/datasheets/Sensors/ForceFlex/hx711_english.pdf
- FSR Integration Guide: https://www.bdtic.com/DataSheet/Sites/Interlink/FSR-Integration-Guide.pdf
- [Robotic Grasping Force Sensing: A Survey](https://doi.org/10.1109/MRA.2020.XXXXXX) (fictional example DOI)
