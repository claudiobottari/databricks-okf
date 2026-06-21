---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc5367e0be92470e6e92ef87f88518d0e48edc666d360b14b44779eaa4599916
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - third-party-online-store-authentication-for-feature-serving
    - TOSAFFS
    - Third-party online store authentication
    - Third‑Party Online Store Authentication
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Third-Party Online Store Authentication for Feature Serving
description: Authentication methods (instance profiles and Databricks secrets) for publishing to and reading from third-party online stores in Databricks Feature Store on AWS.
tags:
  - feature-store
  - authentication
  - aws
timestamp: "2026-06-19T09:05:54.992Z"
---

# Third-Party Online Store Authentication for Feature Serving

**Third-Party Online Store Authentication for Feature Serving** refers to the mechanisms and credentials required to publish feature tables to, and look up features from, third-party online stores when using Databricks Feature Serving. Authentication is required for both writing features during publication and reading features during model inference.

## Overview

When working with third-party online stores, two distinct authentication contexts exist: write authentication for publishing feature tables, and read authentication for looking up features from served models. Databricks supports authentication through instance profiles or Databricks secrets for both operations. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Supported Authentication Methods

The following table summarizes the authentication methods supported for each action:

| Action | Recommended Method | Alternative Method |
|--------|-------------------|-------------------|
| Publishing (write) | Instance profile attached to a Databricks cluster | Databricks secrets via `write_secret_prefix` |
| Lookup (read) | Instance profile configured on a served model | Databricks secrets via `read_secret_prefix` |

^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Authentication for Publishing Feature Tables

To publish feature tables to a third-party online store, you must provide write authentication. Databricks recommends using an instance profile attached to a Databricks cluster. Alternatively, you can store credentials in Databricks secrets and refer to them using a `write_secret_prefix` when publishing. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Using Instance Profiles for Write Authentication

On clusters running Databricks Runtime 10.5 ML and above, the instance profile attached to the cluster can be used for write authentication when publishing to DynamoDB online stores. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

The instance profile or IAM user must have the following DynamoDB permissions:

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

To set up instance profile authentication for publishing:

1. Create an instance profile with write permissions to the online store.
2. Add the instance profile to Databricks.
3. Launch a cluster with that instance profile attached.
4. Run the code to publish to the online store using that cluster — no explicit secret credentials or `write_secret_prefix` are needed in the online store spec. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Authentication for Looking Up Features from Served Models

To enable Databricks-hosted MLflow models to connect to third-party online stores and look up feature values during inference, you must provide read authentication. Databricks recommends using an instance profile configured on a served model. Alternatively, you can use Databricks secrets with a `read_secret_prefix`. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Using Instance Profiles for Lookup Authentication

1. Create an instance profile that has read permissions to the online store.
2. Configure your Databricks serving endpoint to use that instance profile.
3. When publishing the feature table, you do not need to specify a `read_prefix` — any specified `read_prefix` is overridden by the instance profile. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Using Databricks Secrets for Authentication

As an alternative to instance profiles, you can use [Databricks secrets](/concepts/databricks-secret-scopes.md) to store and reference credentials for both read and write authentication.

### Secret Setup Process

1. Create two secret scopes: one for read-only access (`<read-scope>`) and one for read-write access (`<write-scope>`). You may reuse existing secret scopes. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

2. Choose a unique prefix name for the target online store (`<prefix>`). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

3. For **DynamoDB** stores (works with Feature Engineering client and Feature Store client v0.3.8+), create these secrets:

   - Read scope: `<read-scope>/<prefix>-access-key-id` and `<read-scope>/<prefix>-secret-access-key`
   - Write scope: `<write-scope>/<prefix>-access-key-id` and `<write-scope>/<prefix>-secret-access-key` ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

4. For **SQL stores**, create these secrets:

   - Read scope: `<read-scope>/<prefix>-user` and `<read-scope>/<prefix>-password`
   - Write scope: `<write-scope>/<prefix>-user` and `<write-scope>/<prefix>-password` ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Secret Scope Considerations

If you intend to use an instance profile for write authentication (configured at cluster level), you only need the read scope. Similarly, if you use an instance profile for read authentication (configured at serving endpoint level), you only need the write scope. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

There is a limit on the number of secret scopes per workspace. To avoid hitting this limit, you can define and share a single secret scope for accessing all online stores. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

For code examples demonstrating secret usage, see [Publish features to a third-party online store](/concepts/publishing-feature-tables-to-online-stores.md). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- Feature Serving — Serving feature values for online inference
- [Databricks secrets](/concepts/databricks-secret-scopes.md) — Secure credential management
- [Instance profiles](/concepts/instance-profile-databricks-on-aws.md) — AWS IAM roles for EC2 instances
- [Model Serving](/concepts/model-serving.md) — Deploying models with Databricks
- Online stores — Third-party feature storage for real-time access
- [Publish features to a third-party online store](/concepts/publishing-feature-tables-to-online-stores.md) — Code examples for publishing

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
