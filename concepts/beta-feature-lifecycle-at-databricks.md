---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 89c21c38b61231aef7737a9efd3b2e883c6a79a6faa225c0eb2a850e0222c2c4
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - beta-feature-lifecycle-at-databricks
    - BFLAD
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Beta Feature Lifecycle at Databricks
description: The Beta release stage for Databricks features, indicating the AI Runtime CLI is not yet GA and may have limited availability.
tags:
  - databricks
  - release-management
  - beta
timestamp: "2026-06-18T14:21:46.504Z"
---

# Beta Feature Lifecycle at Databricks

**Beta Feature Lifecycle at Databricks** refers to the practice of releasing certain features in a Beta stage before they become generally available (GA). Beta features are functional but may have limitations, and their APIs and behavior are subject to change.

## Currently Documented Beta Features

The following features are explicitly identified as Beta in the provided documentation:

* [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The `air` command-line interface is in Beta. It submits and manages distributed training workloads on AI Runtime using YAML-based job configuration. ^[ai-runtime-cli-databricks-on-aws.md]
* [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based access control policies in Unity Catalog that dynamically grant privileges based on governed tags. GRANT policies are currently in Beta. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Characteristics of Beta Features

Based on the documentation, Beta features often have limited scope. For example:

* **ABAC GRANT policies** support only the `EXECUTE` privilege on models (both customer-registered MLflow models and foundation models in `system.ai`). Additional privileges and securable types are planned for future releases. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
* **GRANT policies** cannot be used with [Delta Sharing](/concepts/delta-sharing.md) for models that have policies defined on them. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

The AI Runtime CLI documentation does not enumerate specific limitations beyond the Beta label, but the Beta status implies that users should expect potential changes before GA. ^[ai-runtime-cli-databricks-on-aws.md]

## Identifying Beta Features in Documentation

Beta features are typically labeled with a **Beta** badge at the top of the page (e.g., AI Runtime CLI) or explicitly stated in the text (e.g., “GRANT policies are currently in Beta”). ^[ai-runtime-cli-databricks-on-aws.md, abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

* [AI Runtime CLI](/concepts/ai-runtime-cli.md) — A Beta CLI for distributed GPU training workloads.
* [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — A Beta access control feature in Unity Catalog.
* Release Types — The general release lifecycle at Databricks.
* [Unity Catalog](/concepts/unity-catalog.md) — The governance platform where ABAC policies are applied.

## Sources

* ai-runtime-cli-databricks-on-aws.md
* abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
