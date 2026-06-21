---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b351c97e304f3cfda11322855c7b36d4915935555f50ffb07fc436235445b09a
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-gateway-databricks
    - AG(
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: AI Gateway (Databricks)
description: Centralized governance layer for managing, monitoring, and setting usage limits on all model endpoints (including externally hosted ones) from the Serving UI.
tags:
  - governance
  - monitoring
  - ai-gateway
  - databricks
timestamp: "2026-06-19T18:29:52.313Z"
---

# AI Gateway (Databricks)

**AI Gateway** is a Databricks solution for governing, monitoring, and managing AI and machine learning models deployed through [Model Serving](/concepts/model-serving.md). It provides centralized oversight of model endpoints, including those hosted externally, enabling organizations to democratize access to large language models (LLMs) while maintaining appropriate guardrails. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Overview

AI Gateway serves as a unified governance layer for AI models served on Databricks. It allows administrators to manage permissions, track usage, set usage limits, and monitor the quality of all types of models from a single interface. This includes both Databricks-hosted models and externally hosted models accessed through [External Models](/concepts/external-models.md). ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Key Capabilities

### Centralized Management

AI Gateway provides a single UI to manage all model serving endpoints, regardless of whether they are hosted on Databricks or externally. This simplifies the process of experimenting with, customizing, and deploying models in production across various clouds and providers. ^[deploy-models-using-model-serving-databricks-on-aws.md]

### Governance and Access Control

Through AI Gateway, organizations can:
- Manage permissions on model endpoints
- Track and set usage limits for different users or groups
- Monitor model quality and performance
- Ensure appropriate guardrails are in place for SaaS and open LLM access ^[deploy-models-using-model-serving-databricks-on-aws.md]

### Monitoring and Observability

AI Gateway enables monitoring of model quality across all types of models. This includes tracking performance metrics, detecting anomalies, and ensuring models continue to meet quality standards in production. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Integration with Model Serving

AI Gateway is tightly integrated with [Model Serving](/concepts/model-serving.md), which provides the underlying infrastructure for deploying AI and ML models for real-time serving and batch inference. Model Serving offers a unified REST API and MLflow Deployment API for CRUD and querying tasks, while AI Gateway adds the governance and monitoring layer on top. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Use Cases

- **Democratizing LLM Access**: Organizations can provide controlled access to foundation models like Meta Llama, GPT-4, and others while maintaining governance over usage and costs.
- **Multi-Provider Management**: Centrally manage endpoints from multiple LLM providers (OpenAI, Anthropic, etc.) through a single interface.
- **Cost Control**: Set usage limits and track spending across different teams and projects.
- **Compliance and Security**: Ensure that model usage complies with organizational policies and regulatory requirements.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The underlying infrastructure for deploying models
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks-hosted foundation models available through Model Serving
- [External Models](/concepts/external-models.md) — Foundation models hosted outside of Databricks
- [AI Playground](/concepts/ai-playground.md) — Chat-like environment for testing and comparing LLMs
- [MLflow](/concepts/mlflow.md) — Machine learning lifecycle management platform
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance solution for managing models and data assets

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
