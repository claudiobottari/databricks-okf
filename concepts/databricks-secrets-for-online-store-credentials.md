---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 30e7df58588eb872891eaf3bfeebf52576b2870564d350c7ff79cd44a6f27ffc
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-secrets-for-online-store-credentials
    - DSFOSC
    - store credentials in Databricks secrets|store credentials in Databricks secrets
    - databricks-secrets-for-third-party-online-store-credentials
    - DSFTOSC
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Databricks Secrets for Online Store Credentials
description: Storing read-only and read-write credentials for third-party online stores in Databricks secret scopes, organized by prefix-based naming conventions for DynamoDB and SQL stores.
tags:
  - authentication
  - secrets
  - databricks
timestamp: "2026-06-19T17:37:08.888Z"
---

# Databricks Secrets for Online Store Credentials

**Databricks Secrets** provide a secure way to store read and write credentials (access keys, passwords) for third‑party online stores, such as Amazon DynamoDB or SQL‑based stores. When publishing feature tables or looking up features from served MLflow models, you can use these secrets instead of, or alongside, instance profiles.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## When to Use Databricks Secrets

Databricks recommends using [instance profiles](/concepts/instance-profile-databricks-on-aws.md) for authentication when possible. However, you can use Databricks Secrets for both write authentication (publishing feature tables) and read authentication (looking up features from served models) when instance profiles are not suitable. If you plan to use an instance profile for write authentication at the cluster level, you do not need a read‑write secret scope; similarly, if you use an instance profile for read authentication at the serving endpoint level, you do not need a read‑only secret scope.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Setting Up Secrets for Online Store Credentials

### Step 1: Create Secret Scopes

Create two secret scopes: one for read‑only access (`<read-scope>`) and one for read‑write access (`<write-scope>`). Alternatively, you can reuse existing secret scopes.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Step 2: Choose a Prefix

Pick a unique name for the target online store, referred to as `<prefix>`. This prefix is used to name the secrets consistently.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Step 3: Create Secrets for DynamoDB Online Stores

For DynamoDB online stores (works with any version of Feature Engineering client, and Feature Store client v0.3.8 and above), create the following secrets:^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

- Read‑only access key ID: `databricks secrets put-secret <read-scope> <prefix>-access-key-id`
- Read‑only secret access key: `databricks secrets put-secret <read-scope> <prefix>-secret-access-key`
- Read‑write access key ID: `databricks secrets put-secret <write-scope> <prefix>-access-key-id`
- Read‑write secret access key: `databricks secrets put-secret <write-scope> <prefix>-secret-access-key`

### Step 4: Create Secrets for SQL Online Stores

For SQL stores, create the following secrets:^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

- Read‑only user: `databricks secrets put-secret <read-scope> <prefix>-user`
- Read‑only password: `databricks secrets put-secret <read-scope> <prefix>-password`
- Read‑write user: `databricks secrets put-secret <write-scope> <prefix>-user`
- Read‑write password: `databricks secrets put-secret <write-scope> <prefix>-password`

## Using Secrets in Publishing and Lookup

After creating the secrets, you refer to them using a `write_secret_prefix` when publishing feature tables and a `read_secret_prefix` when configuring lookup. For code examples illustrating how to use these secrets, see [Publish features to a third‑party online store](/concepts/publishing-feature-tables-to-online-stores.md).^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Best Practices

- **Use a single shared scope**: There is a limit on the number of secret scopes per workspace. To avoid hitting this limit, you can define and share a single secret scope for accessing all online stores.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

- **Separate read and write credentials**: Using separate scopes for read‑only and read‑write access follows the principle of least privilege, ensuring that served models only have the read access they need.

- **Use instance profiles when possible**: Databricks recommends instance profiles over secrets for both write and read authentication, as they simplify credential management.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- Databricks Secrets — The general mechanism for storing sensitive credentials
- [Online Store](/concepts/online-feature-store.md) — Third‑party stores for feature serving
- [Feature Store](/concepts/feature-store.md) — The feature engineering and serving platform
- Instance Profile — An alternative authentication method using AWS IAM roles
- [Publish features to a third‑party online store](/concepts/publishing-feature-tables-to-online-stores.md) — Code examples for using secrets in publishing workflows
- MLflow Model Serving — Serving endpoints that look up features from online stores
- Feature Store Client — The client used for publishing and lookup operations

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
