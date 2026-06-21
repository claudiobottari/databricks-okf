---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b27cae24746eed87980a880fec12cff9fba6156e7974af1f698637124c49b9ee
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-based-evaluation-requirements
    - MTER
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: MLflow Trace-based Evaluation Requirements
description: The structural requirements that MLflow traces must meet for built-in judges to function, including specific span types (e.g., RETRIEVER) and root span input/output fields.
tags:
  - mlflow
  - tracing
  - llm-evaluation
timestamp: "2026-06-19T22:06:44.167Z"
---

---
title: MLflow Trace-based Evaluation Requirements
summary: Trace-level requirements that MLflow built-in LLM judges impose on the span structure of traces for evaluation.
sources:
  - answer-and-context-relevance-judges-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T18:42:00.000Z"
updatedAt: "2026-06-19T18:42:00.000Z"
tags:
  - mlflow
  - evaluation
  - tracing
  - llm-judges
aliases:
  - mlflow-trace-based-evaluation-requirements
  - mtevalreq
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Trace‑based Evaluation Requirements

**MLflow Trace‑based Evaluation Requirements** describe the specific structure and attributes that an [MLflow](/concepts/mlflow.md) Trace must satisfy in order to be evaluated by the built‑in [LLM Judges](/concepts/llm-judges.md) that ship with MLflow 3.4.0 and later. These requirements differ per judge and ensure that the judge can locate the relevant span data (inputs, outputs, retrieved documents) needed to compute relevance scores. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## RelevanceToQuery Judge

The `RelevanceToQuery` judge evaluates whether a model’s response directly addresses the user’s input. To use this judge, the MLflow Trace **must** have both `inputs` and `outputs` present on the **root span** of the trace. Neither deep child spans nor attribute naming variations are accepted; the root span is the only valid location. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

When invoking the judge directly (outside of `mlflow.genai.evaluate`), the user provides `inputs` and `outputs` as dictionary arguments to the scorer callable, so no trace is required in that mode. However, when the judge is used inside `mlflow.genai.evaluate()` with a `predict_fn`, that function must return a trace that satisfies the root‑span requirement. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

**Example direct invocation** (trace not required; inputs/outputs are passed manually):

```python
from mlflow.genai.scorers import RelevanceToQuery

assessment = RelevanceToQuery(name="my_relevance_to_query")(
    inputs={"question": "What is the capital of France?"},
    outputs="The capital of France is Paris.",
)
```

**Trace requirement summary:** `inputs` and `outputs` must be attributes on the Trace’s root span. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## RetrievalRelevance Judge

The `RetrievalRelevance` judge evaluates whether each document returned by the application’s retriever(s) is relevant to the input request. Its trace requirement is different: the MLflow Trace **must contain at least one span** whose `span_type` is set to `"RETRIEVER"`. The content of the documents returned by that span is used for the assessment. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

In a typical [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) application, the retriever function is decorated with `@mlflow.trace(span_type="RETRIEVER")`. The judge then reads the documents from that span’s output. Unlike `RelevanceToQuery`, this judge does not need inputs/outputs on the root span — it only needs a retriever span to exist. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

**Example RAG application with a retriever span:**

```python
@mlflow.trace(span_type="RETRIEVER")
def retrieve_docs(query: str) -> List[Document]:
    # simulated retrieval
    return [Document(...)]

@mlflow.trace
def rag_app(query: str):
    docs = retrieve_docs(query)
    return {"response": f"Found {len(docs)} relevant documents."}
```

**Trace requirement summary:** At least one span with `span_type == "RETRIEVER"` must exist in the trace. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Using the Judges with `mlflow.genai.evaluate`

When either judge is passed as a scorer to `mlflow.genai.evaluate()`, the same trace requirements apply to every trace produced by the `predict_fn`. The `predict_fn` must be decorated with `@mlflow.trace` (or otherwise create a trace) and must emit the required span structure. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

For `RelevanceToQuery`, the root span of the trace created by `predict_fn` must carry `inputs` and `outputs` attributes. For `RetrievalRelevance`, the trace must contain a span with `span_type="RETRIEVER"` (typically created by the retriever function called inside `predict_fn`). ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Related Concepts

- [RelevanceToQuery](/concepts/relevancetoquery.md) — Built‑in judge for response relevance.
- [RetrievalRelevance](/concepts/retrievalrelevance.md) — Built‑in judge for document relevance.
- Span — A unit of work in an MLflow Trace.
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — Framework that calls these judges.
- [RAG Application Evaluation](/concepts/genai-application-evaluation-lifecycle.md) — Common use case for the `RetrievalRelevance` judge.

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
