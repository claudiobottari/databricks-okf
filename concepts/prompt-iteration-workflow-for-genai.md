---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d0f276329ceeefb036ce9159f1e609430e01bf4bdeb4d37996c4f2227a217f5e
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-iteration-workflow-for-genai
    - PIWFG
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: Prompt Iteration Workflow for GenAI
description: The iterative process of defining system prompts, evaluating outputs against criteria, refining prompts, and comparing results in the MLflow UI.
tags:
  - prompt-engineering
  - evaluation
  - iteration
  - workflow
timestamp: "2026-06-19T21:54:01.214Z"
---

# Prompt Iteration Workflow for GenAI

The **Prompt Iteration Workflow for GenAI** is a systematic process for improving a generative AI application by repeatedly modifying its system prompt, re-running an automated evaluation, and comparing the results to identify the best prompt variant. The workflow is supported by [MLflow](/concepts/mlflow.md)'s evaluation tools, which provide structured scoring and side-by-side comparison of different prompt versions. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Overview

The core idea is to treat prompt refinement as a data-driven loop. Rather than manually guessing whether a prompt change is effective, the workflow uses:

- A **predict function** that wraps the GenAI application (e.g., a sentence completion game).
- A fixed **evaluation dataset** of inputs—this stays unchanged so comparisons are fair.
- A set of **scorers** that define the criteria for a good response (e.g., funniness, safety, format adherence).
- The **MLflow evaluation harness** (`mlflow.genai.evaluate()`), which runs the predict function on every example, collects scores, and logs all data to an MLflow Experiment.
- The **MLflow Experiment UI** for reviewing scores and comparing two or more prompt versions side by side. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

The workflow follows these steps:

| Step | Action | Purpose |
|------|--------|---------|
| 1 | Create the initial GenAI application (prompt + function) | Establish a baseline |
| 2 | Create a fixed evaluation dataset | Ensure consistent evaluation across iterations |
| 3 | Define evaluation criteria (scorers) | Quantify what "good" means |
| 4 | Run the evaluation | Collect baseline scores |
| 5 | Review the results | Identify weaknesses and opportunities |
| 6 | Modify the system prompt | Address specific issues |
| 7 | Re-run the evaluation with the same dataset and scorers | Measure the impact of the change |
| 8 | Compare the two runs in the MLflow UI | Determine which prompt performs better |

^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Detailed Steps

### Step 1: Create the GenAI Application

The application is typically a Python function that takes an input (e.g., a sentence template) and calls an LLM to produce a response. The system prompt is stored separately so it can be modified between runs. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

```python
SYSTEM_PROMPT = "You are a smart bot that can complete sentence templates to make them funny. Be creative and edgy."

@mlflow.trace
def generate_game(template: str):
    response = client.chat.completions.create(
        model="databricks-claude-sonnet-4-5",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": template},
        ],
    )
    return response.choices[0].message.content
```

The `@mlflow.trace` decorator automatically captures tracing data for observability. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Step 2: Create a Fixed Evaluation Dataset

The dataset is a list of input objects, each containing the parameters that the predict function expects. It should be diverse enough to stress-test the prompt across different scenarios. The dataset does not change between iterations to ensure fair comparisons. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Step 3: Define Evaluation Criteria with Scorers

[[Scorers]] (also called [LLM Judges](/concepts/llm-judges.md)) are functions that evaluate each generated response against a specific criterion. MLflow provides built-in scorers such as:

- **`Guidelines`**: a configurable scorer that checks textual guidelines (e.g., "Response must be funny or creative").
- **`Safety`**: a built-in scorer that detects harmful or unsafe content.

Users define a list of scorers that capture the desired qualities of the application. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Step 4: Run the Evaluation

```python
results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=generate_game,
    scorers=scorers,
)
```

This call runs the predict function on every item in `eval_data`, applies each scorer to the output, and logs everything to the current MLflow Experiment. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Step 5: Review Results

Results are visible in the notebook's interactive cell output and in the MLflow Experiment UI. The UI displays a table with each input, the generated response, and the score for every scorer. Users can identify patterns—for example, a low "child_safe" score indicates the prompt is producing inappropriate content. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Step 6–7: Modify Prompt and Re-run

Based on the review, the system prompt is updated to address identified shortcomings. For example, if responses are not child-appropriate, the prompt can be rewritten with explicit guidelines (e.g., "Ensure all content is family-friendly and child appropriate for 1 to 6 year olds"). After updating the prompt, the same `mlflow.genai.evaluate` call is executed again. Because the dataset and scorers are unchanged, the new scores are directly comparable to the old ones. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Step 8: Compare Results

The MLflow Experiment UI allows users to select two or more runs and view a side-by-side comparison of scores, including per-scorer metrics. This makes it easy to see whether the prompt change improved or degraded specific criteria. The comparison view also shows sample outputs for qualitative assessment. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Best Practices

- **Keep the evaluation dataset fixed** across all iterations to isolate the effect of the prompt change. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **Start with a minimal set of scorers** and add only those that matter for your use case. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **Use a single logical change per iteration** to attribute score differences to the specific modification. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **Review both quantitative scores and qualitative outputs** in the comparison view—scores may not capture subtle aspects like tone or creativity. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **Run baseline evaluations first** before any prompt optimization to establish a reference point. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) – The platform that provides the evaluation harness and experiment tracking.
- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md) – The broader discipline of assessing large language model outputs.
- Prompt Engineering – The practice of designing and refining prompts.
- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) – The scoring functions used in the evaluation.
- [Generative AI Application](/concepts/tracing-for-generative-ai-applications.md) – The type of application being iteratively improved.
- [Experiment Tracking](/concepts/mlflow-experiment-tracking.md) – Logging runs and comparing results over time.

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
