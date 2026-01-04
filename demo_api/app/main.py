import os
import time
from fastapi import FastAPI
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

APP = FastAPI(title="OrbitOps Demo API", version="1.0.0")

REQ_COUNT = Counter("http_requests_total", "Total HTTP requests", ["route"])
REQ_LATENCY = Histogram("http_request_duration_seconds", "HTTP request latency", ["route"])

@APP.get("/healthz")
def healthz():
    return {"status": "ok", "env": os.getenv("APP_ENV", "dev")}

@APP.get("/api/v1/ping")
def ping():
    route = "/api/v1/ping"
    start = time.time()
    REQ_COUNT.labels(route=route).inc()
    time.sleep(0.02)  # tiny simulated work
    REQ_LATENCY.labels(route=route).observe(time.time() - start)
    return {"pong": True}

@APP.get("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}
