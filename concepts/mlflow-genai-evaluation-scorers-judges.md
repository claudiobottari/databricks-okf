---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21ec9264e89d0c7ef88d9fec27ab9d7d8b969e66c4208880ee529a625f6c529c
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluation-scorers-judges
    - MGES(
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: MLflow GenAI Evaluation Scorers (Judges)
description: A framework within MLflow for using LLM-based judges (scorers) to programmatically evaluate the quality of GenAI application outputs, including relevance, groundedness, safety, and correctness.
tags:
  - mlflow
  - llm-evaluation
  - genai
timestamp: "2026-06-19T22:06:35.183Z"
---

# MLflow GenAI Evaluation Scorers (Judges)

MLflow provides built-in LLM judges that evaluate the quality of GenAI applications. These judges assess aspects such as relevance, groundedness, safety, and correctness. This page covers the two built-in relevance judges: `RelevanceToQuery` and `RetrievalRelevance`. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Prerequisites

To use the built-in judges, install MLflow and required packages:

```python
%pip install --upgrade "mlflow[databricks]>=3.4.0" openai "databricks-connect>=16.1"
dbutils.library.restartPython()
```

Then create an MLflow experiment by following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment). ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Built-in Relevance Judges

Two judges diagnose relevance issues in GenAI applications. If context is not relevant, the generation step cannot produce a helpful response. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

### `RelevanceToQuery`

Evaluates whether your app’s response directly addresses the user’s input without deviating into unrelated topics. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

**Trace requirements**: `inputs` and `outputs` must be on the Trace’s root span. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

**Usage** – invoke directly:

```python
import mlflow
from mlflow.genai.scorers import RelevanceToQuery

assessment = RelevanceToQuery(name="my_relevance_to_query")(
    inputs={"question": "What is the capital of France?"},
    outputs="The capital of France is Paris.",
)
print(assessment)
```

**Usage** – invoke with `mlflow.genai.evaluate()`: pass the scorer to the `scorers` argument. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

### `RetrievalRelevance`

Evaluates whether each document returned by your app’s retriever(s) is relevant to the input request. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

**Trace requirements**: The MLflow Trace must contain at least one span with `span_type` set to `RETRIEVER`. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

**Usage** – invoke directly on a trace:

```python
from mlflow.genai.scorers import retrieval_relevance
import mlflow

trace = mlflow.get_trace("<your-trace-id>")
feedbacks = retrieval_relevance(trace=trace)
print(feedbacks)
```

**Usage** – invoke with `mlflow.genai.evaluate()` (see RAG example below). ^[answer-and-context-relevance-judges-databricks-on-aws.md]

#### RAG Example

The following complete example demonstrates a RAG application with a retriever and evaluation using `RetrievalRelevance`:

```python
import mlflow
from mlflow.genai.scorers import RetrievalRelevance
from mlflow.entities import Document
from typing import List

@mlflow.trace(span_type="RETRIEVER")
def retrieve_docs(query: str) -> List[Document]:
    if "capital" in query.lower() and "france" in query.lower():
        return [
            Document(id="doc_1", page_content="Paris is the capital of France.", metadata={"source": "geography.txt"}),
            Document(id="doc_2", page_content="The Eiffel Tower is located in Paris.", metadata={"source": "landmarks.txt"})
        ]
    else:
        return [Document(id="doc_3", page_content="Python is a programming language.", metadata={"source": "tech.txt"})]

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
    scorers=[
        RetrievalRelevance(
            model="databricks:/databricks-gpt-oss-120b"  # Optional; defaults to custom Databricks model
        )
    ]
)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Select the LLM that Powers the Judge

By default, built-in judges use a Databricks-hosted LLM designed for GenAI quality assessments. To change the judge model, use the `model` argument when creating the judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the provider, the model name is the same as the serving endpoint name. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RelevanceToQuery, RetrievalRelevance

relevance_judge = RelevanceToQuery(model="databricks:/databricks-gpt-5-mini")
retrieval_judge = RetrievalRelevance(model="databricks:/databricks-claude-opus-4-5")

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[relevance_judge, retrieval_judge]
)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Interpret Results

Each judge returns a `Feedback` object with:

- **`value`**: `"yes"` if context is relevant, `"no"` if not.
- **`rationale`**: Explanation of why the judge found the context relevant or irrelevant.

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Next Steps

- Explore other [Built-in Judges](/concepts/built-in-judges.md) – groundedness, safety, and correctness judges.
- Create [Custom Judges](/concepts/custom-judges.md) for specialized use cases.
- Apply relevance judges in comprehensive [RAG evaluation](/concepts/evaluation-run.md) workflows.

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Related Concepts

- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md)
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md)
- [GenAI application monitoring](/concepts/mlflow-genai-production-monitoring.md)
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- [Trace Spans](/concepts/trace-spans.md)

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
