# Skills

## Teaching your coding agent specialized tasks

Agent skills are folders of instructions, scripts, and resources that your coding agent can load when relevant to improve its performance in specific tasks. Think of a skill as a mini instruction manual — it tells the agent *how* to do something, and the agent only loads it when the task calls for it.

For example, a skill could teach your agent to:

- Debug failing GitHub Actions workflows using specific tools
- Convert image formats by running a shell script
- Follow your team's code review checklist
- Navigate this handbook (that is how you are reading this right now!)

> **Note:** Skills are different from [custom instructions](02_PROMPTING.md#custom-instructions). Custom instructions are loaded on *every* prompt (e.g., "always use semantic HTML"). Skills are loaded only when relevant to the current task.

## What a skill looks like

Every skill is a folder containing a `SKILL.md` file and, optionally, other resources like scripts or example files. Here is a minimal example:

```
.github/skills/github-actions-debugging/
├── SKILL.md
```

The `SKILL.md` file has two parts:

1. **YAML frontmatter** — metadata that tells the agent what the skill does
2. **Markdown body** — the actual instructions

> **Real-world example:** The skill you are using right now lives at [`.github/skills/icf-handbook/`](../../) in this repository. It includes a `SKILL.md` with YAML frontmatter and a `references/` folder containing all the handbook pages. Browse its source to see how a skill with multiple reference documents is structured.

### Example `SKILL.md`

```markdown
---
name: github-actions-debugging
description: Guide for debugging failing GitHub Actions workflows. Use when asked to debug failing CI.
---

To debug failing GitHub Actions workflows, follow this process:

1. Use the `list_workflow_runs` tool to look up recent runs and their status
2. Use the `summarize_job_log_failures` tool to get an AI summary of log failures
3. If you need more detail, use `get_job_logs` for the full logs
4. Try to reproduce the failure locally
5. Fix the issue and verify the fix before committing
```

### Frontmatter fields

| Field | Required | Description |
|---|---|---|
| `name` | Yes | A unique identifier, lowercase with hyphens (e.g., `webapp-testing`) |
| `description` | Yes | What the skill does and when the agent should use it |
| `allowed-tools` | No | Tools the skill can use without asking permission (e.g., `shell`) |
| `license` | No | License that applies to this skill |

> **Warning:** Only add `shell` or `bash` to `allowed-tools` if you have reviewed the skill's scripts and fully trust them. Pre-approving shell access means the agent can run terminal commands without asking you first.

## Where to put skills

| Location | Scope | Who can use it |
|---|---|---|
| `.github/skills/` | Project | Anyone who clones the repo |
| `.claude/skills/` | Project (alternative) | Same as above |
| `.agents/skills/` | Project (alternative) | Same as above |
| `~/.copilot/skills/` | Personal | You, across all projects |
| `~/.agents/skills/` | Personal (alternative) | Same as above |

## Creating a skill — step by step

### Step 1 — Create the skill folder

Pick a location from the table above and create a new subdirectory for your skill. Use lowercase names with hyphens:

```bash
mkdir -p .github/skills/my-cool-skill
```

### Step 2 — Write the `SKILL.md` file

Create a `SKILL.md` file inside your skill folder. Start with the frontmatter, then write clear instructions in the Markdown body:

```bash
touch .github/skills/my-cool-skill/SKILL.md
```

Fill it in with your instructions. Be specific about:

- **When** the skill should be used
- **What steps** the agent should follow
- **What tools** to use at each step
- **What the expected outcome** looks like

### Step 3 — Add scripts or resources (optional)

You can include scripts, example files, or supplementary Markdown in the skill folder. The agent automatically discovers all files in the skill directory when the skill is invoked.

For example, a skill that converts SVG images to PNG:

```
.github/skills/image-convert/
├── SKILL.md
└── convert-svg-to-png.sh
```

In your `SKILL.md`, reference the script:

```markdown
When asked to convert an SVG to PNG, run the `convert-svg-to-png.sh` script
from this skill's base directory, passing the input SVG file path as the
first argument.
```

### Step 4 — Use the skill

If you added the skill during an active Copilot CLI session, reload it:

```
/skills reload
```

Then use the skill in one of these ways:

- **By name:** Include the skill name with a `/` prefix in your prompt:

  ```
  Use the /image-convert skill to convert logo.svg to PNG
  ```

- **By inference:** Just describe the task. If your skill's description matches, the agent will load it automatically:

  ```
  Convert logo.svg to a PNG file
  ```

## Managing skills in Copilot CLI

| Command | What it does |
|---|---|
| `/skills list` | List all available skills |
| `/skills info <name>` | Show details about a specific skill, including its location |
| `/skills` | Toggle skills on or off interactively |
| `/skills reload` | Reload skills without restarting the CLI |
| `/skills add` | Add an alternative directory to search for skills |
| `/skills remove <dir>` | Remove a skill directory you previously added |

## Adding skills from the community

You do not have to write every skill from scratch. You can install skills that others have shared:

1. Download a skill directory (e.g., from the [Awesome Copilot](https://github.com/github/awesome-copilot) collection)
2. If it is a `.zip`, unzip it
3. Move the skill folder to `.github/skills/` (project) or `~/.copilot/skills/` (personal)
4. Run `/skills reload` in Copilot CLI

You can also use GitHub CLI to search for and install skills:

```bash
gh skill search <query>
gh skill install <repo>
```

## Tips for writing good skills

- **Be specific in the description.** The agent uses the description to decide when to load the skill. A vague description like "helps with testing" is less useful than "runs integration tests for the Express API using Jest and a PostgreSQL test database."
- **Include step-by-step instructions.** Numbered steps help the agent follow a consistent process.
- **Mention specific tool names.** If your skill relies on particular tools (e.g., MCP server tools, shell commands), name them explicitly.
- **Keep skills focused.** One skill should do one thing well. If you have multiple unrelated tasks, create separate skills.
- **Test your skill.** Try invoking it with different prompts to make sure the agent picks it up and follows the instructions correctly.

## Further reading

- [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [Adding agent skills for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
- [Handbook skill source](../../) — The skill powering this handbook, a real-world example with multiple reference documents
- [Awesome Copilot skills collection](https://github.com/github/awesome-copilot)
- [Agent Skills open standard](https://github.com/agentskills/agentskills)
