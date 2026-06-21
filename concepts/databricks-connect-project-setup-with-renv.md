---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 298bb91e400d0d554d94e19bcfeaa205479a163ee549b6310a842c78aec33569
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-project-setup-with-renv
    - DCPSWR
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Databricks Connect Project Setup with renv
description: A reproducible R project workflow using RStudio, renv, and environment variables (.Renviron) to configure Databricks Connect connections.
tags:
  - r
  - workflow
  - reproducibility
timestamp: "2026-06-19T18:10:53.284Z"
---

# Databricks Connect Project Setup with renv

**Databricks Connect Project Setup with renv** refers to the process of creating a new R project in RStudio Desktop that uses the `renv` package for dependency management, configured to work with [Databricks Connect for R](/concepts/databricks-connect-for-r.md) via the `sparklyr` and `pysparklyr` packages. This setup enables R developers to connect to Databrick clusters from their local IDE.

## Overview

The `renv` package provides reproducible R environment management by creating a project-local library of R packages. When setting up a Databricks Connect project, selecting the `renv` option during project creation ensures that all dependencies are isolated and version-controlled within the project directory, preventing conflicts with other R projects on the same machine. ^[databricks-connect-for-r-databricks-on-aws.md]

## Project Creation

To create a new Databricks Connect project with `renv`:

1. In RStudio Desktop, click **File > New Project**.
2. Select **New Directory**, then **New Project**.
3. Enter a directory name and location for the project.
4. Select **Use renv with this project**. If prompted to install an updated version of the `renv` package, click **Yes**.
5. Click **Create Project**.

^[databricks-connect-for-r-databricks-on-aws.md]

## Installing Dependencies

After project creation, install the required packages:

```r
# Install packages from CRAN
sparklyr, pysparklyr, reticulate, usethis, dplyr, dbplyr
```

Use RStudio's **Tools > Install Packages** menu to install these packages, ensuring **Install dependencies** is selected. The `sparklyr` and `pysparklyr` packages and their dependencies will be installed in the project's R virtual environment. ^[databricks-connect-for-r-databricks-on-aws.md]

### Python and Databricks Connect Installation

Databricks Connect for R requires Python to be installed first via `reticulate`:

```r
reticulate::install_python(version = "3.10")
```

Replace `3.10` with the Python version matching your Databricks cluster's Python version. ^[databricks-connect-for-r-databricks-on-aws.md]

Then install the Databricks Connect package:

```r
pysparklyr::install_databricks(version = "13.3")
```

Alternatively, you can specify a cluster ID to auto-detect the correct Databricks Runtime version:

```r
pysparklyr::install_databricks(cluster_id = "<cluster-id>")
```

^[databricks-connect-for-r-databricks-on-aws.md]

If you later connect to a different cluster with a different Databricks Runtime version, you must run `pysparklyr::install_databricks` again with the new version or cluster ID. ^[databricks-connect-for-r-databricks-on-aws.md]

## Environment Configuration

Databricks recommends storing sensitive connection details as environment variables rather than hard-coding them in scripts. Use an `.Renviron` file in the project root:

1. Run `usethis::edit_r_environ()` to create or edit the `.Renviron` file.
2. Add the following content, replacing placeholders with your actual values:

```
DATABRICKS_HOST=<workspace-url>
DATABRICKS_TOKEN=<personal-access-token>
DATABRICKS_CLUSTER_ID=<cluster-id>
```

3. Save the file and restart R to load the environment variables. ^[databricks-connect-for-r-databricks-on-aws.md]

## Sample Code

Create an R script (e.g., `demo.R`) with the following code to verify the connection:

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

## Authentication

Databricks Connect for R currently only supports [Personal Access Token (PAT) authentication#Databricks PAT|Databricks personal access token authentication](/concepts/databricks-personal-access-token-pat-authentication.md). Tokens are stored in the `DATABRICKS_TOKEN` environment variable and read at runtime via `Sys.getenv()`. ^[databricks-connect-for-r-databricks-on-aws.md]

## Requirements

Before setting up the project, ensure:

- The target Databricks workspace and cluster meet the requirements for [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md).
- The cluster ID is available from the workspace UI (found in the URL between `clusters` and `configuration`).
- RStudio Desktop and Python 3.10 (or matching cluster version) are installed. ^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) — The integration framework this project setup supports
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — Alternative Python-based Databricks Connect setup
- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — Alternative Scala-based Databricks Connect setup
- sparklyr package — The R interface to Apache Spark used in the connection
- [pysparklyr Package](/concepts/pysparklyr.md) — The R bridge to PySpark and Databricks Connect
- renv package — R environment management tool used for dependency isolation
- Reproducible R environments — Broader concept of environment reproducibility in R

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
