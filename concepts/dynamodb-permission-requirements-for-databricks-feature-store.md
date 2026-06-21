---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c4b5f600162b24c310a9400522d7bd8023f92a68c67a44f3885d7b45d0fd38a2
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamodb-permission-requirements-for-databricks-feature-store
    - DPRFDFS
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: DynamoDB Permission Requirements for Databricks Feature Store
description: The comprehensive set of DynamoDB IAM permissions (e.g., DeleteItem, PutItem, Query, Scan) that an instance profile or IAM user must have to publish features to a DynamoDB online store.
tags:
  - aws
  - dynamodb
  - permissions
  - feature-store
timestamp: "2026-06-19T22:09:46.467Z"
---

# DynamoDB Permission Requirements for Databricks Feature Store

**DynamoDB Permission Requirements for Databricks Feature Store** defines the AWS IAM permissions necessary to publish feature tables to and look up features from a third-party online store backed by Amazon DynamoDB. Both write and read authentication must be configured, and the required DynamoDB API actions differ by operation. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Write Authentication Permissions

To publish feature tables to a DynamoDB online store, the instance profile or IAM user must be granted **write authentication** that includes the full set of 22 DynamoDB actions listed below. These permissions cover table creation, item manipulation, scanning, querying, and Time to Live (TTL) management. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

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

## Read Authentication Permissions

To look up features from a DynamoDB online store — typically from a served MLflow model — the model serving endpoint must be configured with **read authentication**. The same set of DynamoDB write permissions listed above is recommended for the instance profile used by the serving endpoint. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Authentication Methods

### Instance Profile (Recommended)

For **write authentication** on clusters running Databricks Runtime 10.5 ML and above, attach an instance profile that has the required DynamoDB permissions to the cluster. No explicit secret credentials or `write_secret_prefix` are needed when publishing. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

For **read authentication**, configure a Databricks serving endpoint to use an instance profile that has write permission to the online store. Any `read_prefix` specified during publishing is overridden with the instance profile. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Databricks Secrets

As an alternative to instance profiles, you can store credentials in Databricks secrets. For DynamoDB online stores, create secrets for both read-only and read-write access using the following naming convention: ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

Create two secret scopes: `<read-scope>` for read-only access and `<write-scope>` for read-write access. Within each scope, create secrets with keys `<prefix>-access-key-id` and `<prefix>-secret-access-key`, where `<prefix>` is a unique name for the target online store. This approach works with any version of the Feature Engineering client and Feature Store client v0.3.8 and above. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — System for managing and serving features for machine learning.
- Third-party Online Stores — External feature storage backends such as DynamoDB.
- Instance Profile — IAM role used to grant AWS permissions to Databricks compute resources.
- Databricks Secrets — Securely managed credentials used for authentication.
- MLflow Model Serving — Serving endpoints that look up features from online stores.

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
