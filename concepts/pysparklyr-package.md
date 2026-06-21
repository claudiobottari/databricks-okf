---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8863e3a82a8985f76c64b9b81185c99c19754345db018f6467118927786cd006
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pysparklyr-package
    - sparklyr package
    - PySpark DataFrame
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: pysparklyr Package
description: An R package that manages installation of Databricks Connect dependencies and Python environments, bridging R and PySpark for Databricks connectivity.
tags:
  - r
  - databricks
  - package-management
timestamp: "2026-06-19T18:10:14.936Z"
---

```markdown
---
title: pysparklyr Package
summary: An R package that bridges PySpark and sparklyr, used to install and configure Databricks Connect dependencies including the correct Databricks Runtime version for R sessions.
sources:
  - databricks-connect-for-r-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:34:38.461Z"
updatedAt: "2026-06-19T14:47:08.805Z"
tags:
  - r
  - databricks
  - package-management
aliases:
  - pysparklyr-package
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# pysparklyr Package

The **pysparklyr** package is an R package that serves as a bridge between the `sparklyr` ecosystem and [[Databricks Connect]] for Databricks Runtime 13.0 and above. It provides functions to install and configure the Python-based Databricks Connect dependencies from within R, enabling R users to connect remote IDEs such as RStudio Desktop to Databricks clusters via the DataFrame API. ^[databricks-connect-for-r-databricks-on-aws.md]

## Overview

`pysparklyr` is part of the broader [[sparklyr]] toolchain. It is not provided or directly supported by Databricks; questions should be directed to the Posit Community (formerly RStudio Community) and issues reported on the `sparklyr` GitHub repository. ^[databricks-connect-for-r-databricks-on-aws.md]

The package automates the installation of the Python Databricks Connect package that `sparklyr` requires when using the `method = "databricks_connect"` connection mode. It ensures that the correct version of the Python environment is created, making it unnecessary for R users to manually manage Python virtual environments for Databricks Connect. ^[databricks-connect-for-r-databricks-on-aws.md]

## Installation

`pysparklyr` is available from CRAN and can be installed using the standard R package manager: ^[databricks-connect-for-r-databricks-on-aws.md]

```r
install.packages("pysparklyr")
```

It is typically installed alongside `sparklyr`, `reticulate`, `dplyr`, and `dbplyr` when setting up a Databricks Connect project in RStudio. ^[databricks-connect-for-r-databricks-on-aws.md]

## Usage

The primary function is `pysparklyr::install_databricks()`, which installs the Python Databricks Connect package and its dependencies into a Python environment that `sparklyr` will later use. The function accepts either a Databricks Runtime version string or a cluster ID: ^[databricks-connect-for-r-databricks-on-aws.md]

```r
# Install based on Databricks Runtime version
pysparklyr::install_databricks(version = "13.3")

# Install by querying a running cluster
pysparklyr::install_databricks(cluster_id = "<cluster-id>")
```

When a cluster ID is provided, `pysparklyr` queries the cluster to determine the correct Databricks Runtime version automatically, simplifying the setup process. ^[databricks-connect-for-r-databricks-on-aws.md]

If a later connection is made to a different cluster with a different Databricks Runtime version, `install_databricks()` must be run again with the new version or cluster ID to create the appropriate Python environment. ^[databricks-connect-for-r-databricks-on-aws.md]

## Limitations

- `pysparklyr` has limited compatibility with Spark MLlib functions because MLlib uses RDDs, whereas Databricks Connect supports only the DataFrame API. To use all of sparklyr's MLlib functions, Databricks recommends using Databricks notebooks or the `db_repl` function from the brickster package. ^[databricks-connect-for-r-databricks-on-aws.md]
- Authentication for Databricks Connect for R currently supports only Databricks personal access tokens. ^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [[sparklyr]] — The primary R interface to Apache Spark
- [[Databricks Connect]] — The framework that allows remote clients to connect to Databricks clusters
- Reticulate — The R package used by `pysparklyr` to manage Python environments
- RStudio Desktop — A common IDE used with `pysparklyr` and Databricks Connect
- brickster package — An alternative package for running sparklyr MLlib functions on Databricks

## Sources

- databricks-connect-for-r-databricks-on-aws.md
```

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
