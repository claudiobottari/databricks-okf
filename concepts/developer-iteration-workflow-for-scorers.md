---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d3b6bc92defa80d8824ab75270fff0f620cde68f6b9c86e0229ceb0a479fdc4b
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - developer-iteration-workflow-for-scorers
    - DIWFS
    - Developer Workflow for Scorers
    - Developer workflow for code-based scorers
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Developer iteration workflow for scorers
description: A 4-step workflow to rapidly iterate on code-based scorers without rerunning the entire AI application by generating, storing, and reusing traces.
tags:
  - mlflow
  - workflow
  - development
  - evaluation
timestamp: "2026-06-19T15:11:18.387Z"
---

# Developer Iteration Workflow for Scorers

The **Developer Iteration Workflow for Scorers** is a recommended process for rapidly developing and refining custom code-based scorers in MLflow Evaluation for GenAI. The workflow avoids repeatedly running the entire application by separating trace generation from scoring, allowing developers to iterate on metric logic against a fixed set of recorded traces. ^[develop-code-based-scorers-databricks-on-aws.md]

## Workflow Steps

The workflow consists of four steps:

1. Define evaluation data
2. Generate traces from the application
3. Query and store the resulting traces
4. Iterate on the scorer by evaluating against the stored traces

^[develop-code-based-scorers-databricks-on-aws.md]

### Prerequisites: Set Up MLflow and Define the Application

Before starting, ensure you have the latest version of `mlflow[databricks]` installed (≥3.1) and any necessary client libraries (e.g., `openai`). Enable [MLflow Tracing](/concepts/mlflow-tracing.md) for automatic instrumentation of your application by calling `mlflow.openai.autolog()`. Define a sample application function (e.g., a question-answering assistant) that the workflow will trace. ^[develop-code-based-scorers-databricks-on-aws.md]

### Step 1: Define Evaluation Data

Create an evaluation dataset as a list of dictionaries. Each dictionary contains an `inputs` key whose value is the input to the application (for example, a list of message dictionaries in a chat format). The dataset will be passed to the evaluation function to generate traces. ^[develop-code-based-scorers-databricks-on-aws.md]

### Step 2: Generate Traces from the Application

Use `mlflow.genai.evaluate()` with a placeholder scorer and the defined evaluation data and prediction function. This call executes the application on each input row and records the resulting traces in the active MLflow experiment. The placeholder scorer is a minimal scorer (e.g., returning a constant value) required because `evaluate()` expects at least one scorer. ^[develop-code-based-scorers-databricks-on-aws.md]

After running, one trace exists per evaluation row. The trace visualizations appear in the Databricks notebook output and in the MLflow Experiment UI. The LLM’s generated response appears in the **Outputs** field of the Trace UI and in the **Response** column of the experiment UI. ^[develop-code-based-scorers-databricks-on-aws.md]

### Step 3: Query and Store the Resulting Traces

Use `mlflow.search_traces()` with the evaluation result’s `run_id` to retrieve the generated traces as a Pandas DataFrame. Store this DataFrame in a local variable. This DataFrame becomes the input for subsequent evaluation calls, eliminating the need to rerun the application. ^[develop-code-based-scorers-databricks-on-aws.md]

### Step 4: Iterate on the Scorer Using Stored Traces

Define or update a custom code-based scorer using the `@scorer` decorator (or the [Scorer class](/concepts/scorer-class.md)). Pass the stored trace DataFrame directly to `mlflow.genai.evaluate()` via the `data` parameter, and omit the `predict_fn` parameter. The evaluation runs the scorer against the pre‑computed traces, allowing rapid iteration on the metric logic without re‑executing the application. ^[develop-code-based-scorers-databricks-on-aws.md]

Example of a simple scorer that measures response length:

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

^[develop-code-based-scorers-databricks-on-aws.md]

## Example Notebook

The Databricks documentation provides an example notebook containing all code from the tutorial. It demonstrates the full workflow from setup through iteration. ^[develop-code-based-scorers-databricks-on-aws.md]

## Next Steps

After iterating on scorers, consider:

- Code-based scorer reference – Detailed reference for `@scorer` and `Scorer`, including signatures, inputs, outputs, metric naming, error handling, and accessing secrets.
- [Custom LLM scorers](/concepts/custom-judge-scorers.md) – Semantic evaluation using LLM-as-a-judge metrics, which can be simpler to define than code-based scorers.
- [Run scorers in production](/concepts/stateful-scorers-in-production.md) – Deploy scorers for continuous monitoring.
- Build evaluation datasets – Create test data for scorers.

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
