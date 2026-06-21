---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 54a93387eff453887d78fffaefd0ecfbdc25b81a5c297364d7c7a3052c3c8dbf
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idle-endpoint-warm-up-delay
    - IEWD
    - Idle Endpoint Warm-Up
    - Idle Endpoint Warm-up
    - Idle endpoint warm-up
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Idle Endpoint Warm-up Delay
description: Timeout risk when a model serving endpoint scaled to 0 receives a request and must warm up before serving.
tags:
  - model-serving
  - timeouts
  - scaling
  - cold-start
timestamp: "2026-06-19T14:56:00.943Z"
---

# Idle Endpoint Warm-up Delay

**Idle Endpoint Warm-up Delay** refers to the additional latency incurred when a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) that has been scaled to 0 receives its first request after a period of inactivity. During this warm‑up period, the endpoint must initialize its underlying resources, which can take long enough to trigger a Client-Side Timeout.

## Cause

Model Serving endpoints can be configured to scale to zero instances when idle, meaning no compute resources are allocated to serve requests. When a request arrives for such an endpoint, the serving infrastructure must provision a fresh instance and load the model before it can process the request. This cold‑start process introduces a warm‑up delay. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Impact on Pipelines

The warm‑up delay is a common source of timeouts in pipelines that chain multiple services. For example, a pipeline that calls a [Provisioned Throughput](/concepts/provisioned-throughput.md) endpoint or an AI Search index may fail if the request to the idle endpoint exceeds the client’s timeout window before the endpoint becomes ready. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Mitigation

- Increase the client‑side timeout (e.g., adjust `MLFLOW_HTTP_REQUEST_TIMEOUT` or the timeout of a third‑party client like the OpenAI SDK) to accommodate the warm‑up period.
- Consider disabling the scale‑to‑zero option for endpoints that serve latency‑sensitive or interactive workloads.
- Use [Provisioned Throughput](/concepts/provisioned-throughput.md) endpoints, which are always active and avoid cold‑start delays.

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- Client-Side Timeout
- [Server-Side Timeout](/concepts/server-side-timeout.md)
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- AI Search
- Scale to 0
- Debug Model Serving Timeouts

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
