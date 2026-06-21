---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9c0b067e188a47532ee4285d0d473ce8495dce90c6c0502ef8681e06e759368d
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - detection-exclusions
  citations:
    - file: data-classification-databricks-on-aws.md
title: Detection Exclusions
description: A beta feature that allows users to exclude individual column detections, removing tags and preventing reapplication while providing feedback to improve future classification accuracy.
tags:
  - classification
  - feedback
  - accuracy
timestamp: "2026-06-19T18:03:57.317Z"
---

# Detection Exclusions

**Detection Exclusions** refer to the mechanism within [Data Classification](/concepts/data-classification.md) in [Unity Catalog](/concepts/unity-catalog.md) that allows users to remove individual column detections from classification results. This feature is currently in Beta.

## Behavior

When a detection is excluded, the engine performs the following actions:

- Removes any existing classification tag that was applied to that column.  
- Prevents future scans from reapplying the same tag to that column.  
- Uses the exclusion as feedback to improve the accuracy of subsequent classification runs.  

Exclusions are reversible: clicking the **Exclude** icon again re‑includes the detection, restoring the original behavior.  

^[data-classification-databricks-on-aws.md]

## How to Exclude a Detection

1. Open the Data Classification results page for a catalog.  
2. Click **Review** next to the classification type you want to inspect.  
3. In the **Detected Columns** tab, locate the column you wish to exclude.  
4. Click the **Exclude** icon (shown as a small “X” or a toggle) to the right of the column entry.  

The exclusion takes effect immediately and will persist across future scans.  

^[data-classification-databricks-on-aws.md]

## Purpose and Benefits

Detection exclusions help refine the classification output by letting users correct false positives. By removing incorrect tags, teams can ensure that governance controls—such as [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies or masking rules—are applied only to genuinely sensitive columns. The feedback loop also trains the classification engine to reduce similar mistakes in the future.  

^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) – The AI‑powered engine that automatically detects and tags sensitive data.  
- Supported Classification Tags – The list of tag types that can be assigned or excluded.  
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) where classification results and tags are managed.  
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – Governance controls that can use classification tags to mask or restrict access.  

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
