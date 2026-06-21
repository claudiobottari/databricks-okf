---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: adf92919877b7e1123883e27e4ccb20d5aef0dd5381c1e32eadbdc393adf3e41
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - debugging-databricks-connect-r-code-in-rstudio
    - DDCRCIR
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: Debugging Databricks Connect R Code in RStudio
description: The ability to set breakpoints and debug R code that runs against Databricks clusters through Databricks Connect within RStudio Desktop.
tags:
  - debugging
  - RStudio
  - databricks
timestamp: "2026-06-18T15:04:38.978Z"
---

# Debugging Databricks Connect R Code in RStudio

**Debugging Databricks Connect R Code in RStudio** refers to the practice of interactively inspecting and stepping through R code that runs on a remote Databricks cluster via [Databricks Connect](/concepts/databricks-connect.md) for R. The integration uses [sparklyr](/concepts/sparklyr.md) and [pysparklyr](/concepts/pysparklyr.md) to connect RStudio Desktop to a Databricks cluster, and RStudio’s built-in debugging tools allow breakpoints, variable inspection, and step‑wise execution of the remote code.

## Overview

Once you have created a Databricks Connect project in RStudio, installed the required packages, and set the environment variables (`DATABRICKS_HOST`, `DATABRICKS_TOKEN`, `DATABRICKS_CLUSTER_ID`), you can debug R code that calls Spark operations on the cluster. Debugging works by setting breakpoints in R scripts and using RStudio’s **Source** command with the debugger active. ^[databricks-connect-for-r-databricks-on-aws.md]

## Step‑by‑Step Debugging

The following steps assume you have completed the tutorial setup (project creation, package installation, environment variable configuration, and code entry) as described in [Databricks Connect for R – Tutorial](/concepts/databricks-connect-for-r.md). ^[databricks-connect-for-r-databricks-on-aws.md]

1. **Set a breakpoint** – Open the R script (e.g., `demo.R`) in RStudio. Click the gutter (the space to the left of the line numbers) next to the line where you want execution to pause. For example, click next to `print(trips, n = 5)`. A red dot appears. ^[databricks-connect-for-r-databricks-on-aws.md]

2. **Run the script with the debugger** – In the toolbar of the script file, click **Source** (the **Source** button runs the script and respects breakpoints, unlike **Run**). The code will execute until it reaches the breakpoint and then pause. ^[databricks-connect-for-r-databricks-on-aws.md]

3. **Inspect variables** – While execution is paused, you can examine the current state of variables in the **Environment** view (**View > Show Environment**). This allows you to check DataFrames, connection objects, or other R objects during the remote execution. ^[databricks-connect-for-r-databricks-on-aws.md]

4. **Continue execution** – On the main menu, click **Debug > Continue** (or use the keyboard shortcut, typically **Shift+F5**). The code resumes from the breakpoint and completes the remaining operations, outputting results to the **Console**. ^[databricks-connect-for-r-databricks-on-aws.md]

## Tips

- Ensure your cluster is running before debugging, as Databricks Connect requires an active cluster. ^[databricks-connect-for-r-databricks-on-aws.md]
- Breakpoints only work on R code that is executed through the **Source** command, not via individual line‑by‑line execution in the console.
- The [Connections pane](/concepts/sap-bdc-connection.md) (**View > Show Connections**) can be used to browse catalogs, schemas, tables, and views while debugging. ^[databricks-connect-for-r-databricks-on-aws.md]
- For more advanced debugging, consider using `recover()` or `traceback()` after an error, though these are not described in the source material.

## Related Concepts

- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) – Setup and configuration guide.
- [sparklyr](/concepts/sparklyr.md) – The R package that provides the `spark_connect()` function.
- [pysparklyr](/concepts/pysparklyr.md) – The package used to install the correct Databricks Connect Python environment.
- [Personal Access Token Authentication](/concepts/databricks-personal-access-token-pat-authentication.md) – How the connection is authenticated.
- .Renviron – How environment variables are stored for credentials.
- RStudio Desktop Debugging – General RStudio debugging features.

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
