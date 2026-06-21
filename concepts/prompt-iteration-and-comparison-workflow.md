---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 389403c807419a3091df4533594bfd21091254118217f86e86110e6100ff3285
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-iteration-and-comparison-workflow
    - Comparison Workflow and Prompt Iteration
    - PIACW
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Prompt Iteration and Comparison Workflow
description: Workflow for iteratively improving GenAI application prompts, re-running evaluations, and comparing results side-by-side in the MLflow UI to measure improvement.
tags:
  - mlflow
  - workflow
  - prompt-engineering
timestamp: "2026-06-19T13:49:27.481Z"
---

# Prompt Iteration and Comparison Workflow

**Prompt Iteration and Comparison Workflow** refers to the systematic process of refining a GenAI application’s prompt through successive evaluation runs, followed by comparative analysis to select the best performing variant. This workflow is central to developing reliable and high‑quality AI applications, allowing developers to measure the impact of prompt changes on defined quality criteria before deploying to production.

## Overview

Iterative prompt development is a core practice in [GenAI application development](/concepts/genai-application-evaluation-lifecycle.md). Instead of guessing whether a prompt change improves output quality, teams use a data‑driven loop:

1. Define the application (for example, a sentence completion function).  
2. Create a representative [Evaluation Dataset](/concepts/evaluation-dataset.md) of inputs.  
3. Define evaluation criteria using [MLflow Scorers](/concepts/mlflow-scorers.md) (e.g., guidelines, safety checks).  
4. Run the evaluation with the current prompt.  
5. Review the results in the [MLflow UI](/concepts/mlflow.md).  
6. Modify the prompt based on insights.  
7. Re‑run the evaluation with the updated prompt.  
8. Compare the two (or more) runs side‑by‑side in the MLflow UI to verify improvement.

This loop can be repeated multiple times until the prompt meets the required quality thresholds. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Key Components

### Application Function

The application is typically wrapped in a function that accepts inputs (e.g., a sentence template) and returns a generated output. The function reads the prompt from a global variable or configuration, so that modifying the prompt automatically affects the next evaluation run. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Evaluation Dataset

The dataset contains inputs that represent real‑world use cases. For a fair comparison, the same dataset is used across all prompt variants. Each entry can include optional `expectations` that judges can reference. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Evaluation Criteria (Scorers)

Scorers assess outputs against specific guidelines. Built‑in options include `Guidelines` (for custom rules) and `Safety()` (for harm detection). Common criteria include language consistency, creativity, age‑appropriateness, and template adherence. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Evaluation Run

Calling `mlflow.genai.evaluate()` with the dataset, the predict function, and the scorers produces an evaluation run. Each run is recorded in an [MLflow Experiment](/concepts/mlflow-experiment.md). ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Comparison

The MLflow UI allows side‑by‑side comparison of runs. Developers can view score distributions, individual judge verdicts, and trace details to understand how the prompt change affected behavior. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Best Practices

- **Control one variable at a time.** Change only the prompt (or the specific aspect being tested) while keeping the dataset, scorers, and other configuration constant. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]  
- **Use a representative evaluation dataset.** The test cases should reflect the range of real‑world inputs the application will encounter in production. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]  
- **Align judges with human feedback.** As you gather expert annotations on agent outputs, fine‑tune the judges to better reflect human quality assessments. See Align judges with human feedback. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]  
- **Document configurations.** Record the exact prompt, dataset, scorers, and code version for each run to ensure reproducibility. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Example Workflow

The following code sketch outlines the iterative loop (simplified from a full tutorial):

```python
# Initial prompt
SYSTEM_PROMPT = "You are a smart bot ..."

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

# First evaluation
results_v1 = mlflow.genai.evaluate(data=eval_data, predict_fn=generate_game, scorers=scorers)

# After reviewing, modify prompt
SYSTEM_PROMPT = "You are a creative sentence game bot for children... RULES: ..."

# Second evaluation
results_v2 = mlflow.genai.evaluate(data=eval_data, predict_fn=generate_game, scorers=scorers)
```

After both runs, open the MLflow Experiment UI and compare the two runs to see if the new prompt improves scores on criteria like child safety and template adherence. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The framework that powers the evaluation harness.  
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – The shared input data used across prompt variants.  
- [MLflow Scorers](/concepts/mlflow-scorers.md) – Judge functions that score outputs against criteria.  
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – A broader technique that can include prompt changes as one axis of comparison.  
- [Custom Judges](/concepts/custom-judges.md) – Creating task‑specific LLM‑based scorers.  
- [Trace‑Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Deeper analysis using execution traces.

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md  
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
