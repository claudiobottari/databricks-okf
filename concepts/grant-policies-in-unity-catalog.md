---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af84e1959a650a923ec8d8e81528087d3f7eae80f0f1c64770a50ca7f84db25e
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policies-in-unity-catalog
    - GPIUC
    - grant-policies-in-unity-catalog-beta
    - GPIUC(
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
title: GRANT policies in Unity Catalog
description: ABAC policy type (Beta) for dynamic privilege grants, currently scoped to EXECUTE on models.
tags:
  - access-control
  - unity-catalog
  - grants
  - policies
timestamp: "2026-06-19T14:04:30.413Z"
---

# GRANT Policies in Unity Catalog

**GRANT policies** are a type of attribute-based access control (ABAC) mechanism in Unity Catalog that enable dynamic privilege grants. They are currently in Beta and are scoped to the `EXECUTE` privilege on models. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Overview

GRANT policies are part of the broader [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md) framework. While ABAC traditionally enforces row- and column-level security through [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md), GRANT policies extend the model to support dynamic privilege assignment based on attributes. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Scope and Capabilities

As of the current Beta release, GRANT policies are limited to granting the `EXECUTE` privilege on models. This allows administrators to define policies that automatically grant execution rights to a model based on the attributes of the principal, the model, or the environment, rather than manually assigning permissions to each user or group. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## How GRANT Policies Work

GRANT policies are attached to a securable object (currently only at the model level) and are evaluated dynamically. When a principal attempts to execute a model, Unity Catalog checks whether any GRANT policy applies based on the attributes of the request. If the conditions defined in the policy are met, the `EXECUTE` privilege is effectively granted for that operation. This enables organizations to manage model access at scale without maintaining explicit permission lists. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Relationship to Other ABAC Features

- [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md) restrict data access at the row or column level.
- GRANT policies control execution access to models.
- All of these policy types rely on [Governed Tags](/concepts/governed-tags.md) to define the attributes used in policy conditions.

GRANT policies bring the same attribute-driven flexibility to privilege management that existing ABAC features provide for data filtering. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Beta Considerations

Because GRANT policies are in Beta, their behavior and API surface may change. The current limitation to `EXECUTE` on models is expected to expand in future releases. Databricks recommends testing GRANT policies in non-production environments before broad deployment. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC) in Unity Catalog](/concepts/attribute-based-access-control-abac-in-unity-catalog.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md)
- EXECUTE privilege on models

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
