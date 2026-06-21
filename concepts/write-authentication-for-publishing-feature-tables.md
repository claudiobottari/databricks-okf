---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 84386a04a958c655beded79fdde80bf00e527d0e656d315736497a226b92ab8a
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - write-authentication-for-publishing-feature-tables
    - WAFPFT
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Write Authentication for Publishing Feature Tables
description: Required write credentials (via instance profile or secrets with write_secret_prefix) for publishing feature tables to third-party online stores from Databricks Feature Store.
tags:
  - feature-store
  - authentication
  - publishing
timestamp: "2026-06-19T17:37:15.441Z"
---

# Write Authentication for Publishing Feature Tables

**Write Authentication** is the mechanism required to publish [Feature Table](/concepts/feature-table.md)s from Databricks to a [Third-Party Online Store](/concepts/third-party-online-stores-for-feature-serving.md), such as DynamoDB or a SQL-based store. Publishing feature tables to a third-party online store requires write authentication to create, update, and delete entries in the store. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

This page describes the two supported authentication methods — instance profiles and Databricks secrets — and the permissions that the authenticated identity must hold.

## Permissions Required

The instance profile or IAM user used for write authentication must have the following permissions on the target online store:

`dynamodb:DeleteItem`, `dynamodb:DeleteTable`, `dynamodb:PartiQLSelect`, `dynamodb:DescribeTable`, `dynamodb:PartiQLInsert`, `dynamodb:GetItem`, `dynamodb:CreateGlobalTable`, `dynamodb:BatchGetItem`, `dynamodb:UpdateTimeToLive`, `dynamodb:BatchWriteItem`, `dynamodb:ConditionCheckItem`, `dynamodb:PutItem`, `dynamodb:PartiQLUpdate`, `dynamodb:Scan`, `dynamodb:Query`, `dynamodb:UpdateItem`, `dynamodb:DescribeTimeToLive`, `dynamodb:CreateTable`, `dynamodb:UpdateGlobalTableSettings`, `dynamodb:UpdateTable`, `dynamodb:PartiQLDelete`, `dynamodb:DescribeTableReplicaAutoScaling`. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

These permissions cover all operations required for publishing feature tables to a DynamoDB-based online store. For SQL-based stores, the required permissions vary by store provider.

## Using an Instance Profile (Recommended)

Databricks recommends providing write authentication by attaching an [instance profile](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) to the Databricks cluster that runs the publishing code. This method only requires steps to configure the cluster and does not require explicit secret credentials or a `write_secret_prefix` in the online store specification. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Steps

1. Create an instance profile that grants write permission to the target online store.
2. Add the instance profile to Databricks.
3. Launch a cluster and attach the instance profile to it.
4. Run the publishing code on that cluster. No explicit secret credentials or `write_secret_prefix` are needed in the [online store spec](/concepts/onlinestoreconfig.md). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

This method is supported on clusters running **Databricks Runtime 10.5 ML and above** for DynamoDB online stores. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Using Databricks Secrets

As an alternative, you can store credentials in Databricks Secrets and refer to them via a `write_secret_prefix` when publishing. This method works for both DynamoDB and SQL-based online stores. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Setup for DynamoDB

Create a write secret scope (e.g., `<write-scope>`) and store the following secrets, using a unique `<prefix>` of your choice:

- `databricks secrets put-secret <write-scope> <prefix>-access-key-id`
- `databricks secrets put-secret <write-scope> <prefix>-secret-access-key`

### Setup for SQL Stores

Create a write secret scope and store:

- `databricks secrets put-secret <write-scope> <prefix>-user`
- `databricks secrets put-secret <write-scope> <prefix>-password`

> Note: There is a limit on the number of secret scopes per workspace. To avoid hitting this limit, you can define and share a single secret scope for accessing all online stores. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Usage

When publishing a feature table, set the `write_secret_prefix` parameter on the online store specification to the scope and prefix you created. The Feature Store client uses the secrets to authenticate against the store. For code examples, see [Publish features to a third-party online store](/concepts/publishing-feature-tables-to-online-stores.md). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Read Authentication (Context)

Looking up features from a third-party online store for served MLflow models requires separate *read* authentication. Read authentication can be provided using a separate read instance profile (attached to a [Model Serving](/concepts/model-serving.md) endpoint) or read Databricks secrets (with a `read_secret_prefix`). The same secrets structure applies, but with read-only credentials. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- Publishing Features to a Third-Party Online Store
- Read Authentication for Feature Lookup
- [Feature Table](/concepts/feature-table.md)
- [Third-Party Online Store](/concepts/third-party-online-stores-for-feature-serving.md)
- Instance Profile
- Databricks Secrets
- Feature Store Client
- Online Store Spec

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
