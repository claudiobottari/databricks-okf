---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ae461f52d79b844229577d37fb2e1c865268a5cffd314fd163d569c0587571d6
  pageDirectory: concepts
  sources:
    - monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - predictive-parity
  citations:
    - file: monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
title: Predictive Parity
description: A fairness metric that compares the model's precision (positive predictive value) between protected and unprotected groups
tags:
  - machine-learning
  - fairness
  - metrics
timestamp: "2026-06-19T19:45:53.015Z"
---

# Predictive Parity

**Predictive Parity** is a fairness metric used in classification models to assess whether a model's precision is comparable across different demographic groups. It is one of several bias monitoring metrics automatically computed by Databricks data profiling when analyzing inference logs for classification problems. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Definition

Predictive parity compares the model's precision between a protected group and an unprotected group. Precision, also known as positive predictive value, measures the proportion of positive predictions that are actually correct. Predictive parity is satisfied when the precision is approximately equal across groups — meaning that when the model predicts a positive outcome, it is equally likely to be correct regardless of group membership. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Computation

Predictive parity is computed as part of the [Fairness and Bias Metrics](/concepts/fairness-and-bias-monitoring-for-classification-models.md) suite when the analysis type is `InferenceLog` and the `problem_type` is `classification`. The metric is calculated by comparing precision between:

- The **protected group**: where a Boolean slice expression evaluates to `True`
- The **unprotected group**: where the same slice expression evaluates to `False`

For example, if you define `slicing_exprs=["age < 25"]`, the system compares the precision of predictions for applicants under age 25 against those 25 and older. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Output Format

Fairness scores for predictive parity are computed across all predicted classes in a **one-vs-all** manner and stored as key-value pairs in the [Profile Metrics Table](/concepts/profile-metrics-table.md). All fairness and bias metrics share a common data type format. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Related Metrics

Predictive parity is one of four fairness metrics automatically computed during classification inference log analysis:

- **[Predictive Equality](/concepts/predictive-equality.md)** — compares false positive rates between groups
- **[Equal Opportunity](/concepts/equal-opportunity.md)** — measures whether a label is predicted equally well for both groups
- **[Statistical Parity](/concepts/statistical-parity.md)** — measures the difference in predicted outcomes between groups

## Usage

Model owners can set up alerts on predictive parity metrics. If the fairness metric exceeds a defined threshold, the alert can be routed to an on-call person or team for investigation. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## References

For formal definitions, see the Wikipedia article on Fairness (machine learning) and the paper "Fairness Definitions Explained" by Verma and Rubin (2018). ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

## Related Concepts

- Classification Model Monitoring
- [Inference Log Analysis](/concepts/inferencelog-analysis.md)
- Bias Detection
- Protected Group
- [Slicing Expressions](/concepts/data-slicing-expressions.md)

## Sources

- monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md

# Citations

1. [monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md](/references/monitor-fairness-and-bias-for-classification-models-databricks-on-aws-14705c6d.md)
