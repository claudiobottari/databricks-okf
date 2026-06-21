---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2c70f27b1215008ba7c6a41c2b39838eaf60ea750230e319e2d1dc540007bab
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-authentication-via-pat
    - DCAVP
    - databricks-connect-authentication-via-personal-access-tokens
    - DCAVPAT
    - databricks-connect-authentication-with-personal-access-tokens
    - DCAWPAT
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Databricks Connect Authentication via PAT
description: Databricks Connect for R currently only supports Databricks personal access token (PAT) authentication for workspace and cluster access.
tags:
  - authentication
  - databricks
  - security
timestamp: "2026-06-19T18:10:26.046Z"
---

# Databricks Connect Authentication via PAT

**Databricks Connect Authentication via PAT** refers to the method of authenticating from a local R environment to a Databricks cluster using a [Databricks personal access token (PAT)]. For Databricks Connect with R (via `sparklyr`), PAT is the only supported authentication mechanism. ^[databricks-connect-for-r-databricks-on-aws.md]

## Overview

Databricks Connect enables you to connect IDEs such as RStudio Desktop to Databricks clusters and run Spark code locally. When using the R integration via the `sparklyr` package, authentication with your Databricks workspace must be performed with a personal access token. The token is passed to the `spark_connect()` function through the `token` parameter or, more securely, through an environment variable. ^[databricks-connect-for-r-databricks-on-aws.md]

## Prerequisites

- A Databricks workspace and cluster that meet the [compute configuration requirements for Databricks Connect].
- The cluster ID of the target cluster (found in the browser URL when viewing the cluster details page). ^[databricks-connect-for-r-databricks-on-aws.md]
- An installed version of PAT-compatible software: RStudio Desktop, Python 3.10, the `sparklyr`, `pysparklyr`, and `reticulate` packages, and the Databricks Connect package appropriate for your cluster’s Databricks Runtime version. ^[databricks-connect-for-r-databricks-on-aws.md]

## Setting up PAT authentication

### Step 1 – Create a personal access token
Follow the steps in the Databricks documentation to [create a personal access token for your user account]. The token is a string that grants programmatic access to the workspace. ^[databricks-connect-for-r-databricks-on-aws.md]

### Step 2 – Store the token as an environment variable
Databricks recommends not hard-coding sensitive values in scripts. Instead, store the workspace URL, token, and cluster ID in an `.Renviron` file in your RStudio project:

```
DATABRICKS_HOST=<workspace-url>
DATABRICKS_TOKEN=<personal-access-token>
DATABRICKS_CLUSTER_ID=<cluster-id>
```

Replace the placeholders with your actual values. After saving the file, restart R (Session > Restart R) to load the variables. ^[databricks-connect-for-r-databricks-on-aws.md]

## Using the token in code

In your R script, call `spark_connect()` with the `method = "databricks_connect"` argument and pass the token via the `token` parameter. The other connection properties—`master` (the workspace URL) and `cluster_id`—are also required:

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

The token is used by the Databricks Connect client to authenticate with the workspace when launching the remote Spark session. ^[databricks-connect-for-r-databricks-on-aws.md]

## Security considerations

- Treat your PAT as a secret. Store it in environment variables or a secrets manager, never hard-coded in source files.
- Tokens can be revoked or rotated from the Databricks workspace UI.
- The PAT grants the same permissions as the user who created it; ensure it has only the necessary scope for the tasks performed by Databricks Connect. ^[databricks-connect-for-r-databricks-on-aws.md]

## Related concepts

- [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md)
- [Databricks Connect](/concepts/databricks-connect.md)
- [sparklyr](/concepts/sparklyr.md)
- RStudio Desktop
- [Environment variables](/concepts/model-serving-environment-variables.md)
- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md)

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
