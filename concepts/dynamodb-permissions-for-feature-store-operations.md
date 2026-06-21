---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1df07ae2ca38456fb808e95153f72c9355b2be774f32f115a7c18c8a94229e53
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamodb-permissions-for-feature-store-operations
    - DPFFSO
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: DynamoDB Permissions for Feature Store Operations
description: Complete set of 24 required DynamoDB IAM permissions needed for publishing feature tables to third-party DynamoDB online stores via Databricks Feature Store.
tags:
  - dynamodb
  - iam
  - permissions
  - aws
timestamp: "2026-06-19T14:05:50.048Z"
---

# DynamoDB Permissions for Feature Store Operations

**DynamoDB Permissions for Feature Store Operations** refers to the set of IAM permissions required to publish feature tables to a DynamoDB online store and to look up feature values from a served MLflow model. Proper configuration of these permissions is essential for the [Feature Store](/concepts/feature-store.md) to function correctly with DynamoDB as the backing online store.

## Overview

When using a third-party online store such as DynamoDB with Databricks Feature Store, two distinct permission sets are needed:

- **Write authentication** – to publish feature tables from a Databricks cluster to the online store.
- **Read authentication** – to allow a Databricks-hosted MLflow model to look up feature values from the online store during serving.

Both types of authentication can be configured using an AWS Instance Profile attached to the compute resource or using Databricks Secrets. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Required Permissions for Publishing (Write Authentication)

The IAM user or instance profile used for write authentication must have all of the following DynamoDB actions on the target table(s):

| Permission | Description |
|------------|-------------|
| `dynamodb:DeleteItem` | Delete an item from the table |
| `dynamodb:DeleteTable` | Delete the table itself |
| `dynamodb:PartiQLSelect` | Run PartiQL SELECT statements |
| `dynamodb:DescribeTable` | Describe table metadata |
| `dynamodb:PartiQLInsert` | Run PartiQL INSERT statements |
| `dynamodb:GetItem` | Retrieve a single item |
| `dynamodb:CreateGlobalTable` | Create a global table |
| `dynamodb:BatchGetItem` | Batch read items |
| `dynamodb:UpdateTimeToLive` | Update TTL settings |
| `dynamodb:BatchWriteItem` | Batch write items |
| `dynamodb:ConditionCheckItem` | Conditionally check items (PartiQL transaction support) |
| `dynamodb:PutItem` | Insert or replace an item |
| `dynamodb:PartiQLUpdate` | Run PartiQL UPDATE statements |
| `dynamodb:Scan` | Scan the entire table |
| `dynamodb:Query` | Query by primary key |
| `dynamodb:UpdateItem` | Update an existing item |
| `dynamodb:DescribeTimeToLive` | Describe TTL configuration |
| `dynamodb:CreateTable` | Create a new table |
| `dynamodb:UpdateGlobalTableSettings` | Update global table settings |
| `dynamodb:UpdateTable` | Update table settings |
| `dynamodb:PartiQLDelete` | Run PartiQL DELETE statements |
| `dynamodb:DescribeTableReplicaAutoScaling` | Describe replica auto‑scaling settings |

^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

This comprehensive set of permissions is required because Databricks Feature Store may need to create, update, and manage the DynamoDB table structure as well as write individual feature values.

## Permissions for Lookup (Read Authentication)

When a served model looks up features from the online store, read authentication is needed. The source document does not enumerate a specific list of DynamoDB actions required for read‑only access, but typical read operations include `dynamodb:GetItem`, `dynamodb:BatchGetItem`, `dynamodb:Query`, and `dynamodb:Scan`. The same configuration methods (instance profile or secrets) apply. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Authentication Methods

### Instance Profile (Recommended for Write)

1. Create an [IAM instance profile](/concepts/model-serving-instance-profile.md) that grants the full list of write permissions above.
2. Attach the instance profile to a Databricks cluster running Databricks Runtime 10.5 ML or later.
3. When publishing a feature table, you do not need to provide explicit secret credentials or a `write_secret_prefix` — the instance profile is automatically used. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Instance Profile (Recommended for Read)

1. Create an instance profile with read‑only DynamoDB permissions.
2. Configure the [Databricks serving endpoint](/concepts/databricks-model-serving-endpoint.md) to use that instance profile (see [Add an instance profile to a serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/add-model-serving-instance-profile)).
3. When publishing the feature table, any `read_secret_prefix` specified is overridden by the instance profile. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Databricks Secrets (Alternative)

If instance profiles are not used, store credentials in Databricks Secrets:

1. Create two secret scopes: one for read‑only access (`<read-scope>`) and one for read‑write access (`<write-scope>`).
2. For DynamoDB, store the access key ID and secret access key for each scope with a shared prefix:

   ```bash
   # Read-only
   databricks secrets put-secret <read-scope> <prefix>-access-key-id
   databricks secrets put-secret <read-scope> <prefix>-secret-access-key

   # Read-write
   databricks secrets put-secret <write-scope> <prefix>-access-key-id
   databricks secrets put-secret <write-scope> <prefix>-secret-access-key
   ```

3. When publishing, refer to the secrets using `write_secret_prefix` and `read_secret_prefix` parameters in the [online store specification](/concepts/onlinestoreconfig.md).

^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

You can share a single secret scope across multiple online stores to avoid hitting the secret scope limit per workspace. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – Centralised feature management for ML.
- [Online Store](/concepts/online-feature-store.md) – Low‑latency storage for feature serving.
- Instance Profile – IAM role attached to EC2 instances or Databricks compute.
- Databricks Secrets – Securely store and reference credentials.
- [Model Serving](/concepts/model-serving.md) – Deploying MLflow models for real‑time inference.
- [Publish Features to a Third‑Party Online Store](/concepts/publishing-feature-tables-to-online-stores.md) – End‑to‑end workflow example.

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
