---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c4e783d1bf46ed74b5a3f01c04f1134e7a83605485ea1486336df331ffcd7c01
  pageDirectory: concepts
  sources:
    - model-serving-limits-and-regions-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automated-container-compliance-rebuilding
    - ACCR
  citations:
    - file: model-serving-limits-and-regions-databricks-on-aws.md
title: Automated Container Compliance Rebuilding
description: Databricks automatically rebuilds outdated served containers within 30 days to maintain compliance, with event log alerts when the automated job fails.
tags:
  - model-serving
  - compliance
  - automation
  - databricks
timestamp: "2026-06-19T19:43:58.273Z"
---

# Automated Container Compliance Rebuilding

**Automated Container Compliance Rebuilding** is a Databricks feature that automatically rebuilds model serving containers to ensure they remain compliant with the most recent compliance security profile standards. This process is required for both CPU/GPU workloads and Foundation Model APIs workloads (including provisioned throughput, pay-per-token, and batch inference). ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Purpose

Compliance security profile standards require that served containers be built **within the most recent 30 days**. To meet this requirement, Databricks automatically rebuilds outdated containers on behalf of the user. This ensures that deployed model containers are always based on current, patched images that satisfy the latest compliance requirements. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Failure Handling

If the automated rebuild job fails, Databricks generates an event log message that provides guidance. The message states:

> "Databricks couldn't complete a scheduled compliance check for model $servedModelName. This can happen if the system can't apply a required update. To resolve, try relogging your model. If the issue persists, contact support@databricks.com."

^[model-serving-limits-and-regions-databricks-on-aws.md]

The recommended action is to **re‑log the model** (i.e., create a new model version) to trigger a fresh container build with the latest patches. If the problem persists, users should contact Databricks support. ^[model-serving-limits-and-regions-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The overall serving infrastructure that uses these containers.
- [Compliance Security Profile](/concepts/compliance-security-profile-databricks-on-aws.md) – The set of standards requiring up‑to‑date containers.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – One of the workload types subject to this automatic rebuilding.
- Custom Models and AI Agents – The other workload types that require compliance rebuilding.

## Sources

- model-serving-limits-and-regions-databricks-on-aws.md

# Citations

1. [model-serving-limits-and-regions-databricks-on-aws.md](/references/model-serving-limits-and-regions-databricks-on-aws-f386cb0e.md)
