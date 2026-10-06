## G4LA13_Gama4_Localizing_Code-Graph 

This repository contains our submission for the Pocketful track (wallet &amp; payments).   

We built a Band Agentic Mesh with three agent seats — Architect, Builder, Reviewer — that plan, implement, and review each other’s work.   

The service evolves across four stages, each folder holding a complete implementation that passes its stage’s tests.

A Band Agentic Mesh for the WeAreDevelopers Hackathon — built to impress judges with a resilient, stage‑by‑stage software factory.

## 🚀 Overview

This repository contains our submission for the **Pocketful track** (wallet & payments).  

We built a **Band Agentic Mesh** with three agent seats — Architect, Builder, Reviewer — that plan, implement, and review each other’s work.  

The service evolves across four stages, each folder holding a complete implementation that passes its stage’s tests.

---

## 🧩 Factory Design
| Seat        | Role                                                                 |
|-------------|----------------------------------------------------------------------|
| Architect   | Reads spec & fixtures, produces mandates and backlog.                |
| Builder     | Implements endpoints stage by stage, containerizes service.          |
| Reviewer    | Runs harness, validates results, rejects failures, ensures resilience.|

---

📂 **Repository Layout**
`
stage-1/   # Basic payments & /me endpoint
stage-2/   # UI integration
stage-3/   # Time-aware balances, statements, corrections
stage-4/   # Refunds & operator correction batches
mandates/  # Architect, Builder, Reviewer contracts
FACTORY.md # Factory rationale, recovery strategy, costs
`

---

✅ **Features by Stage**

- **Stage‑1**: /health, /_test/reset, /auth, /me, /payments  
- **Stage‑2**: UI wiring with Playwright tests  
- **Stage‑3**: Time‑aware balances (as_of), statements, corrections  
- **Stage‑4**: Refunds, correction batches, operator permissions 
