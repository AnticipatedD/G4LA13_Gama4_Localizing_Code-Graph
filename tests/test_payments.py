# tests/test_payments.py
import os
import pytest
import requests

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8080")

@pytest.fixture(scope="session")
def token():
    # Reset fixture
    reset_payload = {
        "users": [
            {
                "id": "u_ada",
                "email": "ada@example.com",
                "password": "pw",
                "display_name": "Ada",
                "handle": "ada",
                "balance": 1000,
            }
        ]
    }
    r = requests.post(f"{BASE_URL}/_test/reset", json=reset_payload)
    assert r.status_code == 204

    # Login
    r = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "ada@example.com", "password": "pw"},
    )
    assert r.status_code == 200
    data = r.json()
    assert "token" in data
    return data["token"]

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_me(token):
    r = requests.get(f"{BASE_URL}/me", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    data = r.json()
    assert data["handle"] == "ada"
    assert "balance" in data

def test_payment_flow(token):
    # Make a payment
    payload = {"to_handle": "bob", "amount": 100, "note": "test payment"}
    r = requests.post(
        f"{BASE_URL}/payments",
        headers={"Authorization": f"Bearer {token}"},
        json=payload,
    )
    assert r.status_code == 200
    data = r.json()
    assert data["amount"] == 100
    assert data["note"] == "test payment"
    assert data["from_handle"] == "ada"
    assert data["to_handle"] == "bob"
