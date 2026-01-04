from fastapi.testclient import TestClient
from app.main import APP

client = TestClient(APP)

def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_metrics():
    r = client.get("/metrics")
    assert r.status_code == 200
    assert b"http_requests_total" in r.content
