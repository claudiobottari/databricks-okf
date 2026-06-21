---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a5a11ed2aedc669ba0da00db982cdce7b7f73261aaf43241f4a01a4fba1b411
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-personal-access-token-authentication-for-r
    - DPATAFR
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Databricks personal access token authentication for R
description: The only supported authentication method for Databricks Connect for R, requiring a PAT stored in the DATABRICKS_TOKEN environment variable.
tags:
  - databricks
  - authentication
  - r
  - security
timestamp: "2026-06-18T11:34:54.303Z"
---

# Databricks Personal Access Token Authentication for R

**Databricks personal access token authentication for R** is the current authentication method for connecting R environments such as RStudio Desktop to Databricks clusters via [Databricks Connect](/concepts/databricks-connect.md). This method uses a long-lived token generated from the Databricks workspace and passed to the connection function through environment variables or code parameters. ^[databricks-connect-for-r-databricks-on-aws.md]

## Overview

Databricks Connect for R, which relies on the `sparklyr` and `pysparklyr` packages, supports only [personal access token](/concepts/databricks-personal-access-token-pat-authentication.md) authentication as of Databricks Runtime 13.0 and above. No other authentication mechanisms — such as OAuth or Azure AD tokens — are currently supported for R connections. ^[databricks-connect-for-r-databricks-on-aws.md]

The token is used together with the workspace URL and cluster ID to establish a connection from a local R environment to a running Databricks cluster. The connection is established by calling `sparklyr::spark_connect()` with the `method = "databricks_connect"` parameter. ^[databricks-connect-for-r-databricks-on-aws.md]

## Creating a Personal Access Token

To authenticate, you must first create a personal access token in the Databricks workspace. If you already have a token, you can reuse it; the following steps will not affect any existing tokens. ^[databricks-connect-for-r-databricks-on-aws.md]

1. In your Databricks workspace, click your user profile icon in the top-right corner and select **Settings**.
2. Under **Developer**, click **Access tokens**.
3. Click **Generate new token**.
4. Optionally, give the token a name and set a lifetime.
5. After generation, copy the token value immediately. Databricks will not display it again.

For detailed instructions, see [Create personal access tokens for workspace users](/concepts/databricks-personal-access-token-pat-authentication.md). ^[databricks-connect-for-r-databricks-on-aws.md]

## Configuring Authentication in R

Databricks recommends not hard-coding the token directly in R scripts. Instead, store it as an environment variable, for example in a `.Renviron` file. ^[databricks-connect-for-r-databricks-on-aws.md]

### Setting Environment Variables

Create or edit the `.Renviron` file in the project root (use `usethis::edit_r_environ()` in RStudio) and add the following lines, replacing the placeholders with your actual values: ^[databricks-connect-for-r-databricks-on-aws.md]

```
DATABRICKS_HOST=https://<workspace-url>
DATABRICKS_TOKEN=<personal-access-token>
DATABRICKS_CLUSTER_ID=<cluster-id>
```

After saving, restart R to load the variables (in RStudio: **Session > Restart R**). ^[databricks-connect-for-r-databricks-on-aws.md]

## Using the Token in Code

The token is passed to the connection function via the `token` parameter. The following example reads the token from the environment variable: ^[databricks-connect-for-r-databricks-on-aws.md]

```r
library(sparklyr)
library(dplyr)
library(dbplyr)

sc <- sparklyr::spark_connect(
  master     = Sys.getenv("DATABRICKS_HOST"),
  cluster_id = Sys.getenv("DATABRICKS_CLUSTER_ID"),
  token      = Sys.getenv("DATABRICKS_TOKEN"),
  method     = "databricks_connect",
  envname    = "r-reticulate"
)
```

Once connected, you can use `dplyr` and `dbplyr` to query tables in Unity Catalog. ^[databricks-connect-for-r-databricks-on-aws.md]

## Security Best Practices

- **Never commit tokens** to version control. Use `.Renviron`, `.env` files (added to `.gitignore`), or a secrets manager.
- **Set token lifetimes** to the minimum necessary period, and rotate tokens regularly.
- **Use separate tokens** for different projects or environments to limit blast radius.
- **Restrict token permissions** to the minimum required for the task (e.g., only cluster access) using Databricks access controls.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The framework that enables remote R connections to clusters
- [sparklyr](/concepts/sparklyr.md) — The R package that provides a `dplyr` interface to Spark
- [pysparklyr](/concepts/pysparklyr.md) — R package facilitating Databricks Connect installation
- reticulate — R package used to manage the Python environment for Databricks Connect
- RStudio Desktop — Common IDE for developing Databricks Connect projects in R
- Personal Access Token — The authentication credential used in this workflow
- Environment Variables in R — Best practices for storing secrets like tokens

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
