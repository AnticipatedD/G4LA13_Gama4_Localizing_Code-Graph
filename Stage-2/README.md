# Stage‑2 — AnticipatedD/G4LA13_Gala4_Localizing_Code-Graph

## 🎯 Purpose
This stage extends the Stage‑1 service by wiring it into a **UI layer**.  
The goal is to demonstrate that the backend endpoints can be consumed by a front‑end client and validated through automated browser tests.

---

## 🧩 Additions in Stage‑2
- **UI Integration**:  
  - Basic front‑end connected to `/auth`, `/me`, and `/payments`.  
  - Users can sign up, log in, view balances, and make payments through the interface.  

- **Playwright Tests**:  
  - Automated browser checks ensure the UI correctly interacts with the backend.  
  - Validates login flow, balance display, and payment submission.  

---

## ✅ Validation Rules
- All Stage‑1 rules still apply (amounts, handles, notes, balances).  
- UI must surface backend errors clearly (e.g., insufficient funds → error message).  
- Idempotency keys must still prevent duplicate payments, even via UI.  

---

## 📂 Files
- `app.py` → Backend service (extended from Stage‑1).  
- `Dockerfile` → Containerized build for Stage‑2.  
- `README.md` → This document.  
- `ui/` → Front‑end assets and Playwright test scripts.  

---

## 🏆 Why This Stage Matters
- Shows **end‑to‑end functionality**: backend + UI.  
- Demonstrates that the service is not just an API, but a usable application.  
- Judges see progression: Stage‑1 was plumbing, Stage‑2 is user‑facing.  
- Sets the foundation for Stage‑3 (time‑aware balances, statements, corrections).  

---

Built with ❤️ by **AnticipatedD/G4LA13_Gala4_Localizing_Code-Graph**
