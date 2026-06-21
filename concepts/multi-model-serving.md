---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 219396c1334b5f3fa87899038511a0e9b1a22e757779e943f562969524c185aa
  pageDirectory: concepts
  sources:
    - model-serving-concepts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-model-serving
    - Multi-Node Serving
  citations:
    - file: model-serving-concepts-databricks-on-aws.md
title: Multi-Model Serving
description: The ability to serve multiple models (e.g., different sizes of Llama) within a single serving endpoint, each with its own configuration.
tags:
  - databricks
  - model-serving
  - multi-model
timestamp: "2026-06-19T19:43:42.154Z"
---

Here is the wiki page for "Multi-Model Serving".

---

## Multi-Model Serving

**Multi-Model Serving** is a capability of Databricks Model Serving that allows a single serving endpoint to host multiple models simultaneously. Instead of deploying each model on its own separate endpoint, you can define multiple "served entities" within one endpoint configuration, each with its own name, entity version, and provisioned throughput settings. ^[model-serving-concepts-databricks-on-aws.md]

### Traffic Routing

A key feature of multi-model serving is the ability to configure a **traffic config** that defines how incoming requests are distributed among the models. Within the traffic configuration, you specify routes that map a served model name to a traffic percentage. The sum of all traffic percentages must equal 100%. ^[model-serving-concepts-databricks-on-aws.md]

For example, you could route 60% of traffic to an 8B parameter model and 40% of traffic to a 70B parameter model, allowing you to balance cost and quality based on your workload requirements. ^[model-serving-concepts-databricks-on-aws.md]

### Multi-Model Serving vs. Multi-Node Serving

Multi-Model Serving should not be confused with Multi-Node Serving or [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md). Multi-Model Serving refers to hosting multiple distinct models on a single endpoint, each handling a portion of traffic. Multi-Node Serving refers to distributing a single model across multiple compute nodes to meet latency or throughput requirements.

### Configuration Example

The following JSON shows a multi-model endpoint configuration with two served entities and a traffic config:

```json
POST /api/2.0/serving-endpoints
{
   "name": "multi-pt-model",
   "config": {
      "served_entities": [
         {
            "name": "meta_llama_v3_1_70b_instruct",
            "entity_name": "system.ai.meta_llama_v3_1_70b_instruct",
            "entity_version": "4",
            "min_provisioned_throughput": 0,
            "max_provisioned_throughput": 2400
         },
         {
            "name": "meta_llama_v3_1_8b_instruct",
            "entity_name": "system.ai.meta_llama_v3_1_8b_instruct",
            "entity_version": "4",
            "min_provisioned_throughput": 0,
            "max_provisioned_throughput": 1240
         }
      ],
      "traffic_config": {
         "routes": [
            {
               "served_model_name": "meta_llama_v3_1_8b_instruct",
               "traffic_percentage": "60"
            },
            {
               "served_model_name": "meta_llama_v3_1_70b_instruct",
               "traffic_percentage": "40"
            }
         ]
      }
   }
}
```

^[model-serving-concepts-databricks-on-aws.md]

### Related Concepts

- [Model Serving](/concepts/model-serving.md) — The core service for deploying machine learning models on Databricks.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Configuration for controlling the number of concurrent requests a served entity can handle.
- Serving Endpoint — The API endpoint that receives inference requests and routes them to the configured model(s).
- LLM Inference Optimization — Techniques for optimizing model inference at scale.
- Multi-Node Serving — Distributing a single model across multiple nodes for performance.

## Sources

- model-serving-concepts-databricks-on-aws.md

# Citations

1. [model-serving-concepts-databricks-on-aws.md](/references/model-serving-concepts-databricks-on-aws-b4c5ea15.md)
