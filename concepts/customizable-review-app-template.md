---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c1079c22288c1fecca681b1cf7c326137f3a9d1b552a0ba39c6c8c92f59adec7
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customizable-review-app-template
    - CRAT
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
title: Customizable Review App Template
description: An open-source, deployable template that provides full frontend control over trace visualization, labeling interfaces, and workflows while using the same MLflow backend APIs and data model.
tags:
  - mlflow
  - customization
  - deployment
  - databricks-apps
timestamp: "2026-06-19T09:16:40.415Z"
---

---
title: Customizable Review App Template
summary: An open-source template for deploying a customized version of the MLflow Review App, giving full control over trace visualization, labeling interfaces, and evaluation workflows while using the same MLflow backend APIs and data model.
sources:
  - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:00:00.000Z"
updatedAt: "2026-06-18T14:00:00.000Z"
tags:
  - mlflow
  - review-app
  - customization
  - frontend
aliases:
  - custom-review-app-template
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Customizable Review App Template

The **Customizable Review App Template** is an open-source project that allows you to deploy a custom frontend for the [MLflow Review App](/concepts/mlflow-review-app.md), giving you full control over the user experience while leveraging the same MLflow backend APIs and data model (labeling sessions, labeling schemas, and assessments). It is designed for use cases that require specialized trace visualization, tailored labeling interfaces, or specific evaluation workflows beyond the standard Review App interface.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Overview

The standard MLflow Review App provides a production-ready interface for collecting expert feedback on GenAI traces. When you need to customize trace rendering, labeling layouts, or domain-specific visualizations, the Customizable Review App Template lets you build and deploy your own frontend without reworking the backend. The template uses the same MLflow APIs and data model, so all existing labeling sessions, schemas, and assessments remain compatible.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Features

The template offers several customization capabilities:

- **Specialized trace renderers** – Display traces in a way that matches your application architecture (e.g., agent flows, multi-step chains).
- **Custom labeling interface layouts** – Rearrange input fields, use different input types, or add interactive elements beyond the default categorical choices, numeric scales, and free‑form text.
- **Domain‑specific visualizations** – Incorporate charts, tables, or custom media relevant to your domain.
- **Control over trace visibility** – Decide exactly which trace information (inputs, outputs, intermediate spans, metadata) is shown to reviewers.

These customizations are built on the same backend APIs that power the standard Review App.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Deployment

The customized Review App deploys as a Databricks App and integrates directly with your existing MLflow experiments and labeling sessions. The template repository includes two approaches for setup:

- **Command‑line tools** for programmatic setup and deployment.
- **AI assistant (Claude Code)** for interactive customization through a guided workflow.

For full instructions, see the template repository: [GitHub – databricks-solutions/custom-mlflow-review-app](https://github.com/databricks-solutions/custom-mlflow-review-app). The repository documentation also covers configuration of authentication, branding, and the specific UI components you wish to modify.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## When to Use the Customizable Template

The customizable template is ideal for teams that need custom trace visualization, evaluation workflows, or specific UI requirements that go beyond what the standard Review App provides. For typical evaluation workflows – such as collecting feedback on standard LLM conversations or simple RAG traces – the built‑in Review App is a production‑ready solution that requires no additional setup.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Related Concepts

- [MLflow Review App](/concepts/mlflow-review-app.md) – The standard interface for collecting expert feedback on traces.
- [Labeling Sessions](/concepts/labeling-sessions.md) – The organizing run that groups traces for review.
- [Labeling Schemas](/concepts/labeling-schemas.md) – The question and input definitions used to collect feedback.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The instrumentation framework that produces the traces reviewed in the app.
- Databricks Apps – The deployment target for the customized frontend.

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
