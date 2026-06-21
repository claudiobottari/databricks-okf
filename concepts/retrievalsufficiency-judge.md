---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 61900537b60770aed4a8e912bde1df8376a28262e47125c85bec133a54549947
  pageDirectory: concepts
  sources:
    - retrievalsufficiency-judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - retrievalsufficiency-judge
    - RetrievalSufficiency
    - Context Sufficiency
  citations:
    - file: retrievalsufficiency-judge-databricks-on-aws.md
title: RetrievalSufficiency Judge
description: An MLflow GenAI scorer that evaluates whether retrieved documents contain enough context to sufficiently answer a user query.
tags:
  - mlflow
  - evaluation
  - rag
  - judge
timestamp: "2026-06-19T20:15:10.966Z"
---

# RetrievalSufficiency Judge

**RetrievalSufficiency Judge** is a built-in scorer in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that evaluates whether the context retrieved by a [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) application contains enough information to answer a user’s query. It is designed to be used with `mlflow.genai.evaluate()`.

## Overview

The RetrievalSufficiency judge checks the retrieved documents for factual completeness relative to a given question. If the retrieved context is missing important facts, the judge will flag the response as insufficient. This is especially valuable for diagnosing retrieval quality in RAG pipelines where incomplete context may lead to hallucinated or incomplete answers. ^[retrievalsufficiency-judge-databricks-on-aws.md]

## Usage

To use the judge, import `RetrievalSufficiency` from `mlflow.genai.scorers` and pass an instance to the `scorers` parameter of `mlflow.genai.evaluate()`. The scorer is typically applied after a retriever function that is traced with `@mlflow.trace(span_type="RETRIEVER")` and a RAG application that generates a response. ^[retrievalsufficiency-judge-databricks-on-aws.md]

### Example

```python
from mlflow.genai.scorers import RetrievalSufficiency
from mlflow.entities import Document
from typing import List

# Define a retriever function with proper span type
@mlflow.trace(span_type="RETRIEVER")
def retrieve_docs(query: str) -> List[Document]:
    # Simulated retrieval
    if "capital of france" in query.lower():
        return [
            Document(
                id="doc_1",
                page_content="Paris is the capital of France.",
                metadata={"source": "geography.txt"}
            ),
            Document(
                id="doc_2",
                page_content="France is a country in Western Europe.",
                metadata={"source": "countries.txt"}
            )
        ]
    elif "mlflow components" in query.lower():
        # Incomplete retrieval
        return [
            Document(
                id="doc_3",
                page_content="MLflow has multiple components including Tracing and Evaluation.",
                metadata={"source": "mlflow_intro.txt"}
            )
        ]
    else:
        return [
            Document(
                id="doc_4",
                page_content="General information about data science.",
                metadata={"source": "ds_basics.txt"}
            )
        ]

# Define RAG app
@mlflow.trace
def rag_app(query: str):
    docs = retrieve_docs(query)
    context = "\n".join([doc.page_content for doc in docs])
    messages = [
        {"role": "system", "content": f"Answer based on this context: {context}"},
        {"role": "user", "content": query}
    ]
    response = client.chat.completions.create(
        model=model_name,
        messages=messages
    )
    return {"response": response.choices[0].message.content}

# Evaluation dataset with expected facts
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

# Run evaluation
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[
        RetrievalSufficiency(
            model="databricks:/databricks-gpt-oss-120b",  # Optional; defaults to custom Databricks model
        )
    ]
)
```

^[retrievalsufficiency-judge-databricks-on-aws.md]

### Parameters

- **`model`** (optional): A string specifying the LLM to use for judging context sufficiency. If not provided, it defaults to a custom Databricks model (`databricks:/databricks-gpt-oss-120b`). When using the default, no explicit API credentials are required as long as the experiment is running in a Databricks workspace with access to the endpoint. ^[retrievalsufficiency-judge-databricks-on-aws.md]

## Integration

The RetrievalSufficiency judge integrates seamlessly with [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) for RAG applications. It uses the `expectations` field in the evaluation dataset, where `expected_facts` provides the ground‑truth facts against which the retrieved context is compared. The judge runs after the predictor function and outputs a metric indicating whether the retrieval was sufficient. ^[retrievalsufficiency-judge-databricks-on-aws.md]

## Related Concepts

- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) – The overall architecture for combining retrieval and generation.
- [MLflow GenAI Scorers](/concepts/mlflow-genai-scorers.md) – The set of built‑in evaluators for generative AI workflows.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – Structure used to provide inputs and ground‑truth expectations.
- Tracing in MLflow – Used to instrument the retriever and RAG app for observability.

## Sources

- retrievalsufficiency-judge-databricks-on-aws.md

# Citations

1. [retrievalsufficiency-judge-databricks-on-aws.md](/references/retrievalsufficiency-judge-databricks-on-aws-ecbf8897.md)
