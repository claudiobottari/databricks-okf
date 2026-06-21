---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b1521e4b8068d1d5a29c60f01687e39423b324326d6d7034d9176bb07c3321fb
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark_connect-function-for-databricks-connect
    - SFFDC
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: spark_connect Function for Databricks Connect
description: The sparklyr::spark_connect function with method='databricks_connect' parameter, which establishes a connection from an R environment to a remote Databricks cluster for distributed data operations.
tags:
  - r
  - databricks
  - spark
  - api
timestamp: "2026-06-19T14:47:02.866Z"
---

# spark_connect Function for Databricks Connect

The **`spark_connect` function** is the primary entry point for establishing a connection between an R environment — such as RStudio Desktop — and a Databricks cluster using Databricks Connect for R. This function is part of the `sparklyr` package and enables remote execution of Spark DataFrame operations from a local R session. ^[databricks-connect-for-r-databricks-on-aws.md]

## Syntax

When connecting to Databricks Connect, `spark_connect` uses the `method = "databricks_connect"` parameter. The full function call requires the Databricks workspace URL, cluster ID, and authentication token as arguments. ^[databricks-connect-for-r-databricks-on-aws.md]

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

## Parameters

- **`master`**: The Databricks workspace instance URL (e.g., `https://dbc-a1b2345c-d6e7.cloud.databricks.com`). Passed via the `DATABRICKS_HOST` environment variable. ^[databricks-connect-for-r-databricks-on-aws.md]
- **`cluster_id`**: The ID of the target Databricks cluster. Found in the workspace URL when viewing the cluster's configuration page. Passed via the `DATABRICKS_CLUSTER_ID` environment variable. ^[databricks-connect-for-r-databricks-on-aws.md]
- **`token`**: A Databricks personal access token for authentication. Databricks Connect for R currently only supports personal access token authentication. Passed via the `DATABRICKS_TOKEN` environment variable. ^[databricks-connect-for-r-databricks-on-aws.md]
- **`method`**: Must be set to `"databricks_connect"` to use Databricks Connect integration. ^[databricks-connect-for-r-databricks-on-aws.md]
- **`envname`**: Specifies the Python environment name used by `reticulate`. The example uses `"r-reticulate"`. ^[databricks-connect-for-r-databricks-on-aws.md]

## Requirements

Before calling `spark_connect`, several prerequisites must be met:

- The target Databricks workspace and cluster must meet the [compute configuration requirements for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md). ^[databricks-connect-for-r-databricks-on-aws.md]
- The cluster's Databricks Runtime version must be 13.0 or above. ^[databricks-connect-for-r-databricks-on-aws.md]
- The required R packages must be installed in the project: `sparklyr`, `pysparklyr`, `reticulate`, `usethis`, `dplyr`, and `dbplyr`. ^[databricks-connect-for-r-databricks-on-aws.md]
- The Databricks Connect Python package must be installed using `pysparklyr::install_databricks()`, specifying either the Databricks Runtime version or the cluster ID. ^[databricks-connect-for-r-databricks-on-aws.md]

## Security Best Practices

Databricks does not recommend hard-coding sensitive values such as workspace URL, access token, or cluster ID directly into R scripts. Instead, these should be stored in environment variables, for example in an `.Renviron` file, and accessed at runtime using `Sys.getenv()`. ^[databricks-connect-for-r-databricks-on-aws.md]

```r
# Inside .Renviron file:
DATABRICKS_HOST=https://dbc-a1b2345c-d6e7.cloud.databricks.com
DATABRICKS_TOKEN=<personal-access-token>
DATABRICKS_CLUSTER_ID=<cluster-id>
```

## Usage After Connection

After a successful connection, the returned `spark_connection` object (`sc`) can be used with standard `dplyr` and `dbplyr` functions to query Databricks tables. ^[databricks-connect-for-r-databricks-on-aws.md]

```r
trips <- dplyr::tbl(
  sc,
  dbplyr::in_catalog("samples", "nyctaxi", "trips")
)
print(trips, n = 5)
```

## Debugging Support

Code running through `spark_connect` supports RStudio Desktop's standard debugging features, including breakpoints and variable inspection in the **Environment** view. ^[databricks-connect-for-r-databricks-on-aws.md]

## Limitations

- Databricks Connect has limited compatibility with [Apache Spark MLlib](/concepts/apache-spark-mllib.md) because Spark MLlib uses RDDs, while Databricks Connect only supports the DataFrame API. ^[databricks-connect-for-r-databricks-on-aws.md]
- Authentication currently only supports Databricks personal access tokens, not other authentication methods. ^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — Overview of the Databricks Connect feature across all languages
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — Python equivalent using `databricks-connect` package
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — Scala equivalent
- [sparklyr](/concepts/sparklyr.md) — The R package providing the `spark_connect` function
- [pysparklyr](/concepts/pysparklyr.md) — Supporting R package for Databricks Connect installation
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Runtime versions compatible with Databricks Connect

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
