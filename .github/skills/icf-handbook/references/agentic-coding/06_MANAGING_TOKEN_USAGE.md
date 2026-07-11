# Managing Token Usage

## Understanding and controlling how much context your agent uses

Every time you interact with a coding agent, your prompt, the agent's response, tool outputs, file contents, and system instructions all occupy space in a **context window** — the total amount of information the model can "see" at once. This space is measured in **tokens** (roughly ¾ of a word).

When the context window fills up, older messages get summarized or dropped. This can cause the agent to "forget" earlier parts of your conversation. Understanding how tokens work helps you have longer, more productive sessions.

## What takes up tokens

| Source | Description | Impact |
|---|---|---|
| **Your prompts** | Every message you type | Small per message |
| **Agent responses** | The agent's replies, including code it writes | Moderate to large |
| **Tool outputs** | Results from reading files, running commands, searching | Can be very large |
| **System instructions** | Built-in rules, custom instructions, loaded skills | Always present |
| **Conversation history** | All previous messages in the session | Grows over time |

The biggest token consumers are usually **tool outputs** — reading a large file or running a command with verbose output can use thousands of tokens in a single step.

## Checking your token usage

Copilot CLI provides commands to monitor how you are using your context window:

### `/context` — see your token usage

Displays a visual breakdown of how your context window is being used — how much is taken by system instructions, conversation history, tool results, and how much room is left.

```
/context
```

Use this when the agent starts giving less relevant answers or seems to have forgotten something you discussed earlier.

### `/usage` — see session statistics

Shows a summary of your session, including:

- Total AI credits consumed
- Session duration
- Lines of code edited
- Token usage broken down by model

```
/usage
```

## Freeing up context space

### `/compact` — summarize your conversation

The `/compact` command compresses your conversation history into a shorter summary, freeing up space in the context window while preserving the key points.

```
/compact
```

You can also give it a focus to tell it what to prioritize when summarizing:

```
/compact focus on the database migration changes
```

> **Tip:** Copilot CLI automatically compacts your history in the background when your conversation approaches 95% of the context window. You do not need to do this manually unless you want to reclaim space earlier.

### Start a new session

If your context is very full and `/compact` is not enough, start a fresh session:

```
/clear
```

Or exit and restart Copilot CLI. You can always resume a previous session later with `/resume`.

## Strategies for using fewer tokens

### 1. Be specific in your prompts

Vague prompts cause the agent to read more files and run more tools to figure out what you mean. Specific prompts lead to targeted actions that use less context.

| Uses more tokens | Uses fewer tokens |
|---|---|
| "Fix the bug" | "Fix the null check in `src/auth.js` line 42" |
| "Explain this project" | "Explain how `src/api/routes.ts` handles authentication" |

### 2. Point to specific files with `@`

Instead of letting the agent search your codebase, tell it exactly which files to look at:

```
Refactor the error handling in @src/utils/validation.js
```

This avoids unnecessary file reads and searches that consume tokens.

### 3. Break work into smaller sessions

Instead of doing everything in one long session, tackle tasks one at a time. Each new session starts with a fresh context window.

For example, instead of one session that builds an entire feature:

1. **Session 1:** Design the data model
2. **Session 2:** Implement the API endpoints
3. **Session 3:** Write the tests

### 4. Use `/compact` proactively

Do not wait until the context window is almost full. Run `/compact` after completing a chunk of work — for example, after finishing one task and before starting the next.

### 5. Choose the right model for the job

Different models have different context window sizes and token costs:

| Model size | Context window | Best for |
|---|---|---|
| Smaller / faster models | 128k tokens | Quick questions, simple edits |
| Larger models | 200k+ tokens | Complex multi-file tasks |
| Extended context models | Up to 1M tokens | Large codebase analysis |

Use `/model` to switch models. Smaller models are faster and use fewer credits for simple tasks.

### 6. Avoid unnecessary tool output

If you ask the agent to run a command that produces a lot of output (like a full test suite), that output fills the context window. Instead:

- Ask for specific test files: *"Run only the auth tests"*
- Ask to summarize: *"Run the tests and just tell me if they pass"*
- Pipe output through filters: *"Run the linter and only show errors, not warnings"*

## Understanding AI credits

GitHub Copilot uses **AI credits** to track usage. Your plan includes a monthly allotment of credits, and different actions consume credits at different rates.

| What | Credits used? |
|---|---|
| Code completions (ghost text) | **Free** — unlimited on all plans |
| Copilot Chat and CLI conversations | Yes |
| Agent mode (multi-step tasks) | Yes — can use more credits per task |
| Code review | Yes |

More powerful models and longer conversations use more credits. You can check your remaining credits in your [GitHub billing settings](https://github.com/settings/billing).

> **Tip:** If you are using Copilot CLI with a [local model through Ollama](01_LOCAL_MODELS.md), token usage does not consume any AI credits — everything runs on your own machine.

## Quick reference

| Command | What it does |
|---|---|
| `/context` | Show context window usage breakdown |
| `/usage` | Show session statistics and credit usage |
| `/compact` | Summarize conversation to free up space |
| `/compact <focus>` | Summarize with a specific focus |
| `/model` | Switch to a different model |
| `/clear` | Start a fresh session |
| `/resume` | Resume a previous session |

## Further reading

- [Using GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/overview)
- [Models and pricing for GitHub Copilot](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)
- [Prompt engineering for GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)