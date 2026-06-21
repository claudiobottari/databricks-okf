---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a3ee04a51461aa69d7c1b24def63a470f1a366eadddc7be0836da8ac19f533a3
  pageDirectory: concepts
  sources:
    - get-started-mlflow-3-for-genai-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-llm-as-a-judge-evaluation
    - MLE
  citations:
    - file: get-started-mlflow-3-for-genai-databricks-on-aws.md
title: MLflow LLM-as-a-Judge Evaluation
description: Automated evaluation of GenAI application outputs using built-in and custom scorers that leverage an LLM to judge metrics like Safety, Correctness, and custom guidelines.
tags:
  - mlflow
  - evaluation
  - llm-as-a-judge
  - genai
timestamp: "2026-06-19T18:58:56.461Z"
---

## MLflow LLM-as-a-Judge Evaluation

**MLflow LLM-as-a-Judge Evaluation** is a technique in [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md) that uses a large language model (LLM) to automatically score the quality of GenAI application outputs. Instead of relying solely on human reviewers, an LLM acts as the judge, applying predefined criteria to assess outputs for metrics such as safety, correctness, adherence to guidelines, and other custom dimensions. This approach integrates seamlessly with MLflow's tracing and evaluation workflows, enabling automated quality checks during development and production monitoring. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

### Overview

LLM-as-a-Judge evaluation is part of MLflow's broader evaluation and monitoring capabilities. It works by defining *scorers* — functions that apply an LLM to judge outputs against specified criteria. MLflow provides both built-in scorers for common metrics and a mechanism for creating fully custom scorers. The evaluation is run using the `mlflow.genai.evaluate()` function, which executes the target application on an evaluation dataset and then applies the scorers to produce quality metrics. These metrics are logged to the active MLflow experiment for review in the Experiment UI. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

### Built-in LLM-as-a-Judge Scorers

MLflow includes built-in LLM-as-a-judge scorers for commonly needed quality dimensions. The source material specifically mentions the **Safety** scorer, which uses an LLM to judge whether model outputs contain unsafe content. Other built-in scorers (such as `Correctness`) are referenced indirectly but not detailed in the source. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

### Custom LLM-as-a-Judge Scorers

Users can define custom LLM-as-a-judge scorers using the **Guidelines** scorer type. Guidelines are textual instructions that the LLM judge uses to evaluate outputs. In the source example, multiple custom guidelines are defined:

- Response must be in the same language as the input
- Response must be funny or creative
- Response must be appropriate for children
- Response must follow the input template structure

Each guideline is wrapped in a `Guidelines(...)` instance with a name and the guideline text. The LLM judge then applies these guidelines to each output and produces a score. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

MLflow also supports [custom code-based scorers](/concepts/code-based-scorers.md), which allow programmatic evaluation rather than using an LLM as a judge. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

### Running an Evaluation

To perform an LLM-as-a-Judge evaluation, you:

1. Create an evaluation dataset — a list of dictionaries with input fields.
2. Define the scorers (built-in and/or custom).
3. Call `mlflow.genai.evaluate(data=..., predict_fn=..., scorers=...)`, where `predict_fn` is the GenAI application being evaluated.

The function runs the application on each input, collects the outputs, applies all scorers, and logs the resulting metrics to the active MLflow experiment. Users can review the results in the Experiment UI under the **Evaluations** tab. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

### Relationship to Human Feedback

LLM-as-a-Judge evaluation provides automated, scalable quality assessment, but it is complemented by [Human Feedback Collection in MLflow](/concepts/human-feedback-collection-in-mlflow.md). Domain experts can use the MLflow Review App to label traces with custom rating schemas (e.g., "Very funny", "Slightly funny", "Not funny"). The same scorers defined for LLM-as-a-Judge evaluation can later be reused for [Production Monitoring](/concepts/production-monitoring.md), ensuring consistent quality metrics in deployment. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

### Next Steps

- Learn about [MLflow Tracing](/concepts/mlflow-tracing.md) to instrument GenAI applications.
- Explore MLflow Evaluation and Monitoring for detailed documentation on scorers and metrics.
- Understand how to [build MLflow evaluation datasets](/concepts/mlflow-evaluation-datasets.md) from logged usage data.
- See [production monitoring with MLflow](/concepts/production-monitoring.md) for deploying scorers in live environments.

## Sources

- get-started-mlflow-3-for-genai-databricks-on-aws.md

# Citations

1. [get-started-mlflow-3-for-genai-databricks-on-aws.md](/references/get-started-mlflow-3-for-genai-databricks-on-aws-4186f156.md)
