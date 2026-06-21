---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea710f003ff9d0a2f664da18e98384de0301896d34e100c0bf42d652de629425
  pageDirectory: concepts
  sources:
    - machine-learning-lifecycle-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - staging-and-testing-ml-models
    - Testing ML Models and Staging
    - SATMM
  citations:
    - file: machine-learning-lifecycle-databricks-on-aws.md
title: Staging and Testing ML Models
description: The practice of testing model versions in staging with integration tests, A/B or shadow tests on production data, and stakeholder sign-off before promoting to production using model aliases.
tags:
  - machine-learning
  - mlops
  - testing
timestamp: "2026-06-19T19:20:38.212Z"
---

# Staging and Testing ML Models

**Staging and Testing ML Models** refers to the process of validating a trained model version under realistic conditions before promoting it to serve production traffic. This stage sits between model training and production deployment in the machine learning lifecycle, and is the point where a candidate model version is evaluated for readiness.

## Purpose

Staging and testing answers the question: *Is this model version ready for production?* After training, a model must be validated in an environment that mirrors production conditions to catch issues that might not appear during development. ^[machine-learning-lifecycle-databricks-on-aws.md]

## Key Activities

Before a new model version serves production traffic, test the version in staging under realistic conditions. The following activities are part of this stage:

- **Label the candidate model version with aliases.** Use aliases like `Staging` or `Production` to signal lifecycle state without renaming artifacts. ^[machine-learning-lifecycle-databricks-on-aws.md]
- **Run integration tests.** Confirm the serving endpoint starts, latency meets requirements, and outputs are well-formed. ^[machine-learning-lifecycle-databricks-on-aws.md]
- **Perform A/B or shadow tests.** Run the candidate against production data to validate performance before full cutover. ^[machine-learning-lifecycle-databricks-on-aws.md]
- **Collect stakeholder sign-off.** Gather approval from relevant stakeholders based on evaluation results. ^[machine-learning-lifecycle-databricks-on-aws.md]

## Model Registry and Version Management

After training an ML model or pipeline, register it to the [MLflow Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md) to simplify governance and management as you promote the model toward production. A registered model has versions, each of which links to the original training run that produced it. Model versions enable safe deployment workflows: you can test a new version in staging before promoting it to production, roll back to a previous version if quality degrades, and maintain a complete audit trail of what was deployed and when. ^[machine-learning-lifecycle-databricks-on-aws.md]

## Relationship to Other Stages

Staging and testing is the **sixth step** in the machine learning lifecycle, following evaluation (step 5) and preceding deployment to production (step 7). ^[machine-learning-lifecycle-databricks-on-aws.md]

The metrics defined during development and training can be reused later as metrics for [Production Monitoring](/concepts/production-monitoring.md). ^[machine-learning-lifecycle-databricks-on-aws.md]

## MLOps Context

This description oversimplifies deployment practices and ML operations (MLOps). For detailed production MLOps workflows, see MLOps workflows on Databricks. ^[machine-learning-lifecycle-databricks-on-aws.md]

## Related Concepts

- Model Lifecycle Management – The overall process of versioning and promoting models
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – The system that stores model versions with their provenance
- Production Deployment – The step following staging and testing
- A/B Testing – A technique for comparing candidate versions against production
- Shadow Testing – A deployment strategy that runs a new version in parallel without serving real traffic
- Model Versioning – The practice of tracking different iterations of a trained model

## Sources

- machine-learning-lifecycle-databricks-on-aws.md

# Citations

1. [machine-learning-lifecycle-databricks-on-aws.md](/references/machine-learning-lifecycle-databricks-on-aws-d195211f.md)
