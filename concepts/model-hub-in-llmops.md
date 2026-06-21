---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c8e64f57c5056fdbc2cfd314497e9805ecda894d0f3ea575037e04c9f36c33d
  pageDirectory: concepts
  sources:
    - llmops-workflows-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-hub-in-llmops
    - MHIL
    - Model Hub
  citations:
    - file: llmops-workflows-on-databricks-databricks-on-aws.md
title: Model Hub in LLMOps
description: Using internal or external model hubs to select pretrained foundation models for LLM applications, reducing time and cost of building custom models
tags:
  - model-hub
  - pretrained-models
  - llmops
timestamp: "2026-06-19T19:12:51.164Z"
---

### Model Hub in LLMOps

The **Model Hub** in LLMOps refers to a centralized repository of pre‑trained foundation models that LLM applications can consume directly or customize through fine‑tuning. It serves as a key architectural component that reduces the cost and time required to build LLM‑based applications from scratch. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

#### Role of the Model Hub

LLM applications frequently rely on existing, pre‑trained models selected from an internal or external model hub. These models can be used as‑is — for example, via a hosted API — or adapted for a specific domain through fine‑tuning. The model hub acts as both a discovery and consumption interface, enabling teams to reuse state‑of‑the‑art model weights without building custom models. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

#### Databricks Model Hub

Databricks provides a built‑in model hub that includes a selection of high‑quality, pre‑trained foundation models. These models are available in two places:

- **Unity Catalog** – Models are registered in a governed catalog alongside other data assets, enabling discovery, access control, and lineage tracking.
- **Databricks Marketplace** – A broader marketplace where third‑party providers publish pre‑trained models that can be imported into a workspace.

By using these pre‑trained models, teams can quickly access advanced AI capabilities, saving the time and expense of training large models from scratch. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

#### Using Models from the Hub

Once a model is selected from the hub, it can be:

- **Consumed directly** – through Databricks [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) endpoints, either as an [External Model](/concepts/external-models.md) (connecting to third‑party APIs) or as a self‑hosted deployment.
- **Fine‑tuned** – using Databricks Foundation Model Fine‑tuning, which customizes the model with application‑specific data while retaining the pre‑trained knowledge.
- **Integrated into a Vector Index** or AI Search pipeline for [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md).

The hub therefore supports both zero‑shot usage and adaptation workflows, making it a flexible starting point for any LLMOps pipeline. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

#### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – Governed metadata and asset management for models and data.
- Databricks Marketplace – External marketplace for pre‑trained models.
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md) – Process of adapting a hub model to a specific task.
- [Model Serving](/concepts/model-serving.md) – Deployment and query interface for models.
- [External Model](/concepts/external-models.md) – Integration of third‑party LLM APIs via Model Serving.
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) – Architecture that combines retrieval from a vector index with LLM generation.
- [LLMOps](/concepts/large-language-models-llms-on-databricks.md) – Operational practices for LLM applications.

#### Sources

- llmops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [llmops-workflows-on-databricks-databricks-on-aws.md](/references/llmops-workflows-on-databricks-databricks-on-aws-6b1b2e6a.md)
