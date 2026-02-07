#!/bin/bash
set -euo pipefail

PORT="${MOOSE_BACKEND_PORT:-8080}"
NGROK_DOMAIN="${MOOSE_NGROK_DOMAIN:-}"

# Keep only one ngrok instance
pkill -f "ngrok http ${PORT}" >/dev/null 2>&1 || true

if [ -n "$NGROK_DOMAIN" ]; then
  exec /opt/homebrew/bin/ngrok http "$PORT" --domain "$NGROK_DOMAIN"
else
  exec /opt/homebrew/bin/ngrok http "$PORT"
fi
