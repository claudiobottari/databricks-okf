---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7040e208807d3a935620ba4983663c49fbaa6e874da0e3ad9cb137e2bad41719
  pageDirectory: concepts
  sources:
    - mount-a-shared-genie-space-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - read-only-provider-data-in-mounted-genie-spaces
    - RPDIMGS
  citations:
    - file: mount-a-shared-genie-space-databricks-on-aws.md
title: Read-Only Provider Data in Mounted Genie Spaces
description: The provider's tables in a mounted Genie Space are read-only — recipients can query them but cannot write to them.
tags:
  - databricks
  - genie
  - limitations
timestamp: "2026-06-19T19:47:12.568Z"
---

# Read-Only Provider Data in Mounted Genie Spaces

When a data provider shares a Genie Space using OpenSharing (currently in Beta), recipients can mount that share to create a local Genie Space in their own workspace. The local space is pre-loaded with the provider's data assets and instructions, enabling immediate Q&A. However, a key constraint applies to the provider's original data: it is **read-only**. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## Read-Only Nature of Provider Tables

The provider's tables that are mounted into the recipient's Unity Catalog [Metastore](/concepts/metastore.md) are read-only. Recipients can query them using SQL or through the Genie Space interface, but they cannot write to them (i.e., no INSERT, UPDATE, DELETE, or DDL operations on those tables). This restriction ensures that the provider's original data remains unchanged and that the recipient's modifications do not affect the provider's space. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## What Recipients Can and Cannot Do

| Can do | Cannot do |
|--------|-----------|
| Query the provider's tables | Write to provider tables |
| Add their own tables and views to the local space | Modify or delete provider data |
| Edit or extend the instructions and SQL examples | Re-share the provider's data assets via OpenSharing |
| Reconfigure the SQL warehouse | Affect the provider's original space |
| Share the local space with other users within the same workspace | |

All modifications made by the recipient — such as adding tables, editing instructions, or reconfiguring the space — apply only to their local copy and are invisible to the provider. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## Implications for Use

Because provider tables are read-only, any [data catalog](/concepts/unity-catalog.md) transformations or enrichment must be done via the recipient's own tables and views that reference the provider data. Databricks rewrites all table references in the provider's instructions and curated SQL examples to point to the mounted catalog, ensuring queries against provider data work correctly without write operations. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## Limitations Related to Read-Only Data

- **External sharing:** Recipients cannot share the mounted Genie Space with users outside their organization using OpenSharing. This prevents unintended redistribution of the provider's read-only data. ^[mount-a-shared-genie-space-databricks-on-aws.md]

## Related Concepts

- Genie Space – The AI-powered conversational analytics feature on Databricks.
- [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md) – The mechanism for sharing Genie Spaces between providers and recipients.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) under which mounted data appears.
- Read-Only Data – General pattern for accessing shared datasets without write access.

## Sources

- mount-a-shared-genie-space-databricks-on-aws.md

# Citations

1. [mount-a-shared-genie-space-databricks-on-aws.md](/references/mount-a-shared-genie-space-databricks-on-aws-3f0ef05b.md)
