---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b1496537393502d90a0dff11fc19cc074feb5640df3b3d1ac7dccd8e361511e9
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-authentication-with-personal-access-tokens
    - DCAWPAT
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Databricks Connect authentication with personal access tokens
description: Databricks Connect for R currently only supports authentication via Databricks personal access tokens (PAT), configured through environment variables DATABRICKS_HOST, DATABRICKS_TOKEN, and DATABRICKS_CLUSTER_ID.
tags:
  - authentication
  - databricks
  - security
timestamp: "2026-06-19T09:48:45.380Z"
---

# Databricks Connect Authentication with Personal Access Tokens

**Databricks Connect authentication with personal access tokens** refers to the authentication mechanism used by [Databricks Connect](/concepts/databricks-connect.md) to establish a secure connection between a local development environment and a Databricks cluster using a [personal access token (PAT)](/concepts/databricks-personal-access-token-pat-authentication.md) instead of interactive browser-based authentication.

## Overview

Databricks personal access tokens provide a programmatic way to authenticate to Databricks workspaces. For Databricks Connect, tokens are the primary authentication method, particularly for non-interactive or IDE-based workflows. ^[databricks-connect-for-r-databricks-on-aws.md]

## Supported Clients

Databricks Connect for R currently supports only Databricks personal access token authentication. Other authentication methods are not available for the R client. ^[databricks-connect-for-r-databricks-on-aws.md]

## Creating a Personal Access Token

To create a personal access token, follow the steps in [Create personal access tokens for workspace users](https://docs.databricks.com/aws/en/dev-tools/auth/pat#pat-user). If you already have a token, you can reuse it without affecting other tokens in your user account. ^[databricks-connect-for-r-databricks-on-aws.md]

## Configuring Authentication

### Environment Variables

Databricks recommends storing authentication credentials in environment variables rather than hard-coding them in scripts. For Databricks Connect, the relevant environment variables are:

- `DATABRICKS_HOST` — Your [workspace instance URL](https://docs.databricks.com/aws/en/workspace/workspace-details#workspace-url), for example `https://dbc-a1b2345c-d6e7.cloud.databricks.com`.
- `DATABRICKS_TOKEN` — Your personal access token.
- `DATABRICKS_CLUSTER_ID` — The ID of the target cluster.

^[databricks-connect-for-r-databricks-on-aws.md]

### RStudio Configuration

In RStudio Desktop, you can store these variables in a `.Renviron` file. Create or edit this file using `usethis::edit_r_environ()` and add the following content (replacing placeholders with your actual values):

```
DATABRICKS_HOST=<workspace-url>
DATABRICKS_TOKEN=<personal-access-token>
DATABRICKS_CLUSTER_ID=<cluster-id>
```

After saving the file, restart R to load the environment variables. ^[databricks-connect-for-r-databricks-on-aws.md]

### Connecting from R

When using `sparklyr` with Databricks Connect, pass the authentication credentials to the `spark_connect()` function:

```r
library(sparklyr)

sc <- sparklyr::spark_connect(
  master     = Sys.getenv("DATABRICKS_HOST"),
  cluster_id = Sys.getenv("DATABRICKS_CLUSTER_ID"),
  token      = Sys.getenv("DATABRICKS_TOKEN"),
  method     = "databricks_connect",
  envname    = "r-reticulate"
)
```

^[databricks-connect-for-r-databricks-on-aws.md]

## Security Best Practices

- **Do not hard-code tokens** in scripts or source files. Use environment variables or a secrets manager instead.
- **Store credentials in `.Renviron`** for RStudio projects, which is not tracked by version control by default.
- **Use scoped tokens** with limited permissions where possible, restricting access to only the necessary clusters and operations.

## Related Concepts

- [Personal Access Token Authentication](/concepts/databricks-personal-access-token-pat-authentication.md) — General PAT authentication on Databricks
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) — The R client for Databricks Connect
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — Python client authentication options
- [Databricks Connect Configuration](/concepts/databricks-connect-configuration.md) — Cluster and network requirements for Databricks Connect
- Workspace Instance URL — How to find your Databricks workspace URL
- Cluster ID — How to obtain your cluster ID

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
