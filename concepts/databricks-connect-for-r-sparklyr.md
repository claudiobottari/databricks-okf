---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5e354aebb1bb3baab6ecb6ccb6a9bf16e9339f5a59a9e76bff9b9108d94d510
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-for-r-sparklyr
    - DCFR(
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Databricks Connect for R (sparklyr)
description: A feature that enables connecting R IDEs like RStudio Desktop to Databricks clusters using the sparklyr package, allowing remote execution of Spark code from local R environments.
tags:
  - databricks
  - r
  - spark
  - connectivity
timestamp: "2026-06-19T14:46:50.221Z"
---

# Databricks Connect for R (sparklyr)

**Databricks Connect for R (sparklyr)** enables R users to connect popular IDEs such as RStudio Desktop, notebook servers, and other custom applications to Databricks clusters using the `sparklyr` package. It is built on [Databricks Connect](/concepts/databricks-connect.md) v2 and is available for Databricks Runtime 13.0 and above. ^[databricks-connect-for-r-databricks-on-aws.md]

> This integration is provided by the `sparklyr` community and is not directly supported by Databricks. For questions, refer to the [Posit Community](https://community.rstudio.com/); for issues, report them on the [`sparklyr` GitHub repository](https://github.com/sparklyr/sparklyr/issues). ^[databricks-connect-for-r-databricks-on-aws.md]

## Overview

Databricks Connect for R allows you to develop R code locally and run it on a remote Databricks cluster without needing to upload scripts manually. The connection uses the Spark Connect protocol via `method = "databricks_connect"` in `sparklyr::spark_connect()`. ^[databricks-connect-for-r-databricks-on-aws.md]

The workflow is as follows:

1. Set up a project in RStudio Desktop.
2. Install the required R and Python packages.
3. Configure environment variables for the workspace URL, personal access token, and cluster ID.
4. Write and execute R code that interacts with Spark DataFrames on the remote cluster.

## Requirements

- A Databricks workspace and cluster that meet the [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) requirements. ^[databricks-connect-for-r-databricks-on-aws.md]
- The cluster ID, available from the cluster’s details page in the workspace (the URL segment between `clusters` and `configuration`). ^[databricks-connect-for-r-databricks-on-aws.md]
- A [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md) (PAT) for authentication. Currently, Databricks Connect for R supports only PAT authentication. ^[databricks-connect-for-r-databricks-on-aws.md]
- RStudio Desktop and Python 3.10 (or the major/minor version matching the cluster’s Python version). ^[databricks-connect-for-r-databricks-on-aws.md]

## Setup

### 1. Create a New Project

In RStudio Desktop, create a new project (File > New Project > New Directory > New Project) and enable `renv` for environment management. ^[databricks-connect-for-r-databricks-on-aws.md]

### 2. Install Packages

Install the following R packages from CRAN:

```r
sparklyr, pysparklyr, reticulate, usethis, dplyr, dbplyr
```

Then install the corresponding Python version using `reticulate::install_python(version = "3.10")`, replacing `3.10` with your cluster’s Python version. ^[databricks-connect-for-r-databricks-on-aws.md]

Next, install the Databricks Connect package for R:

```r
pysparklyr::install_databricks(version = "13.3")
```

Substitute `13.3` with your cluster’s Databricks Runtime version. Alternatively, provide the cluster ID:

```r
pysparklyr::install_databricks(cluster_id = "<cluster-id>")
```

This command queries the cluster for the correct runtime version. ^[databricks-connect-for-r-databricks-on-aws.md]

### 3. Set Environment Variables

Create an `.Renviron` file (via `usethis::edit_r_environ()`) and add:

```r
DATABRICKS_HOST=<workspace-url>
DATABRICKS_TOKEN=<personal-access-token>
DATABRICKS_CLUSTER_ID=<cluster-id>
```

After saving, restart R (Session > Restart R) to load the variables. ^[databricks-connect-for-r-databricks-on-aws.md]

## Usage

Write an R script (e.g., `demo.R`) that connects to the cluster and runs queries. The following example reads the `samples.nyctaxi.trips` table:

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

trips <- dplyr::tbl(
  sc,
  dbplyr::in_catalog("samples", "nyctaxi", "trips")
)

print(trips, n = 5)
```

Click **Source** in RStudio to run the file. The first five rows of the table appear in the Console. The **Connections** view (View > Show Connections) allows browsing available catalogs, schemas, tables, and views. ^[databricks-connect-for-r-databricks-on-aws.md]

### Debugging

Set breakpoints in the R script (click the gutter next to a line) and click **Source**. When execution pauses, inspect variables in the **Environment** view and then continue debugging using **Debug > Continue**. ^[databricks-connect-for-r-databricks-on-aws.md]

## Limitations

- **Apache Spark MLlib support**: Databricks Connect for R has limited compatibility with Spark MLlib because MLlib relies on RDDs, while Databricks Connect supports only the DataFrame API. To use all sparklyr’s Spark MLlib functions, use Databricks notebooks or the `db_repl` function from the [brickster package](https://databrickslabs.github.io/brickster/). ^[databricks-connect-for-r-databricks-on-aws.md]
- **Authentication**: Only Databricks personal access tokens are currently supported. ^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) (general overview)
- [Spark Connect](/concepts/spark-connect.md)
- [sparklyr](/concepts/sparklyr.md) (R interface to Apache Spark)
- RStudio Desktop
- [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md)
- [pysparklyr](/concepts/pysparklyr.md) (bridge R to PySpark)
- [Apache Spark MLlib limitations with Spark Connect](/concepts/spark-mllib-limitations-with-databricks-connect.md)

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
