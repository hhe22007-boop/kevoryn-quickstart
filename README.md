# Kevoryn Quickstart

一个密钥接入 Claude、GPT、Gemini、Grok、DeepSeek 等 80+ 模型。保留 OpenAI、Anthropic、Gemini 原生协议,按量计费,没有月费,支付宝和微信充值。

[![Docs](https://img.shields.io/badge/Docs-kevoryn.com%2Fdocs-orange)](https://kevoryn.com/docs/)
[![Models](https://img.shields.io/badge/Models-model--plaza-blue)](https://kevoryn.com/model-plaza)
[![OpenAI Compatible](https://img.shields.io/badge/API-OpenAI_Compatible-green)](https://kevoryn.com/docs/api)

## 快速开始

1. 注册并登录 → [kevoryn.com](https://kevoryn.com)
2. 在「API 密钥」页创建密钥,选一个分组(不同分组能用的模型和价格不同)
3. 查看这个密钥能用哪些模型,把下面示例里的 `YOUR_MODEL_ID` 换成其中一个

```bash
export KEVORYN_API_KEY=sk-your-key
curl -s https://api.kevoryn.com/v1/models -H "Authorization: Bearer $KEVORYN_API_KEY"
```

模型必须在密钥所属分组的白名单里,否则会返回 `model_not_found`。

### Python
```bash
pip install openai
export KEVORYN_API_KEY=sk-your-key
export KEVORYN_MODEL=YOUR_MODEL_ID
python python/demo.py
```

### Node.js
```bash
npm install openai
export KEVORYN_API_KEY=sk-your-key
export KEVORYN_MODEL=YOUR_MODEL_ID
node nodejs/demo.js
```

### curl
```bash
export KEVORYN_API_KEY=sk-your-key
export KEVORYN_MODEL=YOUR_MODEL_ID
bash examples/curl.sh
```

## 接入地址

| 协议 | 地址 | 认证 |
|---|---|---|
| OpenAI 兼容 | `https://api.kevoryn.com/v1` | `Authorization: Bearer 密钥` |
| Anthropic 原生 | `https://api.kevoryn.com`(客户端追加 `/v1/messages`) | `x-api-key` 或 `Authorization: Bearer` |
| Gemini 原生 | `https://api.kevoryn.com`(客户端追加 `/v1beta`) | `x-goog-api-key` |

## 模型与价格

各分组可用的模型和实时价格见 [模型广场](https://kevoryn.com/model-plaza)。价格因分组而异,这里不写死。

## 工具接入

Claude Code、Codex、Gemini CLI、OpenClaw、Hermes Agent、Cherry Studio、TRAE SOLO 的配置步骤都在 [文档中心](https://kevoryn.com/docs/),按 macOS、Linux、Windows 分别给出。

也可以用 [CC Switch 一键导入](https://kevoryn.com/docs/cc-switch),选好工具和模型,自动写入配置。

## 通用客户端配置

设置 → API → 自定义端点:
```
Base URL: https://api.kevoryn.com/v1
API Key:  sk-your-key-here
```

## 链接

- 官网:[kevoryn.com](https://kevoryn.com)
- 文档:[kevoryn.com/docs](https://kevoryn.com/docs/)
- 模型广场:[kevoryn.com/model-plaza](https://kevoryn.com/model-plaza)
