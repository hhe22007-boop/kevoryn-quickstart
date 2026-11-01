"""Kevoryn Quickstart - Python"""
from openai import OpenAI
import os
import sys

# 在 https://kevoryn.com 的「API 密钥」页创建密钥
client = OpenAI(
    base_url="https://api.kevoryn.com/v1",
    api_key=os.getenv("KEVORYN_API_KEY", "sk-your-key-here"),
)

# 先列出这个密钥能用的模型（取决于密钥所属分组）
models = client.models.list()
ids = [m.id for m in models.data]
print(f"可用模型: {len(ids)} 个")
for mid in ids[:5]:
    print(f"  - {mid}")

model = os.getenv("KEVORYN_MODEL")
if not model:
    sys.exit("请设置环境变量 KEVORYN_MODEL 为上面列表中的一个模型")

response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "用中文解释什么是 API"}],
)
print(response.choices[0].message.content)
