---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b60f9f254512668717652d76fba252e9db61d623231aa44deca0797da5c667f6
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - load-test-cluster-configuration-on-databricks
    - LTCCOD
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Load Test Cluster Configuration on Databricks
description: "Recommended compute configuration for running Locust-based load tests: single-node cluster with Databricks Runtime 15.4 LTS ML and a CPU-optimized instance type with at least 32 cores."
tags:
  - infrastructure
  - databricks
  - cluster-configuration
timestamp: "2026-06-18T14:42:53.560Z"
---

# Load Test Cluster Configuration on Databricks

**Load Test Cluster Configuration on Databricks** refers to the recommended cluster setup for running Locust-based load tests against custom [Model Serving](/concepts/model-serving.md) endpoints. Proper cluster sizing and runtime selection are critical for generating sufficient client-side concurrency and obtaining accurate latency and throughput measurements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Requirements for the Load Test Cluster

The example **Locust load test** notebook provided by Databricks uses the following cluster configuration: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- **Single node cluster** – no worker nodes are required because Locust runs entirely on the driver.
- **Runtime** – 15.4 LTS ML runtime ([Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)).
- **Instance type** – CPU-optimized, with **at least 32 cores**. Instances with more cores can generate higher queries per second (RPS). ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

The required files (`input.json` and `fast-load-test.py`) and the notebook itself are tested against this configuration. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Locust and CPU Resource Considerations

Locust is an open-source load-testing framework used in the provided notebook. It relies on CPU resources to execute its tests. Depending on the payload, Locust can handle roughly **4000 requests per second per CPU core**. The notebook uses the `--processes -1` flag, which allows Locust to auto‑detect the number of CPU cores on the driver and fully utilize them. If Locust becomes CPU-bound, a warning message appears in the output. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

Because the load test runs on the cluster’s driver node, the chosen instance type directly determines the maximum achievable client‑side concurrency. A single‑node cluster with many CPU cores is therefore essential. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Cluster and Endpoint Interaction

The load test cluster must be able to authenticate with the serving endpoint. Authentication uses a Service Principal that has **Can Query** permission on the endpoint. The service principal’s client ID and client secret are stored in a [Databricks secret scope](/concepts/databricks-secret-scopes.md) and read by the notebook. No separate cluster credentials are needed; the notebook handles OAuth token generation. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

The endpoint under test should be configured with a **Small** CPU endpoint (minimum and maximum concurrency of 4), Route Optimization enabled, and **Scale to Zero** disabled. This setup keeps endpoint behavior predictable during the load test series. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Running the Load Test with the Recommended Cluster

After the cluster is created with the specifications above, the notebook performs:

1. A **30‑second warm‑up test** to confirm the endpoint is responding.
2. A **series of load tests** with varying client‑side concurrency, measuring latency percentiles.
3. A **recommendation** for endpoint sizing based on the latency requirements and desired RPS.
4. A **final verification test** against the resized endpoint. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

The cluster configuration (single‑node, 32+ CPU cores, 15.4 LTS ML runtime) remains unchanged throughout the entire process. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- [Endpoint Concurrency](/concepts/endpoint-sizing-and-concurrency-planning.md)
- Route Optimization
- Locust
- Service Principal
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
