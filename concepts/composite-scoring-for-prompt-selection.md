---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe5f3568f4abad84cd4721b69d933f17b758c06047508d30ab8c91106823135c
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - composite-scoring-for-prompt-selection
    - CSFPS
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Composite Scoring for Prompt Selection
description: A technique for combining multiple evaluation metrics (e.g., correctness and compliance) with weighted scores to produce a single quantitative ranking for prompt version selection.
tags:
  - evaluation
  - decision-making
  - genai
timestamp: "2026-06-19T18:40:55.350Z"
---

---
title: Composite Scoring for Prompt Selection
summary: Combining multiple evaluation metrics with weighted averages to compute a single ranking score for choosing the best prompt version.
sources:
  - evaluate-and-compare-prompt-versions-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:22:57.247Z"
updatedAt: "2026-06-19T10:22:57.247Z"
tags:
  - evaluation
  - decision-making
  - metrics
aliases:
  - composite-scoring-for-prompt-selection
  - CSFPS
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Composite Scoring for Prompt Selection

**Composite Scoring for Prompt Selection** is a technique used with [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation to combine multiple individual [quality metrics](/concepts/freshness-data-quality.md) into a single weighted score, enabling systematic comparison and selection of the best performing [prompt versions](/concepts/prompt-versioning.md). ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Overview

After evaluating each prompt version with a set of scorers (such as Correctness and a custom compliance judge), the individual metric means are combined using a weighted sum. This composite score provides a single numeric value that reflects the overall performance of each version. The version with the highest composite score is selected for deployment. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Composite Score Calculation

A composite score is typically computed as a weighted sum of individual metric means:

\[
\text{Composite Score} = w_1 \cdot m_1 + w_2 \cdot m_2 + \dots + w_n \cdot m_n
\]

Where \( w_i \) are weights (often summing to 1) and \( m_i \) are the mean metric values from the evaluation run (e.g., `correctness/mean`, `sentence_count_compliance/mean`). ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Example

In a summarization task, correctness is weighted more heavily than compliance:

```python
composite = 0.7 * correctness + 0.3 * compliance
```

After computing the composite score for each version, the version with the highest value is identified as the best performer. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Common Metrics for Compositing

### Correctness

The [Correctness Scorer](/concepts/correctness-scorer.md) checks how many expected facts from the evaluation dataset appear in the model output. Its mean score (`correctness/mean`) is a common component in composite scores for summarization and question-answering tasks. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Custom Judges

[Custom Judges](/concepts/custom-judges.md) created with the make_judge()|Make Judge API evaluate specific behavioral criteria, such as sentence count compliance. The judge returns a categorical value (e.g., `"correct"` or `"incorrect"`), which is converted to a numeric mean for compositing. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Workflow

Composite scoring follows the steps outlined in the comparative evaluation process: ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

1. Register multiple [prompt versions](/concepts/prompt-versioning.md) in the Unity Catalog prompt registry.
2. Create an evaluation dataset with expected facts and test cases.
3. Define scorers, including built-in metrics like `Correctness()` and custom judges for domain-specific criteria.
4. Run `mlflow.genai.evaluate()` for each prompt version against the same dataset with the same scorers.
5. Extract the mean metric values from each evaluation result.
6. Compute composite scores using a weighted combination of those means.
7. Select the version with the highest composite score for deployment.

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md
- Prompt Version Comparison – The broader process of evaluating and selecting prompt versions.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The framework for running evaluations.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – Structured test data with expected facts for comparison.
- Weighted Metrics – The general technique of combining metrics with different importance levels.
- [Prompt Registry](/concepts/prompt-registry.md) – Central repository for managing prompt versions.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Related technique for comparing complete agent setups.

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
