# MCP Servers

## Extending your coding agent with the Model Context Protocol

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is an open standard that lets AI coding agents connect to external tools, data sources, and services. Think of MCP servers as plugins — they give your agent new abilities beyond reading and editing files.

For example, an MCP server could let your agent:

- Run a browser and interact with web pages ([Playwright](https://github.com/mcp/servers/playwright-mcp))
- Query a database
- Search documentation
- Interact with GitHub APIs (built in to Copilot CLI)

> **Note:** The [GitHub MCP server](https://github.com/github/github-mcp-server) is built into Copilot CLI and available without any additional setup. The steps below are for adding *other* MCP servers.

## How MCP servers work

An MCP server is a small program that exposes **tools** (functions the agent can call). When you connect an MCP server to Copilot CLI, the agent automatically discovers the available tools and can use them when they are relevant to your prompt.

There are two main types:

| Type | How it works | Example |
|---|---|---|
| **Local (stdio)** | Runs a process on your machine, communicates via stdin/stdout | `npx @playwright/mcp@latest` |
| **Remote (http)** | Connects to a server over the network | `https://mcp.context7.com/mcp` |

## Adding an MCP server

### Option 1 — Use the `/mcp add` command (recommended)

This is the easiest way. Inside Copilot CLI:

1. Type `/mcp add` and press Enter. A configuration form appears.
2. Use `Tab` to navigate between fields.
3. Fill in the fields:

   | Field | What to enter |
   |---|---|
   | **Server Name** | A short name you will use to refer to this server (e.g., `playwright`) |
   | **Server Type** | Choose **STDIO** for local servers or **HTTP** for remote servers |
   | **Command** (local only) | The command to start the server, e.g., `npx @playwright/mcp@latest` |
   | **Environment Variables** (local only) | Any environment variables as JSON, e.g., `{"API_KEY": "your-key"}` |
   | **URL** (remote only) | The server's URL, e.g., `https://mcp.context7.com/mcp` |
   | **HTTP Headers** (remote only) | Any required headers as JSON, e.g., `{"Authorization": "Bearer your-token"}` |
   | **Tools** | Enter `*` for all tools, or a comma-separated list of specific tool names |

4. Press `Ctrl+S` to save. The server is available immediately — no restart needed.

### Option 2 — Edit the configuration file directly

You can also add MCP servers by editing the configuration file at `~/.copilot/mcp-config.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "type": "stdio",
      "command": "npx",
      "args": ["@playwright/mcp@latest"],
      "env": {},
      "tools": ["*"]
    },
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp",
      "headers": {},
      "tools": ["*"]
    }
  }
}
```

> **Tip:** You can also put MCP configuration in `.github/mcp.json` in your repository. This is useful for sharing MCP server setups with your team — anyone who clones the repo will have the same servers configured.

## Where MCP configuration is loaded from

Copilot CLI loads and merges MCP configuration from several locations, in the following order of precedence:

| Location | Scope |
|---|---|
| `~/.copilot/mcp-config.json` | Personal — applies to all your projects |
| `.github/mcp.json` | Repository — shared with anyone who clones the repo |
| `.mcp.json` | Workspace — for project-specific overrides |

## Managing MCP servers

Once a server is added, you can manage it using `/mcp` commands inside Copilot CLI:

| Command | What it does |
|---|---|
| `/mcp show` | List all configured MCP servers and their status |
| `/mcp show <name>` | Show details and available tools for a specific server |
| `/mcp edit <name>` | Edit a server's configuration |
| `/mcp disable <name>` | Temporarily disable a server (keeps the configuration) |
| `/mcp enable <name>` | Re-enable a previously disabled server |
| `/mcp delete <name>` | Remove a server entirely |

> **Tip:** Use `/env` to see everything loaded in your current environment — MCP servers, skills, custom instructions, and more.

## Finding MCP servers

The [GitHub MCP Registry](https://github.com/mcp) is a curated list of MCP servers from partners and the community. Browse it to discover servers that might be useful for your project.

Some popular MCP servers include:

| Server | What it does |
|---|---|
| [Playwright](https://github.com/mcp/servers/playwright-mcp) | Browser automation — navigate pages, fill forms, take screenshots |
| [Context7](https://github.com/upstash/context7) | Up-to-date documentation lookup for libraries and frameworks |
| [GitHub MCP Server](https://github.com/github/github-mcp-server) | GitHub API access (built into Copilot CLI) |

## Security considerations

MCP servers can run code on your machine or connect to external services. Keep these things in mind:

- **Only add servers you trust.** A malicious MCP server could access files on your computer or send data to external services.
- **Never hardcode secrets** in configuration files that you commit to a repository. Use environment variables instead.
- **Review tool permissions.** Instead of using `"tools": ["*"]`, consider listing only the specific tools you need.
- Copilot CLI will prompt you before enabling workspace-level MCP configurations from repositories you have not previously trusted.

## Troubleshooting

| Problem | Solution |
|---|---|
| *Server not showing up* | Run `/mcp show` to check if it was added. Make sure the configuration file is valid JSON. |
| *"Command not found"* | Ensure the command (e.g., `npx`, `uvx`) is installed and available in your `PATH`. |
| *Server keeps crashing* | Check that all required environment variables are set. Run the server command manually in a terminal to see error output. |
| *Tools not appearing* | Run `/mcp show <name>` to verify the server started successfully and lists its tools. |
| *Permission denied* | Some MCP servers need API keys or tokens. Check the server's documentation for required credentials. |

## Further reading

- [Official MCP documentation](https://modelcontextprotocol.io/introduction)
- [Adding MCP servers for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers)
- [About Model Context Protocol (MCP)](https://docs.github.com/en/copilot/concepts/about-mcp)
- [GitHub MCP Registry](https://github.com/mcp)
- [GitHub MCP Server](https://github.com/github/github-mcp-server)