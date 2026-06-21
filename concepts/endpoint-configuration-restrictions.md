---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 12538fcf3baad88fdfb5aac8aeafa0a7e91856399a3de38b8c8081359e6a11ab
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-configuration-restrictions
    - ECR
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Endpoint Configuration Restrictions
description: "Constraints on endpoint configuration updates: external_model endpoints can only have one served entity, and the external_model type cannot be added or removed after creation."
tags:
  - model-serving
  - configuration
  - restrictions
timestamp: "2026-06-19T09:37:18.558Z"
---

# Endpoint Configuration Restrictions

**Endpoint Configuration Restrictions** refer to the constraints that apply when creating or updating model serving endpoints that use external models in Databricks Model Serving. These restrictions govern how served entities can be configured and modified over the lifecycle of an endpoint.

## Overview

When working with external model serving endpoints — endpoints that query foundation models hosted outside of Databricks, such as OpenAI's GPT-4 or Anthropic's Claude — specific configuration rules apply to the `served_entities` list and the `external_model` object within an endpoint's configuration. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Single Served Entity Restriction

When an `external_model` is present in an endpoint configuration, the `served_entities` list can only contain one served entity object. This means you cannot serve multiple external models from a single endpoint. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Immutability of External Model Status

Once an endpoint is created with an `external_model`, the following restrictions apply:

- **Cannot remove external model**: Existing endpoints with an `external_model` cannot be updated to no longer have an `external_model`. The external model configuration is effectively locked in for the lifetime of the endpoint. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]
- **Cannot add external model later**: If an endpoint is created without an `external_model`, you cannot update it to add an `external_model` at a later time. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Update Behavior

While a configuration update is in progress, the old configuration continues to serve prediction traffic. During an active update, another update cannot be made. In the Serving UI, you can cancel an in-progress configuration update by selecting **Cancel update** on the top right of the endpoint's details page. This cancellation functionality is only available in the Serving UI. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The Databricks platform for deploying and serving models
- [External Models](/concepts/external-models.md) — Foundation models hosted outside of Databricks
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Curated foundation model architectures with optimized inference
- Create Foundation Model Serving Endpoints — The process of creating endpoints
- Serving Endpoint Lifecycle — Managing endpoint configurations over time

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
