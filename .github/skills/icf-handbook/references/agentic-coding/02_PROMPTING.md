# Prompting

## Tips for effective prompting with Copilot CLI

The way you write your prompts has a big impact on the quality and usefulness of the responses you get from an AI coding agent. This guide covers practical strategies for getting better results.

## Be specific about what you want

Vague prompts produce vague results. Instead of asking the agent to "make a website," describe what you actually need.

| ❌ Vague | ✅ Specific |
|---|---|
| "Make a website" | "Create a React app with a homepage that displays a list of upcoming events from a JSON file" |
| "Fix this bug" | "The login form submits even when the email field is empty — add client-side validation" |
| "Write tests" | "Write unit tests for the `calculateTotal` function in `src/utils.js` using Jest" |

> **See it in action:** The upstream handbook repository includes sample projects — [Blinkers](https://github.com/blbergo/icf-mentee-handbook-2026/tree/main/samples/blinkers) and [bg-dashboard](https://github.com/blbergo/icf-mentee-handbook-2026/tree/main/samples/bg-dashboard) — built by AI coding agents. You can read their session transcripts ([Blinkers](https://github.com/blbergo/icf-mentee-handbook-2026/blob/main/samples/copilot-session.md), [bg-dashboard](https://github.com/blbergo/icf-mentee-handbook-2026/blob/main/samples/bg-dashboard/copilot-session.md)) to see how specific, iterative prompts guided the agent through planning, implementation, and debugging.

## Provide context

The agent works best when it understands the bigger picture. Include relevant details like:

- **What already exists** — "I have a Flask app with a SQLite database and two models: `User` and `Event`"
- **What technology to use** — "Use TypeScript and the Express framework"
- **What constraints apply** — "This needs to work without JavaScript enabled in the browser"
- **Who the audience is** — "This is for a screen reader-accessible registration form"

## Break large tasks into smaller steps

Instead of asking for an entire feature in one prompt, break it down. This gives you more control and makes it easier to catch mistakes early.

For example, instead of:

> "Build a complete user authentication system"

Try a series of prompts:

1. "Create a `User` model with fields for email and hashed password"
2. "Add a registration endpoint that validates the email and hashes the password"
3. "Add a login endpoint that returns a session token"
4. "Add middleware that checks the session token on protected routes"

## Use examples to clarify format

If you need output in a specific format, show the agent what you expect:

> "Generate a JSON array of 5 sample events. Each event should look like this:
> ```json
> {
>   "id": 1,
>   "title": "Opening Ceremony",
>   "date": "2026-07-15",
>   "location": "Main Hall"
> }
> ```"

## State what you do NOT want

Sometimes it helps to be explicit about what to avoid:

- "Do not use any external libraries — use only the Node.js standard library"
- "Do not modify any existing tests"
- "Avoid inline styles — use CSS classes instead"

## Iterate and refine

You do not need to get the perfect prompt on the first try. If the result is not quite right, follow up:

- "That's close, but move the navigation bar to the left side"
- "Can you refactor that to use async/await instead of callbacks?"
- "Add error handling for the case where the API returns a 404"

The agent remembers the conversation context, so you can build on previous responses.

---

## How the agent sees your prompt

Before your message reaches the model, Copilot CLI assembles a **context window** — everything the model can "see" at once. The context window is filled in layers:

1. **System prompt** — Built-in instructions from Copilot that define the agent's behavior, safety rules, and available tools. You cannot edit this, but it is always present.
2. **Custom instructions** — Your project-level or user-level instructions that tailor the agent to your codebase (see below).
3. **Conversation history** — Previous messages in the current session.
4. **Your new message** — The prompt you just typed.

The context window has a fixed size (measured in tokens). When a conversation gets long, older messages may be summarized or dropped to make room. You can use `/compact` to manually summarize the history and free up space.

### Custom instructions

Custom instructions let you give the agent persistent context it should always know — things like your tech stack, coding conventions, or project structure. Copilot CLI reads instructions from several files automatically:

| File | Scope |
|---|---|
| `CLAUDE.md` / `GEMINI.md` / `AGENTS.md` | Project root or current directory |
| `.github/copilot-instructions.md` | Repository-wide |
| `.github/instructions/**/*.instructions.md` | Targeted instructions (can use glob patterns to apply to specific files) |
| `~/.copilot/copilot-instructions.md` | Personal, across all repositories |

This is where you put things you would otherwise repeat in every prompt — for example, *"This project uses Python 3.12 and pytest"* or *"Always use semantic HTML elements."*

> **Tip:** Use `/instructions` to see which instruction files are currently loaded, and `/env` to see the full environment (instructions, MCP servers, skills, and more).

## Agent planning, thinking, and tool use

Understanding how the agent plans, reasons, and uses tools helps you write prompts that work *with* its process rather than against it.

### Planning

For complex tasks, have the agent plan before it codes. Copilot CLI has a built-in **`/plan`** command that creates an implementation plan without making any changes — use it when you want to review the approach first.

You can also guide planning directly in your prompt:

- Ask for a plan: *"Outline the steps you would take to add pagination before making any changes."*
- Provide your own plan: *"First add a `page` query param, then update the query with LIMIT/OFFSET, then return the total count in headers."*

### Thinking

AI models reason step by step ("chain-of-thought"). You can encourage deeper reasoning by flagging complexity or asking the agent to think before it acts:

- *"Think through the edge cases before writing this function."*
- *"This involves tricky date math across time zones — be careful with daylight saving transitions."*

> **Tip:** Use `ctrl+t` in Copilot CLI to toggle the reasoning display and see the agent's thought process as it works.

### Tool use

The agent can read, edit, and create files, search your codebase, run shell commands, search the web, and launch sub-agents. You can steer it toward specific tools in your prompt:

- *"Read the existing tests before writing new ones"* — look before you leap.
- *"Run the tests after making changes"* — verify the work.
- *"Search the codebase for how we handle errors elsewhere"* — match existing patterns.

### Further reading

- [GitHub Copilot documentation — prompt engineering](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- [GitHub Copilot CLI documentation](https://docs.github.com/en/copilot/how-tos/copilot-cli)
- [Example session: building Blinkers](https://github.com/blbergo/icf-mentee-handbook-2026/blob/main/samples/copilot-session.md) — A complete exported Copilot CLI session showing real-world prompting, planning, and iterative development from start to finish
- [Example session: building bg-dashboard](https://github.com/blbergo/icf-mentee-handbook-2026/blob/main/samples/bg-dashboard/copilot-session.md) — Another full session transcript showing how an AI agent built a multi-service full-stack application
