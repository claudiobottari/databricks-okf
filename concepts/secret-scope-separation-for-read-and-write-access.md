---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1885dfea9125e9dc5cdf76be97aeffcd668140d29b11fb886329eed137863c8c
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secret-scope-separation-for-read-and-write-access
    - Write Access and Secret Scope Separation for Read
    - SSSFRAWA
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Secret Scope Separation for Read and Write Access
description: The pattern of creating two separate Databricks secret scopes — one for read-only access and one for read-write access — to manage online store credentials with least-privilege principles.
tags:
  - secrets
  - least-privilege
  - security-pattern
  - feature-store
timestamp: "2026-06-18T14:29:32.042Z"
---

#Secret Scope Separation for Read and Write Access

**Secret Scope Separation for Read and Write Access** is a security pattern used when connecting to third-party online stores from Databricks. It involves creating two distinct [Databricks Secret Scopes](/concepts/databricks-secret-scopes.md)—one for read-only credentials and one for read-write credentials—so that publishing feature tables and serving MLflow models use the minimum necessary permissions. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Overview

Third-party online stores, such as Amazon DynamoDB or SQL online stores, require authentication for two operations: writing feature tables during publishing and reading feature values during model inference. To follow the principle of least privilege, Databricks recommends separating the credentials used for each action. This separation is achieved by storing read-only credentials in a dedicated secret scope and read-write credentials in another. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## When to Use Separate Secret Scopes

Separate secret scopes are used when you are not relying on an instance profile for authentication. If you use an instance profile for write authentication (attached to a cluster) or for read authentication (configured on a serving endpoint), the corresponding secret scope is unnecessary. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

The following table summarizes the authentication methods for each action:

| Action | Recommended Method | Alternative Method |
|--------|-------------------|-------------------|
| Publishing feature tables (write) | Instance profile attached to cluster | Databricks secrets with a `write_secret_prefix` |
| Looking up features from served models (read) | Instance profile configured on serving endpoint | Databricks secrets with a `read_secret_prefix` |

## Creating Separate Secret Scopes

To implement secret scope separation:

1. **Create two secret scopes**: one for read-only access (e.g., `<read-scope>`) and one for read-write access (e.g., `<write-scope>`). You can reuse existing scopes as long as they respect the permission boundary. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

2. **Pick a unique prefix** that identifies the target online store (e.g., `<prefix>`). This prefix is used to name the individual secrets within each scope. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

3. **Store the credentials** as secrets in the appropriate scope, following the naming convention that includes the prefix and the credential type. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Credential Secrets for DynamoDB

For DynamoDB online stores, create the following secrets: ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

**Read-only scope:**
- `<prefix>-access-key-id` – IAM user access key ID with read-only permissions.
- `<prefix>-secret-access-key` – associated secret key.

**Read-write scope:**
- `<prefix>-access-key-id` – IAM user access key ID with read-write permissions.
- `<prefix>-secret-access-key` – associated secret key.

### Credential Secrets for SQL Stores

For SQL online stores, create the following secrets: ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

**Read-only scope:**
- `<prefix>-user` – database user with read-only access.
- `<prefix>-password` – password for that user.

**Read-write scope:**
- `<prefix>-user` – database user with read-write access.
- `<prefix>-password` – password for that user.

## Using the Secrets in Publishing and Serving

When publishing feature tables, you refer to the write-scope and read-scope in the online store specification’s `write_secret_prefix` and `read_secret_prefix` parameters. The write-secret prefix points to the read-write scope, and the read-secret prefix points to the read-only scope. For code examples, see [Publish features to a third-party online store](/concepts/publishing-feature-tables-to-online-stores.md). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Best Practices

- **Scope sharing**: To avoid hitting the workspace limit on the number of secret scopes, define and share a single read-only scope and a single read-write scope across all online stores. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- **Prefix uniqueness**: Choose a unique prefix for each online store to prevent naming conflicts when multiple stores share the same scope.
- **Instance profile alternative**: If possible, use instance profiles instead of secrets for production workloads, as they eliminate the need to manage secret keys manually.

## Related Concepts

- [Databricks Secret Scopes](/concepts/databricks-secret-scopes.md)
- [Instance profiles for third-party online stores](/concepts/instance-profile-authentication-for-feature-store.md)
- [Publish features to a third-party online store](/concepts/publishing-feature-tables-to-online-stores.md)
- [Feature Engineering client](/concepts/featureengineeringclient-api.md)
- Model Serving with online stores

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

---

*Inferred paragraphs: 0*

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
