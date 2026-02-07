#!/bin/bash
# Quick stop command
BACKEND_URL=${BACKEND_URL:-"http://localhost:8080"}
curl -s -X POST "${BACKEND_URL}/stop" | jq -r '.success'
