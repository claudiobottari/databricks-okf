---
title: Monitor fairness and bias for classification models | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/fairness-bias
ingestedAt: "2026-06-18T08:04:20.357Z"
---

With data profiling, you can monitor the predictions of a classification model to see if the model performs similarly on data associated with different groups. For example, you can investigate whether a loan-default classifier generates the same false-positive rate for applicants from different demographics.

## Work with fairness and bias metrics[​](#work-with-fairness-and-bias-metrics "Direct link to Work with fairness and bias metrics")

To monitor for fairness and bias, create a Boolean slice expression. The group where the slice expression evaluates to `True` is the protected group (that is, the group you're checking for bias against). For example, if you create `slicing_exprs=[“age < 25”]`, the slice with `slice_key` = “age < 25” and `slice_value` = `True` is the protected group. The slice with `slice_value` = `False` is the unprotected group.

The profile automatically computes metrics that compare the performance of the classification model between groups. The profile metrics table reports the following metrics:

*   `predictive_parity`, which compares the model's precision between groups.
*   `predictive_equality`, which compares false positive rates between groups.
*   `equal_opportunity`, which measures whether a label is predicted equally well for both groups.
*   `statistical_parity`, which measures the difference in predicted outcomes between groups.

note

These metrics apply only when the analysis type is `InferenceLog` and `problem_type` is `classification`.

For definitions of these metrics, see the following references:

*   [Fairness (machine learning)](https://en.wikipedia.org/wiki/Fairness_\(machine_learning\)) Wikipedia article about fairness in machine learning
*   [Fairness Definitions Explained, Verma and Rubin, 2018](http://fairware.cs.umass.edu/papers/Verma.pdf)

## Fairness and bias metrics outputs[​](#fairness-and-bias-metrics-outputs "Direct link to Fairness and bias metrics outputs")

See the [API reference](https://api-docs.databricks.com/python/lakehouse-monitoring/latest/index.html) for details about these metrics and how to view them in the metric tables. All fairness and bias metrics share the same data type, with fairness scores computed across all predicted classes in a _one-vs-all_ manner as key-value pairs.

You can create an alert on these metrics. For instance, the owner of the model can set up an alert when the fairness metric exceeds some threshold and then route that alert to an on-call person or team for investigation.
