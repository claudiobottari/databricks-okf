---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5086191884b5e26b8add7c968fcd77f0d26da770c234e26727efa4e62504fa63
  pageDirectory: concepts
  sources:
    - delta-lake-limitations-on-s3-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-s3-bucket-versioning-limitations
    - DLSBVL
  citations:
    - file: delta-lake-limitations-on-s3-databricks-on-aws.md
title: Delta Lake S3 bucket versioning limitations
description: Databricks recommends against enabling S3 bucket versioning for Delta Lake tables due to conflicts with Delta's own versioning and garbage collection, suggesting a max of 3 versions retained for ≤7 days if enabled.
tags:
  - delta-lake
  - s3
  - databricks
  - storage
timestamp: "2026-06-19T18:20:16.529Z"
---

---
title: Delta Lake S3 Bucket Versioning Limitations
summary: Databricks recommends against enabling S3 bucket versioning for Delta Lake tables because it interferes with Delta Lake's own versioning and garbage collection, causing retained files and potential performance degradation.
sources:
  - delta-lake-limitations-on-s3-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:59:07.284Z"
updatedAt: "2026-06-19T14:59:07.284Z"
tags:
  - delta-lake
  - s3
  - storage
  - aws
aliases:
  - delta-lake-s3-bucket-versioning-limitations
  - DLSBVL
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

## Delta Lake S3 Bucket Versioning Limitations

**Delta Lake S3 Bucket Versioning Limitations** refer to the performance and management challenges that arise when [S3 bucket versioning](/concepts/s3-bucket-versioning-and-delta-lake.md) is enabled for buckets used to store Delta Lake tables, including [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md). Databricks generally recommends against enabling bucket versioning for these buckets because Delta Lake already implements its own versioning and garbage collection mechanisms. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

### How Versioning Impacts Delta Lake

When S3 bucket versioning is turned on, S3 retains copies of all metadata and data files that Databricks manual and automated processes consider deleted. This includes data files that the `VACUUM` command would permanently delete, as well as transaction logs that are cleaned up during regular [Delta Lake Table](/concepts/delta-lake-table.md) operations. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

### Recommended Configuration

If you choose to use S3 bucket versioning, Databricks recommends retaining a maximum of **three versions** and implementing an S3 lifecycle management policy that retains versions for **7 days or less** for all buckets with versioning enabled. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

### Performance Considerations

If you encounter performance slowdowns on tables stored in buckets where versioning is enabled, you should mention that bucket versioning is enabled when contacting Databricks support. ^[delta-lake-limitations-on-s3-databricks-on-aws.md]

### Related Concepts

- VACUUM
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md)
- Delta Lake table maintenance
- S3 bucket lifecycle policies

## Sources

- delta-lake-limitations-on-s3-databricks-on-aws.md

# Citations

1. [delta-lake-limitations-on-s3-databricks-on-aws.md](/references/delta-lake-limitations-on-s3-databricks-on-aws-516e860e.md)
