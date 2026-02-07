#!/bin/bash
# Quick play command
BACKEND_URL=${BACKEND_URL:-"http://localhost:5000"}
curl -s -X POST "${BACKEND_URL}/play" \
  -H "Content-Type: application/json" \
  -d "{\"song\": \"$1\"}" | jq -r '.success'
