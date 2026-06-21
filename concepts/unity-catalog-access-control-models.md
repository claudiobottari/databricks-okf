---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 84c0da3dd37497c2107306021f230b3e73edb4ad5c1ae940d592e4f0afdb57d1
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-access-control-models
    - UCACM
    - Unity Catalog Access Control
    - Unity Catalog access control
    - Unity Catalog access modes
    - Access Control Models
    - Catalog Access Control
    - U2M OIDC Data Access
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Access Control Models
description: "Four complementary access control models in Unity Catalog: privileges/ownership, ABAC, table-level filtering/masking, and workspace-level restrictions."
tags:
  - unity-catalog
  - access-control
  - databricks
timestamp: "2026-06-19T21:54:38.200Z"
---

```markdown
---
title: Unity Catalog Access Control Models
summary: Four complementary access control models in Unity Catalog: privileges/ownership, attribute-based policies (ABAC), table-level filtering/masking, and workspace-level restrictions.
sources:
  - access-control-in-unity-catalog-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:36:21.013Z"
updatedAt: "2026-06-19T13:50:29.200Z"
tags:
  - unity-catalog
  - access-control
  - authorization
aliases:
  - unity-catalog-access-control-models
  - UCACM
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

## Unity Catalog Access Control Models

**Unity Catalog** provides a multi-layered access control system that combines privilege-based grants, attribute-based policies, table-level filters, and workspace-level restrictions. These models work together to enforce secure, fine-grained access across your data environment. ^[access-control-in-unity-catalog-databricks-on-aws.md]

---

### The Four Complementary Access Control Models

#### 1. Privileges and Ownership
This model controls *who* can access *what* through direct `GRANT` statements and ownership on securable objects (catalogs, schemas, tables, views, volumes, models, and more). Privileges are inherited from parent to child objects in the three-level namespace, and additional privileges can be granted directly on any object. Ownership grants administrative control over an object, including the ability to manage permissions. ^[access-control-in-unity-catalog-databricks-on-aws.md]

#### 2. Attribute-Based Access Control (ABAC)
ABAC uses governed tags and centralized policies to dynamically control *what* data users can access. ABAC policies grant privileges on securable objects whose tags match a condition, evaluated at every access check. This approach centralizes and scales access control without requiring per-object grants. ^[access-control-in-unity-catalog-databricks-on-aws.md]

#### 3. Table-Level Filtering and Masking
Row filters and column masks control *what* data users can see within tables. These are implemented using user-defined functions (UDFs) that filter rows or mask column values at query time. They are applied per table and provide precise content-level restrictions. ^[access-control-in-unity-catalog-databricks-on-aws.md]

#### 4. Workspace-Level Restrictions
Workspace-catalog bindings control *where* users can access data by restricting which workspaces can access specific catalogs, external locations, and storage credentials. This model is primarily used for compliance and organizational boundaries. ^[access-control-in-unity-catalog-databricks-on-aws.md]

---

### When to Use Each Access Control Mechanism

The following table compares the four models across common access control criteria. They are designed to be used together, not in isolation.

| Criterion | Privileges & Ownership | ABAC (Attribute-Based) | Row Filters & Column Masks | Workspace Bindings |
|---|---|---|---|---|
| **What it controls** | Who can access an object | Which objects a principal can access based on tags | Which rows/columns a user sees inside a table | Which workspaces can use a catalog or credential |
| **Granularity** | Object-level (catalog, schema, table, etc.) | Object-level, scoped by tag conditions | Row-level and column-level | Catalog, external location, storage credential |
| **Scalability** | Requires one grant per object or per principal | Scales via tag-based policies; no per-object grants | Per-table UDFs; best for targeted logic | Set once per catalog/credential |
| **Use case** | Standard access provisioning | Dynamic access based on data classification attributes | Redacting sensitive columns, filtering rows per user | Data isolation between workspaces |

^[access-control-in-unity-catalog-databricks-on-aws.md]

### Recommendations

Databricks recommends using attribute-based access control (ABAC) to centralize and scale access control based on governed tags. Use row filters and column masks only when you need per-table logic or haven't adopted ABAC yet. ^[access-control-in-unity-catalog-databricks-on-aws.md]

---

### Related Concepts

- ABAC Policy – Attribute-based policies that dynamically grant privileges
- [[Row Filters and Column Masks]] – Per-table data masking and filtering
- [[Workspace-Catalog Binding]] – Restricting catalog access to specific workspaces
- [[Unity Catalog]] – The data governance platform underlying all models
- Privileges Reference – Detailed descriptions of all Unity Catalog privileges

### Sources

- access-control-in-unity-catalog-databricks-on-aws.md
```

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
