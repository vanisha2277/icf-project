# Cloud Computing

## What it is and why it matters for your project

Cloud computing means using someone else's computers over the internet instead of running everything on your own machine. When you deploy a website, store data in a database, or run a background job "in the cloud," you are renting resources from a provider like Microsoft Azure, AWS, or Google Cloud.

Azure offers a [free tier](https://azure.microsoft.com/free/) and a [free account for students](https://azure.microsoft.com/free/students/) — both include enough resources to get a festival project off the ground.

## Why not just run everything locally?

You can — and for development, you probably should. But there are a few reasons you might want to move to the cloud:

| Reason | Example |
|---|---|
| **Sharing your work** | Other people can visit your site without connecting to your laptop |
| **Always on** | A cloud server stays running even when your computer is off |
| **Scaling** | If your project gets traffic, cloud resources can grow to handle it |
| **Services you can't run locally** | Managed databases, AI APIs, domain names with HTTPS |

If your project is a simple static site or a script that only you run, you may not need cloud hosting at all — and that's fine.

## Core concepts

### Regions

Cloud providers run data centers around the world. When you create a resource, you pick a **region** — the physical location where it runs. Choosing a region close to your users means lower latency (faster load times).

For the festival, any US region works well. `East US` or `West US 2` are common defaults.

### Resource groups

In Azure, a **resource group** is a folder that holds related resources. For example, you might put your web app, database, and storage account in a single resource group called `my-festival-project`. This makes it easy to see everything in one place and delete it all when you're done.

### The three service models

Cloud services are often described in three layers. You don't need to memorize these, but they help explain what you're responsible for versus what the provider handles.

| Model | What the provider manages | What you manage | Azure example |
|---|---|---|---|
| **IaaS** (Infrastructure) | Hardware, networking, VMs | OS, runtime, your app | Virtual Machines |
| **PaaS** (Platform) | Hardware, OS, runtime | Your app and its data | App Service, Azure Functions |
| **SaaS** (Software) | Everything | Configuration and usage | Microsoft 365, GitHub |

For most festival projects, **PaaS** is the sweet spot. You write your code and deploy it — Azure handles the servers, updates, and networking underneath.

### Common Azure services

Here are a few services you're likely to encounter. Each is covered in more detail in later handbook pages.

| Service | What it does | When to use it |
|---|---|---|
| **App Service** | Hosts web apps and APIs | You have a web app in Node.js, Python, .NET, etc. |
| **Azure Functions** | Runs small pieces of code on demand | You need a webhook, scheduled job, or lightweight API |
| **Azure Static Web Apps** | Hosts static sites with optional API backends | You built a frontend with React, Vue, HTML/CSS, etc. |
| **Azure SQL / Cosmos DB** | Managed databases | Your app needs to store and query data |
| **Azure AI Foundry** | Access to AI models and tools | You want to add AI features to your project |

> See [Azure AI Foundry](03_FOUNDRY.md) for more on working with AI services.

## Getting started with Azure

### 1. Create an Azure account

Sign up at [azure.microsoft.com/free](https://azure.microsoft.com/free/). If you have a school email address, the [Azure for Students](https://azure.microsoft.com/free/students/) plan gives you free credits and access to popular services without a credit card.

### 2. Install the Azure CLI

The Azure CLI (`az`) lets you manage resources from your terminal. Install it from [learn.microsoft.com/cli/azure/install-azure-cli](https://learn.microsoft.com/cli/azure/install-azure-cli), then sign in:

```bash
az login
```

### 3. Create a resource group

```bash
az group create --name my-festival-project --location eastus
```

This gives you a container for all the resources your project will use.

### 4. Deploy something

What you deploy depends on your project. A few starting points:

- **Static site →** [Azure Static Web Apps quickstart](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- **Web app →** [App Service quickstart](https://learn.microsoft.com/azure/app-service/quickstart-nodejs)
- **Serverless function →** [Azure Functions quickstart](https://learn.microsoft.com/azure/azure-functions/create-first-function-cli-node)

### Tips

- **Start small.** Use the free or lowest-cost tier for each service while you're experimenting. You can always scale up later.
- **Delete what you don't need.** Some resources cost money even when idle. Delete your resource group when you're done: `az group delete --name my-festival-project`.
- **Check your spending.** See [Managing Cost](02_MANAGING_COST.md) for how to set budgets and alerts so you don't run up an unexpected bill.

> **Sample project:** The [bg-dashboard](https://github.com/blbergo/icf-mentee-handbook-2026/tree/main/samples/bg-dashboard) sample in the upstream handbook repository is a full-stack application (React frontend + FastAPI backend) orchestrated with Docker Compose, built entirely by an AI coding agent. It demonstrates a multi-service architecture that's ready to be deployed to Azure using services like [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/) or [App Service](https://learn.microsoft.com/azure/app-service/). See the [session transcript](https://github.com/blbergo/icf-mentee-handbook-2026/blob/main/samples/bg-dashboard/copilot-session.md) to learn how it was created.

## Further reading

- [Azure fundamentals learning path](https://learn.microsoft.com/training/paths/az-900-describe-cloud-concepts/) — Microsoft's free, beginner-friendly introduction
- [Azure for Students FAQ](https://learn.microsoft.com/azure/education/hub/azure-dev-tools-teaching/program-faq)
- [Azure CLI documentation](https://learn.microsoft.com/cli/azure/)
