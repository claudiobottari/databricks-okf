---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 931da66e2f48d72889ba1dc22629ef782541c9007dc97bf89c0312e47285d941
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-models-databricks
    - EM(
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: External Models (Databricks)
description: A Model Serving feature allowing centrally governed access to foundation models hosted outside Databricks, such as GPT-4 from OpenAI and Anthropic, streamlining multi-provider LLM management.
tags:
  - llm
  - external-models
  - governance
timestamp: "2026-06-19T15:10:33.643Z"
---

# External Models (Databricks)

**External Models** in Databricks are foundation models hosted outside of Databricks, such as OpenAI’s GPT‑4 or Anthropic’s Claude. They are accessible through [Model Serving](/concepts/model-serving.md) via external model endpoints, which enable organizations to centrally govern and manage the use of various LLM providers from a single platform. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Overview

External models belong to the category of foundation models supported by Model Serving. Unlike Databricks-hosted models (available through [Foundation Model APIs](/concepts/foundation-model-apis.md)), external models run on third‑party infrastructure. Databricks provides a unified interface to deploy, query, and govern these models alongside custom and hosted foundation models. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Centralized Governance

The endpoints that serve external models can be centrally governed from Databricks. This allows organizations to streamline the use and management of multiple LLM providers—such as OpenAI and Anthropic—within their workspace. Governance capabilities include controlling permissions, monitoring usage, and enforcing organizational policies through the Serving UI. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The platform that hosts and manages all model endpoints, including external models.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks‑hosted foundation models with pay‑per‑token or provisioned throughput.
- Custom Models — User‑defined MLflow models served via Model Serving.
- [AI Gateway](/concepts/ai-gateway.md) — Monitoring and governance layer for model serving endpoints.

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
