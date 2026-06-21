---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1b517c56f033d6984d2ef3269e3720d994f87d8bc26d44b73d80455227ae5c3
  pageDirectory: concepts
  sources:
    - databricks-connect-for-r-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - r-renviron-databricks-configuration-pattern
    - R.DCP
  citations:
    - file: databricks-connect-for-r-databricks-on-aws.md
title: R .Renviron Databricks configuration pattern
description: Best practice pattern for storing Databricks workspace URL, personal access token, and cluster ID in a .Renviron file for use in R projects with Databricks Connect.
tags:
  - databricks
  - r
  - configuration
  - security
timestamp: "2026-06-18T11:35:10.148Z"
---

# R .Renviron Databricks Configuration Pattern

The **R .Renviron Databricks configuration pattern** is a recommended approach for storing Databricks connection credentials — such as workspace URL, personal access token, and cluster ID — in a local `.Renviron` file when using [Databricks Connect for R](/concepts/databricks-connect-for-r.md) with RStudio Desktop. This pattern avoids hard-coding sensitive or environment-specific values directly into R scripts. ^[databricks-connect-for-r-databricks-on-aws.md]

## Overview

When using Databricks Connect for R with the `sparklyr` and `pysparklyr` packages, you must provide three key connection parameters: the Databricks workspace instance URL, a personal access token for authentication, and the cluster ID of the target cluster. Hard-coding these values into R scripts is not recommended because they may change over time and expose sensitive credentials. ^[databricks-connect-for-r-databricks-on-aws.md]

The `.Renviron` file pattern leverages RStudio Desktop's built-in support for environment variables to store these values separately. The file is loaded automatically when R starts, making the variables available via `Sys.getenv()` in your R scripts. ^[databricks-connect-for-r-databricks-on-aws.md]

## File Structure

Within a Databricks Connect for R project, the `.Renviron` file should contain three environment variables: ^[databricks-connect-for-r-databricks-on-aws.md]

```
DATABRICKS_HOST=<workspace-url>
DATABRICKS_TOKEN=<personal-access-token>
DATABRICKS_CLUSTER_ID=<cluster-id>
```

Replace the placeholders with the following values: ^[databricks-connect-for-r-databricks-on-aws.md]

- `<workspace-url>` — The workspace instance URL, for example `https://dbc-a1b2345c-d6e7.cloud.databricks.com`
- `<personal-access-token>` — A [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md) from the user's account
- `<cluster-id>` — The cluster ID, obtained from the cluster details page URL in the workspace (the string between `clusters` and `configuration`)

## Setup Process

### Creating the .Renviron File

1. In RStudio Desktop, run the following command in the Console to create or open the `.Renviron` file for editing: ^[databricks-connect-for-r-databricks-on-aws.md]
   ```r
   usethis::edit_r_environ()
   ```
2. Add the three environment variable definitions for `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, and `DATABRICKS_CLUSTER_ID`. ^[databricks-connect-for-r-databricks-on-aws.md]
3. Save the file. ^[databricks-connect-for-r-databricks-on-aws.md]
4. Restart R to load the environment variables: click **Session > Restart R**. ^[databricks-connect-for-r-databricks-on-aws.md]

### Using Environment Variables in Code

After loading the environment variables, reference them in your R scripts using `Sys.getenv()`: ^[databricks-connect-for-r-databricks-on-aws.md]

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

The `spark_connect()` call with `method = "databricks_connect"` establishes a connection to the specified Databricks cluster using the credentials stored in the environment variables. ^[databricks-connect-for-r-databricks-on-aws.md]

## Best Practices

- **Do not hard-code credentials.** Always use the `.Renviron` pattern or another secure credential management approach instead of embedding tokens or cluster IDs in source code. ^[databricks-connect-for-r-databricks-on-aws.md]
- **Keep `.Renviron` out of version control.** Add `.Renviron` to your `.gitignore` file to prevent accidental exposure of credentials in shared repositories.
- **Use project-scoped `.Renviron` files.** The `.Renviron` file created via `usethis::edit_r_environ()` is typically project-specific when created within an RStudio project, keeping credentials scoped to the relevant project.
- **Update the Python environment when changing clusters.** If connecting to a cluster with a different Databricks Runtime version, run `pysparklyr::install_databricks()` again with the new version or cluster ID to ensure the correct Python environment is used. ^[databricks-connect-for-r-databricks-on-aws.md]

## Limitations

- **PAT authentication only.** The `.Renviron` pattern for Databricks Connect for R currently supports only [Databricks personal access token](/concepts/databricks-personal-access-token-pat-authentication.md) authentication. ^[databricks-connect-for-r-databricks-on-aws.md]
- **R-specific pattern.** This pattern is specific to R development with RStudio Desktop. Python and Scala clients use different configuration approaches, such as [Databricks CLI configuration profiles](/concepts/databricks-configuration-profiles.md) or [Databricks Connect configuration files](/concepts/databricks-connect-configuration-profiles.md).

## Related Concepts

- [Databricks Connect for R](/concepts/databricks-connect-for-r.md) — The overall integration of R with Databricks Connect
- [sparklyr](/concepts/sparklyr.md) — The R package used to interface with Apache Spark
- Databricks Authentication — Overview of authentication methods for Databricks
- RStudio Project Configuration — Managing R project settings and dependencies
- environment variable best practices — General guidance for managing secrets in development

## Sources

- databricks-connect-for-r-databricks-on-aws.md

# Citations

1. [databricks-connect-for-r-databricks-on-aws.md](/references/databricks-connect-for-r-databricks-on-aws-29a91e1a.md)
