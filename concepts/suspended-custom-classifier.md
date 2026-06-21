---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d594a9e902b274adc05605c5653c9719b92006dd07491c184d3e19a44c4deba
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - suspended-custom-classifier
    - SCC
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Suspended Custom Classifier
description: A state where a custom classifier stops producing detections due to rule generation failure, invalid example columns, or invalid governed tags; requires editing or recreation to resolve.
tags:
  - data-governance
  - classification
  - troubleshooting
timestamp: "2026-06-19T14:39:30.507Z"
---

```markdown
---
title: "Suspended Custom Classifier"
---

# Suspended Custom Classifier

A **Suspended Custom Classifier** is a [Custom Classifier](/concepts/custom-classifiers.md) in [Unity Catalog](/concepts/unity-catalog.md) that Databricks has temporarily disabled because rule generation or validation failed. When a custom classifier enters this state, it produces no new detections on the [Data Classification](/concepts/data-classification.md) results page, and a warning banner is displayed to the [Metastore](/concepts/metastore.md) admin. ^[custom-classifiers-databricks-on-aws.md]

## Causes

A custom classifier is suspended for one or more of the following reasons: ^[custom-classifiers-databricks-on-aws.md]

- **Missing example columns:** One or more of the example columns selected when the classifier was created reference tables that have been deleted or renamed since the classifier was created. The system cannot sample data from a nonexistent column. ^[custom-classifiers-databricks-on-aws.md]
- **Unrepresentative example columns:** The values in the provided example columns are not varied or distinctive enough for the detection engine to learn a stable, reliable pattern. Without sufficient signal, the system cannot confidently generate detection rules. ^[custom-classifiers-databricks-on-aws.md]
- **Invalid governed tag or tag value:** The [governed tag](/concepts/governed-tags.md) that the classifier relies on is no longer a governed tag, or the specific tag value used has been removed or invalidated. Because the tag cannot be changed after creation, an invalid tag leaves the classifier without a valid target to detect. ^[custom-classifiers-databricks-on-aws.md]

## Behavior

- No new detections are produced for the suspended classifier. ^[custom-classifiers-databricks-on-aws.md]
- Existing detections from the classifier that were already auto-applied to columns are **not** removed automatically. Only future scans are affected. ^[custom-classifiers-databricks-on-aws.md]
- A warning icon and message appear on the Data Classification results page, alerting the user that one or more custom classifiers are suspended. ^[custom-classifiers-databricks-on-aws.md]

## Resolution

To resolve a suspension, the [Metastore](/concepts/metastore.md) admin must follow the appropriate remediation path: ^[custom-classifiers-databricks-on-aws.md]

1. **Edit the classifier** – If the problem is caused by inaccessible or unrepresentative example columns, edit the custom classifier in the **Manage custom classifiers** side panel. Replace the example columns with new ones that are still accessible and contain more varied, representative values. After saving, the system will attempt rule generation again on the next scan. ^[custom-classifiers-databricks-on-aws.md]
2. **Delete and recreate the classifier** – If the suspension is caused by an invalid governed tag or tag value, the classifier cannot be fixed by editing. Delete the suspended classifier and create a new one with a valid governed tag and representative example columns. ^[custom-classifiers-databricks-on-aws.md]

## Prevention

To minimize the risk of suspension: ^[custom-classifiers-databricks-on-aws.md]

- Choose example columns from stable tables that are unlikely to be renamed or dropped.
- Provide 1–10 example columns with varied values that are characteristic of the class you want to detect.
- Ensure the governed tag and tag value you select remain valid for the duration of the classifier's lifecycle.

## Related Concepts

- [Custom Classifier](/concepts/custom-classifiers.md)
- [Data Classification](/concepts/data-classification.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Metastore Admin](/concepts/metastore-admin-role.md)

## Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
