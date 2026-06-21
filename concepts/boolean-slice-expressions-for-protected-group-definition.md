---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: acf4d91a7a79540f95832aa00c6cb441c886ccaa73ffa536eedeaef219a95d55
  pageDirectory: concepts
  sources:
    - monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - boolean-slice-expressions-for-protected-group-definition
    - BSEFPGD
  citations:
    - file: monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
title: Boolean Slice Expressions for Protected Group Definition
description: A technique for defining protected and unprotected groups in fairness analysis using Boolean expressions that partition data into slices
tags:
  - machine-learning
  - fairness
  - data-profiling
timestamp: "2026-06-19T19:45:56.356Z"
---

# Boolean Slice Expressions for Protected Group Definition

**Boolean Slice Expressions for Protected Group Definition** is a mechanism used in [Data Profiling](/concepts/data-profiling.md) on Databricks to define a *protected group* for fairness and bias monitoring of classification models. By specifying a Boolean slice expression, the system separates the data into two groups: the group where the expression evaluates to `True` (the protected group) and the group where it evaluates to `False` (the unprotected group). The profile then automatically computes fairness metrics that compare the model’s performance between these two groups. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## How It Works

When creating a profile for an [InferenceLog Analysis](/concepts/inferencelog-analysis.md) with `problem_type` set to `classification`, you supply one or more `slicing_exprs`. Each slice expression is a Boolean condition, such as `"age < 25"`. For each such expression, the system produces two slices:

- **`slice_key`** = `"age < 25"`, **`slice_value`** = `True` → the protected group.
- **`slice_key`** = `"age < 25"`, **`slice_value`** = `False` → the unprotected group.

The profile compares model performance metrics (e.g., false‑positive rates) between these two groups to detect potential bias. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Computed Fairness Metrics

The profile metrics table reports the following fairness metrics for each protected/unprotected group pair. All metrics are computed in a *one‑vs‑all* manner across all predicted classes and stored as key‑value pairs. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

| Metric | Description |
|--------|-------------|
| **predictive_parity** | Compares precision (positive predictive value) between the protected and unprotected groups. |
| **predictive_equality** | Compares false positive rate between the groups. |
| **equal_opportunity** | Measures whether a label is predicted equally well for both groups (true positive rate parity). |
| **statistical_parity** | Measures the difference in predicted outcome rates between groups (demographic parity). |

These metrics apply only when the analysis type is `InferenceLog` and `problem_type` is `classification`. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Example

For a loan‑default classifier, you could define:

```python
slicing_exprs = ["age < 25"]
```

The profile then compares, for example, the false‑positive rate for applicants under 25 (protected group) with that for applicants 25 and older (unprotected group), reporting `predictive_equality`. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Usage Notes

- You can create alerts on fairness metrics, e.g., notify an on‑call team when a metric exceeds a threshold. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]
- The slice expression can reference any column in the inference log table.
- For detailed API reference and output schema, see the [Lakehouse Monitoring API documentation](https://api-docs.databricks.com/python/lakehouse-monitoring/latest/index.html). ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md)
- [Inference Log Analysis](/concepts/inferencelog-analysis.md)
- Classification Models
- [Data Slicing](/concepts/data-slicing-expressions.md)
- Fairness and Bias Monitoring
- [Profile Metrics Table](/concepts/profile-metrics-table.md)
- [Predictive Parity](/concepts/predictive-parity.md)
- [Predictive Equality](/concepts/predictive-equality.md)
- [Equal Opportunity](/concepts/equal-opportunity.md)
- [Statistical Parity](/concepts/statistical-parity.md)

## Sources

- monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md

# Citations

1. [monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md](/references/monitor-fairness-and-bias-for-classification-models-databricks-on-aws-14705c6d.md)
