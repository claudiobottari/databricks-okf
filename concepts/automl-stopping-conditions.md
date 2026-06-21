---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8cd1d2efa596d9beab0032ddc1145bbb044d3af2e2f3009b073cbc668de89098
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
    - regression-with-automl-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - automl-stopping-conditions
    - ASC
  citations:
    - file: classification-with-automl-databricks-on-aws.md
    - file: regression-with-automl-databricks-on-aws.md
title: AutoML Stopping Conditions
description: Default stopping conditions for AutoML experiments including time limits, trial limits, and early stopping based on validation metric improvement
tags:
  - databricks
  - automl
  - optimization
timestamp: "2026-06-19T17:43:44.727Z"
---



# AutoML Stopping Conditions

**AutoML Stopping Conditions** are configurable parameters that control when an AutoML experiment stops training and tuning models. They help manage experiment duration, computational resource consumption, and final model quality by defining limits on the maximum runtime, the maximum number of trials, or by triggering early termination when the validation metric ceases to improve.

## Default Stopping Conditions

Default stopping conditions vary by problem type and Databricks Runtime version. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md]

For **forecasting** experiments, AutoML stops after **120 minutes** regardless of runtime version. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md]

For **classification** and **regression** experiments in Databricks Runtime 10.4 LTS ML and below, AutoML stops after **60 minutes** or after completing **200 trials**, whichever occurs first. For Databricks Runtime 11.0 ML and above, the number of trials is not used as a stopping condition. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md]

## Early Stopping

In Databricks Runtime 10.4 LTS ML and above, for classification and regression experiments, AutoML incorporates **early stopping**. This halts training and tuning of models if the validation metric is no longer improving. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md]

Early stopping helps avoid overfitting and reduces unnecessary computation and experiment runtime.

## Configuring Stopping Conditions

Stopping conditions can be edited when setting up an AutoML experiment. On the **Configure AutoML experiment** page, open the **Advanced Configuration (optional)** section to access and modify the stopping conditions. ^[classification-with-automl-databricks-on-aws.md, regression-with-automl-databricks-on-aws.md]

You can adjust the maximum duration (in minutes) and, where applicable, the maximum number of trials. For production or resource-constrained environments, setting tighter limits helps control costs.

## Related Concepts

- AutoML — The automated machine learning framework that uses these stopping conditions
- [AutoML Experiment Configuration](/concepts/automl-experiment-configuration.md) — How to set up and configure AutoML experiments
- Early Stopping — A technique that halts training when validation metrics stop improving
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — The process that AutoML governs via stopping conditions
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The runtime environment that supports AutoML

## Sources

- classification-with-automl-databricks-on-aws.md
- regression-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
2. [regression-with-automl-databricks-on-aws.md](/references/regression-with-automl-databricks-on-aws-cc5aa3d0.md)
