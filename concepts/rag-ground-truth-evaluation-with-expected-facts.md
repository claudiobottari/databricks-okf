---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6fa01793c560e17adc9690d8443e1426d47057c1be18bdd86e89177afdba35dd
  pageDirectory: concepts
  sources:
    - retrievalsufficiency-judge-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - rag-ground-truth-evaluation-with-expected-facts
    - RGTEWEF
  citations:
    - file: retrievalsufficiency-judge-databricks-on-aws.md
title: RAG Ground Truth Evaluation with Expected Facts
description: A pattern for evaluating retrieval-augmented generation systems by providing expected_facts in the evaluation dataset to ground truth judge assessments.
tags:
  - rag
  - evaluation
  - ground-truth
  - mlflow
timestamp: "2026-06-19T20:15:07.316Z"
---

# RAG Ground Truth Evaluation with Expected Facts

**RAG Ground Truth Evaluation with Expected Facts** is a technique for evaluating [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) systems by comparing the system’s output against a predefined set of factual expectations. The evaluation uses the [RetrievalSufficiency Judge](/concepts/retrievalsufficiency-judge.md) to determine whether the retrieved context contains all the facts needed to answer a query, and then assesses the generated response for correctness and completeness relative to those facts. ^[retrievalsufficiency-judge-databricks-on-aws.md]

## Overview

In a RAG application, the system retrieves relevant documents from a knowledge base and then generates an answer using a large language model. Standard evaluation often measures overall accuracy or similarity, but it does not explicitly verify whether the supporting facts were present in the retrieved context. The expected-facts approach enriches the evaluation dataset with a list of ground-truth facts that the answer must cover. The `RetrievalSufficiency` scorer then checks whether the retrieved context includes each expected fact, providing a more targeted assessment of retrieval quality. ^[retrievalsufficiency-judge-databricks-on-aws.md]

## Setting Up the Evaluation Dataset

The evaluation dataset is a list of dictionaries, each containing:

- **`inputs`**: A dictionary with a `"query"` key representing the user question.
- **`expectations`**: A dictionary with an `"expected_facts"` key, which is a list of string facts that the answer should include.

*Example from the source:*

```python
eval_dataset = [
    {
        "inputs": {"query": "What is the capital of France?"},
        "expectations": {
            "expected_facts": ["Paris is the capital of France."]
        }
    },
    {
        "inputs": {"query": "What are all the MLflow components?"},
        "expectations": {
            "expected_facts": [
                "MLflow has main components",
                "Components include Tracing",
                "Components include Evaluation",
                "Components include Prompt Engineering",
                "Components include Model Registry"
            ]
        }
    }
]
```

^[retrievalsufficiency-judge-databricks-on-aws.md]

## Running the Evaluation

The RAG application is defined as a callable (e.g., a function decorated with `@mlflow.trace`) that retrieves documents and generates a response. The evaluation is performed using `mlflow.genai.evaluate()`, passing the dataset, the prediction function, and the `RetrievalSufficiency` scorer. The scorer optionally accepts a model reference (defaults to a custom Databricks model). ^[retrievalsufficiency-judge-databricks-on-aws.md]

*Example:*

```python
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[
        RetrievalSufficiency(
            model="databricks:/databricks-gpt-oss-120b",
        )
    ]
)
```

The scorer evaluates whether the retrieved context contains each expected fact, producing a score that indicates sufficiency of the retrieved documents for answering the query. ^[retrievalsufficiency-judge-databricks-on-aws.md]

## Benefits

- **Transparency**: Explicitly ties evaluation to specific factual requirements, making it easier to diagnose missing information.
- **Granularity**: Per-fact checking reveals exactly which pieces of information the retrieval failed to capture.
- **Automation**: Can be part of a continuous integration pipeline for RAG systems, catching regressions in retrieval quality.

## Related Concepts

- [RetrievalSufficiency Judge](/concepts/retrievalsufficiency-judge.md) – The specific scorer used for expected-facts evaluation.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The framework for running model evaluations in MLflow.
- Ground Truth – The set of correct outputs used as a reference in evaluation.
- RAG Evaluation – Broader category of metrics for retrieval-augmented generation.
- [Context Sufficiency](/concepts/retrievalsufficiency-judge.md) – The property that retrieved documents provide enough information to answer a query.

## Sources

- retrievalsufficiency-judge-databricks-on-aws.md

# Citations

1. [retrievalsufficiency-judge-databricks-on-aws.md](/references/retrievalsufficiency-judge-databricks-on-aws-ecbf8897.md)
