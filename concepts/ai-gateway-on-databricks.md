---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9fb1f64d2afdea158f95d06b771e34fa9516ae02db761f9e1f81ac6db62315aa
  pageDirectory: concepts
  sources:
    - machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-gateway-on-databricks
    - AGOD
  citations:
    - file: machine-learning-on-databricks-databricks-on-aws.md
title: AI Gateway on Databricks
description: Databricks service to govern and monitor access to deployed models with usage tracking, payload logging, and security controls.
tags:
  - databricks
  - ai-gateway
  - governance
  - security
timestamp: "2026-06-19T19:21:10.109Z"
---

##AI Gateway on Databricks

**AI Gateway** is a managed service on Databricks that governs and monitors access to models served on the platform. It provides usage tracking, payload logging, and security controls to help organizations manage how machine learning models are consumed in production. ^[machine-learning-on-databricks-databricks-on-aws.md]

### Capabilities

The AI Gateway enables administrators to:

- **Track usage** – Monitor how often each model endpoint is called and by whom, enabling cost allocation and capacity planning.
- **Log payloads** – Capture request and response data for auditing, debugging, and compliance purposes.
- **Enforce security controls** – Apply authentication, authorization, and rate-limiting policies to model endpoints.

These features are designed to work with models served via [Model Serving](/concepts/model-serving.md), including both custom models and large language models deployed on Databricks. ^[machine-learning-on-databricks-databricks-on-aws.md]

### Integration with the Model Serving Stack

The AI Gateway is part of the broader model serving ecosystem on Databricks. It complements [Foundation Model APIs](/concepts/foundation-model-apis.md) (which provide access to state‑of‑the‑art open models hosted by Databricks) and [External Models](/concepts/external-models.md) (which allow integration of third‑party models hosted outside Databricks). By centralizing governance across these serving options, the AI Gateway provides a single control plane for security and observability. ^[machine-learning-on-databricks-databricks-on-aws.md]

### Related Concepts

- [Model Serving](/concepts/model-serving.md) – Deploy custom models and LLMs as scalable REST endpoints.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Query open models hosted by Databricks.
- [External Models](/concepts/external-models.md) – Integrate third‑party models with unified governance.
- [Unity Catalog](/concepts/unity-catalog.md) – Centralized governance for data, features, and models.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Experiment tracking that complements production monitoring.
- [Databricks Runtime for ML](/concepts/databricks-runtime-for-ml.md) – Pre‑configured clusters for model development.

### Sources

- machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [machine-learning-on-databricks-databricks-on-aws.md](/references/machine-learning-on-databricks-databricks-on-aws-34650b43.md)
