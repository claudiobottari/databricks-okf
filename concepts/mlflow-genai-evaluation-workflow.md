---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 27ff54afad289f31ab34ce3f6ed2a6631c9daf70579155439ab807854964f7c1
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluation-workflow
    - MGEW
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: MLflow GenAI Evaluation Workflow
description: End-to-end process of defining custom judges, building evaluation datasets, and running evaluations with mlflow.genai.evaluate() to assess GenAI agent quality
tags:
  - mlflow
  - evaluation
  - workflow
  - genai
timestamp: "2026-06-18T14:46:21.478Z"
---

# MLflow GenAI Evaluation Workflow

**MLflow GenAI Evaluation Workflow** is a structured process for assessing and improving the quality of GenAI agents using [MLflow](/concepts/mlflow.md)'s evaluation framework. The workflow enables developers to define quality criteria, create evaluation datasets, run offline evaluations, and compare results across different agent configurations before deploying to production.

## Overview

The MLflow GenAI evaluation workflow provides a systematic approach to measuring agent quality through [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers that evaluate outputs against specific criteria. The workflow supports both input/output analysis and [trace-based evaluation](/concepts/mlflow-trace-based-evaluation.md) for deeper behavioral assessment.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Workflow Steps

### Step 1: Create an Agent to Evaluate

The first step is defining the GenAI agent that will be evaluated. Agents can include:

- LLM-powered conversational applications
- Tools and function calls
- Configurable behavior flags for A/B testing

The agent's behavior is typically controlled through code-level variables that toggle specific features, such as whether an agent attempts to resolve customer issues.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Step 2: Define Custom Judges

[Custom Judges](/concepts/custom-judges.md) are the core evaluation mechanism. Created using the `make_judge()` function, these LLM-based scorers evaluate agent responses against specific quality criteria. Three common types include:^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

- **Input/Output judges** — Evaluate behavior by analyzing conversation history (inputs) and agent responses (outputs)
- **Expected behavior judges** — Compare agent outputs against predefined expectations
- **Trace-based judges** — Analyze the full execution trace including tool invocations and intermediate reasoning steps

### Step 3: Create an Evaluation Dataset

An [Evaluation Dataset](/concepts/evaluation-dataset.md) contains test cases with `inputs` (conversation history passed to the agent) and optional `expectations` that judges can reference. The dataset should represent the range of real-world scenarios the agent will encounter in production.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Step 4: Run Evaluations

The `mlflow.genai.evaluate()` function runs the agent against the evaluation dataset with one or more judges. Multiple judges can evaluate different aspects of the agent simultaneously, such as:^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

- **Issue resolution quality**
- **Expected behaviors compliance**
- **Tool call correctness**

### Step 5: Compare Configurations

A key feature of the workflow is [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md). By running the same evaluation dataset against different agent configurations with consistent judges, teams can quantify the impact of changes before promoting to production.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Best Practices

- **Control one variable at a time.** Change only the agent behavior being tested while keeping all other factors constant.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Use a representative evaluation dataset.** Test cases should reflect the range of real-world inputs the agent will encounter in production.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Align judges with human feedback.** As expert annotations on agent outputs are gathered, fine-tune judges to better reflect human quality assessments. See Align judges with human feedback.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Document configurations.** Record exact parameters, prompts, and code versions for each configuration to ensure reproducibility.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Deploy consistent judges.** Using the same judges across all evaluation runs ensures that score differences reflect changes in agent behavior rather than inconsistencies in evaluation criteria.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Production Monitoring

After evaluation, custom judges can be deployed for [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — continuous quality monitoring of agent performance in production environments.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers that evaluate agent quality
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Systematic comparison of agent variants
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for deeper quality analysis
- Align Judges with Human Feedback — Improving judge accuracy with expert annotations
- [Synthetic Evaluation Generation](/concepts/synthetic-evaluation-data-generation.md) — Creating evaluation datasets automatically

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
