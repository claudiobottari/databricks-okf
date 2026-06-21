---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d6e5f0d6975d68ee3e630baef4cf3b054a098a17518989d0ec07e5b82681cf9
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - write-authentication-for-publishing-feature-tables-to-third-party-online-stores
    - WAFPFTTTOS
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Write Authentication for Publishing Feature Tables to Third-Party Online Stores
description: Methods and requirements for authenticating write operations when publishing Databricks feature tables to external online stores like DynamoDB or SQL databases.
tags:
  - authentication
  - feature-store
  - databricks
  - write-access
timestamp: "2026-06-18T10:49:59.987Z"
---

# Write Authentication for Publishing Feature Tables to Third-Party Online Stores

**Write authentication** is required when publishing feature tables to a third-party online store in the [Databricks Feature Store](/concepts/databricks-feature-store.md). Without proper write credentials, publishing operations will fail, and feature values cannot be served to downstream MLflow models or other consumers. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Authentication Methods

Databricks supports two primary methods for providing write authentication when publishing to third-party online stores:^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

| Method | Recommended for | Description |
|---|---|---|
| **Instance profile** | DynamoDB online stores | Attach an IAM role with write permissions to the cluster |
| **Databricks secrets** | Any online store | Store credentials in [secret scopes](/concepts/databricks-secret-scopes.md) |

The table below shows the authentication methods supported for each action:

| Action | Authentication Method |
|---|---|
| Publish (write) | Instance profile or Databricks secrets |
| Lookup (read) | Instance profile or Databricks secrets |

^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Required Permissions

The instance profile or IAM user used for write authentication must have all of the following permissions on the target DynamoDB table:^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

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

## Providing Write Authentication Through an Instance Profile

Databricks recommends providing write authentication through an instance profile attached to a Databricks cluster, particularly for DynamoDB online stores. This approach works on clusters running **Databricks Runtime 10.5 ML and above**. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

When using an instance profile, you do not need to provide explicit secret credentials or a `write_secret_prefix` to the [online store spec](/concepts/onlinestoreconfig.md). The cluster's attached IAM role handles authentication automatically. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Steps

1. Create an IAM role with a policy that grants the required DynamoDB permissions.
2. Create an instance profile from that IAM role.
3. [Add the instance profile to Databricks](/concepts/instance-profile-databricks-on-aws.md).
4. Attach the instance profile to a cluster when launching it.
5. Run the publishing code on that cluster.

^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Providing Write Credentials Using Databricks Secrets

If you cannot use an instance profile, store credentials in [Databricks secrets](/concepts/databricks-secret-scopes.md) and reference them with a `write_secret_prefix` when publishing. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### For DynamoDB Online Stores

Create a secret scope for write access and store the following secrets:^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

- **Access key ID** for the IAM user with write access: `databricks secrets put-secret <write-scope> <prefix>-access-key-id`
- **Secret access key** for the IAM user with write access: `databricks secrets put-secret <write-scope> <prefix>-secret-access-key`

### For SQL Online Stores

Create a secret scope for write access and store:^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

- **User** with write access: `databricks secrets put-secret <write-scope> <prefix>-user`
- **Password** for the write-access user: `databricks secrets put-secret <write-scope> <prefix>-password`

## Read Authentication for Model Serving

When [served MLflow models](/concepts/legacy-mlflow-model-serving.md) need to look up features from third-party online stores, they require read authentication. This can be configured using:^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

- An instance profile configured on the [Databricks serving endpoint](/concepts/databricks-model-serving-endpoint.md)
- [Databricks secrets](/concepts/databricks-secret-scopes.md) with a `read_secret_prefix`

When publishing a table for lookup, any `read_prefix` specified is overridden by the instance profile if one is configured at the serving endpoint. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Best Practices

- **Use instance profiles when possible** — they eliminate the need to manage secrets separately and reduce operational complexity. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- **Reuse secret scopes** — there is a limit on secret scopes per workspace. Define a single shared secret scope for all online store access. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- **Separate read and write scopes** — create one scope for read-only access and another for read-write access to follow the principle of least privilege. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- [Feature Table Publishing](/concepts/feature-table-publishing.md) — The process of making features available to online stores
- Online Store Spec — Configuration for connecting to a third-party online store
- Databricks Secrets — Secure credential storage for Databricks
- MLflow Model Serving — Serving MLflow models with feature lookup capabilities
- Instance Profile — IAM role attachment for Databricks clusters

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
