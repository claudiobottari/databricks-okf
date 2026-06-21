---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 142bbaa6668137ee242c631dfc0ffc4d5fd5ba0f9b678a4900d2812a4573f692
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customer-managed-key-encryption-for-online-stores
    - CKEFOS
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Customer-Managed Key Encryption for Online Stores
description: Encryption at rest for online feature stores using customer-managed keys, automatically applied when the workspace has CMK configured and the backing Lakebase project was created after CMK support.
tags:
  - security
  - encryption
  - compliance
timestamp: "2026-06-19T14:52:03.414Z"
---

# Customer-Managed Key Encryption for Online Stores

**Customer-Managed Key (CMK) Encryption for Online Stores** refers to the encryption at rest of data stored in Databricks Online Feature Stores using encryption keys that the customer controls, rather than cloud-provider-managed keys. This is made possible through underlying support from Databricks Lakebase Autoscaling.

## Overview

Online feature stores support encryption at rest with a customer-managed key (CMK) due to underlying support from Lakebase Autoscaling. No Lakebase or Feature Store configuration is required; CMK encryption applies automatically for relevant workspaces. ^[databricks-online-feature-stores-databricks-on-aws.md]

CMK encryption applies automatically when all of the following conditions are true:

- The workspace has a customer-managed key configured for managed services (see Customer-Managed Keys for Lakebase).
- The online feature store is backed by a Lakebase Autoscaling project. All online feature stores created with `fe.create_online_store` after March 23, 2026 use Lakebase Autoscaling. ^[databricks-online-feature-stores-databricks-on-aws.md]
- The backing Lakebase project was created after CMK support became available in your region. Lakebase projects created before that are not encrypted with a CMK even if the workspace later enables one. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Verifying Encryption Status

The Lakebase project backing an online feature store has the same name as the online store. To verify encryption status:

1. Click the apps switcher in the top right corner of your workspace to open the Lakebase App.
2. Locate the project with the same name as your online store.
3. Check the **Customer-managed keys** status card on that project to confirm the store is encrypted with your CMK. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Important Considerations

- CMK encryption applies only to online feature stores created after CMK support became available in your region. ^[databricks-online-feature-stores-databricks-on-aws.md]
- Online feature stores created before CMK availability are not retroactively encrypted, even if the workspace later enables CMK. ^[databricks-online-feature-stores-databricks-on-aws.md]
- The underlying Lakebase Autoscaling project must have been created after CMK support was available in the region for encryption to apply. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Stores](/concepts/online-feature-store.md) — High-performance serving of feature data for real-time applications.
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) — The compute infrastructure backing online feature stores.
- Customer-Managed Keys for Lakebase — Configuring CMK for Lakebase projects.
- Encryption at Rest — General data protection concept for stored data.
- [Feature Engineering in Databricks](/concepts/feature-engineering-on-databricks.md) — Broader context for feature management and serving.

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
