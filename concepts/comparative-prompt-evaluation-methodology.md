---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ff0ff30259e73a4cee722925e08406a8e0c3f823c52bb759c02179db50ec365f
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - comparative-prompt-evaluation-methodology
    - CPEM
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Comparative Prompt Evaluation Methodology
description: The practice of evaluating multiple prompt versions against identical datasets and using weighted composite scores to objectively identify the best-performing version.
tags:
  - methodology
  - evaluation
  - comparison
timestamp: "2026-06-18T12:11:41.040Z"
---

# Comparative Prompt Evaluation Methodology

**Comparative Prompt Evaluation Methodology** is a structured approach for systematically assessing different [prompt versions](/concepts/prompt-versioning.md) to identify the most effective ones for GenAI agents and applications. This methodology enables developers to make data-driven decisions about prompt selection by evaluating variants against consistent criteria.

## Overview

The methodology involves creating multiple prompt versions, building [Evaluation Datasets](/concepts/evaluation-datasets.md) with expected facts, and using [MLflow](/concepts/mlflow.md)'s evaluation framework to compare performance across versions. By applying consistent [judges](/concepts/llm-judges.md) and metrics to all versions, teams can quantify which prompts produce the best results for their specific use cases. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Core Principles

### Best Practices

1. **Start simple**: Begin with basic prompts and iteratively improve based on evaluation results.
2. **Use consistent datasets**: Evaluate all versions against the same data for fair comparison.
3. **Track everything**: Log prompt versions, evaluation results, and deployment decisions.
4. **Test edge cases**: Include challenging examples in your evaluation dataset.
5. **Monitor production**: Continue evaluating prompts after deployment to catch degradation.
6. **Document changes**: Use meaningful commit messages to track why changes were made. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Methodology Steps

### Step 1: Configure Environment

Set up a [Unity Catalog](/concepts/unity-catalog.md) schema with required privileges (`CREATE FUNCTION`, `EXECUTE`, and `MANAGE`) on both the [Catalog and Schema](/concepts/catalog-and-schema.md) to create prompts and evaluation datasets. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Step 2: Create Prompt Versions

Register different prompt versions representing different approaches to the task. Each version should have a clear commit message explaining the change. For example, a basic summarization prompt versus one with comprehensive guidelines and constraints. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Step 3: Create Evaluation Dataset

Build a dataset with expected_facts vs expected_response|expected facts that should appear in good outputs. Each example should include:
- `inputs`: The content passed to the prompt
- `expectations`: The `expected_facts` that judges should verify

This dataset forms the basis for comparing all prompt versions. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Step 4: Create Evaluation Functions and Judges

Define functions that use each prompt version and create [Custom Judges](/concepts/custom-judges.md) using `make_judge()` for specific quality criteria. Judges are LLM-based scorers that evaluate outputs against defined requirements. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Step 5: Run Comparative Evaluation

Evaluate each prompt version using both [built-in scorers](/concepts/custom-vs-built-in-scorers.md) (like `Correctness()`) and custom judges. Run evaluations in separate [MLflow runs](/concepts/mlflow-run.md) to track results per version. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Step 6: Compare Results and Select Best Version

Analyze results across all metrics using composite scores. Weight metrics according to priority (e.g., 70% correctness, 30% compliance) to identify the best-performing version. Compare score distributions across versions to determine which configuration better satisfies quality criteria. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Types of Evaluation

### Fact-Based Evaluation

Use `Correctness()` scorers to check whether prompts capture expected_facts vs expected_response|expected facts from input content. Track the percentage of facts captured across versions to measure completeness of summaries. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Constraint-Based Evaluation

Create custom judges that evaluate whether prompts follow specific requirements, such as sentence count limits or format constraints. These judges return [structured feedback](/concepts/label-schemas-for-structured-feedback.md) values that can be compared across configurations. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Comparative Analysis

### Interpreting Results

Each judge returns structured feedback values that can be compared across configurations:

| Judge Type | Feedback Values | Purpose |
|------------|-----------------|---------|
| `Correctness` | Score based on expected facts | Assesses factual accuracy |
| `sentence_count_compliance` | `correct` / `incorrect` | Validates format constraints |

By comparing score distributions across runs, developers can determine which prompt version better satisfies quality criteria. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Composite Scoring

Calculate composite scores by weighting metrics according to business priorities. For example:
- 70% weight on fact correctness
- 30% weight on format compliance

The version with the highest composite score becomes the candidate for production deployment. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Related Concepts

- [Prompt Versions](/concepts/prompt-versioning.md) — Different iterations of prompts for comparison
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers that evaluate prompt quality
- make_judge()|Make Judge API — The `make_judge()` function for creating evaluators
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Structured data for comparing prompt versions
- expected_facts vs expected_response|Expected Facts — Facts that should appear in generated outputs
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Similar approach for agent behavior comparison
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
