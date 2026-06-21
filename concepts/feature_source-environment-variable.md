---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c1c4638346740c6db91e9a4091a4a9c90b5603a1ec6e8041fc7ab9f1e377bcac
  pageDirectory: concepts
  sources:
    - migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature_source-environment-variable
    - FEV
  citations:
    - file: migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md
title: FEATURE_SOURCE Environment Variable
description: An environment variable set on serving endpoints to switch their feature data source from legacy online tables to the Databricks Online Feature Store.
tags:
  - serving
  - configuration
  - migration
timestamp: "2026-06-19T19:33:32.360Z"
---

# FEATURE_SOURCE Environment Variable

The **`FEATURE_SOURCE` environment variable** is a configuration key used during the migration from legacy [Online Tables](/concepts/online-tables.md) to an [Online Feature Store](/concepts/online-feature-store.md) on Databricks. It directs a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) to retrieve features from a specific online store rather than from legacy online tables. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Usage

After you have created an online feature store and published your feature tables to it, you must set the `FEATURE_SOURCE` environment variable to `DATABRICKS_ONLINE_STORE` on each served entity of the endpoint and then redeploy the endpoint. This switches the serving endpoint to use the new online store as the feature source for inference. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Configuration

You can set `FEATURE_SOURCE` in two ways:

- **UI**: In the serving endpoint page, go to **Advanced configuration > Environment variables** and add the variable with value `DATABRICKS_ONLINE_STORE`.
- **REST API**: Include the environment variable in the endpoint configuration when redeploying.

After applying the change, redeploy the endpoint for the setting to take effect. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Related Concepts

- [Online Feature Store](/concepts/online-feature-store.md)
- [Online Tables](/concepts/online-tables.md)
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md)

## Sources

- migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md

# Citations

1. [migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md](/references/migrate-from-legacy-and-third-party-online-tables-databricks-on-aws-4e5cf207.md)
