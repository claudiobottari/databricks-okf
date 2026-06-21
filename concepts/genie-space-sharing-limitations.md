---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a947a9ddf1ff6cdd68c1d985f8cea1a887b16154925066a36c47b69fbac8a26d
  pageDirectory: concepts
  sources:
    - share-a-genie-space-using-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-space-sharing-limitations
    - GSSL
  citations:
    - file: share-a-genie-space-using-opensharing-databricks-on-aws.md
title: Genie Space Sharing Limitations
description: "Constraints on sharing Genie Spaces: snapshot-only (no live updates), 256 KB compressed size limit for configuration, and inability to share spaces containing metric views."
tags:
  - genie-space
  - limitations
  - delta-sharing
timestamp: "2026-06-19T23:04:20.076Z"
---

# Genie Space Sharing Limitations

**Genie Space Sharing Limitations** describes the constraints and restrictions that apply when sharing a Genie Space using [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md) on Databricks. These limitations affect the content, size, and update behavior of shared Genie Spaces.

## Snapshot-Only Sharing

[OpenSharing](/concepts/opensharing.md) for Genie Spaces creates a **point-in-time snapshot** of the space's data assets and instructions at the moment the share is created. The shared content does **not** update when the original Genie Space is modified, and all recipients see the same frozen snapshot. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Size Limit

The Genie Space configuration (including instructions, curated SQL examples, SQL functions, and other metadata) must be less than **256 KB when compressed**. Spaces that exceed this limit return an error when you attempt to share them. To reduce the size, shorten instructions or descriptions, then try again. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Metric Views Restriction

Genie Spaces that include **metric views** cannot be shared via [OpenSharing](/concepts/opensharing.md). If your space contains metric views, you must remove them before sharing, or choose a different sharing method. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Immutable Asset List

After the initial share is created, you **cannot modify the data assets** in the share. The share's asset list is read-only. You can manage recipients and delete the share, but you cannot add or remove data assets manually. To update the shared assets, you must create a new share. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Recipient Access Depends on Original Permissions

Recipients' access to shared data depends on the original sharer retaining `SELECT` privilege on all data assets in the space. If the sharer loses this privilege after sharing, recipients cannot access the shared data. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md) — The underlying protocol for sharing Genie Spaces.
- [Mount a Shared Genie Space](/concepts/mount-a-shared-genie-space.md) — How recipients access shared spaces.
- Genie Space — The original AI-powered analytics space being shared.
- [Delta Sharing](/concepts/delta-sharing.md) — The broader data sharing framework.

## Sources

- share-a-genie-space-using-opensharing-databricks-on-aws.md

# Citations

1. [share-a-genie-space-using-opensharing-databricks-on-aws.md](/references/share-a-genie-space-using-opensharing-databricks-on-aws-d29bfca3.md)
