---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 83607d57da5ad2b7202f3ece12e6d7953527195bec8931eeb8dd9b849c475e33
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-online-store-authentication
    - FSOSA
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Feature Store Online Store Authentication
description: Overview of authentication methods (instance profiles and Databricks secrets) for publishing to and reading from third-party online stores in Databricks Feature Store.
tags:
  - authentication
  - feature-store
  - databricks
timestamp: "2026-06-19T17:36:58.562Z"
---

Here is the wiki page for "Feature Store Online Store Authentication", written using only the provided source material.

---

# Feature Store Online Store Authentication

**Feature Store Online Store Authentication** encompasses the mechanisms required to authenticate operations on third-party online stores — such as Amazon DynamoDB or SQL-based stores — when publishing feature tables (write) and when looking up feature values from served MLflow models (read). Databricks supports two authentication methods: **instance profiles** attached to a cluster or serving endpoint, and **Databricks secrets** with explicit credential references. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Authentication for Publishing Feature Tables (Write)

Publishing feature tables to a third-party online store requires **write authentication**. Databricks recommends using an instance profile attached to a Databricks cluster. Alternatively, credentials can be stored in [Databricks secrets](/concepts/databricks-secret-scopes.md) and referenced via a `write_secret_prefix` when publishing. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Write Authentication via Instance Profile (DynamoDB only)

On clusters running Databricks Runtime 10.5 ML and above, the instance profile attached to the cluster can be used for write authentication when publishing to DynamoDB online stores. The instance profile or IAM user must have all of the following DynamoDB permissions:

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

To use this method: (1) create an instance profile with write permissions, (2) attach it to a Databricks cluster, (3) run the publishing code on that cluster. No explicit `write_secret_prefix` is required. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Write Authentication via Databricks Secrets

For stores that do not support instance profiles, or when you prefer to manage credentials separately, follow the instructions in [Use Databricks Secrets](#use-databricks-secrets-for-read-and-write-authentication) below. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Authentication for Looking Up Features (Read)

To enable Databricks-hosted MLflow models to connect to third-party online stores and look up feature values, **read authentication** must be provided. Databricks recommends using an instance profile configured to a served model. Alternatively, credentials can be stored in Databricks secrets and referenced via a `read_secret_prefix`. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Read Authentication via Instance Profile for Served Models

1. Create an instance profile with read-only permissions to the online store.
2. Configure your [Databricks serving endpoint](/concepts/databricks-model-serving-endpoint.md) to use that instance profile.

When this method is used, any `read_secret_prefix` specified in the publishing code is overridden with the instance profile. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Read Authentication via Databricks Secrets

Follow the instructions in the next section. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Use Databricks Secrets for Read and Write Authentication

This approach works for both publishing and lookups, and for all supported third-party online stores (DynamoDB and SQL stores). It involves creating secret scopes and storing credentials under a consistent naming scheme using a common prefix. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Setup Steps

1. Create two secret scopes (or reuse existing ones):
   - `<read-scope>` — contains credentials with read-only access.
   - `<write-scope>` — contains credentials with read-write access.

   If an instance profile is used for write authentication (cluster-level), the `<write-scope>` may be omitted. Similarly, if an instance profile is used for read authentication (serving endpoint-level), the `<read-scope>` may be omitted.

2. Choose a unique prefix for the target online store (shown as `<prefix>`).

3. Create secrets with the following keys:

**For DynamoDB** (works with any version of Feature Engineering client, and Feature Store client v0.3.8 and above):

| Scope | Secret Key | Value |
|-------|------------|-------|
| `<read-scope>` | `<prefix>-access-key-id` | IAM access key ID (read-only) |
| `<read-scope>` | `<prefix>-secret-access-key` | IAM secret access key (read-only) |
| `<write-scope>` | `<prefix>-access-key-id` | IAM access key ID (read-write) |
| `<write-scope>` | `<prefix>-secret-access-key` | IAM secret access key (read-write) |

**For SQL stores**:

| Scope | Secret Key | Value |
|-------|------------|-------|
| `<read-scope>` | `<prefix>-user` | Username (read-only) |
| `<read-scope>` | `<prefix>-password` | Password (read-only) |
| `<write-scope>` | `<prefix>-user` | Username (read-write) |
| `<write-scope>` | `<prefix>-password` | Password (read-write) |

^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Important Considerations

- There is a limit on the number of secret scopes per workspace. To avoid hitting this limit, you can define and share a single secret scope for accessing all online stores. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- For publishing code examples that illustrate how to use these secrets, see [Publish features to a third-party online store](/concepts/publishing-feature-tables-to-online-stores.md). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Summary

| Operation | Recommended Method | Alternative Method |
|-----------|-------------------|-------------------|
| **Write** (publishing) | Instance profile on cluster | Databricks secrets with `write_secret_prefix` |
| **Read** (lookup from served models) | Instance profile on serving endpoint | Databricks secrets with `read_secret_prefix` |

The table in the source documentation shows the authentication methods supported for each action. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md)
- [Online Store](/concepts/online-feature-store.md)
- Instance Profile
- Databricks Secrets
- [Databricks Serving Endpoint](/concepts/databricks-model-serving-endpoint.md)
- [Publish features to a third-party online store](/concepts/publishing-feature-tables-to-online-stores.md)

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
