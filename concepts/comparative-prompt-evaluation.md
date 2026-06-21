---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3441b61570ecda04d373c8b45de8252b9baeaa699698a66d8772fc856e4e38be
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - comparative-prompt-evaluation
    - CPE
    - comparative-prompt-evaluation-methodology
    - CPEM
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Comparative Prompt Evaluation
description: The systematic process of evaluating multiple prompt versions against a shared dataset and scoring them to identify the best-performing version.
tags:
  - evaluation
  - experimentation
  - optimization
timestamp: "2026-06-18T15:36:58.664Z"
---

## Comparative Prompt Evaluation

**Comparative Prompt Evaluation** refers to the systematic process of testing multiple versions of a prompt—against the same evaluation dataset and scoring criteria—in order to identify the most effective version for a GenAI agent or application. The approach is built into [MLflow GenAI](/concepts/mlflow-3-for-genai.md)'s evaluation framework and helps developers make data-driven decisions about prompt changes before deployment. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Best Practices

When comparing prompt versions, the following practices are recommended: start with simple prompts and iterate based on results; use the same evaluation dataset for every version to ensure fairness; log all prompt versions, evaluation results, and deployment decisions; include edge-case examples in the dataset; continue monitoring after deployment to catch degradation; and use meaningful commit messages to document why changes were made. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Step‑by‑Step Workflow

#### 1. Configure the Environment

Before starting, ensure you have MLflow 3.1.0 or higher, access to an LLM (OpenAI API or Databricks Model Serving), and the necessary Unity Catalog privileges (`CREATE FUNCTION`, `EXECUTE`, and `MANAGE`). Install required packages and set up a Unity Catalog schema where prompts and evaluation datasets will be stored. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

#### 2. Create Prompt Versions

Register different prompt versions in the [Prompt Registry](/concepts/prompt-registry.md) using `mlflow.genai.register_prompt()`. Each version represents a distinct approach to the task (for example, a basic summarization prompt versus one with detailed guidelines). Assign a commit message to document the change. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

#### 3. Build an Evaluation Dataset

Create a [Evaluation Dataset](/concepts/evaluation-dataset.md) with `mlflow.genai.datasets.create_dataset()`. Each record should contain `inputs` (the data passed to the prompt) and optionally `expectations` that encode expected facts the response should cover. These expected facts will be used by scorers to assess correctness. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

#### 4. Define Evaluation Functions and Custom Metrics

Write a wrapper function that loads a specific prompt version, formats it with the input, calls the LLM, and returns the output. Using `@mlflow.trace` enables tracing. Then create custom [judges](/concepts/llm-judges.md) with `make_judge()` to evaluate criteria not covered by built-in scorers. For example, a judge can check that a summary follows a length constraint (e.g., exactly two sentences). ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

#### 5. Run Comparative Evaluation

Use `mlflow.genai.evaluate()` with the same dataset and the same set of scorers for each prompt version. Common scorers include the built-in Correctness scorer (which checks expected facts) and any custom judges. Each evaluation run logs its results as an [MLflow Run](/concepts/mlflow-run.md). ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

#### 6. Compare Results and Select the Best Version

Retrieve the metrics from each run (e.g., `correctness/mean`, custom judge means). Compute a composite score if desired (for example, weighting correctness at 70% and another criterion at 30%). The version with the highest composite score is identified as the best performer. Examine which metric drove the decision. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Example Notebook

A complete working example is available as the *Evaluating a GenAI app quickstart notebook* referenced in the source documentation. It demonstrates the full workflow described above. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) — Central storage and versioning of prompt templates.
- [Judge (MLflow GenAI)](/concepts/built-in-judges-mlflow.md) — LLM‑based scorer for custom evaluation criteria.
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators.
- [Correctness Scorer](/concepts/correctness-scorer.md) — Built‑in scorer that checks expected facts.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` function.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — Structured set of inputs and expectations for testing.

### Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
