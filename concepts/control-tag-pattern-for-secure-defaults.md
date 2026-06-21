---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 89e6de5d73a890d3d859199dec7bc6af711840d3ea8e22775dc6fd44a84f9182
  pageDirectory: concepts
  sources:
    - secure-new-tables-by-default-with-control-tags-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - control-tag-pattern-for-secure-defaults
    - CTPFSD
  citations:
    - file: secure-new-tables-by-default-with-control-tags-databricks-on-aws.md
title: Control Tag Pattern for Secure Defaults
description: A governance pattern using a schema-level control tag (e.g., review_status) to automatically lock down new tables by default until a data steward reviews and releases them.
tags:
  - data-governance
  - unity-catalog
  - access-control
timestamp: "2026-06-19T20:20:15.857Z"
---

## Control Tag Pattern for Secure Defaults

The **Control Tag Pattern for Secure Defaults** is a data governance approach on Databricks that automatically locks down new tables in a schema until a data steward reviews and classifies their contents. It uses a schema-level [governed tag](/concepts/governed-tags.md) (e.g., `review_status = pending`) so that every table created in that schema inherits a masked-by-default posture. After review, the tag is flipped to `reviewed` at the table level, and only columns tagged with [Data Classification](/concepts/data-classification.md) system tags (`class.*`) remain masked. This pattern prevents unclassified sensitive data from being inadvertently exposed to users with `SELECT` permissions. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

### How It Works

A schema-level control tag is set to `pending`. Any table created in that schema automatically inherits the tag. A policy, `review_pending_policy`, uses the `WHEN has_tag_value('review_status', 'pending')` condition with `MATCH COLUMNS TRUE` to apply a column mask to **every** column. The mask uses the built-in `system.data_classification.mask_value` function, which returns a type‑aware placeholder (e.g., `0` for integers, `DATE '1970-01-01'` for dates, a SHA-256 hash for strings). No custom UDF is needed. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

After a data steward reviews the table’s automatically detected classifications and corrects any false positives, they set the table‑level tag `review_status = 'reviewed'`. This overrides the inherited schema tag. A second policy, `review_complete_policy`, activates. It matches **only** columns that carry `class.*` tags (such as `class.name`, `class.email_address`, `class.us_ssn`). Non‑classified columns become visible, while sensitive columns remain masked using the same `mask_value` function. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

### Components

- **Governed tag** – A custom tag created in Catalog Explorer under **Governed Tags**. In this pattern, the tag is named `review_status` with values `pending` and `reviewed`. Tag data is stored as plain text and may be replicated globally; sensitive information should never be placed in tag names or values. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
- **Schema‑level tag** – Applied to the schema (`ALTER SCHEMA ... SET TAGS ('review_status' = 'pending')`). All new tables in that schema automatically inherit the tag. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
- **Table‑level tag** – Overrides the inherited schema tag when set (`ALTER TABLE ... SET TAGS ('review_status' = 'reviewed')`). ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
- **Data Classification** – A system that scans tables in the background and applies `class.*` governed tags (e.g., `class.name`, `class.email_address`) to detected sensitive columns. Auto‑tagging must be explicitly enabled after reviewing initial detections. The scan runs within 24 hours of enabling classification. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
- **Column mask policies** – Two schema‑level policies created with `CREATE POLICY ... ON SCHEMA ... COLUMN MASK ...`. The pending policy matches all columns; the reviewed policy matches columns based on `has_tag('class.*')` conditions. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
- **`system.data_classification.mask_value`** – A type‑aware masking function provided by Databricks. It replaces values with safe defaults depending on the data type, eliminating the need for custom UDFs. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

### Workflow

1. **Enable Data Classification** on the target catalog (optional: select specific schemas). ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
2. **Create the `review_status` governed tag** in Catalog Explorer. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
3. **Create the schema** and set `review_status = 'pending'` at the schema level. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
4. **Create the pending‑review policy** with `MATCH COLUMNS TRUE`. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
5. **Create tables** in the schema. They inherit `pending` and all columns are masked from the start. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
6. **Review classification results** and enable auto‑tagging so that `class.*` tags are applied to detected columns (within 24 hours). For immediate testing, `ALTER COLUMN ... SET TAGS` can be used to simulate tagging. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
7. **Create the reviewed policy** that matches only columns with `class.*` tags (e.g., `class.name`, `class.email_address`, `class.us_ssn`). ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
8. **Flip the table tag** to `reviewed`. The reviewed policy becomes active: non‑classified columns are visible, classified columns remain masked. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
9. **Automatic inheritance** – any new table created in the schema automatically starts with `pending` and full masking until reviewed. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

### Prerequisites

- Databricks Runtime 16.4 or above, or serverless compute.
- Account admin or workspace admin permissions (to create governed tags and enable Data Classification).
- `MANAGE` permission on the target catalog or schema.
- `EXECUTE` permission on the built‑in UDFs (the `mask_value` function).
- A SQL notebook or query editor. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

### Considerations

- To exempt specific groups from the mask, add an `EXCEPT` clause to the policy. For example, `TO \`account users\` EXCEPT \`data_admins\`` allows data admins to see unmasked data. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
- Tag data is stored as plain text and may be replicated globally. Never store personal or sensitive information in tag names, values, or descriptors. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]
- Data Classification scans occur within 24 hours of enabling. For immediate feedback, use manual `ALTER COLUMN ... SET TAGS` statements during development. ^[secure-new-tables-by-default-with-control-tags-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The overall governance framework in which governed tags and policies operate.
- Column-Level Security – The broader concept that includes column masks and row filters.
- [Governed Tags](/concepts/governed-tags.md) – The mechanism for attaching metadata to securable objects.
- [Data Classification](/concepts/data-classification.md) – Automated detection and tagging of sensitive data.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – The access control model underlying tag-based policies.
- [Schema-Level Policies](/concepts/policy-scoping-at-catalog-or-schema-level.md) – Policies applied at the schema level for broad coverage.

### Sources

- secure-new-tables-by-default-with-control-tags-databricks-on-aws.md

# Citations

1. [secure-new-tables-by-default-with-control-tags-databricks-on-aws.md](/references/secure-new-tables-by-default-with-control-tags-databricks-on-aws-955564d7.md)
