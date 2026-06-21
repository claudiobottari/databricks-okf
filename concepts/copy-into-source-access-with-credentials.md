---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03c3ca53bf8bea3835daefc8f01619ae62ddcbf59b2f7aefe392e1754a74a17e
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-source-access-with-credentials
    - CISAWC
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO Source Access with Credentials
description: Mechanisms for providing access to source file locations via named storage credentials, inline temporary credentials, or Unity Catalog external locations.
tags:
  - databricks
  - security
  - cloud-storage
  - unity-catalog
timestamp: "2026-06-18T14:45:35.889Z"
---

# COPY INTO Source Access with Credentials

**COPY INTO Source Access with Credentials** refers to the mechanisms by which the `COPY INTO` command authenticates to read source files from cloud object storage. `COPY INTO` loads data from a file location into a Delta table and is a retryable, idempotent operation—files already loaded are skipped even if they have been modified. The command supports multiple credential strategies to grant access to the source location.^[copy-into-databricks-on-aws.md]

## Access Methods

Access to the source location can be provided through one of three approaches, listed in order of precedence:

1. **Unity Catalog external location** – If the source path is defined as an [external location](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/#external-locations) and you have `READ FILES` permissions on it through Unity Catalog, no inline or named credentials are required.
2. **Named storage credential** – You can reference a named storage credential using `WITH (CREDENTIAL credential_name)` when the source location is not covered by an external location. The credential must grant `READ FILES` permissions through Unity Catalog.
3. **Inline temporary credentials** – Temporary credentials can be provided directly in the `WITH` clause as a set of key-value options.

Access is granted if any of these methods succeed.^[copy-into-databricks-on-aws.md]

### Syntax for the Source Clause

The source clause of `COPY INTO` accepts an optional `WITH` block that specifies credential and encryption information:

```sql
source_clause
  source [ WITH ( [ CREDENTIAL { credential_name |
                                 (temporary_credential_options) } ]
                  [ ENCRYPTION (encryption_options) ] ) ]
```

- **`credential_name`** – The name of a pre-defined storage credential. This is used only if the file location is not included in an external location. See [`credential_name`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-names#credential-name).^[copy-into-databricks-on-aws.md]
- **`temporary_credential_options`** – Inline key-value pairs for temporary credentials. Accepted options depend on the cloud provider:
  - **AWS S3:** `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, and optionally `AWS_SESSION_TOKEN`
  - **Azure ADLS / Blob Storage:** `AZURE_SAS_TOKEN`
- **`encryption_options`** – For server-side encryption with customer-provided keys (AWS S3): `TYPE = 'AWS_SSE_C'` and `MASTER_KEY`.

For examples, see [Load data using COPY INTO with temporary credentials](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/copy-into/temporary-credentials).^[copy-into-databricks-on-aws.md]

### Source Path Considerations

If the source file path is a root path (e.g., `s3://my-bucket/`), you must add a trailing slash (`/`) at the end of the URI.^[copy-into-databricks-on-aws.md]

## Unity Catalog Integration

When the source location is defined as an external location in Unity Catalog and you have the `READ FILES` permission, you do not need to supply credentials—Unity Catalog governs the access automatically. Similarly, using a named storage credential with `READ FILES` permissions allows reading from locations not explicitly defined as external locations.^[copy-into-databricks-on-aws.md]

For writing to a Delta table defined by a location (e.g., `delta./path/to/table`), you may need `WRITE FILES` permissions on the corresponding external location or on a named storage credential. See [Connect to cloud object storage using Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/).^[copy-into-databricks-on-aws.md]

## Related Concepts

- [COPY INTO](/concepts/copy-into-command.md) – The full command syntax and usage
- [Unity Catalog](/concepts/unity-catalog.md) – Central governance for data and storage
- [External Locations](/concepts/external-location.md) – Persistent mappings to cloud storage paths with managed permissions
- [Storage Credentials](/concepts/copy-into-source-credentials.md) – Named authentication objects for cloud storage
- Cloud Object Storage – General guidance on ingesting data from S3, ADLS, GCS, etc.

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
