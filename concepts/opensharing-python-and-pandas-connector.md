---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ed1dfcd91dd14e8e11fb4dd79f2b0d8bcc83fdaf82ef96c96acbf1a237d6fa8
  pageDirectory: concepts
  sources:
    - read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-python-and-pandas-connector
    - Pandas Connector and OpenSharing Python
    - OPAPC
  citations:
    - file: read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
title: OpenSharing Python and Pandas Connector
description: A Python connector (delta-sharing library) that enables listing and reading shared tables as pandas DataFrames, with support for change data feed queries.
tags:
  - python
  - pandas
  - delta-sharing
timestamp: "2026-06-19T20:11:00.241Z"
---

# OpenSharing Python and Pandas Connector

The **OpenSharing Python and Pandas Connector** is a client library that enables reading data shared through the OpenSharing (formerly Delta Sharing) open protocol using Python and the Pandas data analysis library. It allows recipients to discover, list, and load shared datasets without requiring a Databricks workspace or Unity Catalog. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Overview

In the Databricks-to-Open sharing model, data providers share datasets with recipients using a credential file. The OpenSharing Python connector (`delta-sharing`) provides programmatic access to these shared datasets. Recipients can list available tables, load data into Pandas DataFrames, and access change data feeds (CDF) for incremental updates. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

Access persists as long as the credential is valid and the provider continues to share the data. Providers manage credential expiration and rotation. Updates to the data are available in near real time. Recipients can read and make copies of the shared data but cannot modify the source data. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Installation

Install the `delta-sharing` Python connector using pip:

```bash
pip install delta-sharing
```

^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Listing Shared Tables

To discover which tables have been shared with you, create a `SharingClient` using the path to the credential file and call `list_all_tables()`:

```python
import delta_sharing

client = delta_sharing.SharingClient(f"<profile-path>/config.share")
client.list_all_tables()
```

The result is an array of tables with metadata including the table name, share name, and schema. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Loading Shared Data into Pandas

Use the `load_as_pandas()` function to load a shared table into a Pandas DataFrame. The table path follows the format `<profile-path>#<share-name>.<schema-name>.<table-name>`:

```python
import delta_sharing

delta_sharing.load_as_pandas(
    f"<profile-path>#<share-name>.<schema-name>.<table-name>"
)
```

^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Accessing Change Data Feed (CDF)

If the data provider has shared the table's history and change data feed is enabled, you can access incremental changes using `load_table_changes_as_pandas()`. You must provide at least one start parameter (version or timestamp):

```python
import delta_sharing

# By version range
delta_sharing.load_table_changes_as_pandas(
    f"<profile-path>#<share-name>.<schema-name>.<table-name>",
    starting_version=<starting-version>,
    ending_version=<ending-version>
)

# By timestamp range
delta_sharing.load_table_changes_as_pandas(
    f"<profile-path>#<share-name>.<schema-name>.<table-name>",
    starting_timestamp=<starting-timestamp>,
    ending_timestamp=<ending-timestamp>
)
```

^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Prerequisites

- Pandas 0.25.3 or above
- Access to the credential file shared by the data provider
- The credential file must be accessible via an absolute path (can refer to a cloud object or [Unity Catalog](/concepts/unity-catalog.md) volume) ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Limitations

The OpenSharing Python connector has the following limitations:

- Version 1.1.0+ supports snapshot queries on tables with [Column Mapping](/concepts/delta-table-column-mapping.md) but CDF queries on tables with column mapping are not supported.
- CDF queries with `use_delta_format=True` fail if the schema changed during the queried version range.

^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Related Concepts

- [OpenSharing Protocol](/concepts/opensharing-protocol.md) — The open standard for sharing data across platforms
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying technology for OpenSharing
- [OpenSharing Spark Connector](/concepts/opensharing-apache-spark-connector.md) — The Spark-based connector for reading shared data
- Credential File — The authentication mechanism for accessing shared data
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) — Incremental data change tracking
- [Column Mapping](/concepts/delta-table-column-mapping.md) — A Delta Lake feature for renaming and dropping columns

## Sources

- read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md

# Citations

1. [read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md](/references/read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws-9252dd38.md)
