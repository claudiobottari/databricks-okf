---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1fbc4abad311cb66a3615ba52437c2b991b1a27494895149cbe47e3d2a781599
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iterative-prompt-improvement-workflow
    - IPIW
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Iterative Prompt Improvement Workflow
description: "A workflow pattern for GenAI development: evaluate a prompt, review results, revise the prompt based on evaluation criteria, re-run evaluation, and compare runs in the MLflow UI."
tags:
  - workflow
  - prompt-engineering
  - evaluation
timestamp: "2026-06-18T14:15:14.949Z"
---

# Iterative Prompt Improvement Workflow

**Iterative Prompt Improvement Workflow** refers to the systematic process of evaluating, analyzing, and refining the system prompt of a GenAI application through repeated cycles of assessment and modification. This approach allows developers to incrementally enhance response quality by grounding changes in quantitative evaluation results rather than intuition alone.

## Overview

Building a high-quality GenAI application typically requires multiple iterations. An initial prompt may produce outputs that are off-target, unsafe, or not aligned with user expectations. By defining clear evaluation criteria, running an automated assessment, reviewing the results, adjusting the prompt, and re-evaluating, teams can converge on a prompt that reliably meets their quality standards.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

The workflow is a core part of using [MLflow GenAI](/concepts/mlflow-3-for-genai.md)'s evaluation capabilities. It combines the creation of an evaluation dataset, the use of [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) to measure criteria, and the ability to compare runs in the MLflow UI to see how prompt changes affect performance.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Steps in the Workflow

### 1. Define the Application and Prompt

Create the GenAI application — typically a function that takes an input and returns a response using a large language model. Start with a basic system prompt that instructs the model on the task. For example, a sentence completion game might begin with a simple prompt: *"You are a smart bot that can complete sentence templates to make them funny. Be creative and edgy."*^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### 2. Create an Evaluation Dataset

Assemble a representative set of inputs that reflect the range of real-world requests the application will handle. Each entry in the dataset contains the `inputs` field passed to the predict function, and can optionally include `expectations` that judges may reference.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### 3. Define Evaluation Criteria Using Scorers

Select or create [[scorers]] that define the quality dimensions to measure. MLflow provides built-in scorers such as `Guidelines` (to check adherence to specific rules), `Safety` (to flag unsafe content), and the ability to create [Custom Judges](/concepts/custom-judges.md). Example criteria might include language consistency, creativity, child-appropriateness, and template adherence.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### 4. Run the Initial Evaluation

Use `mlflow.genai.evaluate()` to run the evaluation. The function takes the evaluation dataset, the predict function (which uses the current prompt), and the list of scorers. The results are automatically logged to an MLflow experiment.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### 5. Review the Results

Examine the scores for each criterion across all evaluation examples. The MLflow Experiment UI provides a comparison view that shows per-input scores and aggregate metrics. This review reveals where the prompt is failing — for instance, outputs that are not child-safe or not following the template structure.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### 6. Modify the Prompt

Based on the evaluation insights, refine the system prompt to address identified weaknesses. For example, a prompt that originally produced edgy content may be updated with explicit rules about being child-appropriate and adding creative constraints. The new prompt becomes the version to test.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### 7. Re-run the Evaluation

Re-execute `mlflow.genai.evaluate()` with the same dataset and scorers but with the updated prompt. Because the predict function references a global variable for the system prompt, simply updating that variable and rerunning the function applies the new behavior.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### 8. Compare Results

Use the MLflow UI to compare the results of the two runs side-by-side. The comparison highlights improvements and regressions across each criterion, enabling data-driven decisions about whether the prompt change is beneficial.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Using A/B Comparison for More Systematic Iteration

For more complex improvements involving multiple behavior flags or configuration options, teams can adopt an [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) approach. This involves evaluating two or more configurations against the same dataset and scoring them with identical judges, then comparing score distributions to determine which configuration better satisfies the criteria.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Best Practices

- **Keep the evaluation dataset fixed across iterations.** Using the same set of inputs ensures that score differences are attributable to prompt changes, not to variation in test cases.
- **Control one variable at a time.** Change only the prompt (or the specific behavior flag) between iterations to isolate the effect of each modification.
- **Align judges with human feedback.** As you gather expert annotations on agent outputs, fine-tune the judges to better reflect human quality assessments — see Align judges with human feedback.
- **Document each prompt version.** Record the exact prompt text, evaluation scores, and dataset used for each iteration to ensure reproducibility.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) — The components that provide quantitative quality metrics
- [Custom Judges](/concepts/custom-judges.md) — Creating task-specific judges using `make_judge()`
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing multiple configurations systematically
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Extending evaluation to live deployments
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for deeper quality analysis

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
