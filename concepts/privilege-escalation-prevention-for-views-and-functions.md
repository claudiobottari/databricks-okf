---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22e7eb38160a6ff2b5ce3fa35cd9f77f4694d9b69f886b78da57fc58eb20c13a
  pageDirectory: concepts
  sources:
    - manage-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - privilege-escalation-prevention-for-views-and-functions
    - Functions and Privilege Escalation Prevention for Views
    - PEPFVAF
  citations:
    - file: manage-privileges-in-unity-catalog-databricks-on-aws.md
title: Privilege Escalation Prevention for Views and Functions
description: Only a metastore admin can transfer ownership of a view, function, or model to any user/group. Current owners and MANAGE users are restricted to transferring ownership to themselves or a group they belong to, preventing privilege escalation.
tags:
  - unity-catalog
  - security
  - ownership
  - views
  - privilege-escalation
timestamp: "2026-06-19T19:27:41.793Z"
---

# Privilege Escalation Prevention for Views and Functions

**Privilege Escalation Prevention for Views and Functions** is a security control in [Unity Catalog](/concepts/unity-catalog.md) that restricts ownership transfers of views, functions, and models to prevent unauthorized privilege escalation. The rule ensures that only a [metastore admin](/concepts/metastore-admin-role.md) can transfer ownership of these securable objects to any arbitrary principal, while all other grantees are limited in whom they can designate as owner.

## The Rule

To prevent privilege escalations, only a [Metastore](/concepts/metastore.md) admin can transfer ownership of a view, function, or model to any user, service principal, or group in the account. Current owners and users with the `MANAGE` privilege on the object are restricted to transferring ownership only to:

- Their own username (the current owner or the privilege holder), or  
- A group that they are a member of.

^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

This restriction prevents a user who controls a view or function from granting ownership to a principal with higher privileges (e.g., a workspace admin) and thereby gaining escalated access through that object’s definition or execution context.

## Who Can Transfer Ownership

The following principals are subject to the restriction:

- The object owner  
- Users with the `MANAGE` privilege on the object  

These principals **cannot** transfer ownership to an arbitrary user or group outside their own identity or group membership. Only a [Metastore](/concepts/metastore.md) admin can bypass this limitation and transfer ownership to any principal in the account.

^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Applicable Object Types

The privilege escalation prevention rule applies specifically to:

- Views (regular views and metric views)  
- Functions (user-defined functions)  
- Models (registered machine learning models)

^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

### Materialized Views and Streaming Tables

[Materialized views](/concepts/materialized-views-in-databricks.md) and streaming tables follow different ownership transfer rules. These objects can have their ownership transferred when created with Databricks SQL, but those created with Lakeflow Spark Declarative Pipelines cannot have ownership directly transferred; instead, the owner is updated to the pipeline’s run-as user upon the next refresh. The privilege escalation prevention described above does not explicitly apply to materialized views or streaming tables, though their ownership rules are governed by separate documentation.

^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Rationale

Views and functions can contain arbitrary logic (SQL or Python) that executes with the owner’s or invoker’s privileges. Allowing non-admin principals to freely transfer ownership could enable a low-privilege user to assign ownership of a malicious view to a high-privilege principal, effectively escalating their own access. By limiting ownership transfers to the [Metastore](/concepts/metastore.md) admin, Unity Catalog ensures that only centrally trusted administrators can change ownership of these sensitive object types to arbitrary principals.

## Related Concepts

- [Unity Catalog Permissions Model](/concepts/unity-catalog-permissions-model.md) – overall privilege inheritance and ownership model  
- Manage object ownership – general ownership transfer procedures  
- [Metastore admin](/concepts/metastore-admin-role.md) – the role that can bypass the restriction  
- [MANAGE Privilege](/concepts/manage-privilege.md) – grants the ability to manage privileges on an object  
- Views – securable objects subject to this restriction  
- Functions – securable objects subject to this restriction  
- Models – securable objects subject to this restriction  
- Collaborative editing – when a group owns a view, all members can edit its definition  

## Sources

- manage-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [manage-privileges-in-unity-catalog-databricks-on-aws.md](/references/manage-privileges-in-unity-catalog-databricks-on-aws-f0868c6d.md)
