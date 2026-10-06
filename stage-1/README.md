# Stage‑1 — AnticipatedD/G4LA13_Gala4_Localizing_Code-Graph

## 🎯 Purpose
This stage implements the **minimum viable service** for the Pocketful track.  
It builds on the scaffold and adds the first functional endpoints so the harness can validate progress.

---

## 🧩 Endpoints Implemented
- `GET /health` → service heartbeat  
- `POST /_test/reset` → load seeded fixture (Ada, Bob, Cy)  
- `POST /auth/signup` → create new user, derive handle (≤20 chars)  
- `POST /auth/login` → authenticate existing user  
- `GET /me` → return user info and current balance  
- `POST /payments` → transfer funds between users with validation  

---

## ✅ Validation Rules
- **Amount**: integer, ≥1, ≤1,000,000,000  
- **Handle**: must match `^[a-z0-9_]{1,20}$`  
- **Note**: ≤200 characters, stored verbatim  
- **Funds**: insufficient balance → `409 insufficient_funds`  
- **Errors**: consistent shape (`{"error":{"code":…,"message":…}}`)  

---

## 📂 Files
- `app.py` → Stage‑1 backend service implementation  
- `Dockerfile` → containerized build for harness  
- `README.md` → this document  

---

## 🏆 Why This Stage Matters
- Establishes the **floor**: harness can talk to the service.  
- Passes all Stage‑1 tests in `pocketful/test/stage_1/`.  
- Sets the foundation for later stages (UI, statements, refunds).  

---

Built with ❤️ by **AnticipatedD/G4LA13_Gala4_Localizing_Code-Graph**
