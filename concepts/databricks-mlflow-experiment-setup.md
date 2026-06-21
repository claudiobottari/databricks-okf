---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a865a15e06c2293221808f81cc99575c64dca2e1307728611341961b7fe96c2
  pageDirectory: concepts
  sources:
    - instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-mlflow-experiment-setup
    - DMES
    - Databricks MLflow Experiment
  citations:
    - file: instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Databricks MLflow Experiment Setup
description: "Required setup: install mlflow-tracing, create a GenAI Experiment in Databricks, configure authentication via environment variables, and initialize the SDK with a tracking URI and experiment ID."
tags:
  - configuration
  - databricks
  - setup
timestamp: "2026-06-19T19:11:00.525Z"
---

# Databricks MLflow Experiment Setup

Setting up an **MLflow Experiment** on Databricks provides a centralized location for organizing runs, logging parameters, metrics, and artifacts, and enabling tracing for GenAI applications. The setup process includes creating the experiment, configuring authentication, initializing the MLflow SDK, and optionally assigning a serverless budget policy for automated workloads.

## Creating an Experiment

1. Open your Databricks workspace.
2. In the left sidebar, under **AI/ML**, click **Experiments**.
3. At the top of the Experiments page, click **GenAI apps & agents** to create an experiment optimized for generative AI tracing and evaluation.
4. Note the experiment ID displayed next to the experiment name (e.g., by clicking the info icon). ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Configuring Authentication

MLflow requires authentication to communicate with the Databricks workspace. Provide a personal access token and workspace URL via environment variables or a `.env` file:

```bash
export DATABRICKS_TOKEN=<your-databricks-personal-access-token>
export DATABRICKS_HOST=https://<workspace-name>.cloud.databricks.com
```

To generate a token, navigate to your experiment, click the kebab menu (three dots) > **Log traces locally** > **Generate API Key**, then copy the generated code. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Initializing the SDK

In your application code, initialize the [MLflow Tracing](/concepts/mlflow-tracing.md) SDK with the experiment ID. This step is required before any tracing or logging calls.

**TypeScript/JavaScript example:**

```typescript
import * as mlflow from 'mlflow-tracing';

mlflow.init({
  trackingUri: 'databricks',
  experimentId: '<your-experiment-id>',
});
```

The SDK can be used for automatic tracing (e.g., with OpenAI) or manual tracing via the `trace`, `@trace`, or `withSpan` APIs. ^[instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md]

## Setting a Serverless Budget Policy (Optional)

If your experiment triggers serverless workloads—such as scheduled scorers, synthetic evaluation set generation, or agent evaluation—you may need to assign a serverless budget policy to avoid a **403 PERMISSION_DENIED** error.

### Why Set a Budget Policy?

By default, MLflow uses the workspace’s default serverless budget policy. If that default is disabled, MLflow cannot fall back to any policy, resulting in:

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

Assigning an explicit policy to the experiment overrides this behavior. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Setting via the UI

1. Open the MLflow experiment.
2. In the **Details** panel, set the **Budget policy** to a policy you have permission to use.

MLflow will then use that policy for every serverless workload it creates for the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Setting via the API

Use `mlflow.set_experiment_tag()` to attach the policy ID as a tag:

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

After the tag is set, subsequent calls that create serverless workloads (e.g., `Scorer.register()`) apply the specified policy. To find the policy ID, refer to the attribute usage with serverless usage policies documentation. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md, configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) – Organiztional unit for runs and evaluations.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – Controls spending for serverless workloads.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Observability for GenAI applications.
- 403 PERMISSION_DENIED Serverless Budget Policy Error – Common error and resolution.
- [Production Monitoring](/concepts/production-monitoring.md) – Scheduled scoring workflows affected by budget policy.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) – Automated evaluation workflow.

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
- instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md

# Citations

1. [instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws.md](/references/instrument-nodejs-applications-with-mlflow-tracing-databricks-on-aws-1c7052f5.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
