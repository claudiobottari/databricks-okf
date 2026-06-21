---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 123b9a1a91f686f2dda8feee9c88a7b78e8762b96aa6510188207af56ea25224
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - comparative-prompt-evaluation-workflow
    - CPEW
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Comparative Prompt Evaluation Workflow
description: Systematic methodology for evaluating multiple prompt versions against the same dataset using consistent scorers to identify the best performer.
tags:
  - evaluation
  - workflow
  - prompt-engineering
timestamp: "2026-06-19T10:22:02.088Z"
---

# Comparative Prompt Evaluation Workflow

The **Comparative Prompt Evaluation Workflow** is a systematic process for evaluating and comparing different prompt versions to identify the most effective ones for agents and GenAI applications. The workflow uses [MLflow GenAI](/concepts/mlflow-3-for-genai.md)'s evaluation framework to create prompt versions, build evaluation datasets with expected facts, define custom judges, run comparative evaluations, and select the best-performing version based on composite scores.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Prerequisites

The workflow requires MLflow 3.1.0 or higher, OpenAI API access or Databricks Model Serving, and a Unity Catalog schema with `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` privileges. If using a Databricks trial account, the necessary permissions are granted on the `workspace.default` schema.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Best Practices

The source document recommends starting with simple prompts and iteratively improving based on evaluation results. All versions should be evaluated against the same dataset for fair comparison. Practitioners should log prompt versions, evaluation results, and deployment decisions; include edge cases in the evaluation dataset; continue monitoring prompts after deployment; and use meaningful commit messages to document why changes were made.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Step 1: Configure Environment

Set up a Unity Catalog schema and install required packages (`mlflow[databricks]>=3.1.0`, `openai`). Define unique names for the prompt and evaluation dataset. Configure the OpenAI client.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Step 2: Create Prompt Versions

Register different prompt versions representing different approaches to the task using `mlflow.genai.register_prompt()`. Each version consists of a template and a commit message. For example, version 1 might be a basic summarization prompt, while version 2 includes comprehensive guidelines with a sentence count requirement.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Step 3: Create Evaluation Dataset

Build a dataset with expected facts that good responses should contain using `mlflow.genai.datasets.create_dataset()`. Each example in the dataset includes `inputs` (the content to be processed) and `expectations` containing `expected_facts` — a list of key facts that should appear in the output. This dataset is used to score correctness across prompt versions.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Step 4: Create Evaluation Functions and Custom Metrics

Define a function that loads a prompt version, formats it with input content, calls the LLM, and returns the output. This function is wrapped with `@mlflow.trace` for observability. Then create a custom judge using `mlflow.genai.make_judge()` to evaluate specific criteria — for example, a sentence count compliance judge that checks whether summaries contain exactly two sentences.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Step 5: Run Comparative Evaluation

Evaluate each prompt version using `mlflow.genai.evaluate()` with a consistent set of scorers. Scorers include both built-in [Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) (such as `Correctness()`, which checks expected facts) and custom judges (such as the sentence count compliance judge). Each evaluation is run inside a separate `mlflow.start_run()` for tracking. The scorers produce per-version metrics like `correctness/mean` and `sentence_count_compliance/mean`.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Step 6: Compare Results and Select Best Version

Retrieve the metrics from each evaluation run and compute composite scores by weighting individual metrics (for example, 70% correctness and 30% sentence count compliance). The version with the highest composite score is selected as the best performer. The output includes not only the winning version but also explanatory details such as the percentage of expected facts captured and the frequency of sentence requirement compliance.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) – Where prompt versions are stored and managed.
- [Evaluation Harness](/concepts/evaluation-harness.md) – The underlying infrastructure behind `mlflow.genai.evaluate()`.
- [Custom Judges](/concepts/custom-judges.md) – Using `make_judge()` for domain-specific evaluation.
- [Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) – Built-in scorers like `Correctness`.
- Aliases for Deployment – How to deploy the best prompt version using aliases.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer used for prompts and evaluation datasets.

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
