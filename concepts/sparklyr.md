---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 59073a6f044bb643419664c5783b538534d94d2d2688a1f0fbb179b68d6a13f8
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: sparklyr
description: R interface to Apache Spark that serves as the primary integration point for Databricks Connect from R, enabling dplyr and dbplyr workflows against Databricks clusters.
tags:
  - R
  - spark
  - package
timestamp: "2026-06-19T09:48:23.050Z"
---

# sparklyr

**sparklyr** is an R package that provides an interface to Apache Spark from within R. It enables R users to interact with Spark DataFrames using familiar tools such as `dplyr` and the pipe operator, making distributed data processing accessible from R environments like RStudio Desktop. ^[databricks-connect-for-r-databricks-on-aws.md]

## Overview

sparklyr acts as a bridge between R and Spark, allowing R code to be translated into Spark operations. When used with [Databricks Connect for R](/concepts/databricks-connect-for-r.md), sparklyr can connect an R IDE (e.g., RStudio Desktop) to a remote Databricks cluster, run Spark code, and browse catalogs, schemas, tables, and views directly from the R environment. The connection uses the `databricks_connect` method in `sparklyr::spark_connect()`. ^[databricks-connect-for-r-databricks-on-aws.md]

## Setting Up sparklyr with Databricks Connect

To use sparklyr with Databricks Connect (for Databricks Runtime 13.0 and above), the following steps are required (as detailed in the official tutorial):

1. **Create a project** in RStudio Desktop, using `renv` for dependency management. ^[databricks-connect-for-r-databricks-on-aws.md]
2. **Install prerequisite packages** from CRAN: `sparklyr`, `pysparklyr`, `reticulate`, `usethis`, `dplyr`, `dbplyr`. The `pysparklyr` package is used to install the correct Databricks Connect Python package. ^[databricks-connect-for-r-databricks-on-aws.md]
3. **Install Python** (the same version as on the target Databricks cluster) using `reticulate::install_python()`. ^[databricks-connect-for-r-databricks-on-aws.md]
4. **Install the Databricks Connect package** using `pysparklyr::install_databricks(version = "13.3")` or by supplying a cluster ID. The version must match the cluster’s Databricks Runtime version. ^[databricks-connect-for-r-databricks-on-aws.md]
5. **Set environment variables** for authentication: `DATABRICKS_HOST` (workspace URL), `DATABRICKS_TOKEN` (personal access token), and `DATABRICKS_CLUSTER_ID`. This is typically done in an `.Renviron` file. ^[databricks-connect-for-r-databricks-on-aws.md]

### Connection Code Example

The following R code establishes a sparklyr connection via Databricks Connect and queries the sample `nyctaxi.trips` table: ^[databricks-connect-for-r-databricks-on-aws.md]

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

After running the script, the RStudio **Connections** view can be used to explore available catalogs, schemas, tables, and views in the remote cluster. ^[databricks-connect-for-r-databricks-on-aws.md]

## Limitations

Databricks Connect for R (and therefore sparklyr in this context) has limited compatibility with [Apache Spark MLlib](/concepts/apache-spark-mllib.md). MLlib relies on RDDs (Resilient Distributed Datasets), while Databricks Connect supports only the DataFrame API. Users who need full sparklyr MLlib functionality should use Databricks notebooks or the `db_repl` function from the [brickster package](https://databrickslabs.github.io/brickster/). ^[databricks-connect-for-r-databricks-on-aws.md]

## Support and Maintenance

The sparklyr integration with Databricks Connect for Databricks Runtime 13.0 and above is **neither provided by Databricks nor directly supported by Databricks**. For questions, users are directed to the Posit Community; for bug reports, the `sparklyr` GitHub repository’s Issues page. ^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for R](/concepts/databricks-connect-for-r.md)
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md)
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)
- sparklyr documentation (Posit)
- RStudio Desktop
- reticulate
- dplyr / dbplyr integration

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
