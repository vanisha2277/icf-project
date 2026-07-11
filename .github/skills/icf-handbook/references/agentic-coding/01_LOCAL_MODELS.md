# Local Models

## Running Copilot CLI with Ollama (no Copilot subscription required)

If you do not have access to a GitHub Copilot subscription, you can still use **Copilot CLI** by connecting it to a model running locally on your own machine through [Ollama](https://ollama.com). This is completely free and keeps all of your data on your computer.

### What you need

| Requirement | Details |
|---|---|
| **Copilot CLI** | [Install instructions](https://github.com/features/copilot/cli/) |
| **Ollama** | Download from [ollama.com](https://ollama.com) |
| **A compatible model** | Must support **tool calling** (function calling) and **streaming** |

### Step 1 - Check what your hardware can run

Before downloading a model, visit **[canirun.ai](https://www.canirun.ai/)** to find out which models your machine can actually handle.

The site runs entirely in your browser - it detects your CPU, RAM, and GPU automatically and grades 68+ open-weight models from **S** (runs great) to **F** (won't fit). It also shows estimated tokens-per-second and lets you filter by use case (chat, code, reasoning, vision).

> **Tip:** Look for models graded **A or above** at the **Q4_K_M** quantization level. This is a good balance of quality and performance for most laptops. A context window of at least 64k tokens is recommended for best results with Copilot CLI.

### Step 2 - Install Ollama and pull a model

1. Download and install Ollama from [ollama.com](https://ollama.com).

2. Open a terminal and pull the model you chose. For example:

   ```bash
   ollama pull qwen3.5
   ```

   You can browse available models at [ollama.com/library](https://ollama.com/library).

3. Confirm Ollama is running and the model is available:

   ```bash
   curl http://localhost:11434/api/tags
   ```

   You should see your model listed in the JSON response.

### Step 3 - Launch Copilot CLI with Ollama

The easiest way to get started is with the built-in quick setup:

```bash
ollama launch copilot
```

Or run directly with a specific model:

```bash
ollama launch copilot --model qwen3.5
```

#### Manual setup

If you prefer to configure things yourself, Copilot CLI connects to Ollama using the OpenAI-compatible API via environment variables.

**macOS / Linux (bash or zsh):**

```bash
export COPILOT_PROVIDER_BASE_URL=http://localhost:11434/v1
export COPILOT_PROVIDER_API_KEY=
export COPILOT_PROVIDER_WIRE_API=responses
export COPILOT_MODEL=qwen3.5
copilot
```

**Windows (PowerShell):**

```powershell
$env:COPILOT_PROVIDER_BASE_URL = "http://localhost:11434/v1"
$env:COPILOT_PROVIDER_API_KEY = ""
$env:COPILOT_PROVIDER_WIRE_API = "responses"
$env:COPILOT_MODEL = "qwen3.5"
copilot
```

Or run with environment variables inline:

```bash
COPILOT_PROVIDER_BASE_URL=http://localhost:11434/v1 COPILOT_PROVIDER_API_KEY= COPILOT_PROVIDER_WIRE_API=responses COPILOT_MODEL=qwen3.5 copilot
```

Replace `qwen3.5` with whatever model name you pulled in step 2.

### Step 4 (optional) - Run in headless mode

You can run Copilot CLI without interaction for use in Docker, CI/CD, or scripts:

```bash
ollama launch copilot --model qwen3.5 --yes -- -p "how does this repository work?"
```

The `--yes` flag auto-pulls the model, skips selectors, and requires `--model` to be specified. Arguments after `--` are passed directly to Copilot CLI.

### Step 5 (optional) - Run in offline mode

If you want Copilot CLI to avoid contacting GitHub servers entirely (for example, if you are on a limited or no internet connection), add:

```bash
export COPILOT_OFFLINE=true
```

```powershell
$env:COPILOT_OFFLINE = "true"
```

This ensures the CLI only communicates with your local Ollama instance.

### Choosing a model - quick recommendations

These models are recommended by the [official Ollama documentation](https://docs.ollama.com/integrations/copilot-cli) for use with Copilot CLI:

| Model | Notes |
|---|---|
| `qwen3.5` | General coding and chat |
| `glm-4.7-flash` | Fast responses |

> Always verify compatibility on [canirun.ai](https://www.canirun.ai/) with your specific hardware before downloading.

### Troubleshooting

| Problem | Solution |
|---|---|
| *"model does not support tool calling"* | Pick a different model - not all models support function calling. Check the model's page on [ollama.com/library](https://ollama.com/library) for tool-call support. |
| *Connection refused* | Make sure Ollama is running (`ollama serve` in a separate terminal). |
| *Very slow responses* | Try a smaller model or a more aggressive quantization (e.g., Q4 instead of Q8). Check [canirun.ai](https://www.canirun.ai/) for estimated speed. |
| *Out of memory* | Close other applications, or switch to a smaller model. |
| *Context too short* | Copilot requires a large context window (at least 64k tokens). See the [Ollama context length documentation](https://docs.ollama.com/context-length) for how to adjust it. |

### Further reading

- [Official Ollama × Copilot CLI documentation](https://docs.ollama.com/integrations/copilot-cli)
- [Official Copilot CLI BYOK documentation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/use-byok-models)
- [Ollama model library](https://ollama.com/library)
- [canirun.ai source code](https://github.com/midudev/canirun.ai)