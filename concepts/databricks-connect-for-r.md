---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4a9173063919534e8c3dc4382c6b48e38ba8cb873874729e3234e9a3706c8fbb
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
    - databricks-connect-for-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-connect-for-r
    - DCFR
    - Databricks Connect for R tutorial
    - Databricks Connect for R – Tutorial
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Databricks Connect for R
description: A feature enabling R IDEs like RStudio Desktop to connect to Databricks clusters using sparklyr for remote Spark execution.
tags:
  - databricks
  - r
  - spark-connect
timestamp: "2026-06-19T18:10:49.089Z"
---

```markdown
---
title: Databricks Connect for R
summary: Enables connecting R IDEs (like RStudio Desktop) and custom applications to Databricks clusters using sparklyr, for Databricks Runtime 13.0 and above.
sources:
  - databricks-connect-for-r-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:35:11.685Z"
updatedAt: "2026-06-19T09:48:20.394Z"
tags:
  - databricks
  - R
  - integration
aliases:
  - databricks-connect-for-r
  - DCFR
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks Connect for R

**Databricks Connect for R** enables you to connect popular IDEs such as RStudio Desktop, notebook servers, and other custom applications to Databricks clusters using the `sparklyr` package and the `pysparklyr` package. This integration allows R developers to work locally while executing code remotely on Databricks clusters. ^[databricks-connect-for-r-databricks-on-aws.md]

## Overview

Databricks Connect for R uses [[sparklyr]] — an R interface to Apache Spark — to connect R environments to Databricks clusters running Databricks Runtime 13.0 and above. The `pysparklyr` package provides the bridge between sparklyr and Databricks Connect's underlying Python-based infrastructure. ^[databricks-connect-for-r-databricks-on-aws.md]

This integration is provided by Posit (formerly RStudio) and is not directly supported by Databricks. For questions, refer to the Posit Community; for issues, use the Issues section of the sparklyr repository on GitHub. ^[databricks-connect-for-r-databricks-on-aws.md]

## Limitations

- **Apache Spark MLlib compatibility**: Databricks Connect has limited compatibility with Spark MLlib, as Spark MLlib uses RDDs while Databricks Connect only supports the DataFrame API. To use all of sparklyr's Spark MLlib functions, use Databricks notebooks or the `db_repl` function of the brickster package. ^[databricks-connect-for-r-databricks-on-aws.md]
- **Authentication**: Databricks Connect for R authentication currently only supports Databricks personal access tokens. ^[databricks-connect-for-r-databricks-on-aws.md]

## Requirements

To use Databricks Connect for R, you must meet the following requirements: ^[databricks-connect-for-r-databricks-on-aws.md]

- Your target Databricks workspace and cluster must meet the requirements for [[Compute configuration for Databricks Connect]].
- You must have your cluster ID available. To get it, navigate to **Compute** in your workspace sidebar, click your cluster's name, and copy the string between `clusters` and `configuration` in the URL. ^[databricks-connect-for-r-databricks-on-aws.md]

## Installation and Setup

### Prerequisites

- R and RStudio Desktop
- [[Python Wheel Task|Python]] 3.10 (or the version matching your cluster's Databricks Runtime) ^[databricks-connect-for-r-databricks-on-aws.md]

### Step 1: Create a Personal Access Token

Create a Databricks personal access token by following the steps in [[Databricks Personal Access Token (PAT) Authentication|Create personal access tokens for workspace users]]. ^[databricks-connect-for-r-databricks-on-aws.md]

### Step 2: Create the Project in RStudio

1. In RStudio Desktop, click **File > New Project**.
2. Select **New Directory** then **New Project**.
3. Set a directory name and location.
4. Select **Use renv with this project**.
5. Click **Create Project**. ^[databricks-connect-for-r-databricks-on-aws.md]

### Step 3: Install Dependencies

Install the required R packages via **Tools > Install Packages** with the following package list: `sparklyr, pysparklyr, reticulate, usethis, dplyr, dbplyr`. ^[databricks-connect-for-r-databricks-on-aws.md]

After installation, run the following in the Console to install Python (replace `3.10` with the Python version on your cluster): ^[databricks-connect-for-r-databricks-on-aws.md]

```r
reticulate::install_python(version = "3.10")
```

Then install the Databricks Connect package, replacing `13.3` with your cluster's [[Databricks Runtime 13.3 LTS|Databricks Runtime version]]: ^[databricks-connect-for-r-databricks-on-aws.md]

```r
pysparklyr::install_databricks(version = "13.3")
```

Alternatively, you can specify the cluster ID to auto-detect the correct version: ^[databricks-connect-for-r-databricks-on-aws.md]

```r
pysparklyr::install_databricks(cluster_id = "<cluster-id>")
```

### Step 4: Set Environment Variables

Create or edit an `.Renviron` file to store your workspace URL, personal access token, and cluster ID without hard-coding them into scripts. Use `usethis::edit_r_environ()` to open the file, then add: ^[databricks-connect-for-r-databricks-on-aws.md]

```
DATABRICKS_HOST=<workspace-url>
DATABRICKS_TOKEN=<personal-access-token>
DATABRICKS_CLUSTER_ID=<cluster-id>
```

Restart R (Session > Restart R) to load the environment variables. ^[databricks-connect-for-r-databricks-on-aws.md]

## Usage

### Connecting to a Databricks Cluster

Create a new R script and use the following pattern to establish a connection: ^[databricks-connect-for-r-databricks-on-aws.md]

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

### Querying Data

Once connected, you can query tables in your Databricks workspace. For example, to query the Nyctaxi sample data: ^[databricks-connect-for-r-databricks-on-aws.md]

```r
trips <- dplyr::tbl(
  sc,
  dbplyr::in_catalog("samples", "nyctaxi", "trips")
)
print(trips, n = 5)
```

## Debugging

Databricks Connect for R supports debugging through RStudio's built-in debugger. Set breakpoints by clicking the gutter next to a line in your script, then click **Source** to run. When the code pauses, inspect variables in the **Environment** view, then click **Debug > Continue** to resume execution. ^[databricks-connect-for-r-databricks-on-aws.md]

## Related Concepts

- [[Databricks Connect for Python]]
- [[Databricks Connect for Scala]]
- [[Spark Connect]]
- [[sparklyr]]
- brickster package
- RStudio
- Apache Spark DataFrame API
- Databricks personal access tokens

## Sources

- databricks-connect-for-r-databricks-on-aws.md
```

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
