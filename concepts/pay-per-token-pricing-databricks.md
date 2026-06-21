---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 436a031b54766eff3351637e476990694f9fb87e2aa94055541fedb48d28e1b9
  pageDirectory: concepts
  sources:
    - create-foundation-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pay-per-token-pricing-databricks
    - PP(
    - Token Pricing and Billing
  citations:
    - file: create-foundation-model-serving-endpoints-databricks-on-aws.md
title: Pay-per-Token Pricing (Databricks)
description: A consumption-based pricing model for base foundation models available for immediate use without performance guarantees.
tags:
  - databricks
  - pricing
  - pay-per-token
timestamp: "2026-06-18T11:23:24.171Z"
---

# Pay-per-Token Pricing (Databricks)

**Pay-per-Token Pricing** is a consumption-based pricing model for [Foundation Model APIs](/concepts/foundation-model-apis.md) in Databricks Model Serving. Under this model, users are charged based on the number of tokens processed by the model during inference, with no upfront commitment or reserved capacity. It is designed for ad‑hoc experimentation, prototyping, and low‑volume workloads. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Overview

Databricks provides a curated set of state‑of‑the‑art open foundation models — such as Meta‑Llama‑3.3‑70B‑Instruct and GTE‑Large — that are available for immediate use through Foundation Model APIs. These base models are offered with **pay-per-token** pricing, meaning you pay only for the tokens you consume. Databricks automatically creates serving endpoints for these models in your workspace; you do not need to manually provision an endpoint. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Usage

Endpoints backed by pay‑per‑token pricing appear automatically in the **Serving** tab of the workspace under the Foundation Model APIs section. You can query them directly without creating a custom endpoint. For instructions on sending requests, see Use foundation models. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Comparison with Provisioned Throughput

| Feature | Pay‑per‑Token | Provisioned Throughput |
|---|---|---|
| Pricing model | Per‑token consumption | Reserved capacity (hourly/monthly) |
| Performance guarantees | Best‑effort | Guaranteed throughput and latency |
| Suitable for | Experimentation, low‑volume, prototyping | Production workloads, high‑volume, latency‑sensitive |
| Endpoint creation | Automatic (pre‑built by Databricks) | Manual (user creates via API or UI) |

Production workloads that require consistent performance can use **provisioned throughput**, which provides performance guarantees and supports both base and fine‑tuned variants of foundation models. ^[create-foundation-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service that exposes curated foundation models.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Reserved capacity pricing for production workloads.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The endpoints that serve foundation or custom models.
- [External Models](/concepts/external-models.md) — Foundation models hosted outside Databricks, governed centrally.
- Create foundation model serving endpoints — Guide for creating endpoints.

## Sources

- create-foundation-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-foundation-model-serving-endpoints-databricks-on-aws.md](/references/create-foundation-model-serving-endpoints-databricks-on-aws-4acdecfd.md)
