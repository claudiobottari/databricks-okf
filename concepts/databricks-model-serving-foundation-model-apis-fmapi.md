---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a2560d405061c0d649e2ace443293a15b000b853b1fe1480adfa52e16d94d3c
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-model-serving-foundation-model-apis-fmapi
    - DMSFMA(
    - Databricks-hosted foundation models available in Foundation Model APIs
    - Databricks‑hosted foundation models available in Foundation Model APIs
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: Databricks Model Serving Foundation Model APIs (FMAPI)
description: A Databricks model serving capability for foundation models that is explicitly incompatible with express deployments, which require custom models instead.
tags:
  - databricks
  - model-serving
  - foundation-models
  - llm
timestamp: "2026-06-19T10:28:04.142Z"
---

#Databricks Model Serving Foundation Model APIs (FMAPI)

**Foundation Model APIs (FMAPI)** is a deployment type for [Model Serving](/concepts/model-serving.md) endpoints on Databricks that is distinct from custom model deployments. FMAPI endpoints are not eligible for [express deployments](/concepts/express-deployments-databricks.md) (previously called serverless optimized deployments).^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Overview

Express deployments accelerate endpoint deployment time and preserve the serving environment from the training environment. However, this feature is available only for custom models. FMAPI endpoints are explicitly excluded from express deployment support: "The model must be a custom model (not FMAPI)".^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Limitations

- FMAPI models cannot use express deployments.
- All other requirements for express deployments (e.g., Unity Catalog registration, CPU serving, `mlflow>=3.1`, Serverless Notebook with environment version 3 or 4, max environment size 1 GB) are relevant only to custom models and do not apply to FMAPI endpoints.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model serving endpoints](/concepts/model-serving-endpoint.md)
- [Express deployments](/concepts/express-deployments-databricks.md)
- [Custom model serving](/concepts/custom-models-on-model-serving.md)
- [Serverless Notebooks](/concepts/serverless-notebook-environments.md)

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
