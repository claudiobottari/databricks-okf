---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 14fdcd2d57ea893ddaf3663f0ff324f3ba8c665e6086949f143c58d78b5b6475
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamodb-permissions-required-for-feature-store-operations
    - DPRFFSO
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: DynamoDB Permissions Required for Feature Store Operations
description: Complete list of DynamoDB IAM permissions needed for publishing feature tables and looking up features from DynamoDB online stores.
tags:
  - dynamodb
  - iam
  - permissions
  - feature-store
timestamp: "2026-06-18T10:50:14.543Z"
---

# DynamoDB Permissions Required for Feature Store Operations

Publishing feature tables to a third-party online store such as Amazon DynamoDB requires write authentication, and looking up features from served MLflow models requires read authentication. Both can be configured using an instance profile or Databricks Secrets. The required DynamoDB permissions depend on the operation being performed.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Write Permissions for Publishing Feature Tables

To publish feature tables to a DynamoDB online store, the IAM user or instance profile must be granted the following DynamoDB actions:^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

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
- `dynamodb:DescribeTableReplicaAutoScaling

These permissions cover the full range of table creation, item manipulation, and schema updates needed when publishing feature data.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Read Permissions for Feature Lookups

When served MLflow models connect to DynamoDB to look up feature values, read authentication is required. The source material does not enumerate a specific list of DynamoDB read actions; authentication can be provided either through an instance profile configured on the serving endpoint or through Databricks Secrets.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

> **Note**: The source states that for lookup authentication via an instance profile, the instance profile should have write permission to the online store. This is the documented recommendation.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Authentication Methods

### Using Instance Profiles

- **Write authentication (publishing)**: Attach an instance profile with the required DynamoDB permissions to the Databricks cluster running the publish code. No explicit secret credentials or `write_secret_prefix` are needed. This is supported on clusters running Databricks Runtime 10.5 ML and above.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- **Read authentication (lookup)**: Configure the [Databricks Serving Endpoint](/concepts/databricks-model-serving-endpoint.md) to use an instance profile. Any `read_secret_prefix` specified is overridden when an instance profile is used.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Using Databricks Secrets

For write access, create a secret scope with read-write credentials. For read access, create a separate secret scope with read-only credentials. Store the IAM access key ID and secret access key as secrets using the naming convention `<prefix>-access-key-id` and `<prefix>-secret-access-key`. This method works with any version of the Feature Engineering client and Feature Store client v0.3.8 and above.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — Central repository for feature data
- [Online Store](/concepts/online-feature-store.md) — Low-latency storage for serving features (e.g., DynamoDB)
- Instance Profile — IAM role attached to compute resources
- Databricks Secrets — Secure credential storage
- Served MLflow Models — Models deployed for inference that look up features
- [Publish Features to Online Store](/concepts/publishing-feature-tables-to-online-stores.md) — Workflow details for publishing

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
