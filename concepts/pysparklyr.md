---
type: concept
x-llmwiki:
  aliases:
    - pysparklyr-package
    - sparklyr package
    - PySpark DataFrame
  schemaVersion: "0.1"
  contentHash: 87b900c1936bb36312d4060c2ded35d184762fb1632fb78a73f1e5f94ad8050c
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: pysparklyr
description: R package that manages the installation and configuration of Databricks Connect dependencies, including automatically determining the correct Databricks Runtime version from a cluster ID.
tags:
  - R
  - databricks
  - package
timestamp: "2026-06-19T09:49:13.724Z"
---

---
title: pysparklyr
summary: An R package that provides a bridge between sparklyr and Python's PySpark, enabling the installation and configuration of Databricks Connect for R and facilitating integration between R and Databricks environments.
sources:
  - databricks-connect-for-r-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:26:53.977Z"
updatedAt: "2026-06-18T12:26:53.977Z"
tags:
  - databricks
  - r
  - sparklyr
  - pyspark
  - integration
  - dev-tools
aliases:
  - pysparklyr
  - pysparklyr package
  - PySpark ML
  - pyspark.ml
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# pysparklyr

**pysparklyr** is an R package that bridges [sparklyr](/concepts/sparklyr.md) with Python's PySpark, enabling R users to install and configure [Databricks Connect for R](/concepts/databricks-connect-for-r.md) and interact with Databricks clusters from R environments like RStudio Desktop.^[databricks-connect-for-r-databricks-on-aws.md]

## Overview

The `pysparklyr` package simplifies the setup of Databricks Connect for Databricks Runtime 13.0 and above from R. It handles the installation of the Databricks Connect Python package that sparklyr requires for remote connection, and it manages Python environment configuration compatible with the target Databricks Runtime version running on the cluster.^[databricks-connect-for-r-databricks-on-aws.md]

## Key Features

### Databricks Connect Installation

The primary function of `pysparklyr` is to install the correct Databricks Connect package for a given Databricks Runtime version. Users can specify the version directly or provide a cluster ID, and `pysparklyr` will determine the appropriate version automatically.^[databricks-connect-for-r-databricks-on-aws.md]

```r
# Install Databricks Connect for a specific runtime version
pysparklyr::install_databricks(version = "13.3")

# Or let pysparklyr detect the version from a cluster
pysparklyr::install_databricks(cluster_id = "<cluster-id>")
```

If a user later connects to a cluster with a different Databricks Runtime version, they must run `pysparklyr::install_databricks` again with the new version or cluster ID to ensure compatibility.^[databricks-connect-for-r-databricks-on-aws.md]

### Python Environment Management

The package works with reticulate to manage Python environments for R. When used with Databricks Connect, `pysparklyr` installs the required Python dependencies, including the `databricks-connect` package, into the specified Python environment (commonly named `r-reticulate`).^[databricks-connect-for-r-databricks-on-aws.md]

## Usage with sparklyr

After installing the appropriate Databricks Connect package via `pysparklyr`, users connect to a Databricks cluster using `sparklyr::spark_connect()` with `method = "databricks_connect"`. The `pysparklyr` package ensures that the Python environment specified in the `spark_connect()` call contains the correct Databricks Connect version.^[databricks-connect-for-r-databricks-on-aws.md]

## Limitations

Databricks Connect — and by extension `pysparklyr` — has limited compatibility with [Apache Spark MLlib](/concepts/apache-spark-mllib.md), as MLlib uses RDDs while Databricks Connect only supports the DataFrame API. To use all of sparklyr's Spark MLlib functions, Databricks recommends using Databricks notebooks or the `db_repl` function from the brickster package.^[databricks-connect-for-r-databricks-on-aws.md]

## Support

Integration between sparklyr and Databricks Connect via `pysparklyr` is neither provided nor directly supported by Databricks. Users experiencing issues should consult the Posit Community or report issues on the sparklyr GitHub repository.^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [sparklyr](/concepts/sparklyr.md) — The primary R interface to Apache Spark
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) — The full setup guide for R integration
- [Databricks Connect](/concepts/databricks-connect.md) — The underlying technology for remote Spark connections
- reticulate — R package for Python interoperability
- RStudio Desktop — Common IDE for working with pysparklyr
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md) — Spark's machine learning library (limited compatibility)

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
