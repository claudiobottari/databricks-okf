---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 27a691cb94c7331cb02a62138945ef0d2433892b680c726cc7a6a86df183c2d9
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customer-managed-keys-cmk-for-online-feature-stores
    - CK(FOFS
    - Customer-Managed Keys (CMK)
    - Customer-managed key (CMK)
    - customer-managed keys (CMK)
    - customer‑managed keys (CMK)
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
title: Customer-Managed Keys (CMK) for Online Feature Stores
description: Encryption at rest for online feature store data using a workspace-level customer-managed key, automatically applying when the workspace, online store, and region all support CMK.
tags:
  - security
  - encryption
  - compliance
timestamp: "2026-06-18T11:39:43.206Z"
---

# Customer-Managed Keys (CMK) for Online Feature Stores

**Customer-Managed Keys (CMK) for Online Feature Stores** provides encryption at rest for feature data served by Databricks Online Feature Stores. Because Online Feature Stores are backed by Lakebase Autoscaling projects, they inherit Lakebase’s support for encryption using a key that you control in your own cloud key management infrastructure. No additional Lakebase or Feature Store configuration is required; the encryption applies automatically for eligible workspaces. ^[databricks-online-feature-stores-databricks-on-aws.md]

## How It Works

Online feature stores store feature data in a Lakebase Autoscaling project. When the workspace has a customer-managed key configured for managed services, and the backing Lakebase project was created after CMK support became available in your region, all data at rest in that online store is encrypted with the workspace’s CMK. Databricks does not need you to enable CMK separately for the feature store; the encryption is applied at the Lakebase layer. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Requirements

CMK encryption applies automatically when **all** of the following conditions are true: ^[databricks-online-feature-stores-databricks-on-aws.md]

- The workspace has a customer-managed key configured for managed services. See Customer-managed keys for Lakebase.
- The online feature store is backed by a Lakebase Autoscaling project. All online feature stores created with `fe.create_online_store()` after **March 23, 2026** use Lakebase Autoscaling.
- The backing Lakebase project was created **after** CMK support became available in your region.

## Checking Encryption Status

The Lakebase project that backs an online feature store has the same name as the online store. To verify that the store is encrypted with your CMK: ^[databricks-online-feature-stores-databricks-on-aws.md]

1. Click the apps switcher (grid icon) in the top-right corner of your Databricks workspace to open the **Lakebase App**.
2. Locate the project with the same name as your online store.
3. Check the **Customer-managed keys** status card on that project’s detail page. This card shows whether the project is encrypted with your CMK.

For more detail, see the Lakebase documentation on [checking encryption status](https://docs.databricks.com/aws/en/oltp/projects/customer-managed-keys#check-status).

## Limitations

- CMK encryption applies **only** to online feature stores created after CMK support became available in the region. Lakebase projects created before that date remain unencrypted even if the workspace later enables a customer-managed key. ^[databricks-online-feature-stores-databricks-on-aws.md]
- Online feature stores created earlier (before March 23, 2026) may use Lakebase Provisioned instances, which do not support CMK. Only stores backed by [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) are eligible.

## Related Concepts

- Customer-managed keys for Lakebase — How to configure CMK for managed services in Lakebase.
- [Online Feature Stores](/concepts/online-feature-store.md) — Overview of Databricks Online Feature Stores and their architecture.
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) — How to serve features to real-time applications using endpoints.
- [Lakebase Autoscaling](/concepts/lakebase-autoscaling.md) — The underlying compute model for new online feature stores.
- Encryption at rest — Broader concept of data protection in Databricks.

## Sources

- databricks-online-feature-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
