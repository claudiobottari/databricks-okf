---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a018110530a66d11fcfb62e31f3e5093b44899e4bfa74f695b950557c5b742e
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-classifier-suspension-and-troubleshooting
    - Troubleshooting and Custom Classifier Suspension
    - CCSAT
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Custom Classifier Suspension and Troubleshooting
description: When rule generation or validation fails, classifiers are suspended with no new detections; common causes include deleted tables, unrepresentative examples, or invalid tags.
tags:
  - troubleshooting
  - suspension
  - errors
timestamp: "2026-06-19T09:39:11.495Z"
---

---
title: Custom classifier suspension and troubleshooting
summary: Automatic suspension when rule generation or validation fails due to inaccessible example columns, poor representativeness, or invalid governed tags, with specific resolution steps.
sources:
  - custom-classifiers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:56:39.714Z"
updatedAt: "2026-06-18T14:56:39.714Z"
tags:
  - data-governance
  - troubleshooting
  - classification
aliases:
  - custom-classifier-suspension-and-troubleshooting
  - troubleshooting and Custom classifier suspension
  - CCSAT
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

## Custom Classifier Suspension and Troubleshooting

**Custom classifier suspension** occurs when [Data Classification](/concepts/data-classification.md) rule generation or validation fails for a [custom classifier](/concepts/custom-classifiers.md) in Unity Catalog. When suspended, the custom classifier produces no new detections, and a warning is displayed on the Data Classification results page. ^[custom-classifiers-databricks-on-aws.md]

### Causes

Suspension is typically triggered by one of the following: ^[custom-classifiers-databricks-on-aws.md]

- One or more example columns reference tables that have been deleted or renamed since the classifier was created.
- The example columns are not representative enough for the classifier to learn a stable detection rule.
- The [governed tag](/concepts/governed-tags.md) is no longer a governed tag, or the tag value is no longer valid.

### Resolution

To resolve a suspension caused by inaccessible or unrepresentative example columns, edit the custom classifier and replace the problematic columns. Wait for the next Data Classification scan to complete. ^[custom-classifiers-databricks-on-aws.md]

If the suspension is caused by an invalid governed tag or tag value, delete the custom classifier and create a new one with a valid tag. The tag and tag value cannot be changed after creation. ^[custom-classifiers-databricks-on-aws.md]

### Related Troubleshooting

**Permission denied when creating or listing custom classifiers** — The user must be a [metastore admin](/concepts/metastore-admin-role.md). Creating or editing a custom classifier additionally requires `ASSIGN` privileges on the governed tag. ^[custom-classifiers-databricks-on-aws.md]

**Cannot select an example column** — The user must have `SELECT` permission on the table containing the column. If not, ask the table owner to grant it, or choose a different column. ^[custom-classifiers-databricks-on-aws.md]

### Related Concepts

- [Custom Classifiers](/concepts/custom-classifiers.md) — The feature that detects organization-specific data types
- [Data Classification](/concepts/data-classification.md) — The broader scanning system
- [Governed Tags](/concepts/governed-tags.md) — The attribute used to categorize data and drive classification
- [ABAC column-level masks](/concepts/abac-column-level-mask-unity-catalog.md) — A downstream governance control that can use classified tags

### Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
