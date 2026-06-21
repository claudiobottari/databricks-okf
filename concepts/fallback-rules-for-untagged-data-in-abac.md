---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f0d37db3df44e75da5adacf28913197ad39be3b64500edc75e4e005704c0aa3
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fallback-rules-for-untagged-data-in-abac
    - FRFUDIA
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: Fallback Rules for Untagged Data in ABAC
description: Applying default restrictive tags like 'classification:unverified' to new objects and creating policies that restrict access to untagged data until a data steward reviews the classification.
tags:
  - abac
  - data-governance
  - security
timestamp: "2026-06-19T09:09:08.669Z"
---

# Fallback Rules for Untagged Data in ABAC

**Fallback Rules for Untagged Data in ABAC** are access control mechanisms designed to handle objects that lack the correct [Governed Tags](/concepts/governed-tags.md) needed by existing ABAC policies. Because ABAC policies rely on tags to determine which rules apply, untagged or misclassified data can remain unprotected — or worse, be accidentally inaccessible. Fallback rules provide a safety net by applying a restrictive default to such objects until they are properly tagged. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## The Problem: Untagged Data in ABAC

ABAC policies evaluate at query time against tags on catalogs, schemas, tables, and columns. If a data object has no tags, or its tags do not match any policy condition, the policy simply does not apply. This can lead to two undesirable outcomes:

- **Unprotected sensitive data** – A table containing PII might be accessible to all users if no policy matches its (missing) tags.  
- **Blocked access** – A policy intended to restrict access might accidentally lock out legitimate users because the object was never tagged with the expected attribute.

The source material explicitly warns: "Don't assume that all objects are correctly tagged." ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Recommended Fallback Strategy

The recommended approach is to apply a default restrictive tag to every new object and then create a policy that restricts access to objects carrying that tag. This ensures that unclassified data is not inadvertently exposed. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Step 1: Apply a Default Restrictive Tag

Use automation (e.g., a script or a Unity Catalog event-based trigger) to assign a tag such as `classification : unverified` to any object at creation time. This tag indicates that the data has not yet been reviewed by a data steward. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Step 2: Create a Restrictive ABAC Policy

Define a policy (row filter, column mask, or GRANT policy) that targets objects tagged with `classification : unverified`. For example, a row filter policy could return zero rows for all users except the data stewardship team, effectively blocking access until the tag is replaced with a verified value. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Step 3: Steward Review and Tag Update

When a data steward reviews the object and confirms its classification, they update the tag to a verified value (e.g., `classification : public`, `internal`, `confidential`). The restrictive policy no longer matches, and the appropriate policies for that classification apply. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Detailed Example: Prevent Access Until Sensitive Columns Are Tagged

A concrete pattern illustrating this strategy is documented in Common ABAC Patterns under "Prevent access until sensitive columns are tagged." The source material references this pattern as a detailed implementation guide. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Supporting Practices

- **Tagging automation** – Enforce tagging standards with automated tools (e.g., Databricks workflows or external governance systems) to reduce human error. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Audit tag changes** – Regularly audit tag modifications using the [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) to detect objects that were left untagged or whose tags were incorrectly removed. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Restrict tag creation** – Limit the ability to create or modify tags to authorized data stewards or governance admins. See [Governed Tags](/concepts/governed-tags.md) for configuration details. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) – The attribute system that powers ABAC conditions.
- [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md) – Policies that filter rows based on tag conditions.
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) – Policies that mask column values based on tag conditions.
- Common ABAC Patterns – Contains the "prevent untagged columns" pattern.
- Standardize Attributes and Naming – Best practice for maintaining a consistent tag taxonomy.

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
