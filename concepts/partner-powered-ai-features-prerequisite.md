---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 91009cdd80f81608d69c1dc9a3284f961896e22e0f38e36cc6b0ab5010fc8fd9
  pageDirectory: concepts
  sources:
    - model-serving-observability-with-genie-code-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partner-powered-ai-features-prerequisite
    - PAFP
  citations:
    - file: model-serving-observability-with-genie-code-databricks-on-aws.md
title: Partner-powered AI Features Prerequisite
description: Requirement that both the account and workspace must have partner-powered AI features enabled for Genie Code to function.
tags:
  - prerequisites
  - configuration
  - databricks
timestamp: "2026-06-19T19:44:16.156Z"
---

## Partner-powered AI Features Prerequisite

The **Partner-powered AI Features Prerequisite** is a workspace-level and account-level configuration requirement that must be met before certain Databricks AI features can be used. The most prominent example is [Genie Code for Model Serving Observability](/concepts/genie-code-for-model-serving-observability.md), which requires that Partner‑powered AI features are enabled for **both the account and the workspace**. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### Scope

This prerequisite applies to features that rely on Databricks’ partner‑powered AI infrastructure. If the feature is not enabled on the account, or is not enabled on the specific workspace, the dependent functionality (such as Genie Code’s endpoint diagnostics) will be unavailable. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### How to enable

Partner‑powered AI features are configured at the account level and then selectively enabled per workspace. For detailed instructions, see the Partner‑powered AI features documentation(https://docs.databricks.com/aws/en/databricks-ai/partner-powered) (external link). The referenced source directs readers to that documentation for step‑by‑step guidance. ^[model-serving-observability-with-genie-code-databricks-on-aws.md]

### Related concepts

- [Genie Code](/concepts/genie-code.md) – The AI assistant that requires this prerequisite for model serving observability.
- [Model Serving](/concepts/model-serving.md) – The service where Genie Code acts as an observability companion.
- [Designated Services](/concepts/databricks-designated-service-with-geos.md) – Geos and data residency considerations that may also apply to Genie Code.

### Sources

- model-serving-observability-with-genie-code-databricks-on-aws.md

# Citations

1. [model-serving-observability-with-genie-code-databricks-on-aws.md](/references/model-serving-observability-with-genie-code-databricks-on-aws-64add48f.md)
