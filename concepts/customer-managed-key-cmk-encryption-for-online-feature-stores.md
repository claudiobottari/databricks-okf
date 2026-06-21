---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2532b623e8add02deb4ee06c5df87f2e2ed6f3e1406118b156e1414785dd6c68
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customer-managed-key-cmk-encryption-for-online-feature-stores
    - CK(EFOFS
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Customer-Managed Key (CMK) Encryption for Online Feature Stores
description: Encryption at rest for online feature stores using customer-managed keys, automatically applied when the workspace has CMK configured and the backing Lakebase project was created after CMK support became available.
tags:
  - security
  - encryption
  - databricks
timestamp: "2026-06-18T15:08:33.657Z"
---

# Customer-Managed Key (CMK) Encryption for Online Feature Stores

**Customer-Managed Key (CMK) Encryption for Online Feature Stores** refers to the ability to encrypt feature data at rest in Databricks Online Feature Stores using a key that the customer controls, rather than a platform-managed key. This provides an additional layer of security for sensitive feature data used in real-time machine learning applications.

## Overview

Online feature stores support encryption at rest with a customer-managed key because they are backed by Lakebase Autoscaling projects. No separate Lakebase or Feature Store configuration is required; CMK encryption applies automatically for workspaces that meet the necessary prerequisites. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Prerequisites for Automatic CMK Encryption

CMK encryption is applied automatically when **all** of the following conditions are true: ^[databricks-online-feature-stores-databricks-on-aws.md]

1. The workspace has a customer-managed key configured for managed services. For details, see Customer-managed keys for Lakebase.
2. The online feature store is backed by a Lakebase Autoscaling project. All online feature stores created with `fe.create_online_store` after March 23, 2026 use Lakebase Autoscaling.
3. The backing Lakebase project was created after CMK support became available in your region. Lakebase projects created before that date are not encrypted with a CMK, even if the workspace later enables one.

## Verification

To confirm that an online feature store is encrypted with your customer-managed key: ^[databricks-online-feature-stores-databricks-on-aws.md]

1. Click the **apps switcher** icon in the top right corner of your Databricks workspace to open the Lakebase App.
2. Locate the Lakebase project with the same name as the online store.
3. Check the **Customer-managed keys** status card on that project. See Check encryption status for more detail.

## Important Considerations

- CMK encryption does **not** apply retroactively. Only online feature stores created after CMK support became available in the region are encrypted. ^[databricks-online-feature-stores-databricks-on-aws.md]
- The backing Lakebase project shares the name of the online store. If the store was created via `create_online_store`, the corresponding project will have an identical name. ^[databricks-online-feature-stores-databricks-on-aws.md]
- No additional Lakebase or Feature Store configuration is required beyond having a workspace-level CMK for managed services. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- Customer-managed keys for Lakebase
- [Online Feature Stores](/concepts/online-feature-store.md)
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md)
- Encryption at rest
- [Feature Engineering in Databricks](/concepts/feature-engineering-on-databricks.md)

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
