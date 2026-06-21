---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22d0e76bd85152605af526a9d1b423b2a88924de7d9663181064ca5389f7cbd2
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-store-authentication-via-secret-prefixes
    - OSAVSP
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Online Store Authentication via Secret Prefixes
description: Using write_secret_prefix and read_secret_prefix parameters in online store specifications to reference Databricks secrets for authentication.
tags:
  - authentication
  - secrets
  - feature-store
  - configuration
timestamp: "2026-06-18T10:50:09.037Z"
---

# Online Store Authentication via Secret Prefixes

**Online Store Authentication via Secret Prefixes** is a method for providing read and write credentials to third-party online stores in Databricks Feature Engineering using Databricks Secrets. When publishing feature tables to or looking up features from third-party online stores, you can store credentials in Databricks secrets and reference them using a `read_secret_prefix` or `write_secret_prefix` parameter.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Overview

Publishing feature tables to a third-party online store requires write authentication, and looking up features requires read authentication. Databricks recommends using [instance profiles](/concepts/instance-profile-databricks-on-aws.md) for authentication where possible. However, when instance profiles are not suitable, you can store credentials in Databricks secrets and refer to them via a secret prefix when publishing or reading from the online store.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Setting Up Secret Prefixes

To use secret prefixes, you first create secret scopes and secrets in Databricks Secrets, then reference them by a consistent prefix name when interacting with the online store.

### Step 1: Create Secret Scopes

Create two secret scopes: one for read-only access (`<read-scope>`) and one for read-write access (`<write-scope>`). You can also reuse existing secret scopes. If you are using an instance profile for write authentication at the cluster level or for read authentication at the serving endpoint level, you do not need to create both scopes.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Step 2: Choose a Prefix Name

Pick a unique name for the target online store, shown as `<prefix>`. This same prefix name is used when creating secrets and when referencing them in your code.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Step 3: Create Secrets

The secrets you create depend on the type of online store.

**For DynamoDB** (works with any version of Feature Engineering client and Feature Store client v0.3.8 and above):^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

- Read-only access key ID: `databricks secrets put-secret <read-scope> <prefix>-access-key-id`
- Read-only secret access key: `databricks secrets put-secret <read-scope> <prefix>-secret-access-key`
- Read-write access key ID: `databricks secrets put-secret <write-scope> <prefix>-access-key-id`
- Read-write secret access key: `databricks secrets put-secret <write-scope> <prefix>-secret-access-key`

**For SQL stores**:^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

- Read-only user: `databricks secrets put-secret <read-scope> <prefix>-user`
- Read-only password: `databricks secrets put-secret <read-scope> <prefix>-password`
- Read-write user: `databricks secrets put-secret <write-scope> <prefix>-user`
- Read-write password: `databricks secrets put-secret <write-scope> <prefix>-password`

### Secret Scope Limit

There is a limit on the number of secret scopes per workspace. To avoid hitting this limit, you can define and share a single secret scope for accessing all online stores.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Using Secret Prefixes in Code

When publishing feature tables or looking up features, you pass the `read_secret_prefix` and `write_secret_prefix` parameters to the online store specification. The prefix value combines the scope name and the chosen prefix name in the format `{scope}.{prefix}`.

For code examples illustrating how to use these secrets, see [Publish features to a third-party online store](/concepts/publishing-feature-tables-to-online-stores.md).^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Alternative Authentication Methods

### Instance Profile for Write Authentication

On clusters running Databricks Runtime 10.5 ML and above, you can use the instance profile attached to the cluster for write authentication when publishing to DynamoDB online stores. When using this method, you do not need to provide explicit secret credentials or a `write_secret_prefix` to the online store specification. The required instance profile permissions include DynamoDB operations such as `dynamodb:PutItem`, `dynamodb:GetItem`, `dynamodb:Query`, and others.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Instance Profile for Read Authentication

To enable Databricks-hosted MLflow models to connect to third-party online stores for feature lookup, you can configure a [Databricks serving endpoint](/concepts/databricks-model-serving-endpoint.md) to use an instance profile. When you use this method, you do not need to specify a `read_prefix`, and any `read_prefix` specified is overridden with the instance profile.^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Supported Actions

The following table shows the authentication methods supported for each action:^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

| Action | Recommended Method | Alternative Method |
|---|---|---|
| Publish (write) | Instance profile attached to cluster | Databricks secrets with `write_secret_prefix` |
| Lookup (read) | Instance profile configured to served model | Databricks secrets with `read_secret_prefix` |

## Related Concepts

- Databricks Secrets — The secrets management system used to store credentials
- [Instance Profiles](/concepts/instance-profile-databricks-on-aws.md) — IAM roles that can be attached to clusters or serving endpoints
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The service for creating and managing features
- [Online Store](/concepts/online-feature-store.md) — The target storage system for publishing features
- DynamoDB — AWS DynamoDB as an online store backend
- [Databricks Serving Endpoint](/concepts/databricks-model-serving-endpoint.md) — Model serving endpoints that can use instance profiles

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
