# Stage‑4 — AnticipatedD/G4LA13_Gala4_Localizing_Code-Graph

## 🎯 Purpose
This stage completes the Pocketful track by adding **refunds and operator correction batches**.  
The goal is to demonstrate that the system can reverse payments, handle disputes, and apply batch corrections while preserving conservation of funds and auditability.

---

## 🧩 Additions in Stage‑4
- **Refunds**  
  - `POST /refunds` → creates a linked reverse payment.  
  - Refunds reference the original `payment_id`.  
  - Ensures balances are restored correctly and logged in statements.  

- **Correction Batches**  
  - `POST /correction-batches` → settlement operators can apply multiple corrections in one batch.  
  - Each correction is logged with metadata and revision history.  
  - Conservation rules enforced: total balances remain equal to seeded total.  

- **Operator Permissions**  
  - Only users with operator role can issue corrections.  
  - Non‑operators → `403 forbidden`.  

---

## ✅ Validation Rules
- Refunds must link to a valid existing payment.  
- Duplicate refunds prevented by idempotency keys.  
- Correction batches must be atomic: either all corrections apply or none.  
- Balances across all wallets must still sum to seeded total.  
- Statements must reflect refunds and corrections transparently.  

---

## 📂 Files
- `app.py` → Backend service (extended from Stage‑3).  
- `Dockerfile` → Containerized build for Stage‑4.  
- `README.md` → This document.  

---

## 🏆 Why This Stage Matters
- Introduces **dispute resolution** via refunds.  
- Adds **operator authority** with batch corrections.  
- Demonstrates full maturity: payments, UI, statements, corrections, refunds.  
- Judges see a complete financial service with resilience and auditability.  
- Marks the capstone of the Band Agentic Mesh progression.  

---

Built with ❤️ by **AnticipatedD/G4LA13_Gala4_Localizing_Code-Graph**
