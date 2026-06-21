---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 57fcab7b36c300585878dcb3c07ed50f55bb2eaa92474484fb48847a2d067671
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-review-app-ui
    - CRAU
    - Custom Review App
    - code review
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
title: Custom Review App UI
description: An open-source deployable template for customizing the Review App frontend with specialized trace visualizations, tailored labeling interfaces, and domain-specific workflows
tags:
  - mlflow
  - customization
  - ui
  - databricks-apps
timestamp: "2026-06-18T14:38:36.487Z"
---

# Custom Review App UI

**Custom Review App UI** refers to a deployable, open-source frontend template that gives teams full control over the trace review and labeling interface used in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation workflows. While the built-in [MLflow Review App](/concepts/mlflow-review-app.md) provides a production-ready interface for standard evaluation, the custom template is designed for use cases requiring specialized trace visualization, tailored labeling interfaces, domain-specific layouts, or other UI customizations beyond what the default interface offers. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Overview

The Custom Review App UI is an open-source template that interacts with the same MLflow backend APIs and data model — including [Labeling Sessions](/concepts/labeling-sessions.md), [Labeling Schemas](/concepts/labeling-schemas.md), and [Assessments](/concepts/assessments.md) — as the built-in Review App. It differs by relinquishing control over the frontend experience to the developer, allowing modifications to the trace renderer, labeling interface layout, and information displayed to reviewers. The template repository includes command-line tools for programmatic setup as well as an AI assistant (Claude Code) for interactive customization. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

The customized Review App deploys as a Databricks App and integrates directly with your existing MLflow experiments and labeling sessions, preserving the existing data flow for feedback collection. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Use Cases

The custom template is ideal for teams that need any of the following:

- **Specialized trace renderers** for agent types not well represented by the default interface.
- **Custom labeling interface layouts and interactions**, such as multi-step review forms or inline annotations.
- **Domain-specific visualizations**, like showing domain-specific metadata or custom charts alongside traces.
- **Control over reviewer-visible information**, including hiding or highlighting specific trace fields to align with reviewer permissions or workflow requirements.

For standard evaluation workflows, the built-in Review App provides a production-ready solution without additional setup. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Features

- **Full frontend control** – The template exposes the UI code, enabling modifications to components such as the trace viewer, labeling form, and navigation.
- **Backend compatibility** – Uses the same MLflow APIs and data model as the built-in Review App, so existing labeling sessions, schemas, and assessments work without changes.
- **Deployment as a Databricks App** – The customized UI runs as a managed application within the Databricks environment, inheriting workspace authentication and permissions.
- **AI-assisted setup** – The repository provides both CLI commands and an optional Claude Code assistant to guide interactive customization. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Getting Started

The template is hosted on GitHub at [`databricks-solutions/custom-mlflow-review-app`](https://github.com/databricks-solutions/custom-mlflow-review-app). The repository documentation includes complete customization and deployment instructions. After cloning the template, you can:

1. Customize the trace rendering logic and labeling interface.
2. Deploy the application as a Databricks App.
3. Point the app to your existing MLflow experiment and labeling sessions.

The deployed app integrates with the same labeling sessions and schemas you already use with the built-in Review App. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Related Concepts

- [MLflow Review App](/concepts/mlflow-review-app.md) – The built-in, production-ready review interface for standard workflows.
- [Labeling Sessions](/concepts/labeling-sessions.md) – The organizational unit that groups traces for review.
- [Labeling Schemas](/concepts/labeling-schemas.md) – Definitions of the questions and input types used during labeling.
- [Assessments](/concepts/assessments.md) – The stored feedback objects attached to traces.
- Databricks App – The deployment target for the customized UI.
- Collect feedback and expectations by labeling existing traces – The overall workflow that both review apps support.

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
