---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 19096fcb890c980a4be6cb48db0ff32b91e598cd35792d9a9d6be7ef349f96ba
  pageDirectory: concepts
  sources:
    - use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-dbt-profiles-in-databricks-jobs
    - CDPIDJ
  citations:
    - file: use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md
title: Custom dbt Profiles in Databricks Jobs
description: Using a custom profiles.yml file to configure dbt task connections to SQL warehouses or all-purpose compute, with dynamic credential injection via environment variables.
tags:
  - dbt
  - databricks
  - profiles
  - configuration
timestamp: "2026-06-19T23:21:23.778Z"
---

# Custom dbt Profiles in Databricks Jobs

**Custom dbt Profiles** allow you to define a `profiles.yml` file to configure how a dbt Core task connects to a SQL warehouse or all-purpose compute when running in a Databricks Job. By default, the dbt task runs the dbt Python process using Databricks compute and executes the generated SQL against a selected SQL warehouse. Custom profiles override this default connection behavior, giving you control over the target warehouse or compute resource. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

## Overview

When you run a dbt task in a Databricks job, you typically specify a SQL warehouse in the task configuration. The custom profile approach provides an alternative method for defining the connection target by placing a `profiles.yml` file in your dbt project repository. This is useful when you need a specific configuration that differs from the standard task setup. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

## Requirements

- You must use a SQL warehouse (serverless or pro) or all-purpose compute as the target for a dbt task. You cannot use job compute as a dbt target. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
- Your dbt project must be stored in [Databricks Git folders](/concepts/databricks-git-folders-for-cicd.md), not DBFS. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
- You must have the Databricks SQL entitlement enabled. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

## Creating a Custom Profile

1. Fork the dbt project repository (for example, the [jaffle_shop](https://github.com/dbt-labs/jaffle_shop) example project). ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
2. Clone the forked repository to your desktop. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
3. Create a new file named `profiles.yml` in the project directory with the following content: ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

```yaml
jaffle_shop:
  target: databricks_job
  outputs:
    databricks_job:
      type: databricks
      method: http
      schema: '<schema>'
      host: '<http-host>'
      http_path: '<http-path>'
      token: "{{ env_var('DBT_ACCESS_TOKEN') }}"
```

### Configuration Fields

- **`jaffle_shop`**: Replace with your dbt project name as defined in your project's `dbt_project.yml`. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
- **`<schema>`**: The schema name for the project tables. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
- **`<http-host>`**: For a SQL warehouse, use the **Server Hostname** from the Connection Details tab. For all-purpose compute, use the **Server Hostname** from the Advanced Options → JDBC/ODBC tab. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
- **`<http-path>`**: For a SQL warehouse, use the **HTTP Path** from the Connection Details tab. For all-purpose compute, use the **HTTP Path** from the Advanced Options → JDBC/ODBC tab. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
- **`token`**: Uses the `{{ env_var('DBT_ACCESS_TOKEN') }}` Jinja2 template to dynamically insert credentials at runtime. This keeps secrets out of source control. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

### Credential Handling

You do not specify secrets, such as access tokens, directly in the `profiles.yml` file because it is checked into source control. Instead, the file uses dbt's templating functionality to insert credentials dynamically at runtime. The generated credentials are valid for the duration of the run (up to a maximum of 30 days) and are automatically revoked after completion. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

## Configuring the Job to Use a Custom Profile

1. Push the `profiles.yml` file to your forked Git repository. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
2. In the Databricks UI, navigate to **Jobs & Pipelines** and select your dbt job. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
3. In the **Tasks** tab, click **Edit** on the source and enter your forked repository details. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
4. In **SQL warehouse**, select **None (Manual)** — this disables the default warehouse connection and allows the custom profile to define the target. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
5. In **Profiles Directory**, enter the relative path to the directory containing the `profiles.yml` file. Leave blank to use the repository root as the default. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

## Use Cases

- **SQL warehouse with custom profile**: Connect to a specific SQL warehouse by supplying its server hostname and HTTP path in the profile. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
- **All-purpose compute with custom profile**: Connect to all-purpose compute by supplying the server hostname and HTTP path from the compute's JDBC/ODBC settings. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

## Important Considerations

- Only a SQL warehouse or all-purpose compute can be used as the target for a dbt task. Job compute cannot be used as a target. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]
- Databricks recommends using the same Databricks Runtime version for the compute and the SQL warehouse to avoid subtle differences in performance and SQL language support. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

## Related Concepts

- dbt Core — The open-source transformation framework that dbt tasks run.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — The workflow orchestration platform for running dbt tasks.
- SQL warehouse — The compute resource for executing dbt-generated SQL.
- All-purpose compute — An alternative compute target for dbt tasks.
- [Databricks Git folders](/concepts/databricks-git-folders-for-cicd.md) — The required storage location for dbt project files.
- [dbt-databricks](/concepts/dbt-databricks-adapter-package.md) — The recommended adapter package for Databricks.

## Sources

- use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md

# Citations

1. [use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md](/references/use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws-9420061c.md)
