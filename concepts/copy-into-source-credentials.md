---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e0d24ce1e573d42dae3e706b532ed4453dba204f6cf0fa6e24dd685cfed4da7e
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-source-credentials
    - CISC
    - Data Loading with COPY INTO temporary credentials
    - Load data using COPY INTO with temporary credentials
    - Storage Credentials
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO Source Credentials
description: Methods for providing access credentials to source storage locations in COPY INTO, including named credentials, inline temporary credentials, and external locations via Unity Catalog.
tags:
  - security
  - storage
  - unity-catalog
timestamp: "2026-06-19T14:27:13.638Z"
---

# COPY INTO Source Credentials

**COPY INTO Source Credentials** refers to the authentication and authorization mechanisms used by the `COPY INTO` SQL command to access source file locations when loading data into a [Delta table](/concepts/delta-lake-table.md). Credentials can be specified inline, via a named storage credential, or implicitly through [Unity Catalog](/concepts/unity-catalog.md) external locations.

## Overview

The `COPY INTO` command loads data from a file location into an existing Delta table. Access to the source location can be provided through:
- A named storage credential (`credential_name`).
- Inline temporary credentials.
- Defining the source location as an [External location](/concepts/external-location.md) with `READ FILES` permissions in Unity Catalog.
- Using a named storage credential with `READ FILES` permissions that provide authorization to read from a location through Unity Catalog. ^[copy-into-databricks-on-aws.md]

If the source path is already defined as an external location that the user has permissions to use, no explicit credential is required. ^[copy-into-databricks-on-aws.md]

## Credential Options

### Named Credential

You can reference a pre‑defined storage credential by name in the `WITH (CREDENTIAL credential_name)` clause. A named credential is typically used when the file location is not already included in an external location. The credential must grant `READ FILES` permissions for source access or `WRITE FILES` permissions when writing to an external location. ^[copy-into-databricks-on-aws.md]

### Inline Temporary Credentials

Temporary credentials can be provided directly in the `COPY INTO` statement. Supported options vary by cloud provider:

- **AWS S3**: `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, and optional `AWS_SESSION_TOKEN`.
- **ADLS and Azure Blob Storage**: `AZURE_SAS_TOKEN`. ^[copy-into-databricks-on-aws.md]

These are specified within the `CREDENTIAL` clause:
```sql
COPY INTO ...
FROM source
WITH (CREDENTIAL (AWS_ACCESS_KEY = '...', AWS_SECRET_KEY = '...'))
```

### Encryption Options

For encrypted source data, encryption parameters can be provided in the `ENCRYPTION` sub-clause. The accepted options are:

- `TYPE = 'AWS_SSE_C'` with `MASTER_KEY` for AWS S3 server‑side encryption with customer‑provided keys. ^[copy-into-databricks-on-aws.md]

Encryption options are included inside the `WITH` clause alongside the credential:
```sql
COPY INTO ...
FROM source
WITH (CREDENTIAL (temporary_credential_options), ENCRYPTION (TYPE = 'AWS_SSE_C', MASTER_KEY = '...'))
```

## Unity Catalog and External Locations

When Unity Catalog is enabled, access to source files can be governed through external locations. If the source location is defined as an external location in Unity Catalog and the user has `READ FILES` permission, no credential needs to be supplied in the `COPY INTO` statement. ^[copy-into-databricks-on-aws.md]

Similarly, when writing to an external location (target table specified as `delta.`/path/to/table``), you must have either:
- `WRITE FILES` permission on the external location, or
- `WRITE FILES` permission on a named storage credential that authorizes writing to that location. ^[copy-into-databricks-on-aws.md]

## Related Concepts

- [COPY INTO](/concepts/copy-into-command.md) – The full SQL command syntax and usage.
- [Storage Credentials](/concepts/copy-into-source-credentials.md) – Named entities that store cloud authentication details.
- [External Locations](/concepts/external-location.md) – Unity Catalog objects that link storage paths to credentials.
- Temporary Credentials – Inline key/token pairs for one‑time access.
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance layer that controls access to external locations and credentials.
- Auto Loader – Alternative incremental ingestion tool for cloud object storage.
- Data loading patterns – Common ways to use `COPY INTO` with credentials.

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
