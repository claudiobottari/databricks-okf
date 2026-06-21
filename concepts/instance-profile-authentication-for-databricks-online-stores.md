---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5d5ceb8dca659e1a26787ba2f9a93c68d0608f89012c5a321e4b3a34e22c599
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - instance-profile-authentication-for-databricks-online-stores
    - IPAFDOS
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Instance Profile Authentication for Databricks Online Stores
description: Using AWS IAM instance profiles attached to Databricks clusters or serving endpoints to provide read and write authentication to third-party online stores like DynamoDB.
tags:
  - authentication
  - aws
  - feature-store
timestamp: "2026-06-19T22:10:11.898Z"
---

# Instance Profile Authentication for Databricks Online Stores

**Instance Profile Authentication for Databricks Online Stores** is a method for providing [write authentication|write authentication](/concepts/write-authentication-for-feature-publishing.md) and read authentication|read authentication to Databricks when publishing [Feature Tables](/concepts/feature-tables.md) to or looking up features from third-party online stores. This approach uses an AWS instance profile attached to a Databricks cluster (for write) or a served model (for read) to grant the necessary permissions without requiring explicit secret credentials.

## Overview

Publishing feature tables to a third-party online store requires write authentication, and looking up features requires read authentication. Both can be configured using an instance profile or [Databricks secrets](/concepts/databricks-secret-scopes.md). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

The table shows the authentication methods supported for each action:

## Authentication for Publishing Feature Tables to Third-Party Online Stores

To publish feature tables to a third-party online store, you must provide write authentication. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

Databricks recommends providing write authentication through an instance profile attached to a Databricks cluster. Alternatively, you can [store credentials in Databricks secrets|store credentials in Databricks secrets](/concepts/databricks-secrets-for-online-store-credentials.md) and refer to them in a `write_secret_prefix` when publishing. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

The instance profile or IAM user should have all of the following permissions:

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

### Provide Write Authentication Through an Instance Profile Attached to a Databricks Cluster

On clusters running Databricks Runtime 10.5 ML and above, you can use the instance profile attached to the cluster for write authentication when publishing to DynamoDB online stores. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

Use these steps only for write authentication when publishing to DynamoDB online stores:

1. Create an instance profile that has write permission to the online store.
2. Attach the instance profile to a Databricks cluster by:
   - Adding the instance profile to Databricks
   - Launching a cluster with the instance profile
3. Select the cluster with the attached instance profile to run the code to publish to the online store. You do not need to provide explicit secret credentials or `write_secret_prefix` to the [online store spec](/concepts/onlinestoreconfig.md). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Provide Write Credentials Using Databricks Secrets

Follow the instructions in [Use Databricks secrets|Use Databricks secrets](/concepts/accessing-databricks-secrets-in-scorers.md). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Authentication for Looking Up Features from Third-Party Online Stores with Served MLflow Models

To enable Databricks-hosted MLflow models to connect to third-party online stores and look up feature values, you must provide read authentication. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

Databricks recommends providing lookup authentication through an instance profile attached to a Databricks served model. Alternatively, you can store credentials in Databricks secrets and refer to them in a `read_secret_prefix` when publishing. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Provide Lookup Authentication Through an Instance Profile Configured to a Served Model

1. Create an instance profile that has write permission to the online store.
2. Configure your Databricks serving endpoint to use the instance profile.

When publishing your table, you do not have to specify a `read_prefix`, and any `read_prefix` specified is overridden with the instance profile. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Provide Read Credentials Using Databricks Secrets

Follow the instructions in [Use Databricks secrets|Use Databricks secrets](/concepts/accessing-databricks-secrets-in-scorers.md). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Use Databricks Secrets for Read and Write Authentication

This section shows the steps to follow to set up authentication with [Databricks secrets](/concepts/databricks-secret-scopes.md). For code examples, see [Publish features to a third-party online store|Publish features to a third-party online store](/concepts/publishing-feature-tables-to-online-stores.md). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

1. Create two [secret scopes](/concepts/databricks-secret-scopes.md) that contain credentials for the online store: one for read-only access (`<read-scope>`) and one for read-write access (`<write-scope>`). Alternatively, you can reuse existing secret scopes.

   If you intend to use an instance profile for write authentication (configured at Databricks cluster level), you do not need to include the `<write-scope>`. If you intend to use an instance profile for read authentication (configured at Databricks Serving endpoint level), you do not need to include the `<read-scope>`. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

2. Pick a unique name for the target online store (`<prefix>`).

   For DynamoDB (works with any version of [Feature Engineering client](/concepts/featureengineeringclient-api.md) and [Feature Store client](/concepts/feature-store.md) v0.3.8 and above), create the following secrets:

   - Access key ID for the IAM user with read-only access: `databricks secrets put-secret <read-scope> <prefix>-access-key-id`
   - Secret access key for the IAM user with read-only access: `databricks secrets put-secret <read-scope> <prefix>-secret-access-key`
   - Access key ID for the IAM user with read-write access: `databricks secrets put-secret <write-scope> <prefix>-access-key-id`
   - Secret access key for the IAM user with read-write access: `databricks secrets put-secret <write-scope> <prefix>-secret-access-key`

   For SQL stores, create the following secrets:

   - User with read-only access: `databricks secrets put-secret <read-scope> <prefix>-user`
   - Password for user with read-only access: `databricks secrets put-secret <read-scope> <prefix>-password`
   - User with read-write access: `databricks secrets put-secret <write-scope> <prefix>-user`
   - Password for user with read-write access: `databricks secrets put-secret <write-scope> <prefix>-password`

There is a limit on the number of secret scopes per workspace. To avoid hitting this limit, you can define and share a single secret scope for accessing all online stores. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The Databricks feature store for managing and serving features
- [Online store](/concepts/online-feature-store.md) — A third-party storage system for serving features in production
- AWS IAM — Identity and Access Management for AWS permissions
- DynamoDB — A common online store for feature serving
- MLflow Model Serving — Model serving endpoints that require read authentication
- [Secret scopes](/concepts/databricks-secret-scopes.md) — Databricks secrets management for storing credentials

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
