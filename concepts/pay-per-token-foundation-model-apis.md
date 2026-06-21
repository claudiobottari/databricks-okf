---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 628b5008e52c2530bc62ac839df53b5701436dda82302cf802a412c2d9404082
  pageDirectory: concepts
  sources:
    - databricks-foundation-model-apis-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pay-per-token-foundation-model-apis
    - PFMA
    - Pay-Per-Token Foundation Models
    - Pay-per-token foundation models
    - pay-per-token foundation models
  citations:
    - file: databricks-foundation-model-apis-databricks-on-aws.md
title: Pay-per-token Foundation Model APIs
description: Preconfigured endpoints for querying foundation models on a per-token pricing basis, recommended for getting started and low-throughput production workloads.
tags:
  - pricing
  - model-serving
  - serverless
timestamp: "2026-06-19T18:12:35.645Z"
---

# Pay-per-token Foundation Model APIs

**Pay-per-token Foundation Model APIs** is a consumption-based serving mode for Databricks [Foundation Model APIs](/concepts/foundation-model-apis.md) that provides preconfigured endpoints for accessing state-of-the-art open models without maintaining your own model deployment. The name refers to the billing model where you pay for each token processed rather than reserving dedicated compute capacity. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Overview

Pay-per-token is the easiest way to start using foundation models on Databricks. Databricks hosts the models and manages the serving infrastructure, so you can focus on building applications. This mode is recommended for beginning your journey with Foundation Model APIs. While it is not designed for high-throughput applications, it can still be used for production workloads. ^[databricks-foundation-model-apis-databricks-on-aws.md]

The APIs are compatible with the OpenAI client SDK, meaning you can use the standard OpenAI Python client or REST API to query Databricks-hosted models. Alternatively, you can use the Databricks UI, the Foundation Models APIs Python SDK, the MLflow Deployments SDK, or the REST API directly. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## How to Use

### Accessing Endpoints

Preconfigured pay-per-token endpoints appear automatically in your workspace. Navigate to the **Serving** tab in the left sidebar; the Foundation Model APIs are listed at the top of the Endpoints list view. ^[databricks-foundation-model-apis-databricks-on-aws.md]

### Requirements

- A Databricks API token for authentication.
- A workspace in one of the [supported pay-per-token regions](https://docs.databricks.com/aws/en/resources/feature-region-support#model-serving-aws). ^[databricks-foundation-model-apis-databricks-on-aws.md]

### Querying a Model

You can query a pay-per-token endpoint using any compatible client. For example, with the OpenAI Python client:

```python
import openai

client = openai.OpenAI(
    api_key="<databricks-token>",
    base_url="https://<workspace-url>/serving-endpoints"
)

response = client.chat.completions.create(
    model="databricks-meta-llama-3-1-70b-instruct",
    messages=[{"role": "user", "content": "Hello, how are you?"}]
)
```

See Use foundation models for detailed scoring examples. ^[databricks-foundation-model-apis-databricks-on-aws.md]

### Supported Models

A list of supported pay-per-token models is maintained in the Databricks documentation. These models are open models hosted by Databricks. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## When to Use

Pay-per-token is particularly useful for:

- **Quick proofs-of-concept** – verifying a project's validity before investing more resources.
- **Comparing models** – efficiently evaluating different open models to find the best candidate for your use case.
- **Low‑to‑medium‑traffic applications** – building LLM-powered applications that do not require extreme throughput guarantees.
- **Development and testing** – iterating on prompts and application logic before moving to provisioned throughput for production. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Comparison with Other Modes

| Mode | Billing | Use Case |
|------|---------|----------|
| **Pay-per-token** | Per token | Getting started, development, low‑throughput production |
| [Provisioned Throughput](/concepts/provisioned-throughput.md) | Reserved capacity | High‑throughput production, performance guarantees, HIPAA compliance, fine‑tuned models |
| [AI Functions](/concepts/ai-functions.md) | Batch per operation | Batch inference workloads using any generative AI or ML model |

Provisioned throughput is recommended for production workloads that require high throughput, fine-tuned models, or compliance certifications like HIPAA. AI Functions are recommended for batch inference. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Limitations

- Not designed for high-throughput applications, though it can still support production traffic.
- Subject to the same [Foundation Model APIs limits](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#fmapi-limits) (rate limits, concurrency, etc.) as documented by Databricks. ^[databricks-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [AI Functions](/concepts/ai-functions.md)
- [Model Serving](/concepts/model-serving.md)
- Use foundation models
- [OpenAI client compatibility](/concepts/openai-client-compatibility.md)

## Sources

- databricks-foundation-model-apis-databricks-on-aws.md

# Citations

1. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
