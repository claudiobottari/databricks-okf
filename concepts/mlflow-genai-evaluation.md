---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f4e5290ae6353bd9b019af7be6655dc000475a8aa7cd67676eaebf29c67ddf5
  pageDirectory: concepts
  sources:
    - retrievalgroundedness-judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluation
    - MGE
    - MLflow 3 GenAI Evaluation
    - MLflow GenAI Agent Evaluation
    - GenAI Evaluate
    - GenAI Evaluation
    - GenAI Evaluators
    - GenAI evaluation
    - MLflow Evaluation for GenAI|GenAI evaluation
    - MLflow GenAI Evaluate
    - MLflow genai evaluate
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
    - file: retrievalgroundedness-judge-databricks-on-aws.md
title: MLflow GenAI Evaluation
description: A framework within MLflow for evaluating generative AI applications, including built-in judges like RetrievalGroundedness for automated scoring of LLM outputs.
tags:
  - mlflow
  - evaluation
  - genai
timestamp: "2026-06-19T20:14:58.160Z"
---

Here is the wiki page for "MLflow GenAI Evaluation".

---

---
title: MLflow GenAI Evaluation
summary: Framework for evaluating generative AI applications using MLflow, including creating evaluation datasets, defining scorers, running evaluations, and iterating on prompts.
sources:
  - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  - retrievalgroundedness-judge-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:35:27.329Z"
updatedAt: "2026-06-18T14:14:57.449Z"
tags:
  - mlflow
  - genai
  - evaluation
aliases:
  - mlflow-genai-evaluation
  - MGE
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow GenAI Evaluation

**MLflow GenAI Evaluation** is the framework within [MLflow](/concepts/mlflow.md) for assessing the quality of outputs from generative AI applications. It provides a structured, repeatable process for measuring how well a model's responses meet defined criteria—such as correctness, safety, adherence to guidelines, and groundedness—and for comparing results across prompt iterations.

## Overview

Evaluating generative AI applications requires more than traditional accuracy metrics. Because model output is often open-ended and can vary in style, creativity, and appropriateness, MLflow GenAI Evaluation provides **scorers** (evaluation functions) that can be applied to a set of test inputs, producing detailed result tables and visual comparisons in the MLflow UI. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

The evaluation workflow typically follows these steps:

1.  Create or define your application (e.g., a prompt-completion function).
2.  Assemble an [Evaluation Dataset](/concepts/evaluation-dataset.md)—a list of input examples.
3.  Define evaluation criteria by selecting one or more [MLflow Scorers](/concepts/mlflow-scorers.md).
4.  Run `mlflow.genai.evaluate()` on the dataset.
5.  Review the results in the MLflow Experiment UI.
6.  Iterate on your prompt, re-run the evaluation, and compare results. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## The `evaluate()` Function

The central entry point is `mlflow.genai.evaluate()`. It accepts three primary arguments: ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

- **`data`** — A list of dictionaries or a DataFrame containing the input examples. Each entry typically includes an `"inputs"` key with a sub-dictionary of named parameters.
- **`predict_fn`** — A callable (function or method) that takes an input dictionary and returns a string output. This is the application being evaluated.
- **`scorers`** — A list of scorer objects defining the evaluation metrics.

```python
results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=generate_game,
    scorers=[scorers_list]
)
```

The function returns an `EvaluationResult` object, and the results are automatically logged to the active MLflow Experiment. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Evaluation Dataset

An evaluation dataset is a collection of input examples that the app will be tested against. A minimal dataset is a list of dictionaries, each containing an `"inputs"` key. The inputs are passed to the `predict_fn` as keyword arguments. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

```python
eval_data = [
    {"inputs": {"template": "Yesterday, ____ …"}},
    {"inputs": {"template": "I wanted to ____ …"}},
]
```

For RAG applications, the evaluation dataset contains queries, and the `predict_fn` typically connects to a retriever and LLM to produce responses. ^[retrievalgroundedness-judge-databricks-on-aws.md]

```python
eval_dataset = [
    {"inputs": {"query": "What is MLflow used for?"}},
    {"inputs": {"query": "What are the main features of MLflow?"}}
]
```

## Scorers

Scorers are the individual metrics applied to each model output. MLflow provides a set of predefined scorers and also supports creating custom [LLM-as-Judge](/concepts/llm-as-a-judge.md) evaluators using `make_judge()`. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Predefined Scorers

- **`Guidelines`** — Evaluates whether the output adheres to one or more natural-language rules (e.g., "must be funny", "must be appropriate for children"). Each guideline is given a unique name. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **`Safety`** — A built-in scorer that flags content for potential harm or policy violations. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **`Correctness`** — Evaluates how well an output matches an expected response. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **`RelevanceToQuery`** — Assesses whether the output is relevant to the input query. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **`RetrievalSufficiency`** — Evaluates whether the retrieved context contains enough information to answer the query.
- **`RetrievalGroundedness`** — Scores whether each claim in the model's output is supported by the retrieved documents. ^[retrievalgroundedness-judge-databricks-on-aws.md]

### RetrievalGroundedness Scorer

The `RetrievalGroundedness` scorer is specifically designed for [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications. It checks the model's output against the retrieved context to determine whether each factual claim is grounded in the source documents. ^[retrievalgroundedness-judge-databricks-on-aws.md]

To use it, the `predict_fn` must include a function decorated with `@mlflow.trace(span_type="RETRIEVER")` that returns a list of [MLflow Document](/concepts/mlflow-document-entity.md) objects. MLflow automatically extracts the retrieval context from these traces to evaluate groundedness. ^[retrievalgroundedness-judge-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RetrievalGroundedness

@mlflow.trace(span_type="RETRIEVER")
def retrieve_docs(query: str) -> List[Document]:
    # Return relevant documents
    ...

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[
        RetrievalGroundedness(
            model="databricks:/databricks-gpt-oss-120b"
        )
    ]
)
```

The scorer uses a judge model (optional, defaults to a custom Databricks model) to evaluate groundedness for each response. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Output and Iteration

The evaluation produces a table with one row per input example and one column per scorer. Each cell shows the score (e.g., `"PASS"` or `"FAIL"`) and, where applicable, a rationale provided by the judge model. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

After running multiple evaluations (e.g., with different prompts), you can open the [MLflow Experiment UI](/concepts/mlflow-experiment.md) and select two or more runs to compare. The UI highlights which outputs changed between iterations, making it easy to see whether a prompt revision improved or regressed on specific criteria. This supports an iterative workflow: revise a prompt, re-run evaluation on the same dataset, and compare the new run with the previous one. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Related Concepts

- [Evaluation Dataset](/concepts/evaluation-dataset.md) — The collection of test inputs used in evaluation.
- [MLflow Scorers](/concepts/mlflow-scorers.md) — Predefined and custom scoring metrics.
- [LLM-as-Judge](/concepts/llm-as-a-judge.md) — Using a language model as an evaluator.
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — Application architecture that requires groundedness evaluation.
- [MLflow Experiment UI](/concepts/mlflow-experiment.md) — The interface for comparing evaluation runs.

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
- retrievalgroundedness-judge-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
2. [retrievalgroundedness-judge-databricks-on-aws.md](/references/retrievalgroundedness-judge-databricks-on-aws-595883b7.md)
