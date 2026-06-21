---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6dc0206d15dac474e3518eda32ac542537c7b2a42714373f98d7d14e1b5d4bd1
  pageDirectory: concepts
  sources:
    - profile-alerts-databricks-on-aws.md
  confidence: 0.75
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inferencelog-analysis-for-model-retraining
    - IAFMR
  citations:
    - file: profile-alerts-databricks-on-aws.md
title: InferenceLog Analysis for Model Retraining
description: Using drift metrics detected via profile alerts on inference logs to determine when a machine learning model should be retrained.
tags:
  - databricks
  - machine-learning
  - drift-detection
  - model-monitoring
timestamp: "2026-06-19T19:58:17.359Z"
---

# InferenceLog Analysis for Model Retraining

**InferenceLog Analysis for Model Retraining** is a monitoring practice that uses [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) on profile metric tables to detect when a deployed model’s input or output data has drifted sufficiently to warrant retraining. This approach is part of the broader [Data Profiling](/concepts/data-profiling.md) capabilities in Unity Catalog.

## Overview

When a model is in production, its prediction logs (the inference log) can be continuously analyzed for changes in data distribution. If the distribution of new data deviates from the [Baseline Table](/concepts/baseline-table.md) — the reference dataset used during model validation — the model’s accuracy may degrade. Setting up a profile alert on the [Drift Metrics Table](/concepts/drift-metrics-table.md) allows teams to be notified automatically when such drift occurs. For `InferenceLog` analysis specifically, the alert can be configured not only to investigate the changes but also to **indicate that the model should be retrained**. ^[profile-alerts-databricks-on-aws.md]

## How Alerts Work

Profile alerts are created and used the same way as other Databricks SQL alerts. The process is:

1. Create a Databricks SQL query against the profile metrics table or drift metrics table.
2. Create a [Databricks SQL alert](/concepts/databricks-sql-alerts.md) for that query.
3. Configure the alert to evaluate at a desired frequency and send notifications (email, webhook, Slack, PagerDuty, etc.).

If the query uses parameters, the alert evaluates those parameters on their default values. The default values should reflect the intended alert conditions. ^[profile-alerts-databricks-on-aws.md]

## Triggering Model Retraining

A common use case for profile alerts is to detect when the fraction of missing values exceeds a certain threshold or when distribution drift (compared to the baseline table) becomes significant. For `InferenceLog` analysis, the recommended action upon alert is to trigger a model retraining pipeline. The alert itself does not automatically retrain the model, but it serves as the operational signal to begin the retraining process. ^[profile-alerts-databricks-on-aws.md]

## Related Concepts

- Data Drift – Changes in the statistical properties of model inputs.
- [Baseline Table](/concepts/baseline-table.md) – Reference dataset used to compute drift metrics.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores summary statistics for each column, window, and slice.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Stores statistics tracking distribution changes over time.
- Model Retraining – The process of updating a model with new data.
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) – Mechanism for notifying users when a query condition is met.

## Sources

- profile-alerts-databricks-on-aws.md

# Citations

1. [profile-alerts-databricks-on-aws.md](/references/profile-alerts-databricks-on-aws-08d2e777.md)
