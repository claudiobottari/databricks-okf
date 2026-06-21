---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8539894a2f63acd4a293e3d709732dd55d7731e48c3851e644e4319babc174e9
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-llm-judges
    - MLJ
    - MLflow 3 LLM Judges
    - MLflow judge class
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: MLflow LLM Judges
description: Built-in LLM-powered evaluators that assess quality dimensions (relevance, groundedness, safety, correctness) of GenAI application outputs
tags:
  - llm-evaluation
  - mlflow
  - genai
timestamp: "2026-06-19T08:59:51.550Z"
---

# MLflow LLM Judges

**MLflow LLM Judges** are built-in evaluators that use a language model to assess the quality of GenAI applications. They help diagnose issues such as irrelevant responses or poor retrieval, enabling developers to systematically improve their systems. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Overview

MLflow provides LLM judges as part of its [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) framework. These judges return structured feedback — a verdict ("yes"/"no") and a rationale — for each assessment. Two built-in judges focus on relevance: `RelevanceToQuery` and `RetrievalRelevance`. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Built-in Judges

### `RelevanceToQuery`

The `RelevanceToQuery` judge evaluates whether the application’s response directly addresses the user’s input without deviating into unrelated topics. It requires that `inputs` and `outputs` are present on the trace’s root span. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

**Example (direct invocation):**

```python
from mlflow.genai.scorers import RelevanceToQuery

assessment = RelevanceToQuery(name="my_relevance_to_query")(
    inputs={"question": "What is the capital of France?"},
    outputs="The capital of France is Paris.",
)
print(assessment)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

### `RetrievalRelevance`

The `RetrievalRelevance` judge evaluates whether each document returned by the app’s retriever(s) is relevant to the input query. The MLflow trace must contain at least one span with `span_type` set to `RETRIEVER`. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

**Example (trace-based invocation):**

```python
from mlflow.genai.scorers import retrieval_relevance
import mlflow

trace = mlflow.get_trace("<your-trace-id>")
feedbacks = retrieval_relevance(trace=trace)
print(feedbacks)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Full RAG Evaluation Example

The following example creates a RAG application with a simulated retriever and evaluates it using `RetrievalRelevance` with `mlflow.genai.evaluate`:

```python
import mlflow
from mlflow.genai.scorers import RetrievalRelevance
from mlflow.entities import Document
from typing import List

@mlflow.trace(span_type="RETRIEVER")
def retrieve_docs(query: str) -> List[Document]:
    # Simulated retrieval
    if "capital" in query.lower() and "france" in query.lower():
        return [
            Document(id="doc_1", page_content="Paris is the capital of France.",
                     metadata={"source": "geography.txt"}),
            Document(id="doc_2", page_content="The Eiffel Tower is located in Paris.",
                     metadata={"source": "landmarks.txt"})
        ]
    else:
        return [
            Document(id="doc_3", page_content="Python is a programming language.",
                     metadata={"source": "tech.txt"})
        ]

@mlflow.trace
def rag_app(query: str):
    docs = retrieve_docs(query)
    return {"response": f"Found {len(docs)} relevant documents."}

eval_dataset = [
    {"inputs": {"query": "What is the capital of France?"}},
    {"inputs": {"query": "How do I use Python?"}}
]

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[RetrievalRelevance()]
)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Selecting the LLM that Powers the Judge

By default, built-in judges use a Databricks-hosted LLM designed for quality assessments. You can override this with any LiteLLM-compatible model using the `model` argument, specifying the format `<provider>:/<model-name>`. For example:

```python
relevance_judge = RelevanceToQuery(
    model="databricks:/databricks-gpt-5-mini"
)
retrieval_judge = RetrievalRelevance(
    model="databricks:/databricks-claude-opus-4-5"
)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Interpreting Results

Each judge returns a `Feedback` object containing:
- **`value`**: `"yes"` if the context or response is relevant, `"no"` otherwise.
- **`rationale`**: An explanation of why the judge reached that decision.

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Next Steps

Beyond these built-in relevance judges, MLflow supports other built-in judges for groundedness, safety, and correctness. You can also [create custom judges](/concepts/custom-judges.md) tailored to your specific use case. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Related Concepts

- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) – general framework for assessing GenAI applications.
- [RAG evaluation](/concepts/evaluation-run.md) – applying judges in retrieval-augmented generation pipelines.
- [Built-in Judgers](/concepts/built-in-judges.md) – other built-in judges for safety, groundedness, etc.
- [Custom Judges](/concepts/custom-judges.md) – building specialized evaluators with `make_judge`.
- GenAI Monitoring – deploying judges in production for continuous quality checks.

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
