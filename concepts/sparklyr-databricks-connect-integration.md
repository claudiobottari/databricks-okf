---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c448208868181621874171b96e88722920b0d57abe6e3cf88f4242185b284ad7
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sparklyr-databricks-connect-integration
    - SDCI
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: sparklyr Databricks Connect Integration
description: The integration of sparklyr with Databricks Connect for Databricks Runtime 13.0+, enabling R users to run Spark DataFrame operations on remote Databricks clusters.
tags:
  - sparklyr
  - databricks
  - R
timestamp: "2026-06-18T15:04:27.592Z"
---

# sparklyr Databricks Connect Integration

**sparklyr Databricks Connect Integration** allows R users to connect their local R environment — such as RStudio Desktop, notebook servers, or custom applications — to Databricks clusters using the `sparklyr` package with the Databricks Connect protocol. This integration enables remote Spark execution and data access from R while leveraging the cluster’s compute resources.^[databricks-connect-for-r-databricks-on-aws.md]

> **Note:** This integration is neither provided by Databricks nor directly supported by Databricks. For questions, refer to the [Posit Community](https://community.rstudio.com/). To report issues, use the [Issues](https://github.com/sparklyr/sparklyr/issues) section of the `sparklyr` GitHub repository.^[databricks-connect-for-r-databricks-on-aws.md]

## How It Works

The integration relies on the `pysparklyr` package to manage the Python environment and the `sparklyr` package to create a remote connection to a Databricks cluster. Under the hood, it uses the [Databricks Connect](/concepts/databricks-connect.md) client library, which supports the DataFrame API. The connection is established via a [personal access token](/concepts/databricks-personal-access-token-pat-authentication.md) (PAT) for authentication and a cluster ID to target the cluster.^[databricks-connect-for-r-databricks-on-aws.md]

## Limitations

- **Limited MLlib support**: Databricks Connect only supports the Apache Spark DataFrame API, not RDDs. As a result, many [Spark MLlib](/concepts/apache-spark-mllib.md) functions from `sparklyr` are not available through this integration. To use all of sparklyr's Spark MLlib functions, use Databricks notebooks or the `db_repl` function from the brickster package.^[databricks-connect-for-r-databricks-on-aws.md]
- **Authentication**: Only personal access token authentication is supported for Databricks Connect for R.^[databricks-connect-for-r-databricks-on-aws.md]

## Prerequisites

Before using the integration, ensure the following are in place:

- A Databricks workspace and cluster that meet the [compute configuration requirements for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config).^[databricks-connect-for-r-databricks-on-aws.md]
- Your cluster ID, available from the cluster details page in the Databricks workspace (the string between `clusters` and `configuration` in the URL).^[databricks-connect-for-r-databricks-on-aws.md]
- A Databricks personal access token for authentication.^[databricks-connect-for-r-databricks-on-aws.md]

## Setting Up the Integration

The recommended environment is RStudio Desktop with Python 3.10 (or the version matching the cluster’s Databricks Runtime). The following steps outline the process:

1. **Install dependencies**: Install the `sparklyr`, `pysparklyr`, `reticulate`, `usethis`, `dplyr`, and `dbplyr` R packages.^[databricks-connect-for-r-databricks-on-aws.md]
2. **Install Python**: Use `reticulate::install_python()` to install a Python version that matches the cluster’s Databricks Runtime.^[databricks-connect-for-r-databricks-on-aws.md]
3. **Install Databricks Connect**: Run `pysparklyr::install_databricks()`. Provide either the Databricks Runtime version (e.g., `"13.3"`) or a cluster ID to auto-detect the correct version.^[databricks-connect-for-r-databricks-on-aws.md]
4. **Set environment variables**: Store `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, and `DATABRICKS_CLUSTER_ID` in an `.Renviron` file.^[databricks-connect-for-r-databricks-on-aws.md]
5. **Create a connection**: Use `sparklyr::spark_connect()` with `method = "databricks_connect"` and reference the environment variables.^[databricks-connect-for-r-databricks-on-aws.md]

### Example Connection Code

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

^[databricks-connect-for-r-databricks-on-aws.md]

## Connecting to Different Clusters

If you need to connect to a cluster with a different Databricks Runtime version, re-run `pysparklyr::install_databricks()` with the new version or cluster ID to set up the correct Python environment.^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The underlying client library for remote Spark execution.
- [sparklyr](/concepts/sparklyr.md) – The R interface to Apache Spark.
- [pysparklyr](/concepts/pysparklyr.md) – Helper package for managing Python environments and Databricks Connect.
- [Personal access token authentication](/concepts/databricks-personal-access-token-pat-authentication.md) – Authentication method required for Databricks Connect for R.
- [Databricks cluster configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) – Compute requirements for the target cluster.
- [Spark MLlib](/concepts/apache-spark-mllib.md) – Spark's machine learning library; limited through this integration.
- RStudio Desktop – Recommended IDE for the integration.
- dbplyr – Database backend for dplyr used with remote tables.

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
