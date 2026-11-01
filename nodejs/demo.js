// Kevoryn Quickstart - Node.js
const OpenAI = require("openai");

const client = new OpenAI({
  baseURL: "https://api.kevoryn.com/v1",
  apiKey: process.env.KEVORYN_API_KEY || "sk-your-key-here",
});

async function main() {
  // 先列出这个密钥能用的模型（取决于密钥所属分组）
  const models = await client.models.list();
  const ids = models.data.map((m) => m.id);
  console.log(`可用模型: ${ids.length} 个`);
  ids.slice(0, 5).forEach((id) => console.log(`  - ${id}`));

  const model = process.env.KEVORYN_MODEL;
  if (!model) {
    console.error("请设置环境变量 KEVORYN_MODEL 为上面列表中的一个模型");
    process.exit(1);
  }

  const response = await client.chat.completions.create({
    model,
    messages: [{ role: "user", content: "用中文解释什么是 API" }],
  });
  console.log(response.choices[0].message.content);
}

main();
