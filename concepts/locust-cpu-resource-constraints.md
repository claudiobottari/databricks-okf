---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2501e5d4ed0e351aef071e8efe6c5ea0de19ff05c8a7a69807e1476b431778a9
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - locust-cpu-resource-constraints
    - LCRC
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Locust CPU Resource Constraints
description: Understanding that Locust performance is CPU-bound (roughly 4000 requests per second per CPU core) and that auto-detection of CPU cores via the --processes -1 flag maximizes throughput
tags:
  - locust
  - performance
  - resource-management
timestamp: "2026-06-18T11:07:55.446Z"
---

---
title: Locust CPU Resource Constraints
summary: How CPU resources limit Locust load test throughput, including the 4000 RPS per core guideline and how to detect CPU bottlenecks.
sources:
  - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:00:00.000Z"
updatedAt: "2026-06-18T11:00:00.000Z"
tags:
  - locust
  - load-testing
  - cpu
  - performance
  - model-serving
aliases:
  - locust-cpu-resource-constraints
  - cpu-resource-constraints-locust
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 1
---

# Locust CPU Resource Constraints

**Locust CPU resource constraints** refer to the throughput limits that the CPU capacity of the test runner places on a [Locust](https://locust.io/) load test. Since Locust is CPU-bound, the number of requests per second (RPS) a single test instance can generate is proportional to the number of CPU cores available on the driver. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Throughput per CPU core

Locust relies on CPU resources to execute its test logic. As a rule of thumb, depending on the payload, Locust can sustain approximately **4000 requests per second per CPU core**. This means that on a single-core machine, a Locust instance might cap out at roughly 4000 RPS, while a 32-core machine could theoretically support up to 128,000 RPS, assuming no other bottlenecks. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

The notebook used in Databricks sets the `--processes -1` flag, which instructs Locust to auto-detect the number of CPU cores on the driver and fully utilize them. This flag allows the test to scale horizontally across all available cores. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Detecting CPU bottlenecks

During the test run, you should monitor the Locust output for a message indicating that Locust is being bottlenecked by the CPU. If such a message appears, the test is not generating enough load to saturate the serving endpoint because the Locust runner itself lacks sufficient CPU capacity. In that case, you need to either use a more powerful runner (e.g., a cluster with more CPU cores) or distribute the load across multiple Locust workers. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Recommended cluster configuration for Locust

For running the Databricks Locust load test notebook, the recommended cluster is a single-node cluster with the following characteristics:

- Databricks Runtime 15.4 LTS ML
- A CPU-optimized instance type
- At least 32 cores on the driver

Instances with more cores can generate higher RPS and are better suited for testing high-throughput serving endpoints. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Impact on test design

Because Locust’s throughput is limited by CPU, you must factor this into your test planning. If your serving endpoint is expected to handle tens of thousands of RPS, a single Locust instance might not be able to generate enough traffic. In such cases, you can:

- Use a larger instance (more cores) for the driver.
- Run Locust in distributed mode with multiple worker nodes, each contributing its CPU capacity.

The 30‑second warm‑up and test duration used in the notebook helps quickly verify whether the Locust runner is CPU‑bottlenecked before running longer, more detailed tests. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related concepts

- Locust — The open-source load testing framework used in these tests
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The Databricks endpoint being load tested
- [Load testing for serving endpoints](/concepts/load-testing-for-ml-serving-endpoints.md) — The broader process of evaluating endpoint performance
- [Endpoint concurrency and scale](/concepts/model-serving-endpoint-concurrency-scaling.md) — How the serving endpoint’s concurrency settings affect performance
- [Service principal setup for load testing](/concepts/service-principal-authentication-for-load-testing.md) — Authentication prerequisites for running Locust tests

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
