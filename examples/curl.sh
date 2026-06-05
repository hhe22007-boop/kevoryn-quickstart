#!/bin/bash
# Kevoryn Quickstart - curl

API_KEY="${KEVORYN_API_KEY:-sk-your-key-here}"

# Chat completion
curl -s https://api.kevoryn.com/v1/chat/completions \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [{"role": "user", "content": "用中文解释什么是 API"}]
  }' | python3 -m json.tool

# List models
curl -s https://api.kevoryn.com/v1/models \
  -H "Authorization: Bearer $API_KEY" | python3 -c "
import sys,json
d=json.load(sys.stdin)
print(f'{len(d.get(\"data\",[]))} 个模型可用')"
