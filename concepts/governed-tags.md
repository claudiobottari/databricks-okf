---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6b19e8cf100dcf8d54c5a33b4b488e98080307ff1fad0e944250009a19e2ec08
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
    - data-discovery-in-unity-catalog-databricks-on-aws.md
    - tutorial-configure-abac-databricks-on-aws.md
    - tutorial-configure-abac-with-sql-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - governed-tags
    - Governed Tag
    - governance tags
    - governed tag
    - Governed Tag|governed tag
    - Governed Tag|governed tags
    - Governed tag policies
    - system governed tags
    - governed-tags-in-unity-catalog
    - GTIUC
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
    - file: tutorial-configure-abac-with-sql-databricks-on-aws.md
title: Governed Tags
description: User-defined or system-defined key-value metadata tags applied to securable objects in Unity Catalog that can be referenced in ABAC GRANT policy conditions to dynamically determine access.
tags:
  - metadata
  - unity-catalog
  - tagging
  - access-control
timestamp: "2026-06-19T21:55:27.882Z"
---

# Governed Tags

**Governed tags** are account-level key-value pairs in Databricks that serve as the fundamental metadata attributes for attribute-based access control (ABAC) in Unity Catalog. These tags represent characteristics such as sensitivity, classification, or business domain, and are used in policy conditions to dynamically identify which data a policy should protect. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Overview

Governed tags are defined at the **account level**, which means the same tag taxonomy can be reused across the entire data estate, including multiple metastores. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Tags are key-value pairs. Allowed values can be optionally defined for a tag key; when allowed values are specified, only those specific values can be assigned. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md] For example, a tag key `pii` might have allowed values `ssn`, `email`, and `phone_number`. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Governed tags can be referenced in policy conditions using built-in functions like `has_tag()` and `has_tag_value()`, which check whether a given tag is present on the target data object, either directly or through tag inheritance. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Tag Inheritance

Securable objects in Unity Catalog inherit tags from their parent catalog or schema by default. The inheritance chain is:

- A **catalog** can have tags.
- A **schema** inherits tags from its parent catalog and can also have its own tags (overriding or adding).
- A **table, model, or volume** inherits tags from its parent schema and can have its own tags.
- **Columns** do **not** inherit tags from the parent table; column tags must be applied directly to each column. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

![Governed tags hierarchy diagram](https://docs.databricks.com/aws/en/assets/images/governed-tags-hierarchy-2740348868f29ddf0611089d4684adec.png) ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Overriding inherited tags is possible at every level except the column level. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Creating and Managing Governed Tags

### Permissions Required

To **create** a governed tag (define a new key), you must be an account admin or have the `CREATE` permission for tags at the account level. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md] To **assign** a governed tag to a securable object, you need the `ASSIGN` privilege on the tag and the `APPLY TAG` privilege on the object. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Tag Creation

Governed tag keys and their allowed values are created by account‑level administrators. The taxonomy should be designed before tags are applied to data assets. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Tag data is stored as plain text and may be replicated globally. Do not use tag names, values, or descriptors that could compromise the security of your resources. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

## Applying Tags to Unity Catalog Securable Objects

Tags can be applied to catalogs, schemas, tables, columns, models, and volumes. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

When a user creates a securable object, they automatically receive `APPLY TAG` on that object. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Correct tagging is essential for ABAC policies to apply. Tagging is also a security boundary: if a user can change tags on a data asset, they can change which policies apply to it. Organizations should control who can apply tags and audit tag changes. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Applying Tags via SQL

Use the `ALTER` statement with the `SET TAGS` clause to apply tags to columns. For example:

```sql
ALTER TABLE abac.customers.profiles
  ALTER COLUMN SSN
  SET TAGS ('pii' = 'ssn');
```

^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

## Using Governed Tags in ABAC Policies

The following built-in functions evaluate tags on securable objects:

- `has_tag(tag_key)` – returns `TRUE` if the tag key is present (any value), considering inheritance.
- `has_tag_value(tag_key, tag_value)` – returns `TRUE` if the tag has the specific key-value pair. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

These functions are used in the `WHEN` clause (table conditions) and `MATCH COLUMNS` clause (column conditions) of policies. They use snake_case naming (`has_tag`, `has_tag_value`); the older camelCase forms (`hasTag`, `hasTagValue`) continue to work but are not recommended. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Tags don't propagate from tables to columns. Using `has_tag()` in a `MATCH COLUMNS` clause only matches column-level tags, not tags on the parent table or its ancestors. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Example: Row Filter Policy

A row filter policy can restrict rows based on values in columns identified by tags. The following example ensures the EMEA team sees only rows where a column tagged `region` matches `'EMEA'`:

```sql
CREATE FUNCTION filter_by_region(region STRING, allowed STRING) RETURNS BOOLEAN
  RETURN region = allowed;

CREATE POLICY regional_access_emea
ON CATALOG sales
ROW FILTER filter_by_region
TO `emea team`
FOR TABLES
MATCH COLUMNS has_tag('region') AS rgn
USING COLUMNS (rgn, 'EMEA');
```

^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Example: Column Mask Policy

A column mask policy controls what values users see for columns matching tag conditions. The following example masks SSN columns (tagged with `pii : ssn`) so that non-exempt users see only the last four digits:

```sql
CREATE FUNCTION mask_ssn(ssn STRING, show_last INT) RETURNS STRING
  RETURN CONCAT('***-**-', RIGHT(ssn, show_last));

CREATE POLICY mask_ssn_columns
ON CATALOG hr_catalog
COLUMN MASK mask_ssn
TO `account users` EXCEPT `compliance team`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_col
ON COLUMN ssn_col
USING COLUMNS (4);
```

^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Best Practices

- **Standardize tag naming**: Define a controlled taxonomy with consistent key names and allowed values before applying tags to data. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Control who can apply tags**: Tagging is a security boundary – users who can change tags on an object can affect which ABAC policies apply. Audit tag changes. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Use tag inheritance for safe defaults**: Apply default tag values at the catalog or schema level so descendants inherit them, and override only on specific objects when necessary. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Apply policies at the highest level**: Databricks recommends attaching policies at the highest applicable level, usually the catalog, to maximize governance efficiency. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [ABAC](/concepts/abac-attribute-based-access-control.md) – Access control model that uses governed tags.
- [ABAC Row Filter Policies](/concepts/abac-row-filter-policy.md) – Restrict rows based on tag conditions.
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md) – Mask column values based on tag conditions.
- [ABAC GRANT Policies (Beta)](/concepts/abac-grant-policy.md) – Dynamically grant privileges using governed tags.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) where governed tags are defined.
- User-defined functions (UDFs) in Unity Catalog – Used to implement filtering and masking logic in ABAC policies.
- [Data Discovery in Unity Catalog](/concepts/data-discovery-in-unity-catalog.md) – How tags improve data discoverability.
- [Certify and deprecate data](/concepts/certified-and-deprecated-data-flags.md) – System tags for marking data asset quality.

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
- tutorial-configure-abac-with-sql-databricks-on-aws.md
- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
2. [tutorial-configure-abac-with-sql-databricks-on-aws.md](/references/tutorial-configure-abac-with-sql-databricks-on-aws-99ec3df0.md)
