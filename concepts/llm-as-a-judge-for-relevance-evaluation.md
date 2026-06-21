---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 80fc896d484aedab3285cf611cd2a660c88114c2e77107591c82583eab7e6897
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-as-a-judge-for-relevance-evaluation
    - LFRE
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: LLM-as-a-Judge for Relevance Evaluation
description: The paradigm of using a secondary LLM (judge model) to automatically assess the relevance of outputs or retrieved documents in GenAI applications, as implemented by MLflow's built-in scorers.
tags:
  - llm-evaluation
  - mlflow
  - genai
  - automated-testing
timestamp: "2026-06-18T10:46:14.891Z"
---

# LLM-as-a-Judge for Relevance Evaluation

**LLM-as-a-Judge for Relevance Evaluation** is a technique that uses large language models (LLMs) to automatically assess whether a system's response and retrieved context documents are relevant to the user's input. This approach helps diagnose quality issues in GenAI applications—if context isn't relevant, the generation step cannot produce a helpful response. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

MLflow provides two built-in LLM judges for relevance evaluation: `RelevanceToQuery` and `RetrievalRelevance`. These judges are part of the [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation framework and are designed to work with [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) workflows. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Prerequisites

To use the relevance judges, you need:

1. MLflow version 3.4.0 or later installed with the `databricks` extras:
   ```python
   %pip install --upgrade "mlflow[databricks]>=3.4.0" openai "databricks-connect>=16.1"
   dbutils.library.restartPython()
   ```
2. An MLflow experiment set up following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## `RelevanceToQuery` Judge

The `RelevanceToQuery` judge evaluates whether your app's response directly addresses the user's input without deviating into unrelated topics. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

**Requirements:** The `inputs` and `outputs` must be present on the Trace's root span. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Direct Invocation

```python
from mlflow.genai.scorers import RelevanceToQuery

assessment = RelevanceToQuery(name="my_relevance_to_query")(
    inputs={"question": "What is the capital of France?"},
    outputs="The capital of France is Paris.",
)
print(assessment)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Using with `mlflow.genai.evaluate`

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[RelevanceToQuery()]
)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## `RetrievalRelevance` Judge

The `RetrievalRelevance` judge evaluates whether each document returned by your app's retriever(s) is relevant to the input request. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

**Requirements:** The MLflow Trace must contain at least one span with `span_type` set to `RETRIEVER`. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Direct Invocation with a Trace

```python
from mlflow.genai.scorers import retrieval_relevance
import mlflow

trace = mlflow.get_trace("<your-trace-id>")
feedbacks = retrieval_relevance(trace=trace)
print(feedbacks)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

### RAG Evaluation Example

The following example shows how to create a [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) application with a retriever and evaluate it using the `RetrievalRelevance` judge: ^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers import RetrievalRelevance
from mlflow.entities import Document
from typing import List

# Define a retriever function with proper span type
@mlflow.trace(span_type="RETRIEVER")
def retrieve_docs(query: str) -> List[Document]:
    # Simulated retrieval - in practice, this would query a vector database
    if "capital" in query.lower() and "france" in query.lower():
        return [
            Document(
                id="doc_1",
                page_content="Paris is the capital of France.",
                metadata={"source": "geography.txt"}
            ),
            Document(
                id="doc_2",
                page_content="The Eiffel Tower is located in Paris.",
                metadata={"source": "landmarks.txt"}
            )
        ]
    else:
        return [
            Document(
                id="doc_3",
                page_content="Python is a programming language.",
                metadata={"source": "tech.txt"}
            )
        ]

# Define your app that uses the retriever
@mlflow.trace
def rag_app(query: str):
    docs = retrieve_docs(query)
    # In practice, you would pass these docs to an LLM
    return {"response": f"Found {len(docs)} relevant documents."}

# Create evaluation dataset
eval_dataset = [
    {"inputs": {"query": "What is the capital of France?"}},
    {"inputs": {"query": "How do I use Python?"}}
]

# Run evaluation with RetrievalRelevance scorer
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[
        RetrievalRelevance(
            model="databricks:/databricks-gpt-oss-120b",  # Optional
        )
    ]
)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Selecting the Judge Model

By default, built-in judges use a Databricks-hosted LLM designed to perform GenAI quality assessments. You can customize which LLM powers the judge using the `model` argument: ^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RelevanceToQuery, RetrievalRelevance

# Use different judge models
relevance_judge = RelevanceToQuery(
    model="databricks:/databricks-gpt-5-mini"
)
retrieval_judge = RetrievalRelevance(
    model="databricks:/databricks-claude-opus-4-5"
)

# Use in evaluation
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[relevance_judge, retrieval_judge]
)
```

The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the model provider, the model name is the same as the serving endpoint name. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Interpreting Results

The judge returns a `Feedback` object containing: ^[answer-and-context-relevance-judges-databricks-on-aws.md]

- **`value`**: "yes" if context is relevant, "no" if not
- **`rationale`**: Explanation of why the judge found the context relevant or irrelevant

## Related Concepts

- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) — The general methodology of using LLMs for automated evaluation
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The MLflow framework for evaluating GenAI applications
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — Pattern where retrieval relevance is critical
- Groundedness Evaluation — Evaluating whether responses are grounded in retrieved context
- [Safety Judges](/concepts/safety-judge-mlflow.md) — LLM judges that assess content safety
- [Custom Judges](/concepts/custom-judges.md) — Building specialized judges for specific use cases
- [[MLflow Trace|MLflow Traces]] — The tracing mechanism used to capture retrieval spans

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
