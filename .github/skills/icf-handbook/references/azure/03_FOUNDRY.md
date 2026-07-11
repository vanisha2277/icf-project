# Azure AI Foundry

## Adding AI features to your project

Azure AI Foundry is Microsoft's platform for working with AI models. It gives you access to models from OpenAI, Meta, Mistral, and others through a single interface — either in the browser or through an API you can call from your code.

If your festival project involves generating text, summarizing content, answering questions, analyzing images, or anything else that benefits from an AI model, Foundry is one way to do it.

## What you get

| Capability | Description |
|---|---|
| **Model catalog** | Browse and try hundreds of models from different providers |
| **Playgrounds** | Test models in the browser before writing any code |
| **API endpoints** | Call models from your app using REST or SDKs |
| **Prompt management** | Save and version your prompts |
| **Evaluation tools** | Measure how well your model performs on test inputs |

## Key concepts

### Projects and hubs

Foundry organizes work into **projects**. A project is where you deploy models, store prompts, and run evaluations. Projects live inside a **hub**, which handles shared settings like networking and access control.

For a festival project, you'll typically create one hub and one project.

### Model deployments

Before you can call a model from your code, you need to **deploy** it. A deployment gives you an API endpoint — a URL your app sends requests to and gets responses from.

Deployments come in two flavors:

| Type | How it works | Best for |
|---|---|---|
| **Serverless (pay-per-token)** | You pay for what you use, no infrastructure to manage | Most festival projects — simple and low cost |
| **Provisioned** | Reserved capacity with predictable performance | High-traffic production apps (unlikely to need for the festival) |

### Tokens and pricing

Models charge by **tokens** — chunks of text roughly ¾ of a word long. Both your input (the prompt) and the model's output count toward the total. Pricing varies by model; check the [Azure AI Foundry pricing page](https://azure.microsoft.com/pricing/details/azure-ai-foundry/) for current rates.

A short request (a few sentences in, a paragraph out) typically costs a fraction of a cent.

## Getting started

### 1. Open Azure AI Foundry

Go to [ai.azure.com](https://ai.azure.com) and sign in with your Azure account.

### 2. Create a hub and project

1. Click **Create project**
2. Give it a name (e.g., `festival-ai`)
3. Pick a region — `East US` or `West US 2` have good model availability
4. Azure will create a hub automatically if you don't have one

### 3. Try a model in the playground

1. Go to **Model catalog** and browse or search for a model (e.g., `gpt-4o-mini`)
2. Click **Deploy** and choose **Serverless**
3. Once deployed, open the **Playground**
4. Type a prompt and see the response

This is the fastest way to experiment before writing any code.

### 4. Call the model from your code

After deploying a model, you get an endpoint URL and an API key. You can call it using the Azure AI Inference SDK or plain HTTP requests.

**Python example:**

```bash
pip install azure-ai-inference
```

```python
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

client = ChatCompletionsClient(
    endpoint="https://<your-endpoint>.models.ai.azure.com",
    credential=AzureKeyCredential("<your-api-key>"),
)

response = client.complete(
    messages=[
        {"role": "user", "content": "Suggest a name for a hackathon team"}
    ],
    model="gpt-4o-mini",
)

print(response.choices[0].message.content)
```

**JavaScript example:**

```bash
npm install @azure/ai-inference
```

```javascript
import ModelClient, { isUnexpected } from "@azure/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const client = ModelClient(
  "https://<your-endpoint>.models.ai.azure.com",
  new AzureKeyCredential("<your-api-key>")
);

const response = await client.path("/chat/completions").post({
  body: {
    messages: [
      { role: "user", content: "Suggest a name for a hackathon team" }
    ],
    model: "gpt-4o-mini",
  },
});

if (!isUnexpected(response)) {
  console.log(response.body.choices[0].message.content);
}
```

> **Tip:** Keep your API key out of your source code. Use environment variables or a `.env` file and make sure it's in your `.gitignore`.

### 5. Find your endpoint and key

In your Foundry project, go to **Deployments** → click your deployment → the endpoint URL and key are shown on the detail page. You can also retrieve them with the CLI:

```bash
az ai model deployment show \
  --name gpt-4o-mini \
  --project-name festival-ai \
  --query "{endpoint: endpoint, key: key}"
```

## Choosing a model

The model catalog has a lot of options. Here are a few practical guidelines:

| Need | Suggested model | Why |
|---|---|---|
| General text generation | `gpt-4o-mini` | Good quality, low cost |
| Complex reasoning | `gpt-4o` | More capable, higher cost |
| Image understanding | `gpt-4o` | Accepts image inputs |
| Open-weight / self-hosted | `Meta-Llama-3-8B` | No per-token charge if provisioned |
| Embeddings (search, similarity) | `text-embedding-3-small` | Turns text into vectors for search |

Model availability varies by region. If a model you want isn't available, try a different region for your project.

## Keeping costs low

- **Start with `gpt-4o-mini`** — it's significantly cheaper than larger models and handles most tasks well.
- **Keep prompts short** — longer prompts use more tokens and cost more.
- **Set a max token limit** — add `max_tokens` to your API calls to cap response length.
- **Cache responses** — if your app asks the same question repeatedly, store the answer instead of calling the API each time.
- **Monitor usage** — check your deployment's metrics in the portal to see how many tokens you're consuming.

See [Managing Cost](02_MANAGING_COST.md) for general Azure cost management tips.

> **Sample project:** The [bg-dashboard](https://github.com/blbergo/icf-mentee-handbook-2026/tree/main/samples/bg-dashboard) sample in the upstream handbook repository uses a local PyTorch LSTM model for blood-glucose forecasting and was built entirely by an AI coding agent ([session transcript](https://github.com/blbergo/icf-mentee-handbook-2026/blob/main/samples/bg-dashboard/copilot-session.md)). This is a useful example of an AI-powered project. If you wanted to swap the local model for a cloud-hosted one, you could replace the LSTM inference with calls to an Azure AI Foundry deployment using the patterns shown above.

## Quick reference

| Task | How |
|---|---|
| Open Foundry | [ai.azure.com](https://ai.azure.com) |
| Browse models | Model catalog in your project |
| Test a model | Deploy it, then use the Playground |
| Call from code | Use the Azure AI Inference SDK or REST API |
| Check token usage | Portal → Deployments → Metrics |

## Further reading

- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure AI Inference SDK (Python)](https://learn.microsoft.com/python/api/overview/azure/ai-inference-readme)
- [Azure AI Inference SDK (JavaScript)](https://learn.microsoft.com/javascript/api/overview/azure/ai-inference-readme)
- [Model catalog](https://ai.azure.com/explore/models)
- [Azure AI Foundry pricing](https://azure.microsoft.com/pricing/details/azure-ai-foundry/)
