---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 865def5a6e3503fcd2d6a989013b22cd15327d04d983f36f958613d6783a93e2
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rstudio-debugging-with-databricks-connect
    - RDWDC
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: RStudio debugging with Databricks Connect
description: Databricks Connect enables interactive debugging of Spark code in RStudio Desktop, including setting breakpoints, inspecting variables in the Environment view, and stepping through code execution.
tags:
  - RStudio
  - debugging
  - workflow
timestamp: "2026-06-19T09:49:10.606Z"
---

# RStudio Debugging with Databricks Connect

**RStudio debugging with Databricks Connect** enables you to debug R code that runs against a remote Databricks cluster from within the RStudio Desktop IDE. By setting breakpoints and stepping through code interactively, you can inspect variables and troubleshoot logic in a familiar R development environment while the actual computation executes on the cluster. ^[databricks-connect-for-r-databricks-on-aws.md]

## Overview

Databricks Connect for R uses the `sparklyr` package’s `databricks_connect` method to establish a connection to a Databricks cluster. Once connected, R code that calls Apache Spark operations (e.g., via `dplyr` or `dbplyr` verbs) is translated into Spark jobs that run remotely. This allows you to develop and debug R scripts locally in RStudio while leveraging the compute power of Databricks. ^[databricks-connect-for-r-databricks-on-aws.md]

> **Note:** The `sparklyr` integration with Databricks Connect for Databricks Runtime 13.0 and above is not officially provided or supported by Databricks. For questions, refer to the Posit Community or the `sparklyr` GitHub repository. ^[databricks-connect-for-r-databricks-on-aws.md]

## Prerequisites

Before debugging with Databricks Connect, you must complete the setup described in the [Databricks Connect for R](/concepts/databricks-connect-for-r.md) tutorial:

- Install R and RStudio Desktop.
- Install Python (version matching the cluster’s Databricks Runtime).
- Install the required R packages: `sparklyr`, `pysparklyr`, `reticulate`, `dplyr`, `dbplyr`, `usethis`.
- Install Databricks Connect via `pysparklyr::install_databricks()`.
- Create a [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md) for authentication.
- Set environment variables (`DATABRICKS_HOST`, `DATABRICKS_TOKEN`, `DATABRICKS_CLUSTER_ID`) in an `.Renviron` file.
- Establish a connection with `sparklyr::spark_connect(method = "databricks_connect", ...)`. ^[databricks-connect-for-r-databricks-on-aws.md]

## Debugging Workflow

The debugging process uses RStudio’s built-in breakpoint mechanism, identical to debugging a local R script. There are no special debugging commands beyond the standard RStudio interface. The following steps reproduce the tutorial’s example: ^[databricks-connect-for-r-databricks-on-aws.md]

1. **Set a breakpoint** — In the R script editor, click the gutter next to the line where you want execution to pause. For example, clicking the gutter next to `print(trips, n = 5)` places a breakpoint on that line. ^[databricks-connect-for-r-databricks-on-aws.md]
2. **Source the script** — Click **Source** in the editor toolbar (or use the keyboard shortcut). The script starts executing on the remote cluster. ^[databricks-connect-for-r-databricks-on-aws.md]
3. **Inspect variables** — When execution reaches the breakpoint, the code pauses. You can examine the current value of any variable in the **Environment** pane. For instance, you can inspect the `trips` table object to see its schema or preview data. ^[databricks-connect-for-r-databricks-on-aws.md]
4. **Continue execution** — On the main menu, click **Debug > Continue** (or use the shortcut). The script proceeds to the next breakpoint or to completion. ^[databricks-connect-for-r-databricks-on-aws.md]

The illustration below shows the RStudio interface during a debugging session: ^[databricks-connect-for-r-databricks-on-aws.md]

![Debugging an R script with Databricks Connect in RStudio Desktop](https://docs.databricks.com/aws/en/assets/images/debug-project-rstudio-80040085277ea83850c52bbfd1a1927a.png)

## Limitations

- Databricks Connect for R is compatible only with the DataFrame API. [Apache Spark MLlib](/concepts/apache-spark-mllib.md) functions that rely on RDDs are not supported. To use the full set of `sparklyr` MLlib capabilities, consider using Databricks notebooks or the `db_repl` function from the `brickster` package. ^[databricks-connect-for-r-databricks-on-aws.md]
- Authentication is limited to Databricks personal access tokens; other authentication methods are not supported. ^[databricks-connect-for-r-databricks-on-aws.md]
- The debugging experience is limited to R code that runs interactively via `sparklyr`. Complex remote job debugging (e.g., on Spark executors) may require additional logs.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – Connects IDEs and custom applications to Databricks clusters.
- [sparklyr](/concepts/sparklyr.md) – R interface to Apache Spark.
- RStudio Desktop – IDE for R development.
- [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md) – Authentication method for Databricks Connect.
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) – Full setup tutorial.

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
