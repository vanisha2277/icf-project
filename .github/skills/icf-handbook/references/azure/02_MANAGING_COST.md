# Managing Cost

## Keeping your Azure spending under control

Cloud resources can cost money, and charges add up if you leave things running or pick a bigger tier than you need. The good news is Azure gives you tools to track spending and set limits so nothing catches you off guard.

## How Azure pricing works

Most Azure services charge based on what you use. The exact formula varies by service, but it usually comes down to a few factors:

| Factor | Example |
|---|---|
| **Time** | A VM running for 10 hours costs more than one running for 1 hour |
| **Tier / size** | A 4-CPU server costs more than a 1-CPU server |
| **Data transfer** | Sending data out of Azure (egress) can have a per-GB charge |
| **Requests** | Some services (like Functions) charge per invocation |
| **Storage** | Storing more data costs more |

> **Tip:** Many services have a **free tier** that covers small workloads at no cost. Check the [Azure free services page](https://azure.microsoft.com/pricing/free-services/) for what's included.

## Checking what you owe

### Azure portal

The quickest way to see your current charges is the [Cost Management + Billing](https://portal.azure.com/#view/Microsoft_Azure_CostManagement/Menu/~/overview) page in the Azure portal. It shows:

- Your current billing period charges
- A breakdown by service and resource group
- Spending trends over time

### Azure CLI

You can also check costs from the terminal:

```bash
az cost query --type ActualCost --timeframe MonthToDate
```

## Setting a budget

A **budget** tells Azure to warn you when your spending reaches a threshold. It does not automatically stop services — it just sends you a notification so you can act.

### In the portal

1. Go to **Cost Management + Billing** → **Budgets**
2. Click **Add**
3. Set a monthly amount (for example, $20)
4. Add alert thresholds — common choices are 50%, 80%, and 100% of the budget
5. Enter your email address to receive alerts

### With the CLI

```bash
az consumption budget create \
  --budget-name my-festival-budget \
  --amount 20 \
  --time-grain Monthly \
  --category Cost \
  --resource-group my-festival-project
```

> **Important:** Budgets send alerts but do not stop resources from running. If you hit your limit, you still need to manually scale down or delete resources.

## Avoiding surprise charges

### 1. Use free tiers

When creating a resource, look for the **Free** or **Basic** tier. For most festival projects these are more than enough.

| Service | Free tier notes |
|---|---|
| **App Service** | F1 tier — 1 GB RAM, 60 min/day of compute |
| **Azure Functions** | First 1 million executions per month are free |
| **Static Web Apps** | Free plan includes custom domains and SSL |
| **Cosmos DB** | 1000 RU/s and 25 GB storage free |
| **Azure SQL** | Free offer available for new databases |

### 2. Stop or delete idle resources

Resources you are not using can still generate charges. A few common culprits:

- **VMs left running** — stop them when you're not working: `az vm deallocate --name myvm --resource-group my-festival-project`
- **Forgotten databases** — delete test databases you no longer need
- **Storage accounts with old data** — delete blobs and containers you're done with

The simplest cleanup is deleting the entire resource group:

```bash
az group delete --name my-festival-project --yes --no-wait
```

This removes everything in the group. Only do this when you're sure you no longer need any of those resources.

### 3. Use the pricing calculator before you create

The [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/) lets you estimate costs before you deploy anything. Add the services you plan to use, adjust the settings, and see a monthly estimate.

### 4. Set up cost alerts early

Don't wait until the end of the month. Set up a budget (see above) as soon as you create your first resource. Even a simple $10 alert is better than nothing.

### 5. Check spending regularly

Make it a habit to glance at the Cost Management page every few days while your project is live. Catching a runaway resource early saves money.

## Azure for Students

If you signed up with [Azure for Students](https://azure.microsoft.com/free/students/), you receive a credit balance and access to certain services at no cost. A few things to know:

- Your credits have an **expiration date** — usually 12 months from activation
- Some services are free regardless of credits (see the [free services list](https://azure.microsoft.com/pricing/free-services/))
- Once credits run out, pay-as-you-go rates apply unless you've set up spending limits
- You can check your remaining balance in the [Education Hub](https://portal.azure.com/#view/Microsoft_Azure_Education/EducationMenuBlade/~/overview)

## Quick reference

| Task | How |
|---|---|
| Check current charges | Portal → Cost Management, or `az cost query` |
| Set a budget | Portal → Budgets → Add, or `az consumption budget create` |
| See free tier limits | [azure.microsoft.com/pricing/free-services](https://azure.microsoft.com/pricing/free-services/) |
| Estimate costs before deploying | [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/) |
| Stop a VM without deleting it | `az vm deallocate --name <vm> --resource-group <rg>` |
| Delete all resources in a group | `az group delete --name <rg>` |

## Further reading

- [Azure Cost Management documentation](https://learn.microsoft.com/azure/cost-management-billing/)
- [Azure free services](https://azure.microsoft.com/pricing/free-services/)
- [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)
- [Azure for Students FAQ](https://learn.microsoft.com/azure/education/hub/azure-dev-tools-teaching/program-faq)
