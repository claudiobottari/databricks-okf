---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 897c2cf8dcc25ca2c17ec4f74d7d77d2c0c159511993e71431089a959404b2cb
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-access-control-in-unity-catalog
    - MACIUC
    - Access Control in Unity Catalog
    - Access control in Unity Catalog
    - Managed access control in Unity Catalog
    - access control in Unity Catalog
  citations:
    - file: manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
title: Model Access Control in Unity Catalog
description: Using Unity Catalog's GRANT ON FUNCTION syntax and Catalog Explorer to set permissions on registered models, including USE SCHEMA, USE CATALOG, CREATE MODEL, and EXECUTE privileges.
tags:
  - security
  - unity-catalog
  - permissions
timestamp: "2026-06-19T19:24:40.697Z"
---

# Model Access Control in Unity Catalog

**Model Access Control in Unity Catalog** governs how users and service principals can interact with registered ML models and their versions. Unity Catalog treats registered models as a securable subtype of the `FUNCTION` object, enabling fine-grained privilege management that integrates with the broader Unity Catalog access control model. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Securable Type and Grant Model

In Unity Catalog, a registered model is a securable object of type `FUNCTION`. To grant access to a model, you use the SQL `GRANT ON FUNCTION` statement. You can also manage model ownership and permissions through the Catalog Explorer UI. For programmatic access, the [Grants REST API](https://docs.databricks.com/api/workspace/grants) is used, with `securable_type` set to `"FUNCTION"`. For example, send a `PATCH /api/2.1/unity-catalog/permissions/function/{full_name}` request to update permissions. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Required Privileges by Operation

The source material specifies privileges needed for common model management actions:

| Operation | Required Privileges |
| --------- | ------------------- |
| Create a new registered model | `CREATE MODEL` on the schema, `USE SCHEMA` on the schema, `USE CATALOG` on the enclosing catalog |
| Create a new model version | Owner of the registered model **or** `CREATE MODEL VERSION` on it, plus `USE SCHEMA` and `USE CATALOG` on the schema and catalog |
| View a model or its versions in the UI | `EXECUTE` on the registered model, plus `USE SCHEMA` and `USE CATALOG` |
| Load a model version for inference (by alias or version) | `EXECUTE` on the registered model, plus `USE SCHEMA` and `USE CATALOG` |
| Set or delete model aliases | Owner of the registered model, plus `USE SCHEMA` and `USE CATALOG` |
| Rename a model | Owner of the model, `CREATE MODEL` on the schema, plus `USE SCHEMA` and `USE CATALOG` |
| Copy a model version | Ownership of the destination model **or** `CREATE MODEL VERSION` on it, plus `USE CATALOG` on both source and destination catalogs, `USE SCHEMA` on both schemas, and `EXECUTE` on the source model |
| Delete a model version or registered model | Owner of the model, plus `USE SCHEMA` and `USE CATALOG` on the schema and catalog |
| Apply or delete tags on a model or version | Owner of the model **or** `APPLY TAG` privilege, plus `USE SCHEMA` and `USE CATALOG` |
| Add or edit descriptions | Owner of the model, plus `USE SCHEMA` and `USE CATALOG` |

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Granting Privileges

Grant privileges using the SQL command:

```sql
GRANT CREATE MODEL ON SCHEMA <schema-name> TO <principal>;
```

For more details, see Manage privileges in Unity Catalog and the [Unity Catalog securable objects reference](/concepts/unity-catalog-securable-objects.md). ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Cross-Workspace Access

Any workspace attached to the same Unity Catalog [Metastore](/concepts/metastore.md) can access models, provided the caller has the appropriate privileges. For example, a development workspace can read models from a `prod` catalog to compare new models against the production baseline. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

To share models with users in other regions or accounts, use [OpenSharing](/concepts/opensharing.md) with the Databricks-to-Databricks flow. Recipients access shared models in a catalog created from the share, using the same access control model as any other Unity Catalog model. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Ownership and Collaboration

By default, only the creator of a registered model can manage it. To collaborate with others, transfer ownership of the model to a group that includes yourself and the collaborators. Collaborators also need `USE CATALOG` and `USE SCHEMA` on the enclosing [Catalog and Schema](/concepts/catalog-and-schema.md). ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md) – Overview of all securable types (catalogs, schemas, tables, functions, etc.)
- Managed access control in Unity Catalog – The broader privilege model
- [Model Aliases](/concepts/model-aliases.md) – Mutable, named references to model versions, often used to manage deployment stages
- [Model promotion across environments](/concepts/model-version-promotion-across-environments.md) – Using copy and aliases combined with access control to govern model lifecycle

## Sources

- manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/manage-model-lifecycle-in-unity-catalog-databricks-on-aws-5d1bac95.md)
