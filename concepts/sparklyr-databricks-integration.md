---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e76277d4571a5403528c1a20fddd9b90b58ae89227ad5aa8951c296f18d11680
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparklyr-databricks-integration
    - SDI
    - Databricks integration
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: sparklyr Databricks Integration
description: The sparklyr R package's method = 'databricks_connect' integration that provides an R interface to Databricks Connect for remote cluster operations.
tags:
  - r
  - sparklyr
  - databricks
timestamp: "2026-06-19T18:10:17.304Z"
---

# sparklyr Databricks Integration

**sparklyr Databricks Integration** refers to the use of the [`sparklyr`](https://spark.rstudio.com/) R package with Databricks Connect to connect RStudio Desktop and other R environments to Databricks clusters for distributed data processing and machine learning. This integration allows R users to leverage Databricks' Apache Spark clusters directly from their preferred R development tools. ^[databricks-connect-for-r-databricks-on-aws.md]

## Overview

The sparklyr integration with Databricks is achieved through Databricks Connect, which enables popular IDEs such as RStudio Desktop, notebook servers, and other custom applications to connect to Databricks clusters. This integration is not provided or directly supported by Databricks; it is a community-supported feature. Users should direct questions to the [Posit Community](https://community.rstudio.com/) and report issues to the [sparklyr GitHub repository](https://github.com/sparklyr/sparklyr/issues). ^[databricks-connect-for-r-databricks-on-aws.md]

The integration works with Databricks Runtime 13.0 and above. Additional documentation is available in the sparklyr documentation under [Databricks Connect v2](https://spark.rstudio.com/deployment/databricks-connect.html). ^[databricks-connect-for-r-databricks-on-aws.md]

## Compatibility Limitations

Databricks Connect has limited compatibility with [Apache Spark MLlib](/concepts/apache-spark-mllib.md)](https://spark.apache.org/mllib/) because Spark MLlib uses RDDs, while Databricks Connect only supports the DataFrame API. To use all of sparklyr's Spark MLlib functions, users should use Databricks notebooks or the `db_repl` function from the [brickster package](https://databrickslabs.github.io/brickster/). ^[databricks-connect-for-r-databricks-on-aws.md]

## Requirements

To use sparklyr with Databricks Connect, the following must be in place:

- The target Databricks workspace and cluster must meet the requirements for [Compute configuration for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config). ^[databricks-connect-for-r-databricks-on-aws.md]
- The cluster ID must be available. This can be found in the workspace URL when viewing a cluster's details page, between `clusters` and `configuration`. ^[databricks-connect-for-r-databricks-on-aws.md]
- Authentication currently supports only Databricks personal access tokens. ^[databricks-connect-for-r-databricks-on-aws.md]

## Setup Steps

### Install Dependencies

Install the required R packages: `sparklyr`, `pysparklyr`, `reticulate`, `usethis`, `dplyr`, and `dbplyr`. The `pysparklyr` package is used to install Databricks Connect by running `pysparklyr::install_databricks()`, specifying either the Databricks Runtime version or a cluster ID. ^[databricks-connect-for-r-databricks-on-aws.md]

### Configure Authentication

Store the Databricks workspace URL, personal access token, and cluster ID in environment variables — typically in a `.Renviron` file using `usethis::edit_r_environ()`. The required variables are: ^[databricks-connect-for-r-databricks-on-aws.md]

- `DATABRICKS_HOST` — the workspace instance URL
- `DATABRICKS_TOKEN` — the personal access token
- `DATABRICKS_CLUSTER_ID` — the cluster ID

After editing the `.Renviron` file, restart R to load the environment variables. ^[databricks-connect-for-r-databricks-on-aws.md]

### Connect to Databricks

Establish a connection using `sparklyr::spark_connect()` with `method = "databricks_connect"`: ^[databricks-connect-for-r-databricks-on-aws.md]

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

### Query Data and Debug

Once connected, use `dplyr::tbl()` to reference tables from the Unity Catalog, and use standard dplyr operations for data manipulation. The RStudio Connections view allows exploration of available catalogs, schemas, tables, and views. Breakpoints can be set in R scripts for interactive debugging. ^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The general connectivity framework for connecting external tools to Databricks clusters.
- [sparklyr](/concepts/sparklyr.md) — The R package that provides an R interface to Apache Spark.
- RStudio Desktop — A common IDE used with sparklyr for Databricks development.
- [Unity Catalog](/concepts/unity-catalog.md) — The data cataloging and governance layer for Databricks tables.
- dplyr — An R package for data manipulation, used with sparklyr for Spark DataFrames.

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
