---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d287a1e54ccff84602e5fd7f51682670051ca1d0092785dd271b46abc53b9379
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-version-evaluation
    - PVE
    - Prompt Evaluation
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Prompt Version Evaluation
description: A systematic methodology for comparing different prompt versions using consistent evaluation datasets, custom scorers, and composite metrics to identify the best-performing prompt.
tags:
  - evaluation
  - prompt-engineering
  - genai
timestamp: "2026-06-19T18:40:39.743Z"
---

# Prompt Version Evaluation

**Prompt Version Evaluation** is a systematic process of comparing different versions of a prompt to identify the most effective one for a given Generative AI (GenAI) application or agent. On Databricks, this process is performed using [MLflow](/concepts/mlflow.md)’s evaluation framework, which integrates with the [Prompt Registry](/concepts/prompt-registry.md) and [Unity Catalog](/concepts/unity-catalog.md) to provide reproducible, trackable comparisons.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Overview

Evaluating prompt versions helps developers make data-driven decisions about which prompt template yields the best results. The evaluation workflow involves registering multiple prompt versions, building a dataset with expected outputs or facts, defining scoring metrics, and running comparative evaluations. By consistently evaluating all versions against the same data, practitioners can select the best-performing prompt before deploying it to production.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

The process is designed to be iterative: start simple, evaluate, then refine prompts based on the results. It also encourages continuous monitoring after deployment to catch degradation over time.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Process

### 1. Configure the Environment

Before evaluation, the Unity Catalog schema must be set up, and the required packages (`mlflow[databricks]>=3.1.0`, `openai`) installed. Users need `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` privileges on the [Catalog and Schema](/concepts/catalog-and-schema.md) to create prompts and evaluation datasets.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### 2. Create Prompt Versions

Each candidate prompt is registered as a version under a named prompt in the Prompt Registry. For example, a basic summarization prompt (v1) and an improved version with detailed guidelines (v2) can be registered with distinct commit messages to document the changes.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### 3. Build an Evaluation Dataset

An evaluation dataset is created as a Unity Catalog table. It contains input examples and corresponding expectations — typically a list of `expected_facts` that should be present in the model’s output. This dataset is used to score the correctness and completeness of each prompt version’s responses.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### 4. Define Scorers and Judging Criteria

Built-in scorers, such as Correctness, automatically check for expected facts. Custom judges can be created with make_judge()|make_judge to evaluate specific criteria (e.g., whether the output adheres to a sentence‑count requirement). These scorers produce quantitative metrics that allow direct comparison between versions.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### 5. Run Comparative Evaluation

Using `mlflow.genai.evaluate()`, each prompt version is evaluated against the same dataset and set of scorers. The function returns metric scores (e.g., `correctness/mean`, `sentence_count_compliance/mean`) that are logged as part of an [MLflow Run](/concepts/mlflow-run.md) for full traceability.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### 6. Compare Results and Select the Best Version

Results from all versions are compared, optionally by computing a composite score that weights different metrics according to application priorities. The version achieving the highest score is identified as the best performer. The evaluation outputs also explain *why* it performed better — for example, “captures 90% of expected facts” or “follows sentence requirements 100% of the time”.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Best Practices

- **Start simple**: Begin with basic prompts and iteratively improve based on evaluation results.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Use consistent datasets**: Evaluate all versions against the same data for fair comparison.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Track everything**: Log prompt versions, evaluation results, and deployment decisions.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Test edge cases**: Include challenging examples in your evaluation dataset.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Monitor production**: Continue evaluating prompts after deployment to catch degradation.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Document changes**: Use meaningful commit messages to track why changes were made.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Next Steps After Evaluation

Once the best prompt version is identified through evaluation, it can be deployed to production using aliases in the Prompt Registry. For more details, see Use prompts in deployed apps. The evaluated prompt versions can also be linked to application versions for full traceability.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) – Centralized storage and versioning of prompts.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The framework used for scoring and comparing model outputs.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – A structured dataset used as ground truth for evaluation.
- [[Scorers]] – Plugins that compute metrics like correctness or custom criteria.
- Correctness – A built-in scorer that checks for expected facts.
- [Custom Judge](/concepts/custom-judges.md) – A user‑defined scorer created with `make_judge`.
- [Prompt Versioning](/concepts/prompt-versioning.md) – Managing multiple iterations of a prompt template.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) for storing prompts and evaluation datasets.

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
