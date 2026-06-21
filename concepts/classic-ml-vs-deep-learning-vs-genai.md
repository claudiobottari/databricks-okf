---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c79a27f95ec107791cb3c060513b785dba523945da109de666d142d6ad742f9
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - classic-ml-vs-deep-learning-vs-genai
    - CMVDLVG
  citations:
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
title: Classic ML vs Deep Learning vs GenAI
description: The distinctions and overlaps between classic machine learning, deep learning, and generative AI paradigms, and the platform features that support all three.
tags:
  - machine-learning
  - deep-learning
  - genai
  - paradigms
timestamp: "2026-06-18T14:41:58.647Z"
---

# Classic ML vs Deep Learning vs GenAI

**Classic ML vs Deep Learning vs GenAI** describes the three main paradigms within machine learning and artificial intelligence, their technical distinctions, and how they are supported on a unified platform.

## Overview

The boundaries between machine learning (ML), deep learning (DL), and generative AI (GenAI) can be fuzzy, but each represents a distinct approach to building predictive or generative models from data. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Classic Machine Learning

Classic ML includes techniques like classification, regression, anomaly detection, forecasting, and recommendation. These methods typically rely on hand-engineered features and structured data, and they form the foundation of traditional data science and machine learning workflows. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Deep Learning

Deep learning is technically a type of machine learning that uses multi-layered neural networks to learn representations directly from data. It excels at tasks involving unstructured data such as images, audio, and text, and is the underlying technology powering many modern AI applications. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Generative AI (GenAI)

Generative AI is a subset of deep learning focused on creating new content — text, images, code, audio, or video — based on patterns learned from training data. GenAI models, such as large language models (LLMs), are capable of tasks like summarization, translation, question answering, and content generation. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Platform Support

Databricks provides unified infrastructure and tooling that supports all three paradigms across the full ML lifecycle: ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

| Capability | Classic ML | Deep Learning | GenAI |
|------------|-----------|---------------|-------|
| [Model Serving](/concepts/model-serving.md) | Real-time and batch inference | Real-time and batch inference | Real-time and batch inference for custom models |
| ai_query | SQL queries and batch inference | SQL queries and batch inference | SQL queries and batch inference |
| [AI Runtime](/concepts/ai-runtime.md) / [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) | Training and fine-tuning | Training and fine-tuning | Training and fine-tuning |
| [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) | Run and experiment tracking | Run and experiment tracking | Run and experiment tracking |
| Databricks AI Search | Unstructured data serving | Unstructured data serving | Unstructured data serving |

## The ML Lifecycle

All three paradigms follow the same general ML lifecycle stages: ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

1. **Scope the use case** — Define the prediction target, success metrics, and production requirements.
2. **Run exploratory data analysis (EDA)** — Understand data distributions, predictive signals, and data quality issues.
3. **Prepare data and features** — Managed within a [Feature Store](/concepts/feature-store.md).
4. **Train models and track experiments** — Log experiment metadata for analysis and deployment.
5. **Evaluate** — Assess model quality against held-out data and stakeholder criteria.
6. **Register, stage, and test** — Validate models before promoting to production.
7. **Deploy to production** — Real-time endpoints or batch inference jobs.
8. **Monitor and retrain** — Adapt models to changing data or user behavior.

## Key Distinctions

- **Feature engineering**: Classic ML typically requires manual feature engineering, while deep learning and GenAI learn representations automatically from raw data.
- **Data requirements**: Deep learning and GenAI generally require larger datasets than classic ML approaches.
- **Compute needs**: Deep learning and GenAI training often demand specialized hardware like GPUs, whereas many classic ML algorithms can run efficiently on CPUs.
- **Output type**: Classic ML and deep learning primarily produce predictions or classifications, while GenAI produces new content.

## Related Concepts

- Machine Learning Lifecycle
- [Model Serving](/concepts/model-serving.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md)
- GPU Scheduling
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)

## Sources

- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
