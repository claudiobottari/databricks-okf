---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8bc6f0d8eadd019cdd5e73020aca9626ac62d7d4063c012868c49d6e4cd83b04
  pageDirectory: concepts
  sources:
    - monitor-model-quality-and-endpoint-health-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-gateway-inference-tables
    - AGIT
    - AI Gateway-enabled inference tables
    - AI Gateway‑enabled inference tables
    - Git
  citations:
    - file: monitor-model-quality-and-endpoint-health-databricks-on-aws.md
title: AI Gateway Inference Tables
description: Automatically logs online prediction requests and responses into Unity Catalog Delta tables for monitoring, debugging, training data generation, and compliance audits.
tags:
  - logging
  - ai-gateway
  - audit
  - delta-table
timestamp: "2026-06-19T19:46:58.603Z"
---

# AI Gateway Inference Tables

**AI Gateway Inference Tables** are a monitoring feature that automatically logs online prediction requests and responses into [Delta tables](/concepts/delta-lake-table.md) managed by [Unity Catalog](/concepts/unity-catalog.md). This logging applies to model serving endpoints that deliver custom models, external models, or provisioned throughput workloads. The feature is part of the broader [AI Gateway](/concepts/ai-gateway.md) capabilities on Databricks. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Purpose

Inference tables serve multiple purposes: monitoring and debugging model quality or responses, generating training datasets from production data, and conducting compliance audits. By persisting both input and output payloads, they provide a record that can be queried for analysis or used to retrain models. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## How It Works

When enabled, AI Gateway automatically captures each online prediction request and its corresponding response, then writes that data into a Delta table within Unity Catalog. The table schema includes the request payload, response payload, and associated metadata such as timestamps and endpoint identifiers. This design enables long-term storage and SQL-based querying of inference logs without manual instrumentation. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Enabling Inference Tables

Inference tables can be enabled for both existing and new model serving endpoints when AI Gateway features are turned on. Configuration is available through the Serving UI or the REST API. Once enabled, logging begins automatically for all subsequent requests. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Use Cases

- **Model quality monitoring** – Compare actual responses against expected behavior over time.
- **Debugging production issues** – Inspect individual requests and responses to trace errors or unexpected outputs.
- **Training dataset generation** – Collect real-world prediction data to fine-tune or retrain models.
- **Compliance auditing** – Maintain an immutable log of all predictions for regulatory review.

## Related Concepts

- [AI Gateway](/concepts/ai-gateway.md) – The overarching feature set for managing and governing AI workloads.
- [Model Serving](/concepts/model-serving.md) – The infrastructure that hosts models and serves predictions.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages the Delta tables used for inference logging.
- [Delta tables](/concepts/delta-lake-table.md) – The storage format that holds the logged inference data.
- [Endpoint Health Metrics](/concepts/endpoint-health-metrics.md) – Another monitoring tool that provides infrastructure-level metrics for model serving endpoints.

## Sources

- monitor-model-quality-and-endpoint-health-databricks-on-aws.md

# Citations

1. [monitor-model-quality-and-endpoint-health-databricks-on-aws.md](/references/monitor-model-quality-and-endpoint-health-databricks-on-aws-9318b2eb.md)
