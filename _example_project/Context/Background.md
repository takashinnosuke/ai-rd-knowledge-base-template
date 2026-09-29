---
title: Project Background
type: context
date: 2026-09-15
updated: 2026-09-28
---

# Project Background

## Origin

This project started from a recurring problem in our warehouse automation system: robotic grippers frequently drop fragile items because they can't sense grip force accurately.

Current system uses binary contact detection (touched / not touched), which leads to:
- Crushing delicate items (over-gripping)
- Dropping items mid-transport (under-gripping)
- 15% failure rate on items under 200g

---

## Goal

Develop a force-sensing gripper system with:
- **0.1N force resolution** for items 50g-500g
- **Response time under 10ms** for real-time control
- **Cost under $100 per gripper** for production scalability
- **Durability for 100,000+ grip cycles**

---

## Constraints

- **Budget**: $5,000 for prototyping
- **Timeline**: 8 weeks to working prototype, demo in week 12
- **Environment**: Warehouse conditions (5°C-35°C, dust present)
- **Integration**: Must work with existing UR5e robot arm

---

## Success Criteria

1. Grip force control loop maintains ±0.2N of target force
2. Zero drops in 100-item test with varying weights (50g-500g)
3. No damage to fragile test items (eggs, thin plastic containers)
4. Survives 10,000 grip cycle test without calibration drift

---

## Stakeholders

- **Operations team**: Need reduced failure rate
- **Engineering**: Responsible for integration
- **Management**: Budget approval, ROI evaluation
