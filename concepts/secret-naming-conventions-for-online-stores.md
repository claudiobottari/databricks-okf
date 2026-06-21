---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fca02e49d1b43fe88d6fb8daac093f55735b769bd47c74520c39642d3a3b809f
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secret-naming-conventions-for-online-stores
    - SNCFOS
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Secret Naming Conventions for Online Stores
description: Standardized naming pattern for Databricks secrets targeting online stores, using scope-prefix-key combinations with store-specific keys (e.g., access-key-id, secret-access-key, user, password).
tags:
  - databricks
  - secrets
  - naming-convention
  - aws
timestamp: "2026-06-19T14:06:06.529Z"
---

# Secret Naming Conventions for Online Stores

**Secret Naming Conventions for Online Stores** refers to the standardized naming pattern used when storing credentials for third-party online stores (e.g., DynamoDB, SQL stores) in [Databricks secrets](/concepts/databricks-secret-scopes.md). By following a predictable naming scheme, Databricks workloads can locate the correct credentials for read or write authentication based on a user-chosen prefix.

## Overview

When using [Databricks secrets](/concepts/databricks-secret-scopes.md) to authenticate with a third-party online store, you create two [secret scopes](/concepts/databricks-secret-scopes.md): one for read-only access and one for write (read-write) access. You then choose a unique name (the `prefix`) that identifies the target online store. All secrets for that store must follow a specific naming convention using that prefix. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Naming Pattern

The secret key (name) always takes the form:

```
<prefix>-<credential-type>
```

where `<prefix>` is a unique identifier you pick for the online store (e.g., `my-online-store`), and `<credential-type>` depends on the store type.

### DynamoDB Secrets

For DynamoDB online stores, create the following secrets in each applicable scope: ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

| Secret Key                | Contains                                    |
|---------------------------|---------------------------------------------|
| `<prefix>-access-key-id`     | AWS access key ID for the IAM user         |
| `<prefix>-secret-access-key` | AWS secret access key for the IAM user     |

**Example**: If your prefix is `prod-features`, you would create secrets named `prod-features-access-key-id` and `prod-features-secret-access-key`.

### SQL Store Secrets

For SQL-based online stores, create the following secrets in each applicable scope: ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

| Secret Key          | Contains                          |
|---------------------|-----------------------------------|
| `<prefix>-user`     | Username for database access      |
| `<prefix>-password` | Password for database access      |

**Example**: With prefix `analytics-store`, you create `analytics-store-user` and `analytics-store-password`.

## Scope Separation

The same prefix is used in both the read-only scope and the read-write scope. This allows code to reference the same logical store while automatically picking the correct credentials based on whether the operation is read or write. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Best Practices

- Choose a prefix that uniquely identifies the online store (e.g., `my-dynamodb-production`, `my-sql-customer-store`).
- Use the same prefix consistently in both secret scopes to simplify configuration.
- For DynamoDB stores, you can optionally use an instance profile instead of secrets for write authentication (cluster‑level) and read authentication (model serving), eliminating the need for the corresponding secrets. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- [Databricks secrets](/concepts/databricks-secret-scopes.md) – The secure credential storage system.
- [Secret scopes](/concepts/databricks-secret-scopes.md) – Containers that organize secrets and control access.
- [Online store](/concepts/online-feature-store.md) – A third‑party feature store (e.g., DynamoDB, SQL) used for low‑latency feature serving.
- Feature Store Authentication – Broader guidance on read/write authentication for online stores.
- [Publish features to a third-party online store](/concepts/publishing-feature-tables-to-online-stores.md) – Code examples that use these secret conventions.

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
