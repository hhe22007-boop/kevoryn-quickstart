# Kevoryn Quickstart 🚀

一套 API 接入 66 个顶级 AI 模型。OpenAI 兼容，国内直连，按量计费。

[![Models](https://img.shields.io/badge/Models-66-orange)](https://kevoryn.com/models)
[![API](https://img.shields.io/badge/API-OpenAI_Compatible-blue)](https://kevoryn.com/docs)
[![RMB](https://img.shields.io/badge/Billing-RMB-green)](https://kevoryn.com/pricing)

## 快速开始

1. 注册 → [kevoryn.com/register](https://kevoryn.com/register)
2. 获取 API Key → [kevoryn.com/keys](https://kevoryn.com/keys)
3. 复制粘贴👇

### Python
```bash
pip install openai
export KEVORYN_API_KEY=sk-your-key
python python/demo.py
```

### Node.js
```bash
npm install openai
export KEVORYN_API_KEY=sk-your-key
node nodejs/demo.js
```

### curl
```bash
export KEVORYN_API_KEY=sk-your-key
bash examples/curl.sh
```

## 主流模型

| 模型 | 输出价格 (¥/M tokens) |
|------|:---:|
| GPT-5.5 | ¥252 |
| Claude Opus 4.8 | ¥210 |
| Claude Sonnet 4.6 | ¥126 |
| Claude Haiku 4.5 | ¥42 |
| Gemini 3.1 Pro | ¥100.8 |
| DeepSeek V4 Pro | ¥9.6 |
| DeepSeek V4 Flash | ¥4.8 |
| Qwen 3.6 Plus | ¥9.6 |
| Kimi K2.6 | ¥33.3 |
| MiniMax M2.7 | ¥9.6 |

[查看全部 66 个模型 →](https://kevoryn.com/models)

## 为什么选 Kevoryn？

- 🇨🇳 **国内直连**，无需 VPN
- 💳 **支付宝/微信** 充值
- 🔑 **OpenAI 兼容**，一行代码不改
- 📦 **66 个模型**，一个 API 全接入

## Cursor / Windsurf / Claude Code 配置

设置 → API → 自定义端点：
```
Base URL: https://api.kevoryn.com/v1
API Key:  sk-your-key-here
```
