---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 99bbea68cda85ca91de786c2fec2e69c8fae90b8421fb4375daedfeb05c4771f
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cpu-resource-planning-for-locust-tests
    - CRPFLT
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: CPU Resource Planning for Locust Tests
description: Locust performance scales at approximately 4000 requests per second per CPU core, and the framework auto-detects available cores via the --processes -1 flag to maximize throughput.
tags:
  - locust
  - cpu
  - performance
  - load-testing
timestamp: "2026-06-19T17:50:34.699Z"
---

# CPU Resource Planning for Locust Tests

**CPU Resource Planning for Locust Tests** refers to the process of estimating and allocating sufficient CPU capacity on the test driver node to support the desired query throughput during load testing of [Model Serving Endpoints](/concepts/model-serving-endpoint.md) on Databricks. Proper CPU planning ensures that Locust itself does not become a bottleneck, allowing the test to accurately measure endpoint performance.

## Overview

Locust is an open-source framework for load testing that relies on CPU resources to generate and manage concurrent client connections. During a load test, Locust sends requests to the serving endpoint and measures latency and throughput. If the driver node lacks sufficient CPU cores, Locust becomes CPU-bound and cannot generate enough requests to saturate the endpoint, leading to misleading results. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## CPU Throughput Estimation

Locust can handle approximately **4,000 requests per second (RPS) per CPU core**, depending on the payload size and complexity. This estimate provides a baseline for calculating the number of CPU cores needed on the driver node to achieve a target RPS. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

For example, to generate 32,000 RPS, the driver node would need at least 8 CPU cores dedicated to Locust processes.

## Recommended Cluster Configuration

Databricks recommends the following cluster setup for running Locust load tests:

- **Single node cluster** — A single driver node is sufficient; no worker nodes are needed for the load generator itself. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- **15.4 LTS ML runtime** — The tested and supported runtime version. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- **CPU-optimized instance with at least 32 cores** — Instances with more cores can generate higher RPS. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Auto-Detection of CPU Cores

In the Locust load test notebook, the `--processes -1` flag is set to allow Locust to auto-detect the number of CPU cores on the driver and fully utilize them. This ensures that all available CPU resources are used for generating concurrent requests. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Monitoring for CPU Bottlenecks

During the test, monitor the Locust output for messages indicating that Locust is being bottlenecked by the CPU. If such a message appears, the driver node does not have enough CPU capacity to meet the desired concurrency, and the test results may not reflect the true endpoint performance. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Planning Workflow

1. **Determine target RPS** — Identify the desired requests per second for the load test.
2. **Calculate required CPU cores** — Divide target RPS by 4,000 to estimate the minimum number of cores needed.
3. **Select instance type** — Choose a CPU-optimized instance with at least the calculated number of cores (minimum 32 cores recommended).
4. **Configure Locust** — Use the `--processes -1` flag to enable automatic CPU utilization.
5. **Run and monitor** — Execute the test and watch for CPU bottleneck warnings in the output.

## Related Concepts

- [Locust Load Testing Framework](/concepts/locust-load-testing-framework.md) — The open-source tool used for endpoint performance evaluation.
- Model Serving Endpoint Sizing — Determining the endpoint concurrency needed to meet latency and RPS goals.
- [Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md) — General guidance on load testing methodology.
- [Route Optimization for Serving Endpoints](/concepts/route-optimization-for-serving-endpoints.md) — Feature that improves endpoint throughput and must be enabled for accurate testing.
- Service Principal Authentication — Required for generating OAuth tokens to query route-optimized endpoints.

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
