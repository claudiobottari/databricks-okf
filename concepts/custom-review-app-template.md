---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d7b3fdb5b9f7353c63ae766a959b40571b743612426e2865441e497666414e23
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-review-app-template
    - CRAT
    - Review App Template
    - customizable-review-app-template
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
title: Custom Review App Template
description: An open-source, customizable frontend template for the MLflow Review App that allows teams to build tailored trace visualization, labeling interfaces, and workflows while using the same MLflow backend APIs.
tags:
  - mlflow
  - customization
  - frontend
timestamp: "2026-06-19T17:45:54.116Z"
---

# Custom Review App Template

The **Custom Review App Template** is an open-source, customizable frontend for the [MLflow Review App](/concepts/mlflow-review-app.md) that enables teams to tailor the trace review and labeling experience for their specific GenAI application needs. It provides full control over the user interface while using the same MLflow backend APIs and data model, including [Labeling Sessions](/concepts/labeling-sessions.md), [Labeling Schemas](/concepts/labeling-schemas.md), and assessments.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Overview

The Custom Review App Template is designed for teams that require custom trace visualization, evaluation workflows, or specific UI requirements beyond the standard Review App interface. For standard evaluation workflows, the built-in Review App provides a production-ready solution without additional setup.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

The template is available on GitHub at `github.com/databricks-solutions/custom-mlflow-review-app`. It includes command-line tools for programmatic setup and supports interactive customization through an AI assistant such as Claude Code.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Customization Options

The template offers several areas for customization:^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

- **Specialized trace renderers**: Customize how different agent types are visualized for reviewers
- **Custom labeling interface layouts and interactions**: Design the arrangement and behavior of labeling controls
- **Domain-specific visualizations**: Add visual elements tailored to particular use cases or industries
- **Reviewer information control**: Choose which trace information is displayed to reviewers

## Deployment

The customized Review App deploys as a Databricks App and integrates directly with existing MLflow experiments and labeling sessions. Complete customization and deployment instructions are provided in the template repository documentation.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Related Concepts

- [MLflow Review App](/concepts/mlflow-review-app.md) — The standard, built-in review interface for trace labeling
- [Labeling Sessions](/concepts/labeling-sessions.md) — Organizational units that group traces for review
- [Labeling Schemas](/concepts/labeling-schemas.md) — Definitions of questions and input types for expert feedback
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for quality assessment
- [Domain Expert Feedback](/concepts/mlflow-review-app-for-domain-expert-feedback.md) — Collecting human expertise on GenAI application outputs
- Databricks Apps — The deployment platform for the customized template

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
