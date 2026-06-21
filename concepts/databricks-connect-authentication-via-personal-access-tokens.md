---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f0ce0f5ae5ada68daf0d59f508671013df9523b059583d1c70a83da24559badd
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-authentication-via-personal-access-tokens
    - DCAVPAT
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Databricks Connect Authentication via Personal Access Tokens
description: The authentication mechanism for Databricks Connect for R, which currently only supports Databricks personal access tokens (PAT) for workspace authentication.
tags:
  - databricks
  - authentication
  - security
timestamp: "2026-06-19T14:46:53.579Z"
---

# Databricks Connect Authentication via Personal Access Tokens

**Databricks Connect Authentication via Personal Access Tokens** is the primary authentication method for connecting RStudio Desktop and other IDEs to Databricks clusters using [Databricks Connect for R](/concepts/databricks-connect-for-r.md). This method requires a personal access token (PAT) generated from a user's Databricks workspace.

## Overview

Databricks Connect enables you to connect popular IDEs such as RStudio Desktop, notebook servers, and other custom applications to Databricks clusters. For R users, the integration uses the `sparklyr` package. ^[databricks-connect-for-r-databricks-on-aws.md]

Databricks Connect for R authentication currently only supports Databricks personal access tokens. Other authentication methods are not available for this integration. ^[databricks-connect-for-r-databricks-on-aws.md]

## Creating a Personal Access Token

To create a personal access token for authentication, follow the steps in the [Create personal access tokens for workspace users](/concepts/databricks-personal-access-token-pat-authentication.md) documentation. If you already have a token, you can skip this step without affecting any existing tokens in your user account. ^[databricks-connect-for-r-databricks-on-aws.md]

## Configuration

The recommended approach is to store credentials in environment variables rather than hard-coding them into scripts. Use a `.Renviron` file with the following variables: ^[databricks-connect-for-r-databricks-on-aws.md]

- `DATABRICKS_HOST` — The workspace instance URL, for example `https://dbc-a1b2345c-d6e7.cloud.databricks.com`
- `DATABRICKS_TOKEN` — The personal access token
- `DATABRICKS_CLUSTER_ID` — The cluster ID

### Setting Environment Variables

Edit the `.Renviron` file using `usethis::edit_r_environ()` and restart R to load the variables. ^[databricks-connect-for-r-databricks-on-aws.md]

## Connection Example

Use `sparklyr::spark_connect()` with the following parameters: ^[databricks-connect-for-r-databricks-on-aws.md]

- `master` — Set to `Sys.getenv("DATABRICKS_HOST")`
- `token` — Set to `Sys.getenv("DATABRICKS_TOKEN")`
- `cluster_id` — Set to `Sys.getenv("DATABRICKS_CLUSTER_ID")`
- `method` — Set to `"databricks_connect"`
- `envname` — Set to `"r-reticulate"`

## Related Concepts

- Databricks Personal Access Tokens
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md)
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)
- [sparklyr](/concepts/sparklyr.md)
- RStudio Desktop
- Workspace Instance URL
- Cluster ID

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
