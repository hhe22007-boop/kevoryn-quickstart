# Kevoryn Quickstart 🚀

30 秒接入 Claude Opus 4.8、GPT-5.5、Gemini 等 11 个顶级 AI 模型。

[![Agent-Native Level 5](https://img.shields.io/badge/Agent--Native-Level%205-orange)](https://isitagentready.com)
[![Models](https://img.shields.io/badge/Models-11-blue)](https://kevoryn.com/models)
[![Latency](https://img.shields.io/badge/Latency-%3C50ms-green)](https://kevoryn.com)

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

## 支持的模型

| 模型 | 价格 (input/output per 1M tokens) |
|------|:---:|
| GPT-5.5 | $6 / $36 |
| Claude Opus 4.8 | $6 / $30 |
| Claude Sonnet 4.6 | $3.60 / $18 |
| Claude Haiku 4.5 | $1.20 / $6 |
| Gemini 3.1 Pro | $2.40 / $14.40 |
| DeepSeek V4 Pro | $0.52 / $1.04 |
| DeepSeek V4 Flash | $0.17 / $0.34 |
| Qwen 3.6 Plus | $0.43 / $2.34 |
| MiniMax M2.7 | $0.36 / $1.44 |
| Kimi K2.6 | $1.14 / $4.80 |

## 为什么选 Kevoryn？

- 🇨🇳 **国内直连** 50ms，无需 VPN
- 💳 **支付宝/微信** 充值
- 🔑 **OpenAI 兼容**，一套 API 调所有模型
- 🏆 **Agent-Native Level 5** — AI Agent 可自动发现并接入

## Cursor / Windsurf / Claude Code 配置

设置 → API → 自定义端点：
```
Base URL: https://api.kevoryn.com/v1
API Key:  sk-your-key-here
```
