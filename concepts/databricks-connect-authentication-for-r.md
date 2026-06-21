---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b4828041178bcc1ee02e9ca5d2763a1eae54a20cbb94aa4e7786742d482382b8
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-authentication-for-r
    - DCAFR
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Databricks Connect Authentication for R
description: The authentication mechanism for Databricks Connect for R, which currently only supports Databricks personal access tokens (PAT) stored in environment variables.
tags:
  - authentication
  - databricks
  - security
timestamp: "2026-06-18T15:04:39.199Z"
---

# Databricks Connect Authentication for R

**Databricks Connect Authentication for R** refers to the authentication mechanisms and setup required to connect RStudio Desktop and other R environments to Databricks clusters using the `sparklyr` package integration with Databricks Connect.

## Overview

Databricks Connect enables R users to connect popular IDEs like RStudio Desktop, notebook servers, and custom applications to Databricks clusters for executing code and processing data. The integration uses `sparklyr` as the R interface to Apache Spark, with `pysparklyr` providing additional setup utilities. ^[databricks-connect-for-r-databricks-on-aws.md]

## Authentication Method

Databricks Connect for R currently supports only one authentication method: **Databricks personal access tokens** (PAT). This is the sole supported authentication mechanism for the `sparklyr`-based integration with Databricks Connect. ^[databricks-connect-for-r-databricks-on-aws.md]

## Required Credentials

To authenticate with Databricks Connect from R, you need three pieces of information:

- **Workspace URL**: Your Databricks workspace instance URL (e.g., `https://dbc-a1b2345c-d6e7.cloud.databricks.com`). ^[databricks-connect-for-r-databricks-on-aws.md]
- **Personal access token**: A Databricks PAT created in the workspace for authentication. ^[databricks-connect-for-r-databricks-on-aws.md]
- **Cluster ID**: The identifier of the target Databricks cluster, found by navigating to the cluster's details page and copying the string between `clusters` and `configuration` in the URL. ^[databricks-connect-for-r-databricks-on-aws.md]

## Setting Up Authentication

### Step 1: Create a Personal Access Token

Before connecting, create a Databricks personal access token following the [Create personal access tokens for workspace users](/concepts/databricks-personal-access-token-pat-authentication.md) guide. If you already have a token, you can skip this step. ^[databricks-connect-for-r-databricks-on-aws.md]

### Step 2: Configure Environment Variables

Databricks recommends against hard-coding sensitive credentials directly in R scripts. Instead, store workspace URL, token, and cluster ID in environment variables using an `.Renviron` file: ^[databricks-connect-for-r-databricks-on-aws.md]

```
DATABRICKS_HOST=<workspace-url>
DATABRICKS_TOKEN=<personal-access-token>
DATABRICKS_CLUSTER_ID=<cluster-id>
```

Create or edit this file using `usethis::edit_r_environ()` in RStudio, then restart R to load the variables. ^[databricks-connect-for-r-databricks-on-aws.md]

### Step 3: Install Dependencies

Install the required R packages: `sparklyr`, `pysparklyr`, `reticulate`, `usethis`, `dplyr`, and `dbplyr`. Additionally, install Python via `reticulate::install_python()` and the Databricks Connect package via `pysparklyr::install_databricks()`. ^[databricks-connect-for-r-databricks-on-aws.md]

### Step 4: Connect in Code

Use the configured environment variables in your connection code: ^[databricks-connect-for-r-databricks-on-aws.md]

```r
sc <- sparklyr::spark_connect(
  master     = Sys.getenv("DATABRICKS_HOST"),
  cluster_id = Sys.getenv("DATABRICKS_CLUSTER_ID"),
  token      = Sys.getenv("DATABRICKS_TOKEN"),
  method     = "databricks_connect",
  envname    = "r-reticulate"
)
```

## Compatibility Considerations

- Databricks Connect for R has limited compatibility with [Apache Spark MLlib](/concepts/apache-spark-mllib.md) because MLlib uses RDDs while Databricks Connect only supports the DataFrame API. ^[databricks-connect-for-r-databricks-on-aws.md]
- For full MLlib functionality, use Databricks notebooks or the `db_repl` function from the brickster package. ^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — Alternative Python-based integration
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — Alternative Scala-based integration
- [Personal access token authentication](/concepts/databricks-personal-access-token-pat-authentication.md)
- Databricks cluster configuration
- sparklyr package

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
