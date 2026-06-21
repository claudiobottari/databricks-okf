---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 32587f951781ee797f55be6b827bcc1e90d7adf2ef3cd344395e932407c600f2
  pageDirectory: concepts
  sources:
    - limitations-with-databricks-connect-for-scala-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unavailable-databricks-utilities-subset
    - UDUS
  citations:
    - file: limitations-with-databricks-connect-for-scala-databricks-on-aws.md
title: Unavailable Databricks Utilities Subset
description: Certain Databricks Utilities (credentials, library, notebook workflow, widgets) are not available in Databricks Connect for Scala.
tags:
  - databricks-connect
  - utilities
  - limitations
  - scala
timestamp: "2026-06-19T19:12:35.079Z"
---

# Unavailable Databricks Utilities Subset

The **Unavailable Databricks Utilities Subset** refers to the four Databricks Utilities (`dbutils`) commands that are not supported when using [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md). When connecting to a Databricks cluster through Databricks Connect, the following utility commands are unavailable: `credentials`, `library`, `notebook workflow`, and `widgets`. ^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Unavailable Commands

The following `dbutils` commands are not available in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md):

- **`dbutils.credentials`** — Used for managing credential objects for accessing external services.
- **`dbutils.library`** — Used for installing and managing libraries on clusters.
- **`dbutils.notebook.workflow`** — Used for running notebook workflows and managing notebook job parameters.
- **`dbutils.widgets`** — Used for creating and managing notebook widgets (dropdown menus, text boxes, etc.).

^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Impact

These limitations affect developers who rely on [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) to interact with Databricks clusters from external IDEs, notebook servers, or custom applications. If your workflow depends on any of these utilities, you must either refactor to use alternative APIs or run the code directly on the Databricks cluster instead of through Databricks Connect. ^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

The unavailable utilities are part of the broader set of feature limitations in [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md), which also includes restrictions on Spark Context usage, RDDs, scalar UDFs on dedicated access mode compute, and streaming `foreachBatch` operations. ^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Applicable Versions

These limitations apply to Databricks Connect for Databricks Runtime 13.3 LTS and above. For version-specific requirements, consult the Databricks Connect installation documentation. ^[limitations-with-databricks-connect-for-scala-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — The client library that enables remote connection to Databricks clusters.
- Databricks Utilities — The full set of `dbutils` commands available on Databricks.
- [Limitations with Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md) — The complete list of feature restrictions.
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — The Python equivalent, with its own set of limitations.

## Sources

- limitations-with-databricks-connect-for-scala-databricks-on-aws.md

# Citations

1. [limitations-with-databricks-connect-for-scala-databricks-on-aws.md](/references/limitations-with-databricks-connect-for-scala-databricks-on-aws-8e97ac24.md)
