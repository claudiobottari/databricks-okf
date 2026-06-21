---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 27fe0d1d6d60bcf67b9fa42a346df3b35143afd763197d04bb2a8a35850f2a3f
  pageDirectory: concepts
  sources:
    - compute-configuration-for-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-authentication-types
    - DCAT
  citations:
    - file: compute-configuration-for-databricks-connect-databricks-on-aws.md
title: Databricks Connect Authentication Types
description: Supported authentication methods for Databricks Connect including personal access tokens, OAuth M2M, and OAuth U2M
tags:
  - authentication
  - security
  - databricks
timestamp: "2026-06-18T11:04:40.037Z"
---

# Databricks Connect Authentication Types

**Databricks Connect Authentication Types** refers to the supported mechanisms for authenticating a local development environment (IDE, notebook server, or custom application) to a Databricks compute resource — either a classic cluster or serverless compute — when using the Databricks Connect client library.

Databricks Connect supports three authentication types, each with specific configuration requirements. The connection configuration is resolved by searching a predefined hierarchy of sources in order, stopping at the first source that provides valid credentials. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Supported Authentication Types

### Personal Access Token (PAT) Authentication (Legacy)
Uses a Databricks personal access token. This is the only authentication type supported by the `DatabricksSession.builder.remote()` method. Required fields in any configuration source: `host` and `token`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### OAuth Machine-to-Machine (M2M) Authentication
Uses a client ID and client secret for automated (non-interactive) authentication. Supported when the cluster or workspace is configured for OAuth. Required fields: `host`, `client_id`, and `client_secret`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

### OAuth User-to-Machine (U2M) Authentication
Uses an interactive OAuth flow to obtain credentials on behalf of a user. Supported when the workspace is configured for OAuth. Required field: `host`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Configuration Resolution Order

Databricks Connect searches for connection properties in the following order, using the first configuration it finds: ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

1. **`DatabricksSession.builder.remote()`** — Only supports PAT authentication. Specify `host`, `token`, and `cluster_id` (or `serverless=True`). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
2. **A named Databricks configuration profile** — Passed via `.profile("<profile-name>")` in the builder. The profile must contain `cluster_id` (or `serverless_compute_id`) and the required fields for the chosen auth type. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
3. **The `DATABRICKS_CONFIG_PROFILE` environment variable** — Points to a configuration profile name. The builder call uses `.getOrCreate()`. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
4. **Individual environment variables** — Uses `DATABRICKS_CLUSTER_ID` (or `DATABRICKS_SERVERLESS_COMPUTE_ID`) plus the auth-specific variables (`DATABRICKS_HOST`, `DATABRICKS_TOKEN` for PAT; `DATABRICKS_CLIENT_ID`, `DATABRICKS_CLIENT_SECRET` for OAuth M2M; `DATABRICKS_HOST` for OAuth U2M). ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]
5. **A configuration profile named `DEFAULT`** — Falls back to the default profile if no other source is found. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Using Different Authentication Types with the Databricks SDK Config

For authentication types other than PAT, use the Databricks SDK’s `Config` class and pass it to the builder via `.sdkConfig(config)`. This approach works with all three authentication types and allows you to specify a `cluster_id` or `serverless_compute_id` separately from the authentication fields. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Authentication for Serverless Compute

When connecting to serverless compute, the authentication requirements are the same as for classic clusters. The only difference is that instead of `cluster_id`, you set `serverless_compute_id = "auto"` (or use `.serverless()` builder method). The same authentication types and configuration sources apply. ^[compute-configuration-for-databricks-connect-databricks-on-aws.md]

## Best Practices

- Use **OAuth M2M** for automated or CI/CD pipelines where a long-lived secret is acceptable.
- Use **OAuth U2M** for interactive development to avoid managing static tokens.
- Use **configuration profiles** (with named profiles) to separate connection settings from code.
- Set the `DATABRICKS_CLUSTER_ID` environment variable when you want to reuse a single configuration profile across multiple clusters.

## Related Concepts

- [Databricks authentication](/concepts/databricks-authentication-type.md) — General Databricks authentication mechanisms
- [OAuth M2M Authentication](/concepts/machine-to-machine-m2m-authentication.md) — Machine-to-machine OAuth in Databricks
- [OAuth U2M Authentication](/concepts/user-to-machine-u2m-authentication.md) — User-to-machine OAuth in Databricks
- [Databricks Configuration Profiles](/concepts/databricks-configuration-profiles.md) — File-based credential management
- [Databricks Connect](/concepts/databricks-connect.md) — The client library for remote Spark execution

## Sources

- compute-configuration-for-databricks-connect-databricks-on-aws.md

# Citations

1. [compute-configuration-for-databricks-connect-databricks-on-aws.md](/references/compute-configuration-for-databricks-connect-databricks-on-aws-4e42ff3c.md)
