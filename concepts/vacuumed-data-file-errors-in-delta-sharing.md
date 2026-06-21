---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2f36be1852959d3984a048ac262750367a475ee931b462e260469af4c77c435
  pageDirectory: concepts
  sources:
    - troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - vacuumed-data-file-errors-in-delta-sharing
    - VDFEIDS
  citations:
    - file: troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
title: Vacuumed Data File Errors in Delta Sharing
description: Querying a shared table fails with 404 'The specified key does not exist' when a pre-signed URL references a data file that has been vacuumed from a historical table version.
tags:
  - delta-sharing
  - vacuum
  - data-integrity
  - troubleshooting
timestamp: "2026-06-19T23:14:25.143Z"
---

#Vacuumed Data File Errors in [Delta Sharing](/concepts/delta-sharing.md)

When querying a [Delta Sharing](/concepts/delta-sharing.md) table, you may encounter a **404 Not Found** error indicating that the data file referenced by a pre-signed URL no longer exists. This error typically occurs when the underlying data has been vacuumed, removing the file from cloud storage. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Error Messages

The error manifests in different ways depending on the client:

**Spark error examples:**

```
java.lang.Throwable: HTTP request failed with status: HTTP/1.1 404 The specified path does not exist.
```

or

```
HTTP request failed with status: HTTP/1.1 404 Not Found <?xml version="1.0" encoding="UTF-8"?>
<Error><Code>NoSuchKey</Code><Message>The specified key does not exist.</Message>
```

^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Cause

The error appears because the data file corresponding to the pre-signed URL has been vacuumed from the shared table. The file belongs to a historical table version that is no longer retained by the provider. When the recipient tries to read that stale version, the pre-signed URL points to a file that no longer exists in cloud storage. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Workaround

Query the latest snapshot of the shared table instead of a historical version. The current snapshot contains only the active files, which have not been vacuumed. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – Open protocol for sharing data
- [VACUUM (Delta Lake)](/concepts/delta-lake-time-travel-and-vacuum.md) – Removes old files unreferenced by the current table version
- [Pre-signed URLs](/concepts/pre-signed-url-sharing.md) – Temporary credentials used to access shared data
- Snapshot querying – Reading the latest version of a shared table
- Troubleshoot common sharing issues in OpenSharing – Broader troubleshooting guide

## Sources

- troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md

# Citations

1. [troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md](/references/troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws-801ba4c9.md)
