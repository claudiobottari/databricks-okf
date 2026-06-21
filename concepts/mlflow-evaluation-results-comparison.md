---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60dbae25a5143f5fd4d9ae2db5b4fc83b0c0629734ed843720f2e16cbf0d4042
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-evaluation-results-comparison
    - MERC
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: MLflow Evaluation Results Comparison
description: The ability to compare multiple evaluation runs side-by-side in the MLflow UI to assess the impact of prompt changes on GenAI application quality.
tags:
  - mlflow
  - comparison
  - evaluation
timestamp: "2026-06-18T14:15:43.217Z"
---

# MLflow Evaluation Results Comparison

**MLflow Evaluation Results Comparison** is a feature within [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) that allows developers to compare the performance of different configurations of a GenAI application side-by-side in the MLflow UI. By iterating on prompts, models, or other parameters, running independent evaluations, and then comparing the results, teams can measure the impact of changes before deploying to production. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Accessing the Comparison UI

Evaluation results are displayed interactively in the notebook cell output immediately after a run completes. A link to the MLflow Experiment UI is provided in the cell results. From the Experiment UI, users can select two or more runs and view a side-by-side comparison of their evaluation scores. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

Alternatively, navigate to the experiment by clicking **Experiments** in the left sidebar of the Databricks workspace, then clicking the name of the experiment to open it. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## How to Compare Runs

1. **Define evaluation criteria** – Use [MLflow Scorers](/concepts/mlflow-scorers.md) such as `Guidelines` (for custom criteria) and `Safety` (for built-in safety checks) to specify how outputs should be judged.  
2. **Run an initial evaluation** – Call `mlflow.genai.evaluate()` with the evaluation dataset and scorers, using the initial prompt or configuration.  
3. **Modify the configuration** – Adjust the system prompt, model, or other parameters (e.g., for child-appropriateness) to create an improved version.  
4. **Run a second evaluation** – Call `mlflow.genai.evaluate()` again with the same dataset and scorers but the updated configuration.  
5. **Compare in the UI** – Open the Experiment UI, select both runs, and review the comparison table showing each scorer’s numeric or categorical results for every example in the dataset. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

The comparison makes it easy to see which configuration satisfies the desired criteria more consistently across the test cases.

## Interpreting Results

Each [[Scorers|scorer]] returns a value per evaluation record. For example, a `Guidelines` scorer might return a pass/fail judgment, while a `Safety` scorer returns a safety score. The comparison UI aggregates these values and allows drill-down into individual examples, including the input, output, and the judge’s reasoning. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Best Practices

- **Use the same evaluation dataset** – To ensure a fair comparison, evaluate different configurations against the identical set of inputs.
- **Change one variable at a time** – Only modify the system prompt, model, or agent behavior while keeping all other factors constant.
- **Re-run after every improvement** – After updating the prompt or logic, evaluate again and compare the new run with the previous one to validate improvement. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The framework for running offline evaluations of GenAI applications.
- [MLflow Scorers](/concepts/mlflow-scorers.md) — LLM-based judges that evaluate outputs against defined criteria.
- [LLM Judges](/concepts/llm-judges.md) — Another term for the evaluator models used within scorers.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — The set of input examples used for evaluation.
- Prompt Engineering — The iterative process of improving prompts, which benefits from comparison.

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
