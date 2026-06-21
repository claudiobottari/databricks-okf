---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8025835febb67d136d855f830f853b932e89cf14c868d2ccde934dcfb3017ceb
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-locations-and-credentials-in-copy-into
    - credentials in COPY INTO and External locations
    - ELACICI
  citations:
    - file: copy-into-databricks-on-aws.md
title: External locations and credentials in COPY INTO
description: Mechanisms for providing storage access to COPY INTO via Unity Catalog external locations, named credentials, or inline temporary credentials.
tags:
  - security
  - storage
  - unity-catalog
  - databricks
timestamp: "2026-06-18T11:11:19.409Z"
---

# External locations and credentials in COPY INTO

**External locations and credentials in COPY INTO** refers to the mechanisms by which the [COPY INTO](/concepts/copy-into-command.md) SQL command authenticates and authorizes access to source and target cloud storage paths. The command supports both external locations governed by [Unity Catalog](/concepts/unity-catalog.md) and named storage credentials, as well as inline temporary credentials for accessing data that is not already registered as an external location.^[copy-into-databricks-on-aws.md]

## Source location access

The `FROM` clause of `COPY INTO` specifies a file location as a URI. Access to that source location can be provided in three ways:^[copy-into-databricks-on-aws.md]

1. **External location** – If the source path is already defined as an [External location](/concepts/external-location.md) in Unity Catalog and the executing principal has `READ FILES` permission on that external location, no additional credential specification is required.^[copy-into-databricks-on-aws.md]
2. **Named credential** – A named [storage credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) can be referenced with the `WITH (CREDENTIAL credential_name)` syntax. The credential must grant `READ FILES` permissions through Unity Catalog.^[copy-into-databricks-on-aws.md]
3. **Inline temporary credentials** – Short-lived credentials can be provided directly in the `WITH` clause using temporary credential options. Supported options include `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, and `AWS_SESSION_TOKEN` for AWS S3, and `AZURE_SAS_TOKEN` for ADLS and Azure Blob Storage. Additionally, encryption options such as `TYPE = 'AWS_SSE_C'` with a `MASTER_KEY` are accepted for AWS S3. See [Load data using COPY INTO with temporary credentials](/concepts/copy-into-source-credentials.md) for examples.^[copy-into-databricks-on-aws.md]

If a source file path is a root path, a trailing slash (`/`) should be appended — for example, `s3://my-bucket/`.^[copy-into-databricks-on-aws.md]

## Target table location access

When the target table is specified as a location path, such as `` delta.`/path/to/table` ``, Unity Catalog can govern access to the written location. To write to an external location, you must have either:^[copy-into-databricks-on-aws.md]

- `WRITE FILES` permission on the external location that covers that path, or
- `WRITE FILES` permission on a named storage credential used in the `COPY INTO` statement, e.g. `` COPY INTO delta.`/some/location` WITH (CREDENTIAL <named-credential>) ``.^[copy-into-databricks-on-aws.md]

## Permissions summary

| Scenario | Required permission |
|---|---|
| Source path is an existing external location | `READ FILES` on that external location |
| Source path uses a named credential | `READ FILES` on the named storage credential |
| Source path uses inline temporary credentials | No Unity Catalog permission needed on the path (credential is self-contained) |
| Target path is an external location | `WRITE FILES` on that external location |
| Target path using a named credential | `WRITE FILES` on the named storage credential |

## Related concepts

- [External locations](/concepts/external-location.md) – Unity Catalog objects that map cloud storage paths and govern access.
- Storage credentials – Named objects that contain cloud authentication tokens.
- [COPY INTO](/concepts/copy-into-command.md) – The idempotent data ingestion command.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer that enforces permissions on external locations and credentials.
- Cloud object storage connection – How to connect to cloud storage using Unity Catalog.

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
