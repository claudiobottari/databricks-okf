---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac5c2f76c7e4a551140c93e049d9dbe3d1b3f856d5ebe62eb4c1230d40e6cc89
  pageDirectory: concepts
  sources:
    - use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbt-databricks-adapter-package
    - DAP
    - dbt-databricks Package
    - dbt-databricks package
    - dbt-databricks
  citations:
    - file: use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md
title: dbt-databricks Adapter Package
description: The recommended dbt adapter package for Databricks, a fork of dbt-spark optimized for Databricks, used to connect dbt Core to Databricks compute and SQL warehouses.
tags:
  - dbt
  - databricks
  - adapter
  - package
timestamp: "2026-06-19T23:21:29.338Z"
---

Here is the wiki page for "dbt-databricks Adapter Package".

---

## dbt-databricks Adapter Package

The **dbt-databricks Adapter Package** is the recommended dbt adapter for connecting dbt Core projects to Databricks. It is a fork of the `dbt-spark` adapter, optimized specifically for Databricks. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

### Overview

When using dbt Core with Databricks, Databricks recommends the `dbt-databricks` package over the `dbt-spark` package. The `dbt-databricks` adapter is designed to provide better performance and tighter integration with Databricks features compared to the more general `dbt-spark` adapter. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

### Usage with Databricks Jobs

The `dbt-databricks` package is typically installed as a library when running dbt tasks within [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md). When configuring a dbt task via the Jobs REST API, the package is specified as a PyPI library dependency:

```json
"libraries": [
  {
    "pypi": {
      "package": "dbt-databricks>=1.0.0,<2.0.0"
    }
  }
]
```

^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

### Custom Profiles

When using a custom `profiles.yml` file to run a dbt task with a SQL warehouse or all-purpose compute, the adapter type must be specified as `databricks`. The `profiles.yml` configuration includes the Databricks host, HTTP path, and schema, with credentials provided dynamically at runtime via environment variables. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

A sample `profiles.yml` entry for the adapter:

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

^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

### Python Model Support

The `dbt-databricks` adapter supports [dbt Python models](/concepts/dbt-python-models-on-databricks.md) (beta as of dbt 1.3+), allowing transformations that are difficult to implement with SQL to be written using Python. However, Python models cannot be run using a SQL warehouse; they require Databricks compute. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

### Related Concepts

- dbt Core — The underlying transformation framework.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — The orchestration service where dbt tasks are executed.
- SQL warehouse — A compute target for running dbt-generated SQL.
- [dbt Python models](/concepts/dbt-python-models-on-databricks.md) — Python-based transformations supported by the adapter.

### Sources

- use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md

# Citations

1. [use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md](/references/use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws-9420061c.md)
