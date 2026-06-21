---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 115a2fc2544a94e8b66d2d15aa609a98aaf4455b0aaf32c625cfd6ede166505d
  pageDirectory: concepts
  sources:
    - feature-serving-endpoints-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inference-table-logging-for-feature-serving
    - ITLFFS
  citations:
    - file: feature-serving-endpoints-databricks-on-aws.md
title: Inference Table Logging for Feature Serving
description: The ability to log the augmented DataFrame (looked-up feature values and function results) to an inference table for monitoring and debugging, available for endpoints created starting February 2025.
tags:
  - monitoring
  - logging
  - inference-tables
timestamp: "2026-06-19T18:48:34.082Z"
---

# Inference Table Logging for Feature Serving

**Inference Table Logging for Feature Serving** is a configuration option that allows you to log the augmented DataFrame from a Feature Serving endpoint to an inference table. This provides a record of the looked-up feature values and function return values for each inference request.

## Overview

For Feature Serving endpoints created starting February 2025, you can configure the model serving endpoint to log the augmented DataFrame that contains the looked-up feature values and function return values. The DataFrame is saved to the inference table for the served model. ^[feature-serving-endpoints-databricks-on-aws.md]

This logging capability enables monitoring and auditing of feature values used during inference, supporting model observability and debugging workflows.

## Configuration

To enable inference table logging for feature lookup DataFrames, set the configuration on the model serving endpoint. For detailed instructions, see the documentation on Log feature lookup DataFrames to inference tables. ^[feature-serving-endpoints-databricks-on-aws.md]

For general information about inference tables, see Monitor served models using Unity AI Gateway-enabled inference tables. ^[feature-serving-endpoints-databricks-on-aws.md]

## Use Cases

- **Audit trail**: Record exactly which feature values were served for each inference request.
- **Debugging**: Investigate unexpected model behavior by examining the feature values used in past predictions.
- **Monitoring**: Track feature distribution changes over time by analyzing logged DataFrames.

## Related Concepts

- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) — The endpoints that serve features to models and applications.
- [FeatureSpec](/concepts/featurespec.md) — The user-defined set of features and functions that define an endpoint.
- [Inference Tables](/concepts/inference-tables.md) — Unity AI Gateway-enabled tables for monitoring served models.
- [Unity Catalog](/concepts/unity-catalog.md) — The catalog system that stores and manages FeatureSpecs.
- [Model Serving](/concepts/model-serving.md) — Infrastructure for serving machine learning models.
- [Online Feature Store](/concepts/online-feature-store.md) — Stores feature values for low-latency serving.

## Sources

- feature-serving-endpoints-databricks-on-aws.md

# Citations

1. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
