---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b3636bfd13dc4076b836f32b32ed428e6cd0ce7008691caaad64dbca8a469c5b
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - read-vs-write-authentication-separation
    - RVWAS
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Read vs Write Authentication Separation
description: Architectural pattern where read and write authentication for online stores use separate credentials, instance profiles, and secret scopes to enforce least-privilege access.
tags:
  - databricks
  - authentication
  - security
  - architecture
timestamp: "2026-06-19T14:05:53.674Z"
---

# Read vs Write Authentication Separation

**Read vs Write Authentication Separation** is a security pattern used in [Databricks Feature Store](/concepts/databricks-feature-store.md) and [third-party online stores](/concepts/third-party-online-stores-for-feature-serving.md) where different credentials are used for reading feature values versus publishing (writing) feature tables. This separation ensures that production serving endpoints have only the minimal permissions needed for lookup operations, while write operations require more privileged credentials.

## Overview

When working with third-party online stores such as Amazon DynamoDB or SQL-based stores, Databricks supports distinct authentication paths for read and write operations. Publishing feature tables to a third-party online store requires write authentication, while looking up features from served MLflow models requires read authentication. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Authentication Methods

The following authentication methods are supported for each action:

| Action | Authentication Method |
|--------|----------------------|
| Publishing (write) | Instance profile attached to a Databricks cluster, or Databricks secrets |
| Lookup (read) | Instance profile configured to a served model, or Databricks secrets |

^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Write Authentication

To publish feature tables to a third-party online store, you must provide write authentication. Databricks recommends providing write authentication through an instance profile attached to a Databricks cluster. Alternatively, you can store credentials in [Databricks secrets](/concepts/databricks-secret-scopes.md) and refer to them using a `write_secret_prefix` when publishing. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Instance Profile for Write

On clusters running Databricks Runtime 10.5 ML and above, you can use the instance profile attached to the cluster for write authentication when publishing to DynamoDB online stores. The instance profile or IAM user should have permissions including `dynamodb:PutItem`, `dynamodb:BatchWriteItem`, `dynamodb:CreateTable`, and other write-related DynamoDB actions. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Secrets for Write

If using Databricks secrets for write authentication, create a secret scope with read-write credentials. For DynamoDB, this includes an access key ID and secret access key for an IAM user with read-write access. For SQL stores, this includes a user and password with read-write access. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Read Authentication

To enable Databricks-hosted MLflow models to connect to third-party online stores and look up feature values, you must provide read authentication. Databricks recommends providing lookup authentication through an instance profile configured to a served model. Alternatively, you can store credentials in Databricks secrets and refer to them using a `read_secret_prefix`. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Instance Profile for Read

Create an instance profile with read-only permissions to the online store, then configure your Databricks serving endpoint to use that instance profile. When publishing your table, you do not need to specify a `read_prefix`, and any `read_prefix` specified is overridden with the instance profile. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

### Secrets for Read

If using Databricks secrets for read authentication, create a separate secret scope with read-only credentials. For DynamoDB, this includes an access key ID and secret access key for an IAM user with read-only access. For SQL stores, this includes a user and password with read-only access. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Using Databricks Secrets

To set up authentication with Databricks secrets:

1. Create two secret scopes: one for read-only access (`<read-scope>`) and one for read-write access (`<write-scope>`). Alternatively, reuse existing secret scopes.
2. Pick a unique name for the target online store (`<prefix>`).
3. Create the appropriate secrets for your store type (DynamoDB or SQL).

If you intend to use an instance profile for write authentication (configured at Databricks cluster level), you do not need to include the `<write-scope>`. If you intend to use an instance profile for read authentication (configured at Databricks Serving endpoint level), you do not need to include the `<read-scope>`. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Best Practices

- **Use separate credentials for read and write operations** to follow the principle of least privilege. Production serving endpoints should only have read access to online stores. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- **Prefer instance profiles** over secrets when possible, as they avoid managing credential rotation and reduce the risk of credential exposure. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
- **Avoid hitting secret scope limits** by defining and sharing a single secret scope for accessing all online stores, rather than creating separate scopes for each store. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- Feature Store Authentication — General authentication patterns for feature stores
- Third-Party Online Stores — External stores for serving features in production
- [Instance Profiles](/concepts/instance-profile-databricks-on-aws.md) — IAM roles attached to compute resources
- Databricks Secrets — Secure credential storage
- MLflow Model Serving — Serving endpoints that perform feature lookups
- Principle of Least Privilege — Security best practice for access control

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
