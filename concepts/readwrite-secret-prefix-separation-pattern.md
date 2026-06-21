---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a15cad2cedc76bc70d6b397812094157164e0676443a17d47f5536bed934f43a
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - readwrite-secret-prefix-separation-pattern
    - RSPSP
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Read/Write Secret Prefix Separation Pattern
description: The pattern of using separate secret scopes (read-scope vs write-scope) and a shared prefix name to manage independent read-only and read-write credentials for the same online store.
tags:
  - authentication
  - secrets
  - pattern
timestamp: "2026-06-19T22:10:21.621Z"
---

## Read/Write Secret Prefix Separation Pattern

The **Read/Write Secret Prefix Separation Pattern** is an authentication strategy for [Databricks Feature Store](/concepts/databricks-feature-store.md) when publishing feature tables to, or looking up features from, a [third-party online store](/concepts/third-party-online-stores-for-feature-serving.md) (e.g., DynamoDB, SQL‑based stores). The pattern uses two [Databricks secrets|Databricks secret scopes](/concepts/databricks-secret-scopes.md)—one for read‑only access, one for read‑write access—and a shared prefix to name the secrets, thereby isolating read credentials from write credentials. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Motivation

Publishing feature tables requires write authentication; looking up features (often from a served MLflow model) requires only read authentication. By separating the two credential sets, the pattern adheres to the principle of least privilege: a served model that only performs lookups never holds write capabilities. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### How It Works

1. **Create two secret scopes**: one read‑only scope (e.g., `<read-scope>`) and one read‑write scope (e.g., `<write-scope>`). Existing scopes can be reused. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
2. **Choose a unique prefix** (called `<prefix>`) that identifies the target online store. All secrets for that store use this prefix in their key names. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
3. **Store credentials** in the appropriate scope using the prefix. The naming convention differs by store type:

   - **For DynamoDB** (or any AWS‑based store):
     - Read‑only: `databricks secrets put-secret <read-scope> <prefix>-access-key-id` and `databricks secrets put-secret <read-scope> <prefix>-secret-access-key`
     - Read‑write: `databricks secrets put-secret <write-scope> <prefix>-access-key-id` and `databricks secrets put-secret <write-scope> <prefix>-secret-access-key`
   - **For SQL stores**:
     - Read‑only: `databricks secrets put-secret <read-scope> <prefix>-user` and `databricks secrets put-secret <read-scope> <prefix>-password`
     - Read‑write: `databricks secrets put-secret <write-scope> <prefix>-user` and `databricks secrets put-secret <write-scope> <prefix>-password`

   ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

4. **Refer to credentials in the online store specification** using the `write_secret_prefix` (for write operations) and `read_secret_prefix` (for read operations). The system then resolves the correct scope and secret names automatically. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Interaction with Instance Profiles

The pattern is fully optional when an instance profile is used:

- For write authentication, an instance profile attached to the Databricks cluster can replace the `<write-scope>`. In that case, no write secret scope is needed. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- For read authentication, an instance profile configured on the [Databricks serving endpoint|model serving endpoint](/concepts/databricks-model-serving-endpoint.md) can replace the `<read-scope>`. Any `read_secret_prefix` specified is overridden by the endpoint instance profile. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

The pattern is most useful when instance profiles are not available or when finer‑grained control is required.

### Related Patterns and Concepts

- Secret scope sharing – A single read/write secret scope can be shared across multiple online stores, but the prefix approach keeps credentials separate per store.
- [Third-party online store authentication](/concepts/third-party-online-store-authentication-for-feature-serving.md) – Overview of the two authentication methods (instance profile vs. secrets).
- [Databricks Feature Store publish workflow](/concepts/databricks-feature-store-workflow.md) – How `write_secret_prefix` and `read_secret_prefix` are used in the publish API.
- Least privilege principle – The security rationale for separating read and write credentials.

### Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
