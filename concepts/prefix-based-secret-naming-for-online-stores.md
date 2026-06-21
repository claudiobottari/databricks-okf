---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3478c97c02167ea5df547c93626a6f6ff843792a8300d9c9d561b65841137a4e
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prefix-based-secret-naming-for-online-stores
    - PSNFOS
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Prefix-Based Secret Naming for Online Stores
description: A naming convention using a unique prefix combined with -access-key-id/-secret-access-key (DynamoDB) or -user/-password (SQL stores) to organize credentials in Databricks secret scopes.
tags:
  - secrets
  - naming-convention
  - online-store
timestamp: "2026-06-19T17:37:25.184Z"
---

# Prefix-Based Secret Naming for Online Stores

**Prefix-Based Secret Naming for Online Stores** is a convention for organizing credentials in Databricks Secrets when configuring authentication for third-party online stores used with [Feature Store](/concepts/feature-store.md). Under this approach, a shared textual prefix, such as `<prefix>`, is appended to secret key names to associate multiple credential values (access key IDs, secret access keys, usernames, passwords) with a single target online store.

## Overview

When authenticating to a third-party online store — such as Amazon DynamoDB or a SQL Online Store — Feature Store requires separate credentials for read-only and read-write access. Using a consistent, prefix-based naming scheme ensures that each online store's credentials can be looked up reliably by the Feature Engineering client and Feature Store client. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Secret Key Patterns by Store Type

The exact secrets that must be created depend on the type of online store.

### DynamoDB Online Stores

For DynamoDB (works with any version of the Feature Engineering client, and Feature Store client v0.3.8 and above), create the following secrets: ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

| Scope | Secret Key | Description |
|---|---|---|
| `<read-scope>` | `<prefix>-access-key-id` | Access key ID for the IAM user with read-only access |
| `<read-scope>` | `<prefix>-secret-access-key` | Secret access key for the IAM user with read-only access |
| `<write-scope>` | `<prefix>-access-key-id` | Access key ID for the IAM user with read-write access |
| `<write-scope>` | `<prefix>-secret-access-key` | Secret access key for the IAM user with read-write access |

### SQL Online Stores

For SQL-based online stores, create the following secrets: ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

| Scope | Secret Key | Description |
|---|---|---|
| `<read-scope>` | `<prefix>-user` | Username for the user with read-only access |
| `<read-scope>` | `<prefix>-password` | Password for the user with read-only access |
| `<write-scope>` | `<prefix>-user` | Username for the user with read-write access |
| `<write-scope>` | `<prefix>-password` | Password for the user with read-write access |

## Choosing the Prefix

The `<prefix>` must be a unique name that identifies the target online store. This same prefix is then referenced in the `write_secret_prefix` or `read_secret_prefix` parameter when publishing feature tables to the online store. Databricks recomments picking a meaningful name, such as the name of the store or an identifier for the team or project using it. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Secret Scopes

Secrets are stored in two separate [Secret Scopes](/concepts/databricks-secret-scopes.md):

- **`<read-scope>`**: Contains credentials for read-only access.
- **`<write-scope>`**: Contains credentials for read-write access.

If you intend to use an Instance Profile for write authentication (configured at the cluster level), you do not need to create the `<write-scope>`. Similarly, if you intend to use an instance profile for read authentication (configured at the [Databricks Serving Endpoint](/concepts/databricks-model-serving-endpoint.md) level), you do not need to create the `<read-scope>`. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

There is a limit on the number of secret scopes per workspace. To avoid hitting this limit, you can define and share a single secret scope for accessing all online stores. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Usage Context

Once the secrets are created, they are referenced when publishing a feature table. For example, when calling the API to publish to a third-party online store, you provide the `write_secret_prefix` (e.g., `<write-scope>.<prefix>`) and optionally the `read_secret_prefix`. The Databricks client then constructs the full secret key names (e.g., `<prefix>-access-key-id`) automatically. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- Feature Store Authentication — General authentication patterns for online stores
- Databricks Secrets — Secure credential storage mechanism
- [Secret Scopes](/concepts/databricks-secret-scopes.md) — Organizational boundaries for secrets in a workspace
- Instance Profile — Alternative authentication method using IAM roles
- Publishing Feature Tables to Third-Party Online Stores — End-to-end workflow for publishing features
- [Looking Up Features from Online Stores](/concepts/publishing-feature-tables-to-online-stores.md) — Reading feature values at serving time

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
