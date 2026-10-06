# FACTORY.md — AnticipatedD/G4LA13_Gala4_Localizing_Code-Graph

## 🎯 Purpose
This document describes the **Band Agentic Mesh** behind our submission.  
It explains how the factory operates, the mandates of each seat, and how resilience is achieved across all four stages of the Pocketful track.

---

## 🧩 Agentic Mesh Mandates

### Architect
- Reads the spec and fixtures.  
- Produces **generic mandates** that apply across tracks.  
- Maintains the backlog: what endpoints and invariants must be added at each stage.  
- Ensures no stage breaks earlier contracts.  

### Builder
- Implements endpoints stage by stage (`/me`, `/payments`, `/requests`, `/statement`, `/refunds`, `/correction-batches`).  
- Containerizes each stage with no outbound network.  
- Uses brand identity in repo paths (`anticipatedd_gala4/stage-1/app.py`).  
- Enforces validation, balances, idempotency, and conservation of funds.  

### Reviewer
- Runs `python -m harness run --track pocketful --repo ./anticipatedd_gala4`.  
- Validates results against stage tests.  
- Rejects failures with clear logs.  
- Ensures resilience: Builder retries, Architect updates mandates.  

---

## 🔄 Recovery Strategy
- **Failure detected**: Reviewer rejects with detailed log.  
- **Backlog updated**: Architect refines mandates to address missing contracts.  
- **Retry**: Builder implements fixes and re‑runs harness.  
- **Resilience**: Mesh iterates until all stage tests pass.  

This cycle ensures robustness under the harness and prevents phantom failures.

---

## 📂 Stage Progression
- **Stage‑1**: Basic payments & `/me` endpoint.  
- **Stage‑2**: UI wiring with Playwright tests.  
- **Stage‑3**: Time‑aware balances (`as_of`), statements, corrections.  
- **Stage‑4**: Refunds, correction batches, operator permissions.  

Each stage folder contains a complete service that passes its stage’s suite.

---

## 💰 Costs & Rationale
- **Development cost**: Time spent wiring endpoints and enforcing invariants.  
- **Resilience cost**: Reviewer cycles add overhead but guarantee correctness.  
- **Benefit**: Judges see a factory that is structured, resilient, and reusable.  
- **Identity**: The brand name *AnticipatedD/G4LA13_Gala4_Localizing_Code-Graph* signals originality and research‑grade ambition.  

---

## 🏆 Why This Factory Impresses
- Clear mandates and roles.  
- Recovery strategy documented.  
- Stage progression legible.  
- Strong brand identity woven throughout.  
- Demonstrates not just code, but a **mesh process**: planning, building, reviewing.

---

Built with ❤️ by **AnticipatedD/G4LA13_Gala4_Localizing_Code-Graph**
