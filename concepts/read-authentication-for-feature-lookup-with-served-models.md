---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f9a0277c1715a51e554db44f704cc61a9a1dc9bd1bebe7da65a5f7d719fc86d
  pageDirectory: concepts
  sources:
    - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - read-authentication-for-feature-lookup-with-served-models
    - RAFFLWSM
  citations:
    - file: authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
title: Read Authentication for Feature Lookup with Served Models
description: Authentication required when Databricks-hosted MLflow models look up feature values from third-party online stores during serving, supporting instance profiles or Databricks secrets with a read_secret_prefix.
tags:
  - authentication
  - model-serving
  - feature-store
timestamp: "2026-06-19T22:09:38.188Z"
---

Here is the updated wiki page for "Read Authentication for Feature Lookup with Served Models", written solely from the provided source material.

```markdown
---
title: Read Authentication for Feature Lookup with Served Models
summary: Providing read credentials, via instance profile on served MLflow models or Databricks secrets, to enable Databricks-hosted models to look up features from third-party online stores.
sources:
  - authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:29:17.176Z"
updatedAt: "2026-06-18T14:29:17.176Z"
tags:
  - authentication
  - mlflow
  - feature-lookup
  - model-serving
  - read-access
aliases:
  - read-authentication-for-feature-lookup-with-served-models
  - RAFFLWSM
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Read Authentication for Feature Lookup with Served Models

**Read authentication for feature lookup with served models** refers to the credentials and configuration required to allow Databricks-hosted MLflow models to connect to [[Third-Party Online Stores for Feature Serving|third-party online stores]] and retrieve feature values during inference. When a model is served as a [[model serving endpoint]], it must be able to authenticate to the online store to look up features that were published as part of a [[feature table]]. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Overview

Enabling a served model to read from a third-party online store requires providing read authentication. Databricks supports two methods for this: using an instance profile attached to the serving endpoint, or using [[Databricks Secret Scopes|Databricks secrets]] to store credentials. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

The same online store publishing workflow also requires write authentication (for publishing feature tables), but read authentication is specifically for lookup by served models. Databricks recommends using an instance profile for read authentication when possible. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Method 1: Instance Profile Attached to the Served Model

This approach uses an [[Instance Profile (Databricks on AWS)|instance profile (IAM role)]] that is configured directly on the Databricks serving endpoint. The model serving infrastructure assumes the role's permissions when connecting to the online store. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

To set this up:

1. **Create an instance profile** that has read‑only permissions to the target online store (e.g., DynamoDB `GetItem`, `Query`, `Scan` actions). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
2. **Configure the serving endpoint** to use that instance profile, following the [Databricks documentation](https://docs.databricks.com/aws/en/machine-learning/model-serving/add-model-serving-instance-profile). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
3. When publishing the feature table, **do not specify a `read_secret_prefix`** — any value set is overridden by the instance profile. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

The instance profile must have at minimum read‑level DynamoDB permissions such as `dynamodb:GetItem`, `dynamodb:Query`, `dynamodb:Scan`, and related actions. For a full list of required read permissions, see the source documentation. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Method 2: Databricks Secrets for Read Credentials

Alternatively, you can store read‑only credentials as [[Databricks Secret Scopes|Databricks secrets]] and reference them during feature table publishing with a `read_secret_prefix`. This method works for both DynamoDB and SQL-based online stores. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

The general steps are:

1. **Create or reuse a secret scope** specifically for read‑only access (e.g., `<read-scope>`). ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
2. **Create secrets** in that scope that match a naming convention. Choose a unique `<prefix>` for the online store. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]
3. For **DynamoDB**, the required secrets are:
   - `<prefix>-access-key-id` — the AWS access key ID for a read‑only IAM user.
   - `<prefix>-secret-access-key` — the corresponding secret access key.
4. For **SQL stores**, the required secrets are:
   - `<prefix>-user` — the database username.
   - `<prefix>-password` — the database password.

These secrets are then referenced in the online store specification when publishing the feature table (as `read_secret_prefix = "<read-scope>/<prefix>-"`). The serving endpoint will use these credentials on every lookup. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

> **Note:** There is a limit on the number of secret scopes per workspace. To avoid hitting this limit, you can define and share a single secret scope for all online store credentials. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Comparison of Methods

| Method | Recommended for | Configuration complexity | Override behavior |
|--------|----------------|--------------------------|-------------------|
| Instance profile on serving endpoint | Most setups; recommended approach | Medium (requires IAM role and endpoint configuration) | Any `read_secret_prefix` set during publishing is overridden |
| Databricks secrets | When instance profiles are not feasible | Low to medium (secret scope creation and naming) | Explicit `read_secret_prefix` is required |

Both methods achieve the same goal: enabling a served model to authenticate to a third-party online store for feature lookup. ^[authentication-for-working-with-third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- [[Third-Party Online Stores for Feature Serving|Third-party online stores]]
- [[Feature tables]] and [[Feature Table Publishing|Feature publishing]]
- [[Model Serving Endpoint|Model serving endpoints]]
- [[Instance Profile (Databricks on AWS)|Instance profiles in Databricks]]
- [[Databricks Secret Scopes|Databricks secrets]]
- [[Write authentication for feature publishing]]
- [[Feature Store]]

## Sources

- authentication-for-working-with-third-party-online-stores-databricks-on-aws.md
```

# Citations

1. [authentication-for-working-with-third-party-online-stores-databricks-on-aws.md](/references/authentication-for-working-with-third-party-online-stores-databricks-on-aws-d6806fd9.md)
