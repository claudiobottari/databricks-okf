---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fbfb8b6ac34d72571c3360e257ffdb7ac7b73eaa51eaec1757e51765df4a0675
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inference-tables
    - Inference Table
    - Inference table
    - inference table
    - Databricks Inference Table
    - Enable inference tables for AI agents
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
      start: 100
      end: 110
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
      start: 120
      end: 130
title: Inference Tables
description: A Databricks AI Gateway feature that automatically captures incoming requests and outgoing responses from model serving endpoints for logging and audit.
tags:
  - model-serving
  - logging
  - ai-gateway
timestamp: "2026-06-19T18:01:22.613Z"
---

```markdown
# Inference Tables

**Inference Tables** are a Databricks feature that automatically captures incoming requests and outgoing responses from model serving endpoints into Delta tables for auditability and analysis. ^[create-custom-model-serving-endpoints-databricks-on-aws.md#L100-L110]

## Overview

When enabled on a model serving endpoint, every prediction request and its corresponding response are automatically logged without requiring custom logging code. The data is stored in a Delta table, enabling downstream monitoring, debugging, and compliance workflows. ^[create-custom-model-serving-endpoints-databricks-on-aws.md#L100-L110]

## Enabling Inference Tables

Inference tables can be enabled during the endpoint creation process in the **Serving** UI. After configuring the endpoint's served entities and compute settings, a section appears where you can toggle inference tables on. ^[create-custom-model-serving-endpoints-databricks-on-aws.md#L100-L110]

## Feature Lookup DataFrame Logging

When inference tables are enabled on a serving endpoint, you can optionally log the [[FeatureLookup|feature lookup DataFrame]] to the inference table. This requires setting an environment variable on the served entity and using MLflow 2.14.0 or above. The feature lookup DataFrame contains the features retrieved from a [[feature store]] that were used during model inference. ^[create-custom-model-serving-endpoints-databricks-on-aws.md#L120-L130]

## Related Concepts

- [[Model Serving]] — The platform that hosts and serves models, with inference tables as a logging capability.
- [[Unity AI Gateway]] — The governance framework that can be configured alongside inference tables.
- [[Feature Store]] — Source of features that can be logged alongside predictions in inference tables.
- [[Production Quality Monitoring (MLflow GenAI)|Production Monitoring for GenAI]] — Monitoring workflows that can leverage inference table data.

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md
```

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md:100-110](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
2. [create-custom-model-serving-endpoints-databricks-on-aws.md:120-130](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
