---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ab7702f90edac835b83ce97f4f7fb024db3374a986940df0607f8d63be0ad77a
  pageDirectory: concepts
  sources:
    - manage-access-requests-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prerequisite-permission-validation
    - PPV
  citations:
    - file: manage-access-requests-databricks-on-aws.md
title: Prerequisite Permission Validation
description: Automatic checking of prerequisite privileges (e.g., USE CATALOG, USE SCHEMA) when users request a privilege like SELECT, with missing prerequisites generating additional requests.
tags:
  - unity-catalog
  - access-control
  - validation
timestamp: "2026-06-19T19:22:39.017Z"
---

# Prerequisite Permission Validation

**Prerequisite Permission Validation** is an automated check performed by [Unity Catalog](/concepts/unity-catalog.md) when a user requests privileges on a securable object. The system verifies that the requesting user already holds the necessary prerequisite privileges (such as `USE CATALOG` and `USE SCHEMA`) before granting the requested privilege (such as `SELECT` on a table).

## How It Works

When a user requests a privilege like `SELECT` on a table, Unity Catalog automatically checks whether the user possesses the required ancestor-level privileges — specifically `USE CATALOG` on the containing catalog and `USE SCHEMA` on the containing schema. ^[manage-access-requests-databricks-on-aws.md]

If any prerequisite privileges are missing, the system does not simply deny the request. Instead, it generates additional access requests that are routed to the approvers of the parent objects where the prerequisites are lacking. This ensures that the user does not need to make separate, manual requests for each level of the hierarchy. ^[manage-access-requests-databricks-on-aws.md]

## Scope of Validation

The validation applies to all access requests submitted through the Databricks access request feature, including requests made on behalf of other users, service principals, or groups. ^[manage-access-requests-databricks-on-aws.md]

The following scenarios are covered:

- Requests made by the user for themselves
- Requests made on behalf of another user
- Requests made on behalf of a service principal
- Requests made on behalf of a group

## Impact on Request Routing

When prerequisite permission validation identifies missing privileges, the generated requests for those missing prerequisites are sent to the approvers configured for the relevant parent objects (catalog or schema). This routing follows the standard [Access Request Destinations](/concepts/access-request-destinations.md) configured on those objects. ^[manage-access-requests-databricks-on-aws.md]

## Related Concepts

- [Access Request Destinations](/concepts/access-request-destinations.md) — Configured endpoints (email, Slack, webhook) that receive access requests
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The permission model governing securable objects
- USE CATALOG Privilege — Required to access any object within a catalog
- USE SCHEMA Privilege — Required to access any object within a schema
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI surface where users can request privileges
- INSUFFICIENT_PERMISSIONS Error — Error shown when a query fails due to missing privileges

## Sources

- manage-access-requests-databricks-on-aws.md

# Citations

1. [manage-access-requests-databricks-on-aws.md](/references/manage-access-requests-databricks-on-aws-de8a9a55.md)
