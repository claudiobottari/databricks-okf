---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee27833cf613b28575216919c9a4d9fee7a81fd2a7096afdcbeee73b785b6093
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iterative-scorer-development-workflow
    - ISDW
    - mlflow-trace-based-scorer-development-workflow
    - MTSDW
    - code-based scorer development workflow
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Iterative Scorer Development Workflow
description: "A four-step development process for building code-based scorers: define evaluation data, generate traces, store traces, and iterate on scorers using stored traces."
tags:
  - workflow
  - development
  - MLflow
  - evaluation
timestamp: "2026-06-19T18:31:14.050Z"
---

```yaml
---
title: Iterative Scorer Development Workflow
summary: A four-step developer workflow for rapidly iterating on code-based scorers without rerunning the full application: define evaluation data, generate traces, store traces, then evaluate new scorers against stored traces.
sources:
  - develop-code-based-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:14.817Z"
updatedAt: "2026-06-19T10:12:53.329Z"
tags:
  - mlflow
  - workflow
  - development
  - evaluation
aliases:
  - iterative-scorer-development-workflow
  - ISDW
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0
---

# Iterative Scorer Development Workflow

The **Iterative Scorer Development Workflow** is a methodology for developing and refining [[code-based scorers]] in MLflow Evaluation for GenAI. It allows you to update your scorer logic without re-running the full application each time, significantly accelerating the iteration cycle during development. ^[develop-code-based-scorers-databricks-on-aws.md]

The workflow consists of four steps:

1. Define evaluation data.
2. Generate traces from your application.
3. Query and store the resulting traces.
4. As you iterate on your scorer, evaluate using the stored traces.

By decoupling trace generation from scorer evaluation, you can rapidly test and modify your scoring logic against a fixed set of precomputed traces. ^[develop-code-based-scorers-databricks-on-aws.md]

## Prerequisites

Ensure you have a working MLflow setup and an instrumented application. The example below uses `mlflow.openai.autolog()` to automatically capture traces via [[MLflow Tracing]]. You must also have an evaluation dataset prepared. Update `mlflow[databricks]` to version 3.1 or later and install `openai`. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
%pip install -q --upgrade "mlflow[databricks]>=3.1" openai
dbutils.library.restartPython()
import mlflow
mlflow.openai.autolog()
```

## Step 1: Define Evaluation Data

Create a list of input dictionaries that represent the requests your application will process. Each entry typically contains an `"inputs"` key with the parameters expected by your app, such as a list of messages in a conversation. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
eval_dataset = [
    {
        "inputs": {
            "messages": [
                {"role": "user", "content": "How much does a microwave cost?"}
            ]
        }
    },
    {
        "inputs": {
            "messages": [
                {"role": "user", "content": "Can I return the microwave I bought 2 months ago?"}
            ]
        }
    },
]
```

## Step 2: Generate Traces from Your Application

Use `mlflow.genai.evaluate()` with a placeholder scorer to run your application against the evaluation dataset. Because `evaluate()` requires at least one scorer, define a placeholder metric that returns a constant value. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def placeholder_metric() -> int:
    return 1

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=sample_app,
    scorers=[placeholder_metric]
)
```

After this step, one trace exists per evaluation row in the experiment. The trace contains the full execution record, including the LLM response. ^[develop-code-based-scorers-databricks-on-aws.md]

## Step 3: Query and Store the Resulting Traces

Retrieve the generated traces as a Pandas DataFrame using `mlflow.search_traces()`, filtering by the evaluation run ID. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
generated_traces = mlflow.search_traces(run_id=eval_results.run_id)
```

This DataFrame can now be stored locally (e.g., as a variable) and reused for subsequent evaluation runs. ^[develop-code-based-scorers-databricks-on-aws.md]

## Step 4: Iterate on Your Scorer Using Stored Traces

Pass the stored DataFrame directly to `mlflow.genai.evaluate()` as the `data` parameter, omitting the `predict_fn` argument. The evaluation will run your scorer against the precomputed traces without re-invoking the application. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def response_length(outputs: str) -> int:
    return len(outputs)

mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[response_length],
)
```

You can now modify the scorer logic and repeat this step as many times as needed. Each run uses the same stored traces, so the evaluation is fast and deterministic. ^[develop-code-based-scorers-databricks-on-aws.md]

## Example Notebook

A complete example containing all code from this workflow is available as an example notebook in the source documentation. ^[develop-code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [[Code-based scorers]] — The programmable metrics you develop with this workflow.
- MLflow Evaluation for GenAI — The evaluation framework that powers trace-based scoring.
- [[MLflow Tracing]] — Automatic instrumentation that records application traces.
- [[Custom Judge Scorers|Custom LLM scorers]] — Semantic evaluation using LLM-as-a-judge, an alternative approach.
- [[Production Quality Monitoring (MLflow GenAI)|Production monitoring for GenAI]] — Deploying scorers for continuous monitoring after development.

## Sources

- develop-code-based-scorers-databricks-on-aws.md
```

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
