---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3cac362e1079ab02b078de6761ddaf6d5009241312ccf50fdb67a297f2ea9971
  pageDirectory: concepts
  sources:
    - optimize-prompts-tutorial-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-prompt-optimization
    - MGPO
  citations:
    - file: optimize-prompts-tutorial-databricks-on-aws.md
title: MLflow GenAI Prompt Optimization
description: A framework within MLflow for automatically optimizing prompt templates using evolutionary algorithms and evaluation scorers
tags:
  - mlflow
  - prompt-optimization
  - genai
timestamp: "2026-06-19T19:52:09.959Z"
---

## MLflow GenAI Prompt Optimization

**MLflow GenAI Prompt Optimization** is a feature within [MLflow](/concepts/mlflow.md) that automates the refinement of prompts for large language models (LLMs). It uses optimization algorithms and evaluation scorers to improve prompt performance against a given dataset, aligning model outputs with task-specific requirements. The feature is demonstrated in a tutorial using the GEPA (Generation‑Evaluation‑Prompt‑Adjustment) optimizer and a GPT‑OSS 20B model for a text classification task. ^[optimize-prompts-tutorial-databricks-on-aws.md]

### Key Components

- **GepaPromptOptimizer** – The optimizer that iteratively improves prompts based on reflection from a powerful model (e.g., `databricks-claude-sonnet-4-5`). It takes a `reflection_model` parameter. ^[optimize-prompts-tutorial-databricks-on-aws.md]
- **Correctness Scorer** – A scorer that evaluates the quality of the model’s output against expected answers. In the tutorial, it uses `databricks-gpt-5` as the evaluation engine. ^[optimize-prompts-tutorial-databricks-on-aws.md]
- **Predict Function** – A user‑defined function that calls the target LLM (e.g., `databricks-gpt-oss-20b`) with a formatted prompt. This function is passed to the optimizer for evaluation. ^[optimize-prompts-tutorial-databricks-on-aws.md]
- **Training Data** – A dataset containing `inputs` (with a `query` field), expected `outputs` (a `response` field), and `expectations` (such as allowed classification labels). The optimizer uses this data to guide optimization. ^[optimize-prompts-tutorial-databricks-on-aws.md]

### Optimization Process

1. **Register an initial prompt** – A simple prompt template (e.g., `"classify this: {{query}}"`) is registered in the [MLflow Prompt Registry](/concepts/prompt-registry.md) under a specified [Catalog and Schema](/concepts/catalog-and-schema.md). ^[optimize-prompts-tutorial-databricks-on-aws.md]
2. **Define the prediction function** – The function loads the prompt version, formats it with the query, sends it to the LLM, and returns the response. ^[optimize-prompts-tutorial-databricks-on-aws.md]
3. **Call `mlflow.genai.optimize_prompts`** – This API takes the prediction function, training data, prompt URIs, the optimizer instance, and a list of scorers. It returns a result containing one or more optimized prompts. ^[optimize-prompts-tutorial-databricks-on-aws.md]
4. **Review and deploy** – The optimized prompt is loaded back into the prediction function for testing. The prompt version can also be viewed in the MLflow experiment UI if the experiment type is set to **GenAI apps and agents**. ^[optimize-prompts-tutorial-databricks-on-aws.md]

### Example Workflow

The tutorial walks through classifying sentences from academic abstracts into one of five labels: `BACKGROUND`, `METHODS`, `RESULTS`, `OBJECTIVE`, `CONCLUSIONS`. The initial prompt (`"classify this: {{query}}"`) is evaluated against training data, then optimized to adhere strictly to the allowed label set. After optimization, the new prompt produces outputs aligned with the expected label format. ^[optimize-prompts-tutorial-databricks-on-aws.md]

### Related Concepts

- [MLflow Prompt Registry](/concepts/prompt-registry.md)
- GenAI Apps and Agents
- [Correctness Scorer](/concepts/correctness-scorer.md)
- [GEPA Prompt Optimizer](/concepts/gepapromptoptimizer.md)
- Prompt Engineering
- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md)

### Sources

- optimize-prompts-tutorial-databricks-on-aws.md

# Citations

1. [optimize-prompts-tutorial-databricks-on-aws.md](/references/optimize-prompts-tutorial-databricks-on-aws-b91f2148.md)
