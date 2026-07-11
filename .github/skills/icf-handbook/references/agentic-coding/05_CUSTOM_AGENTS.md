# Custom Agents

## Building specialized personas for your coding agent

Custom agents let you create specialized versions of your coding agent, each with tailored expertise for specific tasks. Instead of explaining what you need every time, you define an agent once and it is ready to use whenever you need it.

For example, you could create custom agents for:

- **Security auditing** — reviews code for vulnerabilities and creates GitHub issues
- **Test writing** — focuses on test coverage without modifying production code
- **Documentation** — generates and maintains project documentation
- **Implementation planning** — creates detailed technical specs and task breakdowns

When you give the agent a task that matches a custom agent's expertise, it automatically delegates the work to that agent in a separate context window. This keeps the main conversation focused on high-level planning while the custom agent handles the specialized work.

## What a custom agent looks like

Each custom agent is defined by a single Markdown file with an `.agent.md` extension. Like [skills](04_SKILLS.md), it has YAML frontmatter for configuration and a Markdown body for instructions.

### Example agent file

Here is a simple custom agent that specializes in writing tests:

```markdown
---
name: test-specialist
description: Focuses on test coverage, quality, and testing best practices without modifying production code
---

You are a testing specialist focused on improving code quality through
comprehensive testing. Your responsibilities:

- Analyze existing tests and identify coverage gaps
- Write unit tests, integration tests, and end-to-end tests
- Review test quality and suggest improvements
- Ensure tests are isolated, deterministic, and well-documented
- Focus only on test files — avoid modifying production code unless
  specifically requested

Always include clear test descriptions and use appropriate testing
patterns for the language and framework.
```

### Frontmatter fields

| Field | Required | Description |
|---|---|---|
| `name` | No | Display name for the agent (e.g., `test-specialist`) |
| `description` | **Yes** | What the agent does and when it should be used — the agent uses this to decide when to delegate |
| `tools` | No | Which tools the agent can use. Defaults to all tools. Use `[]` to disable all tools |
| `model` | No | Override the AI model for this agent |
| `disable-model-invocation` | No | If `true`, the agent must be manually selected — it will not be used automatically |
| `user-invocable` | No | If `false`, the agent cannot be selected manually and is only available programmatically |

## Where to put agent files

| Location | Scope |
|---|---|
| `.github/agents/` | Project — shared with anyone who clones the repo |
| `~/.copilot/agents/` | Personal — available across all your projects |

> **Note:** If you have agents with the same file name in both locations, the personal one (`~/.copilot/agents/`) takes precedence.

## Creating a custom agent

### Option 1 — Use the interactive wizard (recommended for beginners)

1. In Copilot CLI, type `/agent` and press Enter
2. Select **Create new agent**
3. Choose where to save it:
   - **Project** → `.github/agents/`
   - **User** → `~/.copilot/agents/`
4. Choose whether Copilot should write the agent profile for you, or you want to write it manually:

   **If Copilot writes it:** Describe the agent's expertise and when it should be used. For example:

   > I am a security expert. I check code files for potential security issues like exposed secrets, SQL injection, and cross-site scripting. Use me whenever a security review is requested.

   Copilot will generate a full agent profile. You can review and edit it before saving.

   **If you write it manually:** You will be prompted for the name, description, and instructions step by step.

5. Choose which tools the agent should have access to (default is all tools)
6. Restart the CLI to load your new agent

### Option 2 — Create the file manually

1. Create a new `.agent.md` file in the appropriate directory:

   ```bash
   touch .github/agents/security-auditor.agent.md
   ```

2. Write the frontmatter and instructions:

   ```markdown
   ---
   name: security-auditor
   description: Reviews code for security vulnerabilities. Use when a security review or audit is requested.
   tools: ["read", "search", "edit"]
   ---

   You are a security specialist. When reviewing code:

   1. Search for common vulnerability patterns:
      - Hardcoded secrets or credentials
      - SQL injection risks
      - Cross-site scripting (XSS)
      - Insecure authentication patterns
   2. Check dependency files for known vulnerable packages
   3. Report findings with risk level and recommended fix
   4. Create a GitHub issue summarizing all findings
   ```

3. Restart the CLI or start a new session to load the agent

## Using a custom agent

There are several ways to invoke a custom agent:

### By name (slash command)

```
/agent
```

Then select the agent from the list and enter your prompt.

### By explicit instruction

Tell the agent which custom agent to use in your prompt:

```
Use the security-auditor agent on all files in the src/ directory
```

### By inference

Just describe the task. If the description in your agent file matches, the agent will use it automatically:

```
Check all Python files for potential security vulnerabilities
```

### From the command line

You can specify the agent directly when launching Copilot CLI:

```bash
copilot --agent security-auditor --prompt "Review src/auth.py"
```

The `--agent` value is the file name without the `.agent.md` extension.

## Controlling tool access

By default, custom agents have access to all tools. You can restrict this in the frontmatter:

```yaml
# Only allow reading and searching — no editing or shell commands
tools: ["read", "search"]
```

Common tool aliases:

| Alias | What it allows |
|---|---|
| `read` | Read file contents |
| `edit` | Edit and create files |
| `search` | Search for files and text |
| `execute` / `shell` | Run shell commands |
| `web` | Fetch URLs and search the web |
| `agent` | Invoke other custom agents |

Use an empty list (`tools: []`) to create a "read-only" or "advice-only" agent that cannot make any changes.

## Skills vs. custom agents

Skills and custom agents are both ways to customize your coding agent, but they serve different purposes:

| | Skills | Custom Agents |
|---|---|---|
| **What they are** | A set of instructions for a specific task | A specialized persona with its own context window |
| **File format** | `SKILL.md` in a folder | `<name>.agent.md` single file |
| **When loaded** | Injected into the main agent's context | Runs as a separate subagent |
| **Best for** | Step-by-step procedures, scripts, checklists | Broad areas of expertise, complex multi-step tasks |
| **Example** | "How to debug GitHub Actions" | "Security auditor that reviews code and files issues" |

> **Tip:** Use **skills** when you want to teach the agent a specific procedure. Use **custom agents** when you want to create a specialist that handles an entire category of work.

## Tips for writing good agents

- **Write a clear description.** This is the most important field — it determines when the agent gets used. Be specific about the agent's expertise and when it should be activated.
- **Define boundaries.** Tell the agent what it should *not* do. For example, a testing agent should probably not modify production code.
- **Restrict tools when appropriate.** An implementation planner might only need `read` and `search`, not `shell`.
- **Test with different prompts.** Try invoking the agent explicitly and by inference to make sure it activates when expected.
- **Start simple, then iterate.** Begin with a short description and a few instructions. Refine the agent profile as you discover what works.

## Sample project: Blinkers

The [Blinkers sample](https://github.com/blbergo/icf-mentee-handbook-2026/tree/main/samples/blinkers) in the upstream handbook repository was built entirely by an AI coding agent and demonstrates building a specialized agent using the [GitHub Copilot SDK](https://github.com/github/copilot-sdk) and [Microsoft Agent Framework](https://github.com/microsoft/agent-framework). While it uses the SDK rather than an `.agent.md` file, it illustrates the same principles covered in this guide:

- **Focused persona** — Blinkers is a neurodivergent-friendly text simplifier with a clear, specific purpose
- **Custom system prompt** — tailored instructions that define the agent's behavior and tone
- **Tool registration** — a custom `read_pdf` tool added to the agent's capabilities
- **Boundary setting** — the agent handles edge cases like video links and failed URLs gracefully

You can also read the [full Copilot CLI session](https://github.com/blbergo/icf-mentee-handbook-2026/blob/main/samples/copilot-session.md) that built Blinkers from scratch to see how iterative prompting and planning shaped the agent's design.

## Further reading

- [Creating custom agents for Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli)
- [Custom agents configuration reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [Awesome Copilot custom agents collection](https://github.com/github/awesome-copilot/tree/main/agents)
- [Custom agent examples](https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents)
- [Blinkers sample](https://github.com/blbergo/icf-mentee-handbook-2026/tree/main/samples/blinkers) — A .NET console app demonstrating a specialized agent built with the GitHub Copilot SDK
