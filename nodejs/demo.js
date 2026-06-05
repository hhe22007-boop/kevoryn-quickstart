// Kevoryn Quickstart - Node.js
const OpenAI = require("openai");

const client = new OpenAI({
  baseURL: "https://api.kevoryn.com/v1",
  apiKey: process.env.KEVORYN_API_KEY || "sk-your-key-here",
});

async function main() {
  const response = await client.chat.completions.create({
    model: "claude-sonnet-4-6",
    messages: [{ role: "user", content: "用中文解释什么是 API" }],
  });
  console.log(response.choices[0].message.content);
}

main();
