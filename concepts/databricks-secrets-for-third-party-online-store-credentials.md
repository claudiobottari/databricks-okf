---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: be98165e17d74082a7d9de1eaf70afffc6b3c517579eba384228003ed0f33167
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-secrets-for-third-party-online-store-credentials
    - DSFTOSC
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Databricks Secrets for Third-Party Online Store Credentials
description: Storing read-only and read-write credentials (access keys, passwords, usernames) in Databricks secret scopes with a consistent prefix naming scheme for authenticating to online stores.
tags:
  - authentication
  - secrets
  - feature-store
timestamp: "2026-06-19T22:09:18.263Z"
---

# Databricks Secrets for Third-Party Online Store Credentials

**Databricks Secrets for Third-Party Online Store Credentials** is a method for storing and managing authentication credentials required to publish feature tables to and look up features from third-party online stores, such as Amazon DynamoDB or SQL-based stores. This approach uses Databricks Secrets to securely store access keys, secret access keys, usernames, and passwords, and then references them through a `write_secret_prefix` or `read_secret_prefix` when publishing feature tables. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Overview

When working with third-party online stores in the [Databricks Feature Store](/concepts/databricks-feature-store.md), you must provide authentication for two distinct operations:

- **Write authentication** — Required for publishing feature tables to the online store.
- **Read authentication** — Required for looking up features from the online store, typically by served MLflow Models.

Databricks supports two authentication methods: [Instance Profiles](/concepts/instance-profile-databricks-on-aws.md) and Databricks Secrets. While instance profiles are recommended for simplicity, Databricks Secrets provide a flexible alternative when instance profiles are not available or when you need separate credentials for read and write access. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## When to Use Databricks Secrets

Use Databricks Secrets for third-party online store credentials in the following scenarios:

- You cannot use an instance profile for write authentication (e.g., the cluster does not have an appropriate instance profile attached).
- You cannot use an instance profile for read authentication (e.g., the serving endpoint does not have an instance profile configured).
- You need separate credentials for read-only access and read-write access to the online store.
- You want to manage credentials centrally using [Secret Scopes](/concepts/databricks-secret-scopes.md) and rotate them without modifying code. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Setting Up Secrets

### Step 1: Create Secret Scopes

Create two [Secret Scopes](/concepts/databricks-secret-scopes.md) — one for read-only access and one for read-write access. You can also reuse existing secret scopes if they already contain the required credentials. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

If you intend to use an instance profile for write authentication (configured at the Databricks cluster level), you do not need to create a write scope. Similarly, if you intend to use an instance profile for read authentication (configured at the Databricks Serving endpoint level), you do not need to create a read scope. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Step 2: Create Secrets with a Prefix

Pick a unique name for the target online store, referred to as `<prefix>`. The prefix is used to name the secrets consistently. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

#### For DynamoDB Online Stores

Create the following secrets using the Databricks CLI:

- **Read-only access:**
  - `databricks secrets put-secret <read-scope> <prefix>-access-key-id`
  - `databricks secrets put-secret <read-scope> <prefix>-secret-access-key`

- **Read-write access:**
  - `databricks secrets put-secret <write-scope> <prefix>-access-key-id`
  - `databricks secrets put-secret <write-scope> <prefix>-secret-access-key`

^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

#### For SQL Online Stores

Create the following secrets:

- **Read-only access:**
  - `databricks secrets put-secret <read-scope> <prefix>-user`
  - `databricks secrets put-secret <read-scope> <prefix>-password`

- **Read-write access:**
  - `databricks secrets put-secret <write-scope> <prefix>-user`
  - `databricks secrets put-secret <write-scope> <prefix>-password`

^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Step 3: Reference Secrets When Publishing

When publishing feature tables to the online store, reference the secrets using the `write_secret_prefix` and `read_secret_prefix` parameters in the Online Store Spec. The prefix format is `<scope>:<prefix>`. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

For code examples illustrating how to use these secrets, see Publish Features to a Third-Party Online Store. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Limitations

There is a limit on the number of secret scopes per workspace. To avoid hitting this limit, you can define and share a single secret scope for accessing all online stores. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Alternative: Instance Profile Authentication

Databricks recommends using [Instance Profiles](/concepts/instance-profile-databricks-on-aws.md) as an alternative to Databricks Secrets:

- **For write authentication:** Attach an instance profile with write permissions to the Databricks cluster. This works on clusters running Databricks Runtime 10.5 ML and above for DynamoDB online stores. When using an instance profile, you do not need to provide explicit secret credentials or a `write_secret_prefix`. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

- **For read authentication:** Configure the [Databricks Serving Endpoint](/concepts/databricks-model-serving-endpoint.md) to use an instance profile. When publishing the table, any `read_prefix` specified is overridden with the instance profile. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- Databricks Secrets — General mechanism for storing sensitive information
- [Secret Scopes](/concepts/databricks-secret-scopes.md) — Organizational containers for secrets
- [Instance Profiles](/concepts/instance-profile-databricks-on-aws.md) — IAM role-based authentication alternative
- Online Store Spec — Configuration object for online store connections
- [Feature Store](/concepts/feature-store.md) — Central repository for feature engineering
- Publish Features to a Third-Party Online Store — Code examples for using secrets
- MLflow Models — Served models that look up features from online stores

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
