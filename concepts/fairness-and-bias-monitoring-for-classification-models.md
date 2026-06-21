---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ce32ed2712d57441eb642102f79b801a1a72a788f54ed2760b6f4f94b0cc537a
  pageDirectory: concepts
  sources:
    - monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fairness-and-bias-monitoring-for-classification-models
    - Bias Monitoring for Classification Models and Fairness
    - FABMFCM
    - Fairness and Bias Statistics for Classification Models
    - Fairness and Bias Metrics
    - Fairness and Bias Statistics
    - Fairness and Bias in ML
    - Fairness and bias statistics
    - Monitor fairness and bias for classification models
    - Monitoring Fairness and Bias for Classification Models
  citations:
    - file: monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md
    - file: |-
        monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md

        For example
    - file: if you create a slicing expression `slicing_exprs=["age < 25"
title: Fairness and Bias Monitoring for Classification Models
description: Using data profiling to detect whether a classification model performs differently across demographic or protected groups
tags:
  - machine-learning
  - fairness
  - classification
  - monitoring
timestamp: "2026-06-19T19:46:36.133Z"
---

Here is the wiki page for **Fairness and Bias Monitoring for Classification Models**.

---

## Fairness and Bias Monitoring for Classification Models

**Fairness and Bias Monitoring for Classification Models** is a data profiling capability that allows you to continuously monitor the predictions of a classification model to determine if the model performs similarly across data associated with different demographic or behavioral groups. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

For example, a bank could use this monitoring to investigate whether a loan-default classifier generates the same false positive rate for applicants from different demographics. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

### How it Works

To monitor for fairness and bias, you create a Boolean slice expression. The group for which the slice expression evaluates to `True` is considered the **protected group** (the group being checked for bias). The group for which the expression evaluates to `False` is considered the **unprotected group**. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md

For example, if you create a slicing expression `slicing_exprs=["age < 25"]`, the slice with `slice_key` = "age < 25" and `slice_value` = `True` represents the protected group. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

### Metrics

The profile automatically computes metrics that compare the classification model's performance between the protected and unprotected groups. These metrics are stored in the [Profile Metrics Table](/concepts/profile-metrics-table.md) and reported as key-value pairs in a one-vs-all manner across all predicted classes. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

The following fairness metrics are computed:

- **Predictive Parity**: Compares the model's **precision** (positive predictive value) between groups. A high difference indicates that the model is more precise for one group than another. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]
- **Predictive Equality**: Compares the **false positive rate** between groups. A high difference indicates that one group receives more false alarms than the other. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]
- **Equal Opportunity**: Measures whether a label is predicted **equally well** for both groups. It compares the true positive rates between the protected and unprotected groups. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]
- **Statistical Parity**: Measures the **difference in predicted outcomes** between groups. It captures whether one group is more likely to receive a positive prediction than the other, regardless of the actual label. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

### Applicability

These metrics only apply when the analysis type is `InferenceLog` and the `problem_type` is `classification`. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

### Alerts

You can create an alert on these fairness and bias metrics. For instance, the owner of the model can set up an alert that triggers when a fairness metric exceeds a predefined threshold, and then route that alert to an on-call person or team for investigation. ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

### Definitions

For formal definitions of these fairness concepts, see:

- [Fairness (machine learning)](https://en.wikipedia.org/wiki/Fairness_\(machine_learning\)) on Wikipedia
- [Fairness Definitions Explained](http://fairware.cs.umass.edu/papers/Verma.pdf), by Verma and Rubin (2018) ^[monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md]

### Related Concepts

- [Inference Log Analysis](/concepts/inferencelog-analysis.md)
- Model Monitoring
- [Data Slicing](/concepts/data-slicing-expressions.md)
- [Drift Metrics Table](/concepts/drift-metrics-table.md)
- Classification Model

## Sources

- monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md

# Citations

1. [monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md](/references/monitor-fairness-and-bias-for-classification-models-databricks-on-aws-14705c6d.md)
2. monitor-fairness-and-bias-for-classification-models-databricks-on-aws.md

For example
3. if you create a slicing expression `slicing_exprs=["age < 25"
