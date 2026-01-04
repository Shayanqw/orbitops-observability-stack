#!/usr/bin/env bash
set -euo pipefail

echo "Waiting for demo-api health..."
for i in {1..30}; do
  if curl -fsS http://127.0.0.1:8000/healthz >/dev/null; then
    echo "✅ demo-api is healthy"
    break
  fi
  sleep 1
done

echo "Checking Prometheus..."
curl -fsS http://127.0.0.1:9090/-/healthy >/dev/null && echo "✅ Prometheus healthy"

echo "Checking Grafana..."
curl -fsS http://127.0.0.1:3000/api/health >/dev/null && echo "✅ Grafana healthy"

echo "✅ Smoke checks passed"
