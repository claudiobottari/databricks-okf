---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c75d02ca2884fc03f1c23690e8ad08c5f377ebcab4fb1eeaa440dabd68947d63
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secret-scope-management-for-feature-store
    - SSMFFS
    - Secret Scopes Management
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Secret Scope Management for Feature Store
description: Creating and managing Databricks secret scopes for accessing multiple online stores, including naming conventions (prefix-based) and avoiding scope limits by sharing scopes.
tags:
  - secrets
  - management
  - best-practices
timestamp: "2026-06-19T09:05:36.919Z"
---

# Secret Scope Management for Feature Store

**Secret Scope Management for Feature Store** refers to the process of creating and organizing Databricks Secrets to authenticate publishing and lookup operations for Third-Party Online Stores (such as DynamoDB or SQL stores) used by the [Feature Engineering client](/concepts/featureengineeringclient-api.md). Proper secret scope management ensures that write access (for publishing feature tables) and read access (for looking up features by served MLflow models) are configured securely and separately.

## Overview

When working with third-party online stores, [Feature Store](/concepts/feature-store.md) requires authentication for two distinct operations:

- **Publishing feature tables** to an online store → write authentication.  
- **Looking up features** from an online store with served MLflow models → read authentication.

Databricks provides two authentication methods: **instance profiles** and **Databricks secrets**. Secret scope management is the recommended fallback when instance profiles are not used. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Use Databricks Secrets for Feature Store Authentication

If you choose to use Databricks secrets instead of instance profiles, you must create two [secret scopes](/concepts/databricks-secret-scopes.md):

- A **read-only scope** (`<read-scope>`) containing credentials that allow only read access to the online store.  
- A **read-write scope** (`<write-scope>`) containing credentials that allow both read and write access. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

These scopes are then referenced by a `read_secret_prefix` or `write_secret_prefix` when publishing the feature table to the online store. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

You can also reuse existing secret scopes to avoid hitting the per-workspace secret scope limit. If you intend to use an instance profile for write authentication (attached at cluster level), you do not need the `<write-scope>`. Similarly, if you use an instance profile for read authentication (configured at the Databricks Serving endpoint level), you do not need the `<read-scope>`. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Setting Up Secret Scopes and Secrets

To configure authentication using secrets:

1. **Create two secret scopes** – one for read-only access and one for read-write access – using the [Databricks secrets CLI or API](https://docs.databricks.com/aws/en/security/secrets/#secrets). The source document refers to them as `<read-scope>` and `<write-scope>`.
2. **Pick a unique prefix** for the target online store (shown as `<prefix>`). This prefix is used in the secret keys.
3. **Add the required secrets** to each scope according to the online store type. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Secret Naming Conventions

### For DynamoDB online stores

Works with any version of the Feature Engineering client, and Feature Store client v0.3.8 and above. Create the following secrets:

- **Read-only scope:**  
  - `databricks secrets put-secret <read-scope> <prefix>-access-key-id`  
  - `databricks secrets put-secret <read-scope> <prefix>-secret-access-key`

- **Read-write scope:**  
  - `databricks secrets put-secret <write-scope> <prefix>-access-key-id`  
  - `databricks secrets put-secret <write-scope> <prefix>-secret-access-key` ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### For SQL stores

- **Read-only scope:**  
  - `databricks secrets put-secret <read-scope> <prefix>-user`  
  - `databricks secrets put-secret <read-scope> <prefix>-password`

- **Read-write scope:**  
  - `databricks secrets put-secret <write-scope> <prefix>-user`  
  - `databricks secrets put-secret <write-scope> <prefix>-password` ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

After setting up these secrets, you can reference them in the online store spec using `read_secret_prefix` and `write_secret_prefix` when publishing or looking up features. For code examples, see [Publish features to a third-party online store](/concepts/publishing-feature-tables-to-online-stores.md). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Best Practices and Limitations

- **Separate scopes for read and write** is a security best practice – the read scope can be shared with model serving endpoints without exposing write credentials. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- **Secret scope limits** – There is a limit on the number of secret scopes per workspace. To avoid hitting this limit, you can define and share a single secret scope for accessing all online stores, reusing the same scope across multiple prefixes. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- **Instance profiles as an alternative** – If you attach an instance profile with write permissions to a Databricks cluster (Databricks Runtime 10.5 ML and above), you do not need to provide `write_secret_prefix`. Similarly, configuring an instance profile on a Databricks serving endpoint overrides any `read_prefix`. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- Databricks Secrets – General secret storage and management.
- Third-Party Online Stores – External stores (e.g., DynamoDB, SQL stores) used for real-time feature serving.
- [Feature Store](/concepts/feature-store.md) – Centralized feature management platform.
- Instance Profile – IAM role attached to clusters or serving endpoints for AWS authentication.
- [Publish Features to Online Store](/concepts/publishing-feature-tables-to-online-stores.md) – The operation that consumes `read_secret_prefix` and `write_secret_prefix`.
- MLflow Model Serving – The serving infrastructure that performs online feature lookups.

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
