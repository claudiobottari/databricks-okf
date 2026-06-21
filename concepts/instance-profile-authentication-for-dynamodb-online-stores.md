---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 25771acb9c665617b30ed82f4dff19bca5f3d752a21f6c8714e9620010c9c080
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - instance-profile-authentication-for-dynamodb-online-stores
    - IPAFDOS
    - Instance profiles for third-party online stores
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Instance Profile Authentication for DynamoDB Online Stores
description: Using AWS instance profiles attached to Databricks clusters (for write) or serving endpoints (for read) to authenticate with DynamoDB online stores without explicit secret credentials.
tags:
  - authentication
  - aws
  - dynamodb
  - instance-profile
timestamp: "2026-06-19T17:37:58.098Z"
---

# Instance Profile Authentication for DynamoDB Online Stores

**Instance Profile Authentication for DynamoDB Online Stores** refers to the use of an AWS instance profile (IAM role) attached to a Databricks cluster or serving endpoint to grant the necessary permissions for publishing feature tables to a [DynamoDB online store](/concepts/amazon-dynamodb-online-store-integration.md) or looking up features from that store during model serving. This method avoids storing static credentials in Databricks Secrets and relies on AWS IAM roles for temporary, scoped access. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Overview

When working with a third-party online store such as DynamoDB, two distinct authentication needs arise:

- **Write authentication** – required when publishing feature tables from [Feature Store](/concepts/feature-store.md) to the online store.
- **Read authentication** – required when a MLflow Model Serving endpoint retrieves feature values from the online store during inference.

Databricks recommends using an instance profile for both scenarios, as it integrates natively with AWS IAM and eliminates the need for secret management. Administrators can choose to use instance profiles for write, for read, or for both, depending on the deployment model. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Write Authentication via Instance Profile (Publishing)

To enable a Databricks cluster to publish feature tables to a DynamoDB online store without explicit secret credentials, attach an instance profile that has the required DynamoDB permissions. This approach works on clusters running **Databricks Runtime 10.5 ML and above**. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Procedure

1. **Create an IAM instance profile** with write permissions to the target DynamoDB tables. The profile must include the full set of DynamoDB actions listed below.
2. **Add the instance profile to Databricks** following the [standard instructions](https://docs.databricks.com/en/archive/storage/tutorial-s3-instance-profile#add-instance-profile).
3. **Launch a cluster with the instance profile** – during cluster configuration, select the instance profile under the advanced options.
4. **Run the publishing code on that cluster**. No `write_secret_prefix` or explicit secret references are needed in the online store spec. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Read Authentication via Instance Profile (Serving)

To enable a [Databricks serving endpoint](/concepts/databricks-model-serving-endpoint.md) to look up feature values from a DynamoDB online store during model serving, configure the endpoint to use an instance profile with read-only DynamoDB permissions. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Procedure

1. **Create an IAM instance profile** with read-only permissions to the target DynamoDB tables (a subset of the actions listed below, such as `GetItem` and `BatchGetItem`).
2. **Configure the serving endpoint to use the instance profile** by following the [add-model-serving-instance-profile](https://docs.databricks.com/en/machine-learning/model-serving/add-model-serving-instance-profile) guide.
3. When publishing the feature table, **do not specify a `read_prefix`** – any `read_prefix` provided is overridden by the instance profile configured on the serving endpoint. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Required DynamoDB Permissions

The instance profile (whether for write or read) must be granted the following DynamoDB actions. For read-only access, a subset may suffice (e.g., `GetItem`, `BatchGetItem`, `Query`, `Scan`). For write access, all of the following are typically needed: ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

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

## Alternative: Databricks Secrets

If instance profiles cannot be used, administrators can provide authentication via Databricks Secrets. For DynamoDB, this involves storing an AWS access key ID and secret access key in separate secret scopes for read and write access, then referencing them using a `read_secret_prefix` or `write_secret_prefix` in the online store configuration. This approach works with any version of the Feature Engineering client and Feature Store client v0.3.8 and above. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- [DynamoDB Online Store](/concepts/amazon-dynamodb-online-store-integration.md)
- [Feature Store](/concepts/feature-store.md) – Publishing and serving feature tables.
- Instance Profile – AWS IAM role attached to EC2 instances.
- MLflow Model Serving – Real-time inference endpoints.
- Databricks Secrets – Alternative credential storage.
- IAM Permissions for DynamoDB – Full list of required actions.
- Cluster Configuration with Instance Profiles
- [Feature Publishing to Online Stores](/concepts/feature-publishing-to-online-stores.md)

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
