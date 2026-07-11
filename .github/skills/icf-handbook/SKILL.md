---
name: icf-handbook
description: >
  Optional technical handbook for the Inclusive Coding Festival 2026. Use this skill when participants ask about
  agentic coding topics including: running local models with Ollama, prompting strategies, MCP servers,
  creating skills or custom agents, or managing token usage and context windows. Also use when asked
  about Azure cloud computing, cost management, Azure AI Foundry, or the festival handbook and its
  references.
---

You are helping participants of the Inclusive Coding Festival 2026. When answering questions, cite the
relevant reference document(s) below. Do not assume technical experience — explain concepts clearly and
link to further reading when appropriate.

This skill is optional. If the student is asking how to plan, build, test, document, or submit their own
project, follow the repository's `AGENTS.md` workflow first. Use this skill as background reference for
agent tooling, Copilot, MCP, local models, token usage, skills, custom agents, and Azure.

Source credit: adapted from Bryan Bergo's MIT-licensed ICF 2026 technical handbook repository:
https://github.com/blbergo/icf-mentee-handbook-2026

## Agentic Coding References

- [Local Models](references/agentic-coding/01_LOCAL_MODELS.md) — Running Copilot CLI with local models via Ollama (free, no subscription required)
- [Prompting](references/agentic-coding/02_PROMPTING.md) — Tips for writing effective prompts, understanding the context window, and using custom instructions
- [MCP Servers](references/agentic-coding/03_MCP_SERVERS.md) — Extending your agent with Model Context Protocol servers for external tools and data sources
- [Skills](references/agentic-coding/04_SKILLS.md) — Teaching your agent specialized tasks with reusable instruction folders (`SKILL.md`)
- [Custom Agents](references/agentic-coding/05_CUSTOM_AGENTS.md) — Building specialized agent personas with tailored expertise (`.agent.md` files)
- [Managing Token Usage](references/agentic-coding/06_MANAGING_TOKEN_USAGE.md) — Understanding tokens, monitoring context usage, and strategies to stay within limits

## Azure References

- [Cloud Computing](references/azure/01_CLOUD_COMPUTING.md) — What cloud computing is, core concepts, and getting started with Azure
- [Managing Cost](references/azure/02_MANAGING_COST.md) — Setting budgets, monitoring spending, and avoiding surprise charges
- [Azure AI Foundry](references/azure/03_FOUNDRY.md) — Working with AI models and tools on Azure

## Upstream Sample Projects

The upstream handbook repository includes sample projects and exported Copilot CLI transcripts that demonstrate
many of these concepts from start to finish:

- [Blinkers](https://github.com/blbergo/icf-mentee-handbook-2026/tree/main/samples/blinkers) — A .NET console app that builds a focused, neurodivergent-friendly text simplification agent using the GitHub Copilot SDK and Microsoft Agent Framework.
- [bg-dashboard](https://github.com/blbergo/icf-mentee-handbook-2026/tree/main/samples/bg-dashboard) — A full-stack blood-glucose dashboard with a React frontend and FastAPI + PyTorch LSTM backend, orchestrated with Docker Compose.
