---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd2397ddcfd37c9d57e9c34e21f0a6eb389f91f6123fec19e02af93778876706
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-source-credential-options
    - CISCO
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO Source Credential Options
description: Mechanisms for providing access to source file locations including named credentials, inline temporary credentials, and external locations via Unity Catalog
tags:
  - databricks
  - security
  - cloud-storage
timestamp: "2026-06-19T09:25:29.366Z"
---

# COPY INTO Source Credential Options

**COPY INTO Source Credential Options** define how a `COPY INTO` statement authenticates to cloud object storage when reading source files. You can specify credentials either as a named storage credential, inline temporary credentials, or rely on an existing Unity Catalog external location permission. ^[copy-into-databricks-on-aws.md]

## Overview

When loading data from a file location using `COPY INTO`, the system needs to authenticate to the cloud storage provider. The `COPY INTO` command supports three mechanisms for providing source credentials, listed in order of preference:

1. **External location** (recommended) – the source path is registered as an external location in Unity Catalog and the caller has `READ FILES` permission.
2. **Named storage credential** – a credential object that has `READ FILES` permission on the location.
3. **Inline temporary credentials** – explicit keys or tokens provided directly in the `CREDENTIAL` clause.

If the path is already defined as an external location and you have the necessary permissions, no additional credential specification is needed. ^[copy-into-databricks-on-aws.md]

## Credential Options in the `source_clause`

The `source_clause` syntax allows an optional `WITH` block that contains a `CREDENTIAL` subclause and an optional `ENCRYPTION` subclause:

```
source [ WITH ( [ CREDENTIAL { credential_name |
                                (temporary_credential_options) } ]
                 [ ENCRYPTION (encryption_options) ] ) ]
```

^[copy-into-databricks-on-aws.md]

### Named Storage Credential (`credential_name`)

A named credential is a Unity Catalog object that holds cloud provider authentication information. To use it, provide the credential name after the `CREDENTIAL` keyword. This is required only when the source file location is **not** covered by an external location. The executing user must have `READ FILES` permission on the credential. ^[copy-into-databricks-on-aws.md]

**Example:**

```sql
COPY INTO my_table
FROM 's3://my-bucket/data/'
FILEFORMAT = CSV
WITH (CREDENTIAL my_s3_credential)
```

### Inline Temporary Credentials

You can provide cloud-specific keys or tokens inline by wrapping them in parentheses after `CREDENTIAL`. The accepted options depend on the cloud provider:

| Provider | Options |
|----------|---------|
| AWS S3 | `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, `AWS_SESSION_TOKEN` |
| ADLS / Azure Blob Storage | `AZURE_SAS_TOKEN` |

^[copy-into-databricks-on-aws.md]

**Example (AWS):**

```sql
COPY INTO my_table
FROM 's3://my-bucket/data/'
FILEFORMAT = PARQUET
WITH (CREDENTIAL (
  AWS_ACCESS_KEY = 'AKIA...',
  AWS_SECRET_KEY = '...',
  AWS_SESSION_TOKEN = '...'
))
```

**Example (Azure):**

```sql
COPY INTO my_table
FROM 'abfss://container@storage.dfs.core.windows.net/data/'
FILEFORMAT = CSV
WITH (CREDENTIAL (
  AZURE_SAS_TOKEN = '...'
))
```

### Encryption Options

For AWS S3 sources encrypted with server-side encryption using customer-provided keys (SSE-C), you can supply the encryption configuration:

```sql
ENCRYPTION (TYPE = 'AWS_SSE_C', MASTER_KEY = '...')
```

^[copy-into-databricks-on-aws.md]

## External Location Priority

If the source path is registered as an external location in Unity Catalog and the user has `READ FILES` permission on that location, no inline or named credential is necessary. The system uses the external location’s configured credential automatically. See [External Locations](/concepts/external-location.md) for details. ^[copy-into-databricks-on-aws.md]

## Important Notes

- If the source file path is a root path (e.g., `s3://my-bucket/`), append a trailing slash (`/`) to avoid ambiguity. ^[copy-into-databricks-on-aws.md]
- Temporary credentials are less secure than named credentials or external locations; use them only when necessary and avoid hard-coding in production scripts.
- For a complete walkthrough of using temporary credentials, see [Load data using COPY INTO with temporary credentials](/concepts/copy-into-source-credentials.md).

## Related Concepts

- [COPY INTO](/concepts/copy-into-command.md) – The full command syntax and parameters
- [External Locations](/concepts/external-location.md) – Unity Catalog objects that map storage paths to credentials
- [Storage Credentials](/concepts/copy-into-source-credentials.md) – Named credential objects for cloud authentication
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for managing data access
- Auto Loader – Alternative incremental ingestion approach

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
