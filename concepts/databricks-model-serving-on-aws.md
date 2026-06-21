---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 74ff803cee827db643aabf1f08f8fb9a27144361fd2d45ca918492274bc5e4c6
  pageDirectory: concepts
  sources:
    - applicable-model-terms-databricks-on-aws.md
  confidence: 0.4
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-model-serving-on-aws
    - DMSOA
  citations:
    - file: applicable-model-terms-databricks-on-aws.md
title: Databricks Model Serving on AWS
description: A Databricks platform service for deploying and serving machine learning models on AWS infrastructure.
tags:
  - databricks
  - machine-learning
  - aws
  - model-serving
timestamp: "2026-06-19T22:07:17.750Z"
---

Here is the wiki page for **Databricks Model Serving on AWS**, based solely on the provided source material.

---

# Databricks Model Serving on AWS

**Databricks Model Serving** on AWS is a managed infrastructure service for deploying, serving, and monitoring machine learning models in production. This page covers the acceptable use policies that apply to models served through this service on AWS infrastructure, as defined in Databricks' acceptable use terms for models. ^[applicable-model-terms-databricks-on-aws.md]

## Acceptable Use Policies

When using Model Serving on AWS, you must comply with Databricks' applicable model terms. These terms govern acceptable use of models served on the platform and apply to all models — whether customer-registered MLflow Models or Databricks-hosted foundation models accessed through [Foundation Model APIs](/concepts/foundation-model-apis.md). ^[applicable-model-terms-databricks-on-aws.md]

### Prohibited Use Cases

You may not serve models on Databricks on AWS for certain high-risk or regulated activities unless you have explicit approval from Databricks. Prohibited uses include deploying models for automated decision-making in areas such as credit, employment, housing, or healthcare that could lead to unlawful discrimination or other prohibited outcomes. ^[applicable-model-terms-databricks-on-aws.md]

### Content Safeguards

Models served on AWS must not be used to generate, distribute, or facilitate harmful content, including hate speech, harassment, violence, or sexually explicit material. ^[applicable-model-terms-databricks-on-aws.md]

### Compliance with AWS Terms

All model serving activities on Databricks on AWS are additionally subject to the underlying AWS Acceptable Use Policy and any other service-specific terms that apply. You are responsible for ensuring that your model inputs, outputs, and usage patterns comply with these AWS policies. ^[applicable-model-terms-databricks-on-aws.md]

## Enforcement

Databricks may suspend or terminate model serving for accounts that violate these acceptable use policies. Determinations of prohibited use are at Databricks' sole discretion. ^[applicable-model-terms-databricks-on-aws.md]

## Related Concepts

- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) — Core documentation for the model serving infrastructure
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks-hosted endpoints for foundation models accessed through Model Serving
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer that can be used to track model metadata and access
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based access control for model serving policies
- [AI Governance with Unity Catalog](/concepts/ai-governance-with-unity-catalog.md) — Broader framework for governing AI assets on Databricks

## Sources

- applicable-model-terms-databricks-on-aws.md

# Citations

1. [applicable-model-terms-databricks-on-aws.md](/references/applicable-model-terms-databricks-on-aws-2e13c689.md)
