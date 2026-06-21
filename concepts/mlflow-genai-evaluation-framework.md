---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 426df6342a6dc9e46569a6bf2d0e3542e423008348335bbfbb903cf9e3da27e2
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
    - retrievalgroundedness-judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluation-framework
    - MGEF
    - MLflow Evaluation Framework
    - MLflow's evaluation framework
    - MLflow Evaluation Framework|evaluation framework
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
    - file: retrievalgroundedness-judge-databricks-on-aws.md
title: MLflow GenAI Evaluation Framework
description: A framework within MLflow for evaluating generative AI applications using structured datasets, custom scorers, and automated tracing.
tags:
  - mlflow
  - evaluation
  - genai
  - databricks
timestamp: "2026-06-19T21:53:41.372Z"
---

# MLflow GenAI Evaluation Framework

The **MLflow GenAI Evaluation Framework** provides a structured, systematic approach for assessing the quality of generative AI applications. It combines an evaluation dataset, a prediction function (the application under test), and one or more **scorers** (also called LLM judges) to produce per-example scores with rationales and aggregated metrics. The framework is orchestrated through the `mlflow.genai.evaluate()` function and includes a set of built-in judges for safety, correctness, guidelines compliance, and retrieval quality. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md] ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md] ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Overview

Evaluation is performed by calling `mlflow.genai.evaluate()` with three key components:

1. **`data`** – a list of examples, each containing `inputs` and optional `expectations` (ground truth, such as `expected_facts`).
2. **`predict_fn`** – a callable that generates outputs from inputs (optional; if omitted, pre-computed `outputs` in the data are used).
3. **`scorers`** – a list of judge instances that define the quality criteria.

The function returns an evaluation results object with aggregated metrics and per-example breakdowns, viewable in the MLflow Experiment UI. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md] ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Built-in Judges

### Guidelines Judge

The `Guidelines` scorer checks whether a response meets custom, user-defined rules. It is instantiated with a textual guideline and an optional name. Multiple guideline scorers can be combined in a single evaluation. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Guidelines

scorers = [
    Guidelines(
        guidelines="Response must be in the same language as the input",
        name="same_language",
    ),
    Guidelines(
        guidelines="Response must be funny or creative",
        name="funny"
    ),
]
```

### Safety Judge

The `Safety` judge evaluates text content for harmful, offensive, or inappropriate material. It returns a pass/fail assessment (`"yes"` or `"no"`) and a detailed rationale. It can be used directly on a single output or included as a scorer in `mlflow.genai.evaluate()`. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Safety

safety_judge = Safety()
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[safety_judge]
)
```

### Correctness Judge

The `Correctness` scorer evaluates whether generated outputs contain the expected facts specified in the evaluation data. It compares the output against the `expected_facts` field in the `expectations` of each example. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness

scorers = [
    Correctness(),  # Checks expected facts
]
```

### RetrievalGroundedness Judge

The `RetrievalGroundedness` judge assesses whether the generated response is grounded in the retrieved context documents. It is designed for RAG Evaluation and requires the prediction function to return a structure that includes retrieved documents. ^[retrievalgroundedness-judge-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RetrievalGroundedness

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[
        RetrievalGroundedness(
            model="databricks:/databricks-gpt-oss-120b"  # Optional
        )
    ]
)
```

The judge compares the response against the retrieved documents, returning a verdict and rationale for each example. The prediction function should return a dictionary with a `response` key, and the retrieval function should be decorated with `@mlflow.trace(span_type="RETRIEVER")` to provide the retrieved documents to the judge. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Custom Judges with `make_judge`

The framework provides `make_judge` for creating custom evaluation criteria with specific instructions and feedback types. This allows you to define domain-specific metrics tailored to your application. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
from typing import Literal
from mlflow.genai import make_judge

sentence_count_judge = make_judge(
    name="sentence_count_compliance",
    instructions="""Evaluate if this summary follows the 2-sentence requirement.
Summary: {{ outputs }}
Count the sentences carefully and determine if the summary has exactly 2 sentences.""",
    feedback_value_type=Literal["correct", "incorrect"],
)
```

## Using the Evaluation API

The `mlflow.genai.evaluate()` function orchestrates the entire evaluation workflow. In practice, it is used to run a set of scorers on an application, and the results are reviewed in the MLflow Experiment UI. Multiple evaluation runs can be compared to track improvements across prompt versions or model changes. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md] ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=my_app,
    scorers=scorers,
)
```

## Prerequisites

- MLflow 3.1.0 or higher.
- OpenAI API access or Databricks Model Serving.
- For Unity Catalog integration: `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` privileges on the [Catalog and Schema](/concepts/catalog-and-schema.md). ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md] ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Best Practices

- **Start simple**: Begin with basic prompts and iteratively improve based on evaluation results. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Use consistent datasets**: Evaluate all versions against the same data for fair comparison. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Track everything**: Log prompt versions, evaluation results, and deployment decisions. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Test edge cases**: Include challenging examples in your evaluation dataset. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Monitor production**: Continue evaluating prompts after deployment to catch degradation. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Document changes**: Use meaningful commit messages to track why changes were made. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- Use `expected_facts` in the evaluation data to provide ground truth for judges like `Correctness`. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- When using a custom `predict_fn` for RAG apps, ensure it returns a structure that judges can parse (e.g., a dictionary with a `response` key) and that retrieval functions are properly traced. ^[retrievalgroundedness-judge-databricks-on-aws.md]
- Iterate on prompts by re-running evaluations and comparing runs in the MLflow UI. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Related Concepts

- [LLM Judges](/concepts/llm-judges.md) – The concept of using a language model to evaluate outputs.
- RAG Evaluation – Assessing retrieval-augmented generation pipelines.
- [MLflow](/concepts/mlflow.md) – The open-source platform for ML lifecycle management.
- [Prompt Version Management](/concepts/prompt-version-management.md) – Tracking and comparing different prompt versions.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying judges for ongoing quality checks.

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
- evaluate-and-compare-prompt-versions-databricks-on-aws.md
- retrievalgroundedness-judge-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
2. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
3. [retrievalgroundedness-judge-databricks-on-aws.md](/references/retrievalgroundedness-judge-databricks-on-aws-595883b7.md)
