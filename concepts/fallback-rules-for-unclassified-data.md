---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f4b062f388ff30ae19e4fbfd4cf8629f6061ce43a46ca78be71bbf978b4f026
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fallback-rules-for-unclassified-data
    - FRFUD
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: Fallback Rules for Unclassified Data
description: Applying default restrictive tags and policies to unclassified or unverified data objects as a safety net
tags:
  - data-governance
  - abac
  - security
  - unity-catalog
timestamp: "2026-06-19T22:13:20.330Z"
---

# Fallback Rules for Unclassified Data

**Fallback rules for unclassified data** are access control mechanisms that automatically restrict or govern data assets lacking proper tag classifications. They act as a safety net to prevent unprotected access to data that has not been reviewed or tagged by authorized data stewards. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Purpose

In a tag‑based governance model, policies apply only when the correct tags are present on a data asset. Wrong or missing tags can leave data unprotected or inaccessible. Fallback rules address this risk by providing default protection for unclassified objects until a data steward can review and appropriately tag them. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Implementation

The recommended approach consists of two components: ^[best-practices-for-abac-policies-databricks-on-aws.md]

1. **Default restrictive tag** – Apply a default tag such as `classification : unverified` to new objects as they are created, before any data steward review occurs.
2. **Restrictive ABAC policy** – Create a policy that restricts access to objects carrying the default tag, ensuring unclassified data is protected by default.

For a detailed example, see [Prevent access until sensitive columns are tagged](/concepts/prevent-access-until-sensitive-columns-are-tagged.md) in the common patterns documentation. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Best Practices

### Automate tag enforcement

Use automation to enforce tagging standards and apply default tags to new objects. Manual processes are prone to gaps and delays. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Review and promote tags

Establish a workflow where data stewards review unclassified objects, determine the correct classification, and promote the tag from the fallback value (e.g., `unverified`) to an appropriate classification (e.g., `public`, `internal`, `confidential`, `restricted`). Once the correct tag is applied, the fallback policy no longer restricts that object. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Audit tag changes

Regularly audit tag changes using the [audit log system table](/concepts/audit-log-system-table-requirements.md) to detect unauthorized modifications or missing tags that could compromise data protection. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Standardize attributes

Establish a consistent tagging taxonomy before creating policies. A small, well‑defined set of tags is easier to manage than a proliferation of ad‑hoc tags. For example, use a single `sensitivity` tag with controlled values (`public`, `internal`, `confidential`, `restricted`) rather than multiple overlapping tags like `is_sensitive`, `data_class`, and `pii_level`. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Combine with tag governance

Fallback rules are most effective when combined with proper [governed tag](/concepts/governed-tags.md) permissions. Restrict tag creation and modification to authorized data stewards or governance admins. This prevents users from changing tags on data assets and altering which policies apply to them. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The governance model within which fallback rules operate.
- [Governed Tags](/concepts/governed-tags.md) — Tags used in ABAC policies to determine access permissions.
- Best practices for ABAC policies — Broader guidance for ABAC policy design.
- Common ABAC policy patterns — Examples including the prevent‑untagged pattern.
- [Audit log system table](/concepts/audit-log-system-table-requirements.md) — For monitoring tag changes and policy effectiveness.

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
