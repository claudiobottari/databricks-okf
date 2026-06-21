---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a729ff26a1bf1863bf60874e1f00160bebd5624a54afad5dc1216b67b71d9c22
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-source-credentials-encryption
    - CISC&E
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO Source Credentials & Encryption
description: Mechanisms for providing temporary or named credentials and encryption options to access source file locations during COPY INTO operations.
tags:
  - databricks
  - security
  - cloud-storage
  - credentials
timestamp: "2026-06-19T17:53:36.449Z"
---

# COPY INTO Source Credentials & Encryption

**COPY INTO Source Credentials & Encryption** defines how the `COPY INTO` command authenticates and secures access to source file locations. When loading data from cloud storage into a Delta table, you can provide inline credentials, reference a named storage credential, or rely on an external location that is already governed by Unity Catalog. For encrypted source files, you can specify server-side encryption parameters.

## Overview

The `COPY INTO` command supports three mechanisms for granting access to source data:

- Rely on an external location that you have `READ FILES` permissions on through Unity Catalog.
- Reference a named storage credential that provides `READ FILES` permissions.
- Provide inline temporary credentials directly in the SQL statement.

For encrypted source files in AWS S3, you can supply a customer master key for server-side encryption with customer-provided keys (SSE-C). ^[copy-into-databricks-on-aws.md]

## Syntax

The relevant part of the `COPY INTO` syntax is the **source clause**, which allows an optional `CREDENTIAL` and an optional `ENCRYPTION` block:

```sql
source_clause
  source [ WITH ( [ CREDENTIAL { credential_name |
                                 (temporary_credential_options) } ]
                  [ ENCRYPTION (encryption_options) ] ) ]
```

The `source` is a URI pointing to the file location. `CREDENTIAL` and `ENCRYPTION` are both optional and can be used together or separately. ^[copy-into-databricks-on-aws.md]

## Credential Options

### Named Storage Credential

You can specify a named credential that has already been defined in Unity Catalog. Use the `credential_name` parameter:

```sql
COPY INTO ...
FROM 's3://my-bucket/path'
WITH (CREDENTIAL my_credential)
```

You need `READ FILES` permissions on that credential. No inline credential parameters are required. ^[copy-into-databricks-on-aws.md]

### Inline Temporary Credentials

You can provide temporary credentials directly as key-value pairs inside parentheses. The accepted options depend on the cloud provider:

| Cloud Provider | Credential Keys |
|----------------|-----------------|
| AWS S3         | `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, `AWS_SESSION_TOKEN` |
| ADLS / Azure Blob Storage | `AZURE_SAS_TOKEN` |

Example for AWS S3:

```sql
COPY INTO ...
FROM 's3://my-bucket/path'
WITH (CREDENTIAL (
  AWS_ACCESS_KEY = '...',
  AWS_SECRET_KEY = '...',
  AWS_SESSION_TOKEN = '...'
))
```

^[copy-into-databricks-on-aws.md]

### External Locations (No Explicit Credentials)

If the source path is already defined as an external location in Unity Catalog and you have the required `READ FILES` permissions, you can omit the `CREDENTIAL` clause entirely. Databricks automatically uses the external location’s credentials. ^[copy-into-databricks-on-aws.md]

> **Note:** If the source file path is a root path (e.g. `s3://my-bucket/`), you must add a trailing slash (`/`) at the end of the URI. ^[copy-into-databricks-on-aws.md]

## Encryption Options

To read source files that are encrypted using AWS server-side encryption with customer-provided keys (SSE-C), specify the encryption options:

```sql
ENCRYPTION (TYPE = 'AWS_SSE_C', MASTER_KEY = '<base64-encoded-key>')
```

The only accepted encryption type is `'AWS_SSE_C'`. The `MASTER_KEY` must be the base64-encoded customer key used to encrypt the objects. ^[copy-into-databricks-on-aws.md]

## Credentials for Target Table (Write)

When the target table is specified as a path (e.g. `delta.`/some/location``), you can supply a named storage credential using `CREDENTIAL` in the `WITH` clause to authorize the write operation. This is separate from the source credentials. You need `WRITE FILES` permissions on the credential or on the external location. ^[copy-into-databricks-on-aws.md]

## Examples

### Using inline credentials and SSE-C encryption

```sql
COPY INTO my_table
FROM 's3://encrypted-bucket/data/'
FILEFORMAT = PARQUET
WITH (CREDENTIAL (
  AWS_ACCESS_KEY = 'AKIA...',
  AWS_SECRET_KEY = '...'
),
ENCRYPTION (
  TYPE = 'AWS_SSE_C',
  MASTER_KEY = 'base64key=='
))
```

## Related Concepts

- [Copy Into Data Loading (Databricks)](/concepts/copy-into-databricks.md)
- Unity Catalog External Locations
- [Storage Credentials](/concepts/copy-into-source-credentials.md)
- Cloud Object Storage Ingestion
- External Locations in Unity Catalog
- [Data Loading with COPY INTO temporary credentials](/concepts/copy-into-source-credentials.md)

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
