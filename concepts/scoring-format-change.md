---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6727754025632187da2293f2816ca2dddd693f49bd1a33cb225658cdc8a4ba05
  pageDirectory: concepts
  sources:
    - migrate-to-model-serving-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scoring-format-change
    - SFC
  citations:
    - file: migrate-to-model-serving-databricks-on-aws.md
title: Scoring Format Change
description: The difference in request/response format between Legacy MLflow Model Serving and new Model Serving, requiring application updates during migration.
tags:
  - api
  - scoring
  - model-serving
timestamp: "2026-06-19T19:36:11.179Z"
---

# Scoring Format Change

The **Scoring Format Change** refers to the differences in request and response formatting between the Legacy MLflow Model Serving experience and the current [Model Serving](/concepts/model-serving.md) experience on Databricks. When migrating from the legacy system to the new serverless-based Model Serving, applications must update their scoring requests to use the new format.

## Overview

When migrating from Legacy MLflow Model Serving to the current Model Serving, the format of API requests to the endpoint and the responses from the endpoint are slightly different. This requires updating any client applications that interact with the model serving endpoint. ^[migrate-to-model-serving-databricks-on-aws.md]

## Key Differences

The most notable change in the scoring format is the endpoint URL structure. In the current Model Serving, the endpoint URL includes `serving-endpoints` instead of `model` as used in the legacy system. This URL change, along with the altered request/response format, means applications must be updated to point to the new endpoint and send properly formatted requests. ^[migrate-to-model-serving-databricks-on-aws.md]

For detailed information on the new scoring protocol, including the exact request and response format, see [Scoring a model endpoint](/concepts/foundation-model-serving-endpoints.md). ^[migrate-to-model-serving-databricks-on-aws.md]

## Example Endpoint URLs

When querying a model after migration:

- **Legacy format:** `POST /model/<model-name>/invocations`
- **New format:** `POST /serving-endpoints/<endpoint-name>/invocations` ^[migrate-to-model-serving-databricks-on-aws.md]

This is demonstrated in the migration steps for deployed model versions, where staging and production endpoints are queried using the new format:

- For Staging endpoint: `POST /serving-endpoints/modelA-Staging/invocations`
- For Production endpoint: `POST /serving-endpoints/modelA-Production/invocations` ^[migrate-to-model-serving-databricks-on-aws.md]

## Migration Impact

When transitioning applications to the new Model Serving experience, you must:

1. Transition your application to use the new URL provided by the serving endpoint. ^[migrate-to-model-serving-databricks-on-aws.md]
1. Update your application to use the new scoring format protocol. ^[migrate-to-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The current production-ready serving experience
- [Legacy MLflow Model Serving](/concepts/legacy-mlflow-model-serving.md) — The deprecated serving experience
- Migrate to Model Serving — The overall migration process
- [Scoring a model endpoint](/concepts/foundation-model-serving-endpoints.md) — Detailed documentation on the new scoring format
- [Create custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md) — Guide for creating endpoints with the new experience

## Sources

- migrate-to-model-serving-databricks-on-aws.md

# Citations

1. [migrate-to-model-serving-databricks-on-aws.md](/references/migrate-to-model-serving-databricks-on-aws-7f642342.md)
