---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef1ab4205a5b972b31afaa2c73b1d7c60c442f8245ebcc6192b9caaaaf6194e2
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - tutorial-configure-abac-databricks-on-aws.md
    - tutorial-configure-abac-with-sql-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - column-mask-policies
    - CMP
    - Column Mask (CM) Policies
    - Column Mask (CM) policies
    - Column Masking Policies
    - COLUMN_MASK
    - Column Mask (CM)
    - Column Mask CM
    - Column Mask Policy
    - Column mask
    - Column mask policy
    - Column masks
    - Masking policies
    - PII masking policies|PII masking
    - column mask policy
    - column mask policy|column mask
    - column-mask-policies-in-unity-catalog
    - CMPIUC
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - file: tutorial-configure-abac-databricks-on-aws.md
    - file: tutorial-configure-abac-with-sql-databricks-on-aws.md
title: Column Mask Policies
description: ABAC policy type that enforces column-level security on tables, materialized views, and streaming tables by masking column values based on attributes
tags:
  - access-control
  - column-level-security
  - unity-catalog
timestamp: "2026-06-19T22:08:49.248Z"
---

---
title: Column Mask Policies
summary: Unity Catalog security feature that masks column values at query time using attribute-based access control (ABAC) and user-defined functions.
sources:
  - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
  - tutorial-configure-abac-databricks-on-aws.md
  - tutorial-configure-abac-with-sql-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T12:00:00.000Z"
updatedAt: "2026-06-19T12:00:00.000Z"
tags:
  - databricks
  - unity-catalog
  - security
  - abac
aliases:
  - column mask policies
  - column masking
  - column mask
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Column Mask Policies

**Column Mask Policies** are a data governance mechanism in [Unity Catalog](/concepts/unity-catalog.md) that dynamically redact or transform column values at query time based on user attributes or other conditions. They are part of [Attribute-based Access Control (ABAC)](/concepts/attribute-based-access-control-abac-in-unity-catalog.md) and work alongside [Row Filter Policies](/concepts/row-filter-policies.md) to enforce fine-grained, attribute-driven data security. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md, tutorial-configure-abac-databricks-on-aws.md]

## How Column Mask Policies Work

A column mask policy uses a user-defined function (UDF) to transform the values of a column before they are returned to the user. The UDF receives the original column value and can return any value—a static placeholder, a partially masked string, or the original value conditionally. ^[tutorial-configure-abac-databricks-on-aws.md, tutorial-configure-abac-with-sql-databricks-on-aws.md]

Policies are attached at the schema or catalog level and apply to all matching columns within that scope. ABAC policies discover which columns to protect by matching [Governed Tags](/concepts/governed-tags.md) assigned to columns. For example, a column tagged `pii = ssn` can be targeted by a masking policy that applies a `redact_ssn` UDF. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

Column mask policies are created with a `MATCH COLUMNS` condition that uses tag-based predicates (`has_tag_value` or `has_tag`) to identify columns dynamically. This allows a single policy to protect every column that carries a given governed tag, even as new columns are added. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

## Creating a Column Mask Policy

Column mask policies can be created through the Catalog Explorer UI or with SQL. Both approaches require `MANAGE` or ownership on the target schema or catalog, and `EXECUTE` on the UDF used in the policy. ^[tutorial-configure-abac-databricks-on-aws.md, tutorial-configure-abac-with-sql-databricks-on-aws.md]

### Prerequisites

- Databricks Runtime 16.4 or above (or serverless compute).
- Account admin or workspace admin permissions (to create governed tags).
- `MANAGE` permission on the target catalog or schema.
- `EXECUTE` on the UDFs referenced by the policy.
- Compute running older runtimes cannot access tables secured by ABAC. ^[tutorial-configure-abac-databricks-on-aws.md, tutorial-configure-abac-with-sql-databricks-on-aws.md]

### Using the Catalog Explorer UI

1. Navigate to the target catalog or schema and click the **Policies** tab.
2. Click **New policy**.
3. Enter a name and description, select the principals the policy applies to (e.g., `All account users`), and choose the scope (catalog or schema).
4. For **Purpose**, choose **Mask column data**.
5. In **Conditions**, choose **Mask column if it has specific tag**, select the governed tag (e.g., `pii : ssn`), and then choose a UDF.
6. Optionally test the masking function.
7. Click **Create policy**. ^[tutorial-configure-abac-databricks-on-aws.md]

### Using SQL

Define a UDF that performs the masking logic, then create the policy using `CREATE POLICY` with the `COLUMN MASK` clause. Example:

```sql
CREATE POLICY redact_ssn_policy
ON SCHEMA target_catalog.target_schema
COLUMN MASK redact_ssn
TO `account users`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_col
ON COLUMN ssn_col;
```

The `MATCH COLUMNS` clause identifies columns by governed tag. `USING COLUMNS` allows passing additional column values (e.g., a consent flag) to the UDF for conditional masking. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

## UDF Patterns

The UDF can implement any masking logic. Common patterns include:

- **Static replacement**: Return a constant string such as `'***-**-****'`. ^[tutorial-configure-abac-databricks-on-aws.md]
- **Partial masking**: Show only the first character and domain of an email. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]
- **Conditional masking**: Use an additional argument (passed from another column via `USING COLUMNS`) to decide whether to mask or show the original value. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

## Conditional Masking (Consent-Aware)

ABAC supports conditional masking where the mask behavior depends on another column in the same row. For example, an email mask might show the full email only if a `has_consent` column is `TRUE`. To achieve this:

1. Tag the condition column (e.g., `has_consent`) with a governed tag.
2. In the UDF, accept both the column to be masked and the condition column as parameters.
3. In the policy, use `USING COLUMNS` to pass the condition column to the UDF, referencing it by the tag-based alias from `MATCH COLUMNS`. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

## Scope and Applicability

Column mask policies apply to tables, materialized views, and streaming tables. They are evaluated dynamically at query time; the user sees the masked value based on their identity and the policy's conditions. Multiple policies can coexist—row filters and column masks can be combined to hide rows and mask columns simultaneously. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md, tutorial-configure-abac-with-sql-databricks-on-aws.md]

## Limitations

- Column mask policies require governed tags to be defined at the account level.
- Tags are stored as plain text and may be replicated globally; avoid tagging with sensitive or personal data.
- Compute running older runtimes (below Databricks Runtime 16.4) cannot access tables secured by ABAC. As a workaround, you can configure ABAC to apply only to a specific group and add users exempted from the policy to another group. ^[tutorial-configure-abac-databricks-on-aws.md, tutorial-configure-abac-with-sql-databricks-on-aws.md]

## Related Concepts

- [Row Filter Policies](/concepts/row-filter-policies.md) – Hide entire rows based on column values.
- [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md) – The overarching framework.
- [Governed Tags](/concepts/governed-tags.md) – Key-value metadata used to identify columns for policy matching.
- Unity Catalog User-Defined Functions (UDFs) – Functions that implement masking logic.
- [Data Masking](/concepts/conditional-column-masking.md) – Broader security pattern for obfuscating sensitive data.
- DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE – Known error when column masks are incompatible with external metadata sources.

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
- tutorial-configure-abac-databricks-on-aws.md
- tutorial-configure-abac-with-sql-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
2. [tutorial-configure-abac-databricks-on-aws.md](/references/tutorial-configure-abac-databricks-on-aws-cbba5828.md)
3. [tutorial-configure-abac-with-sql-databricks-on-aws.md](/references/tutorial-configure-abac-with-sql-databricks-on-aws-99ec3df0.md)
