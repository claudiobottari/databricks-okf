---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea1ebbfba536886c3e869cd5d338111f402ecc456acdf7a6b511b78b4cd1ad8d
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
    - data-classification-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - intelligent-scanning
    - intelligent-scanning-databricks
    - IS(
  citations:
    - file: data-classification-databricks-on-aws.md
    - file: anomaly-detection-databricks-on-aws.md
title: Intelligent Scanning
description: An automated scanning mechanism that prioritizes high-impact tables based on popularity and downstream usage while reducing scan frequency for less critical tables.
tags:
  - data-quality
  - automation
  - scanning
timestamp: "2026-06-19T22:06:11.469Z"
---

```markdown
# Intelligent Scanning

**Intelligent Scanning** is a feature of [[Data Classification]] in [[Unity Catalog]] that automatically determines when to scan tables for sensitive data classification. It leverages Unity Catalog and the Data Intelligence Engine to perform incremental and optimized scanning, ensuring that new data is classified efficiently without requiring manual configuration. ^[data-classification-databricks-on-aws.md]

## How It Works

Intelligent Scanning uses metadata from Unity Catalog to decide which tables need to be rescanned. The system scans incrementally, focusing on new or changed data rather than performing full rescans. This approach reduces computational costs while maintaining up-to-date classification coverage. ^[data-classification-databricks-on-aws.md]

New tables and columns in a catalog are typically scanned within 24 hours of being created. The system intelligently prioritizes high-impact tables based on popularity and downstream usage, reducing frequency for less critical tables. ^[data-classification-databricks-on-aws.md, anomaly-detection-databricks-on-aws.md]

## Cost Optimization

The initial scan of a catalog is more costly than subsequent scans, which are incremental and typically incur lower costs. This optimization helps manage resource usage while maintaining up-to-date classification. ^[data-classification-databricks-on-aws.md]

## Benefits

- **Automatic discovery**: No manual configuration required for individual tables
- **Incremental updates**: Only new or changed data is rescanned
- **Cost efficiency**: Optimized scanning reduces computational overhead
- **Timely classification**: New tables are typically classified within 24 hours
- **Priority-based scanning**: High-impact tables are prioritized based on usage patterns ^[data-classification-databricks-on-aws.md, anomaly-detection-databricks-on-aws.md]

## Configuration

Users can enable data classification for multiple catalogs at once from the classification results page, or configure individual catalogs with granular schema-level control. When enabling a catalog, all schemas are included by default, but you can select specific schemas to include. ^[data-classification-databricks-on-aws.md]

## Error Handling

If scan errors occur for individual tables, those failures are skipped and automatically retried the following day. An **Errors** button appears on the results page to show which tables failed and the associated error messages. ^[data-classification-databricks-on-aws.md]

## Integration with Anomaly Detection

Intelligent Scanning also supports [[Anomaly Detection]] within Unity Catalog. For anomaly detection, intelligent scanning automates table scan frequencies by prioritizing high-impact tables and reducing frequency for less critical tables. This ensures monitoring resources are focused where they provide the most value. ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [[Data Classification]] — The broader system that uses intelligent scanning
- [[Unity Catalog]] — The governance layer leveraged for intelligent scanning
- [[Anomaly Detection]] — Data quality monitoring that uses intelligent scanning
- Incremental Scanning — The approach of scanning only new or changed data
- Scan Cost Optimization — Managing costs through incremental scans
- Data Intelligence Engine — The underlying AI system that powers intelligent decisions

## Sources

- data-classification-databricks-on-aws.md
- anomaly-detection-databricks-on-aws.md
```

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
2. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
