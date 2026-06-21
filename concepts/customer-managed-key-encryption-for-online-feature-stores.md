---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1658dcfe2d92b9ff001a99fe890eb2945b6d0d1f60ebc0e2609dfeb262e8d440
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customer-managed-key-encryption-for-online-feature-stores
    - CKEFOFS
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Customer-Managed Key Encryption for Online Feature Stores
description: Online feature stores support encryption at rest with customer-managed keys (CMK) via underlying Lakebase Autoscaling support, applying automatically when workspace CMK is configured and the store was created after CMK became available in the region.
tags:
  - security
  - encryption
  - compliance
timestamp: "2026-06-19T09:52:59.254Z"
---

# Customer-Managed Key Encryption for Online Feature Stores

**Customer-Managed Key (CMK) Encryption for Online Feature Stores** refers to the encryption at rest of feature data stored in Databricks Online Feature Stores using encryption keys that the customer controls and manages. This capability is built on underlying support from Lakebase Autoscaling and requires no additional configuration in the Feature Store or Lakebase itself.

## Overview

Online feature stores support encryption at rest with a customer-managed key (CMK) due to underlying support from Lakebase Autoscaling. No Lakebase or Feature Store configuration is required; CMK applies automatically for relevant workspaces. ^[databricks-online-feature-stores-databricks-on-aws.md]

## How CMK Applies Automatically

CMK encryption applies automatically when all of the following conditions are met: ^[databricks-online-feature-stores-databricks-on-aws.md]

1. **Workspace has a CMK configured for managed services.** The workspace must have a customer-managed key configured for managed services. See Customer-managed keys for Lakebase.

2. **Online feature store is backed by a Lakebase Autoscaling project.** All online feature stores created with `fe.create_online_store` after March 23, 2026 use Lakebase Autoscaling.

3. **Backing Lakebase project was created after CMK support became available in your region.** Lakebase projects created before CMK support became available in a region are not encrypted with a CMK, even if the workspace later enables one.

## Verifying Encryption Status

The Lakebase project backing an online feature store has the same name as the online store. To verify encryption status: ^[databricks-online-feature-stores-databricks-on-aws.md]

1. Click the apps switcher icon in the top right corner of your workspace to open the Lakebase App.
2. Locate the project with the same name as your online store.
3. Check the **Customer-managed keys** status card on that project.

See Check encryption status for detailed instructions.

## Important Considerations

- CMK encryption applies only to online feature stores created after CMK became available in your region. Pre-existing online stores are not retroactively encrypted. ^[databricks-online-feature-stores-databricks-on-aws.md]
- No additional configuration in the Feature Store or Lakebase is required — the encryption is automatic when the prerequisites are met. ^[databricks-online-feature-stores-databricks-on-aws.md]
- This is a documented limitation that customers should be aware of when planning their encryption strategy. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Online Feature Stores](/concepts/online-feature-store.md) – The high-performance serving layer for real-time ML features
- Customer-Managed Keys – General CMK concepts in Databricks
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) – The underlying infrastructure powering online feature stores
- Encryption at Rest – Broader data protection strategies
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) – How served features are consumed by applications

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
