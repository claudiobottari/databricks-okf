---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8cbd4cdb922898566848bdf769c05bade2e7382e7a80ca69c27dad3b80a2cb6
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - instance-profile-authentication-for-feature-store
    - IPAFFS
    - instance-profile-authentication-for-databricks-feature-store
    - IPAFDFS
    - instance-profile-authentication-for-databricks-online-stores
    - IPAFDOS
    - instance-profile-authentication-for-dynamodb-online-stores
    - Instance profiles for third-party online stores
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Instance Profile Authentication for Feature Store
description: Using AWS instance profiles attached to Databricks clusters (for write) or serving endpoints (for read) to authenticate with DynamoDB online stores without explicit credentials.
tags:
  - authentication
  - instance-profile
  - aws
timestamp: "2026-06-19T09:05:06.103Z"
---

# Instance Profile Authentication for Feature Store

**Instance Profile Authentication for Feature Store** refers to using AWS IAM instance profiles to authenticate [Feature Store](/concepts/feature-store.md) operations against third-party online stores such as Amazon DynamoDB. Databricks recommends instance profiles over Databricks secrets for both write authentication (when publishing feature tables) and read authentication (when serving MLflow models).^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Write Authentication (Publishing)

To publish feature tables to a third-party online store, the cluster issuing the publish operation must have write-level credentials. Databricks recommends providing these credentials through an instance profile attached to the Databricks cluster.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Prerequisites

- The cluster must run Databricks Runtime 10.5 ML or above.
- The instance profile must have all of the following DynamoDB permissions:
  `dynamodb:DeleteItem`, `dynamodb:DeleteTable`, `dynamodb:PartiQLSelect`, `dynamodb:DescribeTable`, `dynamodb:PartiQLInsert`, `dynamodb:GetItem`, `dynamodb:CreateGlobalTable`, `dynamodb:BatchGetItem`, `dynamodb:UpdateTimeToLive`, `dynamodb:BatchWriteItem`, `dynamodb:ConditionCheckItem`, `dynamodb:PutItem`, `dynamodb:PartiQLUpdate`, `dynamodb:Scan`, `dynamodb:Query`, `dynamodb:UpdateItem`, `dynamodb:DescribeTimeToLive`, `dynamodb:CreateTable`, `dynamodb:UpdateGlobalTableSettings`, `dynamodb:UpdateTable`, `dynamodb:PartiQLDelete`, and `dynamodb:DescribeTableReplicaAutoScaling`.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Steps

1. Create an IAM instance profile with write permission to the target online store.
2. Add the instance profile to Databricks.
3. Launch a cluster with that instance profile attached.
4. Run the publish code on that cluster. No explicit secret credentials or `write_secret_prefix` need to be provided to the online store spec.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Read Authentication (Lookup)

Databricks-hosted MLflow models that perform online feature lookups must have read-only credentials. Databricks recommends providing read authentication through an instance profile configured on the [serving endpoint](/concepts/serving-endpoint-acls.md).^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Steps

1. Create an IAM instance profile with read permission to the target online store (the required permissions are a subset of the write permissions listed above).
2. Configure the serving endpoint to use that instance profile as described in the model-serving instance profile documentation.
3. When publishing the feature table, do not specify a `read_prefix`; any `read_prefix` specified is overridden by the endpoint's instance profile.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Alternative: Databricks Secrets

If instance profiles cannot be used, [Databricks secrets](/concepts/databricks-secret-scopes.md) remain an option for both write and read authentication. For write, separate secret scopes (`<read-scope>` and `<write-scope>`) can be created with access key IDs and secret access keys (for DynamoDB) or user/password pairs (for SQL stores). The secrets are then referenced as a prefix during publish.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The feature engineering and serving platform
- [Third-party online stores](/concepts/third-party-online-stores-for-feature-serving.md) — External stores like Amazon DynamoDB
- Databricks Secrets — Alternative credentials store
- [Model Serving](/concepts/model-serving.md) — Serving MLflow models with instance profile authentication
- [Instance profile](/concepts/model-serving-instance-profile.md) — AWS IAM role for EC2 instances

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
