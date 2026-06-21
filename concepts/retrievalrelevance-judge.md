---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ce924db4317734737c3fd64a1ef1543452baef397ef77523293d13e138f25a0
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - retrievalrelevance-judge
    - Retrieval Relevance Judge
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: RetrievalRelevance Judge
description: An MLflow built-in LLM judge that evaluates whether each document returned by a retriever in a RAG application is relevant to the user's input request.
tags:
  - mlflow
  - llm-evaluation
  - rag
  - genai
timestamp: "2026-06-19T22:06:29.854Z"
---

# RetrievalRelevance Judge

**`RetrievalRelevance`** is a built-in MLflow LLM judge that evaluates whether each document returned by an application’s retriever is relevant to the user’s input query. It is primarily used for diagnosing quality issues in [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) pipelines — if the retrieved context is not relevant to the query, the generation step cannot produce a helpful response.^[answer-and-context-relevance-judges-databricks-on-aws.md]

Together with the [RelevanceToQuery Judge](/concepts/relevancetoquery-judge.md) (which evaluates whether the final response directly addresses the user’s input), `RetrievalRelevance` forms the relevance-assessment layer of MLflow’s GenAI evaluation toolkit.^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Prerequisites

1. Install MLflow and required packages:
   ```bash
   %pip install --upgrade "mlflow[databricks]>=3.4.0" openai "databricks-connect>=16.1"
   dbutils.library.restartPython()
   ```
   ^[answer-and-context-relevance-judges-databricks-on-aws.md]

2. Create an [MLflow Experiment](/concepts/mlflow-experiment.md) by following the [setup environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Trace Requirements

The [[MLflow Trace]] must contain at least one span whose `span_type` is set to `RETRIEVER`. This is typically done by decorating the retrieval function with `@mlflow.trace(span_type="RETRIEVER")`.^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Usage

### Direct Invocation

You can call the judge directly on an existing trace to assess whether each retrieved document is relevant:^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
from mlflow.genai.scorers import retrieval_relevance
import mlflow

trace = mlflow.get_trace("<your-trace-id>")
feedbacks = retrieval_relevance(trace=trace)
print(feedbacks)
```

### Evaluation with `mlflow.genai.evaluate`

You can also include `RetrievalRelevance` in a full evaluation run by passing it as a scorer:^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RetrievalRelevance

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[RetrievalRelevance()]
)
```

### Complete RAG Example

Here is a full example showing how to define a retriever, create a RAG application, and evaluate it:^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers import RetrievalRelevance
from mlflow.entities import Document
from typing import List

@mlflow.trace(span_type="RETRIEVER")
def retrieve_docs(query: str) -> List[Document]:
    if "capital" in query.lower() and "france" in query.lower():
        return [
            Document(id="doc_1", page_content="Paris is the capital of France.",
                     metadata={"source": "geography.txt"}),
            Document(id="doc_2", page_content="The Eiffel Tower is located in Paris.",
                     metadata={"source": "landmarks.txt"})
        ]
    else:
        return [Document(id="doc_3", page_content="Python is a programming language.",
                         metadata={"source": "tech.txt"})]

@mlflow.traced
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

## Selecting the Judge Model

By default, built-in judges use a Databricks-hosted LLM designed for GenAI quality assessments. You can change the judge model using the `model` argument when creating the judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the provider, the model name is the same as the serving endpoint name.^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RetrievalRelevance

retrieval_judge = RetrievalRelevance(
    model="databricks:/databricks-claude-opus-4-5"
)

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[retrieval_judge]
)
```

## Interpreting Results

The judge returns a `Feedback` object (or a list of feedback objects when called directly) with:^[answer-and-context-relevance-judges-databricks-on-aws.md]

- **`value`**: `"yes"` if the document is relevant to the input, `"no"` if not.
- **`rationale`**: A textual explanation of why the judge found the context relevant or irrelevant.

These results help identify which retrieved documents are contributing to poor response quality, enabling developers to refine their retrieval strategy.^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Related Concepts

- [RelevanceToQuery Judge](/concepts/relevancetoquery-judge.md) – Evaluates if the final response addresses the user's input.
- [MLflow](/concepts/mlflow.md) – The platform providing these judges.
- [[MLflow Trace]] – Required trace data structure containing [RETRIEVER Spans](/concepts/retriever-spans.md).
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) – The application pattern these judges evaluate.
- [LLM Judges](/concepts/llm-judges.md) – Overview of MLflow's built-in judges for GenAI evaluation.
- [Custom Judges](/concepts/custom-judges.md) – Building specialized judges for specific use cases.

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md
- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
