---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44fda6c9fdbefd94d3d1ceb03cb421798217673f13ae8e2fa4da1ec54ebfc258
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - write-authentication-for-feature-publishing
    - WAFFP
    - write authentication|write authentication
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Write Authentication for Feature Publishing
description: Authentication required when publishing feature tables from the Databricks Feature Store to third-party online stores, supporting instance profiles or Databricks secrets with a write_secret_prefix.
tags:
  - authentication
  - feature-store
  - publishing
timestamp: "2026-06-19T22:10:02.919Z"
---

# Write Authentication for Feature Publishing

**Write Authentication for Feature Publishing** refers to the credential configuration required to publish feature tables from a Databricks [Feature Store](/concepts/feature-store.md) to a third-party online store, such as Amazon DynamoDB or a SQL-based online store. Databricks recommends providing write authentication through an instance profile attached to a cluster; alternatively, credentials can be stored in Databricks Secrets and referenced when publishing. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Prerequisite Permissions

When publishing to a DynamoDB online store, the instance profile or IAM user used for write authentication must have all of the following DynamoDB permissions:

- `dynamodb:DeleteItem`
- `dynamodb:DeleteTable`
- `dynamodb:PartiQLSelect`
- `dynamodb:DescribeTable`
- `dynamodb:PartiQLInsert`
- `dynamodb:GetItem`
- `dynamodb:CreateGlobalTable`
- `dynamodb:BatchGetItem`
- `dynamodb:UpdateTimeToLive`
- `dynamodb:BatchWriteItem`
- `dynamodb:ConditionCheckItem`
- `dynamodb:PutItem`
- `dynamodb:PartiQLUpdate`
- `dynamodb:Scan`
- `dynamodb:Query`
- `dynamodb:UpdateItem`
- `dynamodb:DescribeTimeToLive`
- `dynamodb:CreateTable`
- `dynamodb:UpdateGlobalTableSettings`
- `dynamodb:UpdateTable`
- `dynamodb:PartiQLDelete`
- `dynamodb:DescribeTableReplicaAutoScaling`

^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Using an Instance Profile (Recommended)

1. Create an instance profile that has write permission to the online store.
2. Add the instance profile to Databricks and launch a cluster with that instance profile attached. This is available on clusters running Databricks Runtime 10.5 ML and above.
3. Run the publishing code on that cluster. No explicit secret credentials or `write_secret_prefix` need to be provided to the online store specification. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Using Databricks Secrets

When an instance profile is not used, you can provide write credentials via Databricks secrets:

1. Create a secret scope for write access (shown as `<write-scope>`) or reuse an existing secret scope.
2. Choose a unique prefix for the target online store (shown as `<prefix>`).
3. For DynamoDB stores, create the following secrets:
   - `databricks secrets put-secret <write-scope> <prefix>-access-key-id`
   - `databricks secrets put-secret <write-scope> <prefix>-secret-access-key`
4. For SQL stores, create:
   - `databricks secrets put-secret <write-scope> <prefix>-user`
   - `databricks secrets put-secret <write-scope> <prefix>-password`

These secrets are then referenced by the publishing code using the `write_secret_prefix` parameter. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

If you intend to use an instance profile for write authentication configured at the cluster level, you do not need to include the `<write-scope>`. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- **Read Authentication for Feature Lookup** — Separate authentication required for served models to read features from online stores.
- **Instance Profile** — IAM role attachment method for both write and read authentication.
- **Databricks Secrets** — Secure storage for credentials.
- **[Feature Store](/concepts/feature-store.md)** — The Databricks feature engineering platform.
- **[Online Store](/concepts/online-feature-store.md)** — External key-value store for low-latency feature serving.
- **External Feature Lookup in Model Serving** — How models access features from online stores during inference.

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
