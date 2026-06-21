---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d2b82155f3d9ea9f73c340f8f58fa33291e6ecd7741b95e6c181773631412133
  pageDirectory: concepts
  sources:
    - delta_duplicate_columns_found-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-metadata-update-duplicate-detection
    - DLMUDD
  citations:
    - file: delta_duplicate_columns_found-error-condition-databricks-on-aws.md
title: Delta Lake metadata update duplicate detection
description: A sub-condition under DELTA_DUPLICATE_COLUMNS_FOUND specifically for detecting duplicate columns when updating table metadata, distinct from schema or partition validation.
tags:
  - delta-lake
  - metadata
  - validation
timestamp: "2026-06-19T18:24:44.948Z"
---

# Delta Lake metadata update duplicate detection

**Delta Lake metadata update duplicate detection** refers to the built-in check that prevents duplicate column names from being introduced when a Delta table’s metadata is updated. When a metadata update would create duplicate columns, Delta Lake raises the `DELTA_DUPLICATE_COLUMNS_FOUND` error with SQLSTATE `42711`. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Error condition

The error class `DELTA_DUPLICATE_COLUMNS_FOUND` produces the generic message `Found duplicate column(s): <duplicateCols>`. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

Delta Lake classifies the source of the duplicate detection into several sub‑classes. The sub‑class that directly covers metadata updates is **EXISTING_SCHEMA**. Its description states that “The duplicate was found in the existing table schema” and, more specifically, “The duplicate was found in the metadata update.” ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Sub‑classes

Below is the full list of sub‑classes under `DELTA_DUPLICATE_COLUMNS_FOUND`, each providing the context in which the duplicate was detected:

- `ADDING_COLUMNS` – duplicate while adding columns
- `CLUSTER_BY` – duplicate in `CLUSTER BY`
- `CONVERT_TO_DELTA` – duplicate during conversion to Delta
- `DATA` – duplicate in the data being saved
- `EXISTING_SCHEMA` – duplicate found in the existing table schema / metadata update
- `PARTITION_COLUMNS` – duplicate in partition columns
- `PARTITION_SCHEMA` – duplicate in the partition schema
- `READ_SCHEMA` – duplicate in the schema of the data being read
- `REPLACING_COLUMNS` – duplicate while replacing columns
- `SPECIFIED_COLUMNS` – duplicate in specified columns
- `TABLE_SCHEMA` – duplicate in the table schema

The `EXISTING_SCHEMA` sub‑class is the one that directly applies to metadata update operations. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Related concepts

- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format
- Delta table schema – The schema definition of a Delta table
- Table metadata – Properties, schema, and configuration stored in the Delta transaction log
- SQLSTATE codes – Standard SQL error code classification

## Sources

- delta_duplicate_columns_found-error-condition-databricks-on-aws.md

# Citations

1. [delta_duplicate_columns_found-error-condition-databricks-on-aws.md](/references/delta_duplicate_columns_found-error-condition-databricks-on-aws-42950ac1.md)
