---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1cf90c2cfcbf1596e28f421738ea08ad3146a9314aaeb12a27ff9775223a0e27
  pageDirectory: concepts
  sources:
    - mlops-workflows-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ml-model-monitoring-and-automated-retraining
    - Automated Retraining and ML Model Monitoring
    - MMMAAR
  citations:
    - file: mlops-workflows-on-databricks-databricks-on-aws.md
title: ML Model Monitoring and Automated Retraining
description: The practice of profiling input data and model predictions for drift and performance, publishing metrics to dashboards, setting up alerts, and triggering automated retraining cycles via scheduled or event-driven jobs.
tags:
  - mlops
  - monitoring
  - retraining
  - automation
timestamp: "2026-06-19T19:42:37.227Z"
---

# ML Model Monitoring and Automated Retraining

**ML Model Monitoring and Automated Retraining** is a critical MLOps practice that tracks the performance, stability, and behavior of machine learning models in production, and automatically triggers retraining when performance degrades or data distributions shift. This process ensures that deployed models continue to deliver accurate predictions over time as real-world conditions change. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Overview

Model monitoring and automated retraining form the core of production-stage MLOps. After a model is deployed to production, it must be continuously observed to detect [data drift](/concepts/data-drift-detection.md), concept drift, and performance degradation. When these issues are identified, the system can automatically initiate retraining to restore model quality. This lifecycle is managed through databricks workflows that connect monitoring outputs to training pipeline triggers. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Monitoring Components

Production monitoring covers several key dimensions:

### Data Ingestion
The monitoring pipeline reads logs from batch, streaming, or online inference endpoints. These logs contain both input data and model predictions that form the basis for all subsequent analysis. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Accuracy and Drift Detection
The pipeline computes metrics about:
- **Input data distributions** - changes in the statistical properties of incoming features
- **Model predictions** - shifts in prediction behavior or output distributions
- **Infrastructure performance** - latency, throughput, and system health

Data scientists specify data and model metrics during development, while ML engineers define infrastructure metrics. Custom metrics can also be defined to address specific business or regulatory requirements. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Metric Publication and Alerting
The monitoring pipeline writes results to tables in the production catalog for analysis and reporting. These tables should be configured as readable from the development environment so data scientists have access for investigation. Databricks SQL can be used to create monitoring dashboards that track model performance over time. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Data Profiling

[Data Profiling](/concepts/data-profiling.md) is a built-in capability that monitors statistical properties of input data and model predictions. It tracks:
- [Data drift](/concepts/data-drift-detection.md) - changes in the distribution of input features over time
- Model performance - accuracy, precision, recall, or other business-relevant metrics

Alerts can be created based on these metrics, and they can be published in dashboards for real-time visibility. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Retraining Strategies

The architecture supports two complementary retraining approaches, with Databricks recommending a progressive strategy:

### Scheduled Retraining (Recommended Starting Point)
If new data is available on a regular basis, create a scheduled job to run the model training code on the latest available data. This approach is simpler to implement and provides predictable model updates. See automate jobs with schedules and triggers. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Triggered Retraining (Advanced)
When the monitoring pipeline can identify model performance issues and send alerts, it can also trigger retraining. Common triggers include:
- **Significant data distribution changes** - when input data drift exceeds a threshold
- **Model performance degradation** - when accuracy or quality metrics fall below acceptable levels

Automatic retraining and redeployment can boost model performance with minimal human intervention when these conditions are detected. This can be achieved through a SQL alert that checks whether a metric is anomalous (for example, comparing drift or model quality against a defined threshold). The alert can be configured to use a webhook destination, which subsequently triggers the training workflow. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Alert-Triggered Retraining Workflow

The alert-to-retraining pipeline follows this pattern:

1. **Monitoring detects anomaly** - The data profiling pipeline identifies that a metric (such as drift magnitude or model quality score) exceeds a predefined threshold
2. **SQL alert fires** - A Databricks SQL alert checks the metric against the threshold and triggers when anomalous conditions are detected
3. **Alert sends webhook** - The notification is delivered to a webhook destination
4. **Webhook triggers training workflow** - The training pipeline receives the trigger and begins retraining on current data
5. **New model is validated and deployed** - The standard production validation and deployment pipeline runs

## Handling Retraining Issues

If the retraining pipeline or other monitoring/deployment pipelines exhibit performance issues, the data scientist may need to return to the development environment for additional experimentation. In this case, production models fall back to their last-known-good state while investigation proceeds. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Related Concepts

- MLOps workflows - The complete lifecycle that monitoring and retraining are part of
- [Data Profiling](/concepts/data-profiling.md) - The statistical analysis used to detect drift and performance issues
- Model deployment - The process that follows successful retraining
- [Drift Metrics Table](/concepts/drift-metrics-table.md) - Stores statistics tracking distribution changes over time
- [Inference log analysis](/concepts/inferencelog-analysis.md) - A profile type for monitoring model predictions and accuracy
- [Production Monitoring](/concepts/production-monitoring.md) - The broader context of managing deployed models

## Sources

- mlops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [mlops-workflows-on-databricks-databricks-on-aws.md](/references/mlops-workflows-on-databricks-databricks-on-aws-a1b056b9.md)
