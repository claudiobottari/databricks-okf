---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf3c2d3b665a809985ac8ec4a9b574d515821bbfa935f9ff2e1086400158ba82
  pageDirectory: concepts
  sources:
    - troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - aws-s3-bucket-naming-restrictions-for-delta-sharing
    - ASBNRFDS
  citations:
    - file: troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md
title: AWS S3 Bucket Naming Restrictions for Delta Sharing
description: Dots (periods) in S3 bucket names cause SSL/certificate errors when Delta Sharing generates pre-signed URLs, due to an AWS limitation on bucket naming conventions.
tags:
  - delta-sharing
  - aws-s3
  - networking
  - troubleshooting
timestamp: "2026-06-19T23:14:06.179Z"
---

# AWS S3 Bucket Naming Restrictions for [Delta Sharing](/concepts/delta-sharing.md)

**AWS S3 Bucket Naming Restrictions for Delta Sharing** refers to a known limitation where using an S3 bucket name that contains dot (period) characters can cause SSL/TLS certificate verification failures when recipients attempt to read shared data. This restriction is rooted in AWS S3 bucket naming rules and affects how [Delta Sharing](/concepts/delta-sharing.md) generates pre-signed URLs for data access.

## Issue

When a recipient queries a shared table, the following error patterns may appear depending on the client:

- **Spark**: `SSLPeerUnverifiedException: Certificate for - <workspace name>.cloud.databricks.com.s3.us-east-1.amazonaws.com doesn't match any of the subject alternative names [s3.amazonaws.com, *.s3.amazonaws.com…]`
- **Pandas**: `FileNotFoundError: https://xxxx.xxxxxx.s3.xx-xxxx-1.amazonaws.com/xxxxxx/part-00000-...`
- **Power BI**: `DataSource.Error: The underlying connection was closed: Could not establish trust relationship for the SSL/TLS secure channel.`

^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Cause

The typical cause is that the S3 bucket name uses dot or period notation (for example, `incorrect.bucket.name.notation`). This violates AWS bucket naming rules, which can lead to SSL certificate validation failures when the bucket name is embedded in a subdomain of the pre-signed URL. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

Even if the bucket name is correctly formatted, some clients (such as PyCharm) may still encounter an `SSLCertVerificationError`. In that case, the issue is not the bucket naming itself but a client-side SSL configuration. ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Recommended Fix

If the bucket name contains dots or otherwise violates AWS S3 naming conventions, use a different bucket for [Unity Catalog](/concepts/unity-catalog.md) and [Delta Sharing](/concepts/delta-sharing.md). The AWS S3 bucket naming rules are documented at [AWS bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html). ^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

If the bucket name follows valid naming conventions and you still encounter a `FileNotFoundError` in Python, enable debug logging to help isolate the issue:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

^[troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for sharing data across platforms.
- [Unity Catalog](/concepts/unity-catalog.md) – The unified governance layer that manages data assets, including shared buckets.
- Troubleshooting Delta Sharing – Common errors and resolutions when accessing shared data.
- S3 Bucket Naming Rules (external reference) – AWS requirements for bucket names (no dots for virtual-hosted‑style access).

## Sources

- troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md

# Citations

1. [troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws.md](/references/troubleshoot-common-sharing-issues-in-opensharing-databricks-on-aws-801ba4c9.md)
