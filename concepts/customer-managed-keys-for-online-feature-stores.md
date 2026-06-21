---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e86acc3adc07b4b38915971c20fa95a6d7386ec9dc7423e07772751c60bb3f93
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customer-managed-keys-for-online-feature-stores
    - CKFOFS
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Customer-Managed Keys for Online Feature Stores
description: Encryption at rest support using customer-managed keys (CMK) via underlying Lakebase Autoscaling, requiring specific workspace and regional prerequisites.
tags:
  - security
  - encryption
  - compliance
timestamp: "2026-06-19T18:14:09.597Z"
---

# Customer-Managed Keys for Online Feature Stores

**Customer-Managed Keys (CMK) for Online Feature Stores** provide encryption at rest for feature data stored in Databricks Online Feature Stores, using encryption keys that you control rather than Databricks-managed keys. This capability is enabled by the underlying support for CMK in [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) projects. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Overview

Online feature stores support encryption at rest with a customer-managed key due to underlying support from Lakebase Autoscaling. No Lakebase or Feature Store configuration is required; CMK applies automatically for relevant workspaces. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Requirements for Automatic CMK Application

CMK applies automatically when all of the following conditions are true: ^[databricks-online-feature-stores-databricks-on-aws.md]

1. **Workspace CMK configuration**: The workspace has a customer-managed key configured for managed services. See Customer-managed keys for Lakebase.
2. **Lakebase Autoscaling backing**: The online feature store is backed by a Lakebase Autoscaling project. All online feature stores created with `fe.create_online_store` after March 23, 2026 use Lakebase Autoscaling.
3. **Project creation timing**: The backing Lakebase project was created after CMK support became available in your region. Lakebase projects created before that are not encrypted with a CMK even if the workspace later enables one.

## Verifying CMK Encryption

The Lakebase project backing an online feature store has the same name as the online store. To verify encryption status: ^[databricks-online-feature-stores-databricks-on-aws.md]

1. Click the apps switcher icon in the top right corner of your workspace to open the Lakebase App.
2. Locate the project with the same name as your online store.
3. Check the **Customer-managed keys** status card on that project to confirm the store is encrypted with your CMK.

## Limitations

Customer-managed keys apply only to online feature stores created after CMK became available in the region. Online feature stores created before CMK support was available in a region are not encrypted with a CMK, even if the workspace later enables one. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Stores](/concepts/online-feature-store.md) — The high-performance serving infrastructure for real-time ML features
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) — The underlying compute infrastructure for online feature stores
- Customer-managed keys for Lakebase — Configuration details for setting up CMK on Lakebase projects
- [Feature Engineering in Databricks](/concepts/feature-engineering-on-databricks.md) — Overview of the feature engineering ecosystem
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance and lineage for feature tables
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) — How features are served to real-time applications

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
