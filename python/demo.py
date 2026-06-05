"""Kevoryn Quickstart - Python"""
from openai import OpenAI
import os

# Get your API key from https://kevoryn.com/keys
client = OpenAI(
    base_url="https://api.kevoryn.com/v1",
    api_key=os.getenv("KEVORYN_API_KEY", "sk-your-key-here")
)

# Chat completion
response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "用中文解释什么是 API"}]
)
print(response.choices[0].message.content)

# List available models
models = client.models.list()
print(f"\n可用模型: {len(models.data)} 个")
for m in models.data[:5]:
    print(f"  - {m.id}")
