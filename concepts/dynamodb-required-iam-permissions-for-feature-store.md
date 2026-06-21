---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b18d0975bf952ec111ef86d28cb66c632cfedd5ebf84d851ae00839708a2aa63
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamodb-required-iam-permissions-for-feature-store
    - DRIPFFS
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: DynamoDB Required IAM Permissions for Feature Store
description: "The complete set of IAM permissions (dynamodb: actions) required for write authentication when publishing feature tables to DynamoDB online stores from Databricks."
tags:
  - iam
  - dynamodb
  - permissions
timestamp: "2026-06-19T09:05:43.518Z"
---

# DynamoDB Required IAM Permissions for Feature Store

**DynamoDB Required IAM Permissions for Feature Store** refers to the set of AWS Identity and Access Management (IAM) permissions that a Databricks cluster or serving endpoint must have to publish feature tables to a DynamoDB online store or read features from it. These permissions are configured through an instance profile or Databricks secrets.

## Overview

When using a third-party online store with [Feature Store](/concepts/feature-store.md), the Databricks instance profile or IAM user must be granted specific DynamoDB actions. The required permissions differ between write (publishing) and read (lookup) operations. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Write Authentication (Publishing Feature Tables)

To publish feature tables to a DynamoDB online store, the instance profile or IAM user must have all of the following permissions: ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

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

Write authentication can be provided via an instance profile attached to the Databricks cluster (recommended) or through Databricks secrets. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Read Authentication (Feature Lookup from Served Models)

To look up features from a DynamoDB online store via a served MLflow model, the endpoint must have read authentication. The source material does not enumerate specific DynamoDB actions required for read; however, it recommends providing read credentials via an instance profile configured on the serving endpoint or via Databricks secrets. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

- For instance profile‑based lookup, the profile should have read access to the DynamoDB tables. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- For secret‑based lookup, create a secret scope with read‑only credentials and reference it as a `read_secret_prefix` when publishing. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Authentication Methods

### Instance Profile

- **Write**: Attach an instance profile with the write permissions listed above to the cluster (Databricks Runtime 10.5 ML and above). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- **Read**: Configure the [Model Serving](/concepts/model-serving.md) endpoint to use an instance profile that has read access to the online store. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Databricks Secrets

Secrets can store AWS access keys for IAM users with appropriate permissions. For both read and write, you create secrets and reference them with a `write_secret_prefix` or `read_secret_prefix` in the online store spec. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

See the detailed steps in Use Databricks secrets for read and write authentication.

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – Central metadata store for features.
- [Online Store](/concepts/online-feature-store.md) – Low‑latency store for feature serving.
- Instance Profile – IAM role attached to a Databricks cluster or endpoint.
- Databricks Secrets – Secure credential management.
- [Model Serving](/concepts/model-serving.md) – Deploying models with online feature lookup.

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
