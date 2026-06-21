---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 50e65e98d3e8f3b88101d436d328cbb331929ff5e5f94b07648dba01e1f2c88c
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policies-in-unity-catalog-beta
    - GPIUC(
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
title: GRANT Policies in Unity Catalog (Beta)
description: A type of ABAC policy supporting dynamic privilege grants, currently scoped to EXECUTE on models in Unity Catalog.
tags:
  - unity-catalog
  - privileges
  - beta
timestamp: "2026-06-19T17:36:13.110Z"
---

# GRANT Policies in Unity Catalog (Beta)

**GRANT Policies** are a Beta feature of [Attribute-based access control (ABAC)](/concepts/attribute-based-access-control-abac-in-unity-catalog.md) that enable dynamic privilege grants based on attribute conditions. They allow administrators to define policies that automatically grant permissions to principals when the policy’s conditions are met, without requiring explicit per-principal grants. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Overview

GRANT policies extend Unity Catalog’s ABAC model by supporting dynamic privilege grants. While other ABAC policy types (such as row filters and column masks) control data access, GRANT policies control who can perform actions on a securable object. The policy conditions are evaluated at access time, and if a principal satisfies the conditions, the specified privilege is granted. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Current Scope

As of the public beta, GRANT policies are scoped to the `EXECUTE` privilege on **models**. This means a GRANT policy can be attached to a model (or to a catalog/schema that contains models) to automatically grant `EXECUTE` permission to principals whose attributes match the policy’s conditions. The scope may expand to other privileges and securable objects in future releases. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Attribute-based access control in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md) – The foundational ABAC framework that GRANT policies are part of.
- [Row Filter Policies](/concepts/row-filter-policies.md) – ABAC policy type for row-level filtering.
- [Column Mask Policies](/concepts/column-mask-policies.md) – ABAC policy type for column-level masking.
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md) – The objects (catalogs, schemas, tables, models) that policies protect.
- [Governed Tags](/concepts/governed-tags.md) – The attributes used to define policy conditions.

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
