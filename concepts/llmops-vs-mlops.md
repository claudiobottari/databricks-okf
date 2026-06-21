---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b78a589203fe540dc66927456e0e1efad2a016d7c170993f54dd3c0f4240504e
  pageDirectory: concepts
  sources:
    - llmops-workflows-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llmops-vs-mlops
    - LVM
  citations:
    - file: llmops-workflows-on-databricks-databricks-on-aws.md
title: LLMOps vs MLOps
description: Key differences and commonalities between traditional MLOps and LLMOps workflows for large language models
tags:
  - llmops
  - mlops
  - workflow
timestamp: "2026-06-19T19:12:51.098Z"
---

# LLMOps vs MLOps

**LLMOps** (Large Language Model Operations) is the adaptation of traditional **MLOps** (Machine Learning Operations) to the specific workflow and infrastructure requirements of large language models. While fundamentally built on the same MLOps principles, LLMOps introduces several new components and process adjustments to handle the unique characteristics of LLMs, such as their large size, reliance on pretrained models, and the need for human feedback in evaluation. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Commonalities Between MLOps and LLMOps

Many core MLOps practices remain unchanged when applied to LLMs. The following guidelines apply equally to both MLOps and [LLMOps](/concepts/large-language-models-llms-on-databricks.md): ^[llmops-workflows-on-databricks-databricks-on-aws.md]

- **Environment separation**: Use separate environments for development, staging, and production. ^[llmops-workflows-on-databricks-databricks-on-aws.md]
- **Version control**: Use Git for version control. ^[llmops-workflows-on-databricks-databricks-on-aws.md]
- **Model lifecycle management**: Manage model development with [MLflow](/concepts/mlflow.md), and use [Models in Unity Catalog](/concepts/models-in-unity-catalog.md) to manage the model lifecycle. ^[llmops-workflows-on-databricks-databricks-on-aws.md]
- **Data storage**: Store data in a lakehouse architecture using Delta tables. ^[llmops-workflows-on-databricks-databricks-on-aws.md]
- **CI/CD infrastructure**: Existing CI/CD infrastructure does not require any changes. ^[llmops-workflows-on-databricks-databricks-on-aws.md]
- **Pipeline structure**: The modular structure of MLOps remains the same, with pipelines for featurization, model training, model inference, and so on. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Key Differences Introduced by LLMOps

The development and evaluation of LLMs differ in important ways from traditional ML models. The following subsections outline the major changes to the MLOps reference architecture when applied to LLM applications. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### Model Hub

Traditional MLOps typically involves training models from scratch using organization-specific data. In LLMOps, applications often use existing, pretrained models selected from an internal or external **model hub**. The model can be used as-is or fine-tuned. Databricks includes a selection of pre-trained foundation models in Unity Catalog and in Databricks Marketplace, allowing teams to access state-of-the-art AI capabilities without building custom models from scratch. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### Vector Index

Some LLM applications require fast similarity searches to provide context or domain knowledge in LLM queries — a need rarely present in traditional MLOps. LLMOps workflows may incorporate a **vector index** (e.g., Databricks AI Search) that uses any Delta table in Unity Catalog as an index and automatically syncs with the underlying table. This enables retrieval-augmented generation (RAG) patterns. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### Fine‑Tuning Instead of Training from Scratch

Because LLMs are expensive and time-consuming to create from scratch, LLMOps workflows emphasize **fine-tuning** an existing model to improve performance in a particular scenario, rather than training a new model. In the reference architecture, fine-tuning and model deployment are represented as distinct jobs. Validating a fine-tuned model before deployment is often a manual process. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### Model Serving Changes

In traditional MLOps, model serving typically loads a single model artifact and returns predictions. In LLMOps, especially in a RAG scenario using a third-party API, the LLM pipeline makes external API calls from the Model Serving endpoint to internal or third-party LLM APIs. This adds complexity, potential latency, and additional credential management. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

### Human Feedback in Monitoring and Evaluation

Human feedback loops are essential in most LLM applications but are less central in many traditional ML workflows. In LLMOps, human feedback should be managed like other data, ideally incorporated into monitoring based on near real-time streaming. Tools like the [MLflow Review App](/concepts/mlflow-review-app.md) help gather feedback from human reviewers. ^[llmops-workflows-on-databricks-databricks-on-aws.md]

## Summary Table

| Aspect | MLOps | LLMOps |
|--------|-------|--------|
| **Model origin** | Trained from scratch on proprietary data | Usually selected from a model hub (pretrained) and optionally fine-tuned |
| **Data retrieval** | Typically not required at inference time | Often uses vector indexes for similarity search (RAG) |
| **Training approach** | Full training pipeline | Fine-tuning of existing models |
| **Serving complexity** | Single model artifact served internally | May call external APIs, adding latency and credential management |
| **Human evaluation** | Often automated or minimal | Essential; requires structured human feedback loops |

## Related Concepts

- MLOps workflow on Databricks
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- [Foundation Model Fine-tuning](/concepts/foundation-model-fine-tuning-databricks.md)
- [Model Serving](/concepts/model-serving.md)
- AI Search (Databricks)
- [MLflow Review App](/concepts/mlflow-review-app.md)

## Sources

- llmops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [llmops-workflows-on-databricks-databricks-on-aws.md](/references/llmops-workflows-on-databricks-databricks-on-aws-6b1b2e6a.md)
