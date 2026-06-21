---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3032cd15e46efcc06c58123d88844ff5a3183b2e6a1f005fcf5b4ae58a1a8066
  pageDirectory: concepts
  sources:
    - retrievalgroundedness-judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-decorator
    - MTD
  citations:
    - file: retrievalgroundedness-judge-databricks-on-aws.md
title: MLflow trace decorator
description: A decorator (@mlflow.trace) for instrumenting functions with span types (e.g., RETRIEVER) to enable observability and tracing in GenAI application evaluation.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T20:14:59.269Z"
---

# MLflow Trace Decorator

**`@mlflow.trace`** is a Python decorator provided by the MLflow library for instrumenting functions with [MLflow Tracing](/concepts/mlflow-tracing.md). It allows developers to mark specific function calls as spans in a trace, enabling detailed observability of complex workflows such as [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications. The decorator is commonly used in combination with MLflow’s evaluation infrastructure, such as [RetrievalGroundedness](/concepts/retrievalgroundedness-judge.md), to track retrieval and generation steps. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Usage

The decorator can be applied without arguments or with a `span_type` parameter to label the span’s role in the trace. In the following example, `retrieve_docs` is decorated with `@mlflow.trace(span_type="RETRIEVER")` to indicate that the function performs a document retrieval step, while `rag_app` is decorated with a plain `@mlflow.trace` to mark the overall application entry point: ^[retrievalgroundedness-judge-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RetrievalGroundedness
from mlflow.entities import Document
from typing import List

@mlflow.trace(span_type="RETRIEVER")
def retrieve_docs(query: str) -> List[Document]:
    # Simulated retrieval based on query
    if "mlflow" in query.lower():
        return [
            Document(
                id="doc_1",
                page_content="MLflow is the largest open source AI engineering platform "
                             "for agents, LLMs, and ML models.",
                metadata={"source": "mlflow_docs.txt"}
            ),
            Document(
                id="doc_2",
                page_content="MLflow provides tools for experiment tracking, "
                             "model packaging, and deployment.",
                metadata={"source": "mlflow_features.txt"}
            )
        ]
    else:
        return [
            Document(
                id="doc_3",
                page_content="Machine learning involves training models on data.",
                metadata={"source": "ml_basics.txt"}
            )
        ]

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
```

## Parameters

The decorator accepts the following optional argument:

- `span_type` – A string identifying the type of the span. For retrieval functions the recommended value is `"RETRIEVER"`. Other span types (e.g., `"LLM"`, `"TOOL"`) are also supported by the tracing framework. ^[retrievalgroundedness-judge-databricks-on-aws.md]

When called without arguments, the decorator creates a generic span with no explicit type annotation.

## Integration with Evaluation

The `@mlflow.trace` decorator is particularly useful when using [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) with judges such as `RetrievalGroundedness`. These judges rely on the trace hierarchy to isolate retrieval spans and compute metrics like groundedness. By decorating the retrieval function with `span_type="RETRIEVER"`, the evaluation pipeline can automatically locate and score the retrieved documents. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [RetrievalGroundedness judge](/concepts/retrievalgroundedness-judge.md)
- [MLflow GenAI Scorers](/concepts/mlflow-genai-scorers.md)
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)

## Sources

- retrievalgroundedness-judge-databricks-on-aws.md

# Citations

1. [retrievalgroundedness-judge-databricks-on-aws.md](/references/retrievalgroundedness-judge-databricks-on-aws-595883b7.md)
