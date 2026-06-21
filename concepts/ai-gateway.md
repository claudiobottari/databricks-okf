---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c20a6c92d16848145d67d90f14eb298bcff1943d6f801ec7357d568b8bf387f5
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-gateway
    - API Gateway
    - NAT Gateway
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: AI Gateway
description: A feature for centrally managing permissions, usage limits, and monitoring quality across all model endpoints including externally hosted ones
tags:
  - governance
  - monitoring
  - security
timestamp: "2026-06-19T10:11:41.628Z"
---

# AI Gateway

**AI Gateway** is a centralized governance and monitoring layer within Databricks [Model Serving](/concepts/model-serving.md) that enables administrators to manage permissions, set usage limits, and monitor quality across all model endpoints — including those hosted externally — from a single interface. It is designed to help organizations democratize access to LLMs and other AI services while maintaining appropriate security and operational guardrails. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Capabilities

Through AI Gateway, teams can:

- **Manage permissions** – Control which users, service principals, or groups can query, deploy, or manage serving endpoints.
- **Track and set usage limits** – Monitor consumption of model endpoints and enforce quotas or budgets to prevent cost overruns.
- **Monitor quality of all model types** – Observe performance metrics, latency, error rates, and response quality across both Databricks-hosted and externally-hosted (e.g., OpenAI, Anthropic) models.

These capabilities are available directly within the Serving UI, providing a single pane of glass for all model governance activities. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Integration with Model Serving

AI Gateway is tightly integrated with [Model Serving](/concepts/model-serving.md) — the Databricks platform for deploying and querying AI models in real time and batch. Model Serving supports deployment of custom MLflow models, Databricks-hosted foundation models (e.g., Meta Llama, Mistral), and external models hosted by third-party providers. AI Gateway extends that infrastructure by adding governance controls that apply uniformly across all endpoint types. ^[deploy-models-using-model-serving-databricks-on-aws.md]

Because Model Serving automatically scales up or down to meet demand, AI Gateway’s usage limits help prevent unexpected scaling-driven costs while ensuring that legitimate workloads are not throttled unnecessarily. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Use Cases

- **Enterprise governance** – Centralized control of model access and spending across multiple teams and projects.
- **Cost management** – Setting per-endpoint or per-user consumption caps to keep AI spend within budget.
- **Quality assurance** – Continuously monitoring model performance and drift, with the ability to roll back or replace underperforming endpoints.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The underlying serving infrastructure that AI Gateway governs.
- Foundation Models — Pre-trained models (Databricks-hosted or external) that can be served and governed via AI Gateway.
- Custom Models — User-uploaded MLflow models that can be deployed and monitored.
- [External Models](/concepts/external-models.md) — Models hosted by third-party providers (e.g., OpenAI, Anthropic) that are accessed through Model Serving and governed by AI Gateway.
- [AI Playground](/concepts/ai-playground.md) — A chat-based environment for testing LLMs, complementary to AI Gateway’s monitoring capabilities.

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
