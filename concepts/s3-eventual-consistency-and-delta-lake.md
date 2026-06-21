---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b35a3438903b37c27cd9db7d79fe4f30aac26e69f713602c0640bc62bcf04d88
  pageDirectory: concepts
  sources:
    - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - s3-eventual-consistency-and-delta-lake
    - Delta Lake and S3 eventual consistency
    - SECADL
    - Amazon S3 eventual consistency
    - Delta Lake Consistency
    - s3-eventual-consistency-impact-on-delta-tables
    - SECIODT
  citations:
    - file: delta_versions_not_contiguous-error-condition-databricks-on-aws.md
title: S3 eventual consistency and Delta Lake
description: The phenomenon where AWS S3's eventual consistency model can cause non-contiguous Delta log versions when a table is deleted and recreated at the same location.
tags:
  - aws
  - delta-lake
  - consistency
timestamp: "2026-06-19T18:29:17.134Z"
---

```markdown
---
title: S3 eventual consistency and Delta Lake
summary: A cause of the DELTA_VERSIONS_NOT_CONTIGUOUS error unique to AWS S3, where the eventual consistency model can introduce gaps when a table is deleted and recreated at the same location.
sources:
  - delta_versions_not_contiguous-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:10:42.993Z"
updatedAt: "2026-06-19T10:10:42.993Z"
tags:
  - aws
  - s3
  - eventual-consistency
  - delta-lake
aliases:
  - s3-eventual-consistency-and-delta-lake
  - Delta Lake and S3 eventual consistency
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 2
---

# S3 eventual consistency and Delta Lake

**S3 eventual consistency and Delta Lake** describes the operational challenges that arise when [[Delta Lake]] tables are stored on Amazon S3, a storage system with eventual consistency guarantees. Under certain write patterns, this consistency model can corrupt the Delta transaction log, leading to read failures and data integrity issues.

## The DELTA_VERSIONS_NOT_CONTIGUOUS error

The most common symptom of S3 eventual consistency interacting with Delta Lake is the `DELTA_VERSIONS_NOT_CONTIGUOUS` error condition. The error message reads:

> Versions (`<versionList>`) are not contiguous. A gap in the delta log between versions `<startVersion>` and `<endVersion>` was detected while trying to load version `<versionToLoad>`.

This error signals that the Delta transaction log has missing entries — a gap in the sequence of version files that Delta Lake relies on to reconstruct table state. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Causes

The source material identifies two possible causes for this error:

1. **Manual removal of files** from the Delta log directory.
2. **S3 eventual consistency** when a Delta table is deleted and recreated at the same location. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

On Amazon S3, delete and create operations are eventually consistent. If a table is dropped and a new table is immediately created at the same path, S3 may serve stale or incomplete listings of the Delta log directory. The new write of version files might not be fully visible, or old version files from the dropped table may still appear, producing a non-contiguous log sequence. The error note applies only to the **AWS** platform; the Azure and generic variants of the error do not mention S3 eventual consistency as a cause. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md]

## Prevention

To avoid the S3-induced form of this error, do not delete and immediately recreate a Delta table at the same S3 path. If a table must be replaced, either use a different target location for the new table, or wait long enough for S3’s eventual consistency to stabilize before reusing the path (the required wait period is not specified in the source).

## Remediation

When the `DELTA_VERSIONS_NOT_CONTIGUOUS` error occurs, the source material directs the user to **contact Databricks support** to repair the table. ^[delta_versions_not_contiguous-error-condition-databricks-on-aws.md] Self-service repair is not recommended because modifying the Delta log manually can cause further corruption.

## Related concepts

- [[Delta Lake transaction log]] – The core structure that can become non-contiguous.
- [[S3 Eventually Consistent Model|S3 eventual consistency]] – The underlying storage behavior that triggers the error.
- [[Delta Lake|Delta Lake on AWS]] – Best practices for running Delta Lake on S3.
- Databricks support – The recommended channel for table repair.

## Sources

- delta_versions_not_contiguous-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_versions_not_contiguous-error-condition-databricks-on-aws.md](/references/delta_versions_not_contiguous-error-condition-databricks-on-aws-ad1fe2ac.md)
