# FACTORY.md -G4LA13_Gala4_Localizing_Code-Graph

## 🎯 Purpose
This document describes the **Band Agentic Mesh** behind our submission.  
It explains how the factory operates, the mandates of each seat, and how resilience is achieved across all four stages.

---

## 🧩 Agentic Mesh Mandates

### Architect
- Reads the spec and fixtures.  
- Produces **generic mandates** that apply across tracks.  
- Maintains the backlog: endpoints and invariants per stage.  
- Ensures no stage breaks earlier contracts.  

### Builder
- Implements endpoints stage by stage (`/me`, `/payments`, `/requests`, `/statement`, `/refunds`, `/correction-batches`).  
- Containerizes each stage with no outbound network.  
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

---

## 📂 Stage Progression
- **Stage‑1**: Basic payments & `/me` endpoint.  
- **Stage‑2**: UI wiring with Playwright tests.  
- **Stage‑3**: Time‑aware balances (`as_of`), statements, corrections.  
- **Stage‑4**: Refunds, correction batches, operator permissions.  

Each stage folder contains a complete service that passes its stage’s suite.

---

## 💬 Messaging & Room Tools
Agents coordinate through Band’s always‑on tools:
- `band_send_message` → Architect hands backlog items to Builder.  
- `band_send_event` → Reviewer posts validation results.  
- `band_add_participant / band_remove_participant` → Architect recruits/removes agents.  
- `band_get_participants` → Builder checks active peers.  
- `band_lookup_peers` → Reviewer searches for resilience helpers.  
- `band_create_chatroom` → Architect spins up private sub‑rooms.  

Contact management tools (`band_list_contacts`, `band_add_contact`, etc.) are used for cross‑account collaboration.

---

## 🌐 Band API Surfaces
- **Agent API (`/api/v1/agent`)** → Used by agents to validate identity, recruit peers, join chats, send messages, and post events.  
- **Human API (`/api/v1/me`)** → Powers the Band.ai dashboard; not used in hackathon.  

Key behaviors: mention‑scoped visibility, messages vs. events, peers vs. participants, reconnect‑safe history.

---

## 📚 Additional Resources
See README.md for full resource list (docs, APIs, SDKs, community links).

---

## 🏆 Why This Factory Impresses
- Clear mandates and roles.  
- Recovery strategy documented.  
- Stage progression legible.  
- Strong brand identity woven throughout.  
- Demonstrates not just code, but a **mesh process**: planning, building, reviewing.

---

Built with ❤️ by **AnticipatedD/G4LA13_Gala4_Localizing_Code-Graph (G4LA13)**
