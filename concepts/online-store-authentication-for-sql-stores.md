---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bed2a3b0ab5127e4fd0a58c514f20ab114375d5f8dc029142779b3cf2d42f6e1
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-store-authentication-for-sql-stores
    - OSAFSS
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
    - file: authentication-for-working-third-party-online-stores-databricks-on-aws.md
title: Online Store Authentication for SQL Stores
description: The pattern of storing user/password credentials in Databricks secrets for SQL-based third-party online stores, as opposed to access keys used for DynamoDB.
tags:
  - authentication
  - sql
  - secrets
  - online-store
timestamp: "2026-06-18T14:29:41.423Z"
---

# Online Store Authentication for SQL Stores

**Online Store Authentication for SQL Stores** refers to the process of configuring read and write credentials for [feature stores](/concepts/feature-store.md) that use SQL-based [third-party online stores](/concepts/third-party-online-stores-for-feature-serving.md), such as those built on Amazon DynamoDB or other SQL-compatible backends. Authentication is required both for publishing feature tables to the online store and for looking up features from served MLflow models.

## Overview

When working with third-party online stores in Databricks, two distinct authentication modes are required: write authentication for publishing feature tables, and read authentication for looking up features during model serving. Both modes can be configured using an instance profile or [Databricks secrets](/concepts/databricks-secret-scopes.md).^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Supported Authentication Methods

The following table summarizes the authentication methods supported for each action:

| Action | Recommended Method | Alternative Method |
|--------|-------------------|-------------------|
| Publish feature tables (write) | Instance profile attached to cluster | Databricks secrets (write scope) |
| Look up features (read) | Instance profile on serving endpoint | Databricks secrets (read scope) |

^[authentication-for-working-third-party-online-stores-databricks-on-aws.md]

## Authentication for Publishing Feature Tables

To publish feature tables to a third-party online store, you must provide write authentication. Databricks recommends using an instance profile attached to a Databricks cluster. Alternatively, you can store credentials in [Databricks secrets](/concepts/databricks-secret-scopes.md) and reference them in a `write_secret_prefix` when publishing.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Required Permissions

For DynamoDB-based online stores, the instance profile or IAM user must have the following permissions:

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

## Authentication for Looking Up Features

To enable Databricks-hosted MLflow models to connect to third-party online stores and look up feature values, you must provide read authentication. Databricks recommends configuring read authentication through an [instance profile on a served model](/concepts/instance-profile-for-model-serving-endpoints.md) endpoint. Alternatively, you can use [Databricks secrets](/concepts/databricks-secret-scopes.md) for read credentials.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Using Databricks Secrets

### Creating Secret Scopes

1. Create two secret scopes:
   - A read-only scope (`<read-scope>`) containing credentials for read access
   - A read-write scope (`<write-scope>`) containing credentials for write access
   
   Alternatively, you can reuse existing secret scopes or use a single scope.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Creating Secrets for SQL Stores

For SQL stores, create the following secrets:

- **Read scope:**
  - `databricks secrets put-secret <read-scope> <prefix>-user` — User with read-only access
  - `databricks secrets put-secret <read-scope> <prefix>-password` — Password for the read-only user

- **Write scope:**
  - `databricks secrets put-secret <write-scope> <prefix>-user` — User with read-write access
  - `databricks secrets put-secret <write-scope> <prefix>-password` — Password for the read-write user

^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Best Practices

- Use an instance profile for write authentication (configured at cluster level) to avoid creating a write secret scope if not needed.
- Use an instance profile for read authentication (configured at the serving endpoint) to avoid creating a read secret scope if not needed.
- There is a limit on the number of secret scopes per workspace. To avoid hitting this limit, define and share a single secret scope for accessing all online stores.

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The central repository for managing and serving features
- [Online Store](/concepts/online-feature-store.md) — The low-latency storage for serving features to production models
- Instance Profile — AWS IAM role for granting permissions to Databricks clusters
- Databricks Secrets — Secure credential management for Databricks
- MLflow Model Serving — Production deployment of ML models

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
2. authentication-for-working-third-party-online-stores-databricks-on-aws.md
