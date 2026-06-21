---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c310a1d1f8b6f1ae1360f61f98582a8f730e5048257adbcbeeeb20044703e46
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-version-management
    - PVM
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Prompt Version Management
description: Registering, versioning, and iterating prompt templates in MLflow's prompt registry with semantic commit messages.
tags:
  - mlflow
  - prompt-engineering
  - version-control
timestamp: "2026-06-19T10:22:13.126Z"
---

Here is the updated wiki page for **Prompt Version Management**, rewritten to draw facts solely from the source material and structured per the authoring guidelines.

---

---
title: Prompt Version Management
summary: Creating, registering, and versioning prompt templates in MLflow GenAI's prompt registry, building evaluation datasets, defining custom judges, and running comparative evaluations to select the best performing version.
sources:
  - evaluate-and-compare-prompt-versions-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:36:58.781Z"
updatedAt: "2026-06-18T15:36:58.781Z"
tags:
  - mlflow
  - prompt-engineering
  - version-control
aliases:
  - prompt-version-management
  - PVM
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Prompt Version Management

**Prompt Version Management** is the practice of systematically creating, tracking, and evaluating different versions of prompts used in [GenAI](/concepts/mlflow-genai-evaluate-api.md) agents and applications. By registering prompt versions in a dedicated registry and running structured evaluations against a consistent dataset, teams can objectively compare alternatives, select the best performing prompt, and maintain a clear, reproducible history of changes. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Overview

Prompt quality directly affects the output of LLM-based applications. As prompts evolve through iterative improvements, bug fixes, or feature additions, it becomes essential to manage those changes in a reproducible way. The process integrates prompt storage with [MLflow](/concepts/mlflow.md)’s evaluation framework so that each version can be assessed against the same dataset and scoring criteria. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

The workflow relies on three key components:

- **Prompt Registry** – A centralized store (backed by [Unity Catalog](/concepts/unity-catalog.md)) that holds prompt templates and version metadata.
- **Evaluation Datasets** – Curated collections of input examples and expected facts that define what a good response should contain.
- **Judges (Scorers)** – LLM-based evaluators (both built-in and custom) that assign scores to responses automatically.

## Best Practices

The source material recommends the following practices for prompt version management ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]:

1. **Start simple**: Begin with basic prompts and iteratively improve based on evaluation results.
2. **Use consistent datasets**: Evaluate all versions against the same data for fair comparison.
3. **Track everything**: Log prompt versions, evaluation results, and deployment decisions.
4. **Test edge cases**: Include challenging examples in your evaluation dataset.
5. **Monitor production**: Continue evaluating prompts after deployment to catch degradation.
6. **Document changes**: Use meaningful commit messages to track why changes were made.

## Creating Prompt Versions

Prompt templates are registered in the prompt registry using `mlflow.genai.register_prompt()`. Each registration creates a new version with a unique version number and an associated commit message. For example:

- **Version 1** – A basic prompt: `"Summarize this text: {{content}}"`
- **Version 2** – An improved prompt with detailed guidelines and a sentence‑count requirement. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

The registry preserves the full history, making it possible to load any previous version by name and version number. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Building Evaluation Datasets

An evaluation dataset contains input examples (the `inputs` dictionary) and `expectations` objects that specify the facts or qualities a correct response should contain. These expected facts serve as ground truth for Correctness scoring and can also guide custom judges. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

Datasets are created as Unity Catalog tables using `mlflow.genai.datasets.create_dataset()`, and examples are added with `merge_records()`. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Defining Evaluation Functions and Custom Judges

Each prompt version is wrapped in a prediction function that loads the prompt, formats it with the input, calls the LLM, and returns the response. These functions are passed to `mlflow.genai.evaluate()`. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

In addition to built-in scorers like `Correctness`, custom judges can be created using `make_judge()`. A judge is an LLM-based scorer that evaluates responses against specific criteria (e.g., compliance with a sentence‑count rule). ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Running Comparative Evaluation

To compare prompt versions, call `mlflow.genai.evaluate()` for each version, using the **same evaluation dataset** and the **same set of scorers**. Each run logs the prompt version as a parameter and returns metrics such as `correctness/mean` and `sentence_count_compliance/mean`. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

The results can then be aggregated into composite scores (e.g., weighting correctness at 70% and compliance at 30%) to identify the best performing version. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Selecting and Deploying the Best Version

The best performing version can be promoted to production by assigning an alias (e.g., `"prod"` or `"latest"`) to the prompt version. Aliases allow deployed applications to always use the current recommended prompt without hardcoding a version number. See Use Prompts in Deployed Apps for details. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) – Centralized storage for prompt templates and version history.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The framework behind `mlflow.genai.evaluate()`.
- [Custom Judges](/concepts/custom-judges.md) – User‑defined LLM‑based scorers for domain‑specific criteria.
- [Evaluation Harness](/concepts/evaluation-harness.md) – Deep dive into the evaluation API.
- [[Scorers|Scorers (Predefined)]] – Built‑in metrics such as `Correctness`.
- [Track Prompts with App Versions](/concepts/prompt-versioning.md) – Associating prompt versions with application releases.

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
