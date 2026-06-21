---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4a11d942b621f1c69c9f541b65a3dc48e1214b3c69a459ee0e20377ad0de9db
  pageDirectory: concepts
  sources:
    - feature-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inference-tables-for-feature-logging
    - ITFFL
    - inference-table-logging-for-feature-serving
    - ITLFFS
  citations:
    - file: feature-serving-endpoints-databricks-on-aws.md
title: Inference Tables for Feature Logging
description: A capability to log the augmented DataFrame containing looked-up feature values and function return values to an inference table for monitoring and debugging, available for endpoints created starting February 2025.
tags:
  - monitoring
  - observability
  - databricks
timestamp: "2026-06-19T10:30:18.875Z"
---

# Inference Tables for Feature Logging

**Inference Tables for Feature Logging** is a configuration option for Feature Serving endpoints that automatically logs the augmented DataFrame—containing looked-up feature values and function return values—to the endpoint's inference table. This capability enables detailed observability of the feature data used during inference requests. ^[feature-serving-endpoints-databricks-on-aws.md]

## Overview

For endpoints created starting February 2025, you can configure the model serving endpoint to log the augmented DataFrame produced during feature retrieval. The DataFrame includes:

- Pre-materialized feature values looked up from online feature stores.
- Return values of feature functions (including [FeatureFunction](/concepts/featurefunction.md) outputs).

This data is saved to the [inference table](/concepts/inference-tables.md) associated with the served model. ^[feature-serving-endpoints-databricks-on-aws.md]

## Configuration

To enable feature logging, the endpoint must be configured to store the augmented DataFrame in the inference table. For step-by-step instructions, see the Databricks documentation on [Log feature lookup DataFrames to inference tables](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving#features). Commercial information about inference tables is available in the guide [Monitor served models using Unity AI Gateway-enabled inference tables](https://docs.databricks.com/aws/en/ai-gateway/inference-tables). ^[feature-serving-endpoints-databricks-on-aws.md]

## Use Cases

- **Audit and debugging**: Review the exact feature values supplied to a model at inference time.
- **Model monitoring**: Correlate feature values with prediction outcomes in the inference table.
- **Compliance**: Maintain a record of feature data used for each request.

## Related Concepts

- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md)
- [Inference Tables](/concepts/inference-tables.md)
- [Unity AI Gateway](/concepts/unity-ai-gateway.md)
- [FeatureFunction](/concepts/featurefunction.md)
- [FeatureLookup](/concepts/featurelookup.md)

## Sources

- feature-serving-endpoints-databricks-on-aws.md

# Citations

1. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
