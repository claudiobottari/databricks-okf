---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca4b60473f2b481c12905a2194b1edfd01c0f581809b18d217f8bdbb7b9d49ed
  pageDirectory: concepts
  sources:
    - flag-data-as-certified-or-deprecated-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - searching-by-certification-status-in-databricks
    - SBCSID
  citations:
    - file: flag-data-as-certified-or-deprecated-databricks-on-aws.md
title: Searching by Certification Status in Databricks
description: Using the 'certificationStatus' keyword in Databricks search to filter for certified or deprecated data assets across supported object types.
tags:
  - search
  - data-discovery
  - unity-catalog
timestamp: "2026-06-19T10:36:17.091Z"
---

---
title: Searching by Certification Status in Databricks
summary: How to use the search page to filter assets by `certified` or `deprecated` certification status using the `certificationStatus` keyword or the UI filter menu.
sources:
  - flag-data-as-certified-or-deprecated-databricks-on-aws.md
kind: how-to
createdAt: "2026-07-20T10:00:00.000Z"
updatedAt: "2026-07-20T10:00:00.000Z"
tags:
  - databricks
  - search
  - certification
  - governance
aliases:
  - searching-by-certification-status-in-databricks
  - SBCS
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Searching by Certification Status in Databricks

**Searching by Certification Status** allows users to find assets that have been marked as `certified` or `deprecated` using the [Certification Status System Tag](/concepts/certification-status-system-tag.md). This helps data consumers quickly locate trusted data or avoid outdated assets directly from the Databricks search page.

## How to Search

You can filter for certified or deprecated assets in two ways:

### Using the Search Query

In the **Search** field, use the `certificationStatus` keyword to query objects by their certification status. For example, the following snippet returns only certified tables: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

```
type:table certificationStatus:certified
```

The following snippet returns only deprecated assets across all supported object types: ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

```
certificationStatus:deprecated
```

### Using the UI Filter

In the search filters panel, you can also select **Certified** or **Deprecated** from the **Certification status** filter menu. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

![Search by certification status.](https://docs.databricks.com/aws/en/assets/images/search-certification-status-551865cf6048a0433b0084842eb3fcda.png)

## Supported Object Types

The certification status tag can be applied to catalogs, schemas, tables, views, volumes, functions, registered models, dashboards, Genie Spaces, Databricks apps, and notebooks. However, search by certification status is **not supported** for dashboards, Genie Spaces, or Databricks apps. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Propagation Delay

It might take a few minutes for certification or deprecation updates to appear in search results. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Related Concepts

- [Certification Status System Tag](/concepts/certification-status-system-tag.md) — The underlying governed tag and its values (`certified`, `deprecated`).
- [Flag data as certified or deprecated](/concepts/certified-and-deprecated-data-flags.md) — How to assign the certification status to objects.
- [Migration of system tags to governance in Unity Catalog](/concepts/ai-governance-unity-catalog.md)
- Search in Databricks — General search functionality.

## Sources

- flag-data-as-certified-or-deprecated-databricks-on-aws.md

# Citations

1. [flag-data-as-certified-or-deprecated-databricks-on-aws.md](/references/flag-data-as-certified-or-deprecated-databricks-on-aws-ee1b377b.md)
