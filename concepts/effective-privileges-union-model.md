---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 893df5c5426701a669895de2936127768e76c7d7ad7727db0f6c42871fd49e14
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - effective-privileges-union-model
    - EPUM
    - Effective privileges
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Effective Privileges Union Model
description: The principle that effective privileges on a securable object are the union of direct grants and any applicable GRANT policies, meaning a more selective policy does not override broader direct grants.
tags:
  - access-control
  - unity-catalog
  - security-model
timestamp: "2026-06-19T21:54:17.255Z"
---

# Effective Privileges Union Model

The **Effective Privileges Union Model** is the principle by which [Unity Catalog](/concepts/unity-catalog.md) determines a principal's access to a securable object: the effective privileges are the union of direct grants and any applicable [ABAC GRANT Policies](/concepts/abac-grant-policies.md). This means a principal holds a privilege on an object if either source — or both — grants it. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## How It Works

Unity Catalog evaluates access at each request by combining two independent mechanisms:

- **Direct grants** – Privileges assigned explicitly via `GRANT` statements on the object, its parent schema, or its parent catalog. These can be granted directly to the principal or inherited through group membership or administrative privileges.
- **GRANT policies** – Attribute-based policies attached at the catalog or schema level that dynamically grant privileges to every securable object whose governed tags match the policy's `WHEN` condition. A GRANT policy lists principals in its `TO` clause (and optionally excludes some via `EXCEPT`).

A principal holds the privilege when **any** of the following is true:

- A GRANT policy whose scope covers the object lists the principal in `TO` (and not in `EXCEPT`), and the policy's condition matches the tags on the object.
- A direct grant of that privilege on the object, its schema, or its catalog is in effect for the principal.

Because the effective set is the union, a more restrictive GRANT policy does not by itself revoke privileges that are already granted directly. The principal can still hold the privilege through a direct grant on the object or its ancestors. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Key Concepts

- **Union semantics** – Access is granted if either source provides it. There is no conflict resolution that prefers one source over the other; both are additive.
- **Tag-based conditions** – GRANT policies use governed tags (user-defined or system tags) to decide which objects the policy covers. Tags are evaluated at access time.
- **Scope** – GRANT policies are attached to a catalog or schema (not directly to the object). `SHOW EFFECTIVE POLICIES` on a schema or catalog lists all policies that apply to objects within that scope.

## Interaction with Direct Grants

The union model requires care when both mechanisms are used for the same privilege on overlapping objects. To audit effective access:

- Use `SHOW EFFECTIVE POLICIES ON SCHEMA <name>` (or `ON CATALOG <name>`) to list all GRANT policies whose scope covers the objects.
- Use `SHOW GRANTS` on the object and its ancestors to enumerate direct grants.
- For a complete view, combine the results of both commands — `SHOW GRANTS` does not include privileges granted by a GRANT policy.

If you intend GRANT policies to be the primary control for a privilege, first check whether any direct grants already exist that would override the policy’s intent. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best Practices

- **Don't mix GRANT policies and direct grants for the same privilege.** For a given privilege on a securable, choose one mechanism. Mixing makes it harder to reason about who has access and to audit changes.
- **Use groups in `TO` and `EXCEPT`.** Adding or removing users from a named group changes who the policy applies to without editing the policy itself.
- **Attach policies at the smallest scope that covers the targets.** A broader scope may bring unrelated securables into the policy’s tag-matching and grant unintended access.
- **Grant `USE CATALOG` and `USE SCHEMA` directly.** GRANT policies do not support these prerequisite permissions; they must be granted directly. Use GRANT policies for the privilege on the target objects (e.g., `EXECUTE` on models). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations

- In Beta, only the `EXECUTE` privilege on models is supported via GRANT policies.
- `SHOW GRANTS` does not reflect privileges obtained through GRANT policies.
- Deleting a model or version is not covered by GRANT policies; direct grants are required for that operation.
- Delta Sharing cannot share models that have GRANT policies defined on them. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) — The policy object that implements tag-based privilege assignment.
- [Direct Grant](/concepts/grant-policy-vs-direct-grant.md) — Explicit privilege assignment using `GRANT` statements.
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The full set of privileges and securable types in Unity Catalog.
- [Governed Tags](/concepts/governed-tags.md) — The tags used in GRANT policy conditions to match securable objects.
- Effective Permissions API — The REST API that returns the union of direct and inherited grants (but does not include GRANT policies).

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
