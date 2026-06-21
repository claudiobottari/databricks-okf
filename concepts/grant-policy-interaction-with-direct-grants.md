---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b901d60f4c46fba2c87454f565f98139c5d871e9ae84320010528c69dc637d68
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-interaction-with-direct-grants
    - GPIWDG
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy Interaction with Direct Grants
description: Effective privileges are the union of direct grants and GRANT policies; a principal holds EXECUTE if either mechanism grants it, making mixing the two approaches potentially confusing.
tags:
  - unity-catalog
  - access-control
  - permissions
timestamp: "2026-06-19T13:50:22.400Z"
---

## GRANT Policy Interaction with Direct Grants

**GRANT Policy Interaction with Direct Grants** describes how attribute-based access control (ABAC) policies and explicit privilege assignments work together in [Unity Catalog](/concepts/unity-catalog.md). When a [GRANT policy](/concepts/grant-policies-beta.md) and a [Direct Grant](/concepts/grant-policy-vs-direct-grant.md) both apply to the same securable object, the effective privileges a principal receives are the **union** of the two sources.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Union of Privileges

The effective `EXECUTE` privilege on a model is granted to a principal if *any* of the following conditions is true:^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

1.  A GRANT policy attached to the model’s parent catalog or schema lists the principal in its `TO` clause (and not in `EXCEPT`), and the policy’s `WHEN` condition matches the governed tags on the model.
2.  A direct `GRANT EXECUTE` on the model itself, on its schema, or on its catalog is in effect for that principal – whether granted directly to the principal, through group membership, or through other administrative privileges (e.g., `OWNERSHIP`).

Because the union model applies, a more restrictive GRANT policy does **not** automatically exclude a principal who already holds `EXECUTE` through a direct grant. The principal retains access until the direct grant is revoked.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Implications

If you intend to use GRANT policies as the primary mechanism for controlling `EXECUTE` on models, you must first determine whether any existing direct grants might override the policy’s intent. The source recommends:^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- Use `SHOW EFFECTIVE POLICIES ON SCHEMA` (or `ON CATALOG`) to list every GRANT policy whose scope covers the models in that schema or catalog. (The equivalent REST API is `GET /api/2.1/unity-catalog/policies/{on_securable_type}/{on_securable_fullname}?include_inherited=true`; Python SDK: `w.policies.list_policies(..., include_inherited=True)`.)
- Use `SHOW GRANTS` on the model and its ancestors to enumerate direct grants. (REST API for direct grants: `GET /api/2.1/unity-catalog/permissions/{securable_type}/{full_name}`; Python SDK: `w.grants.get(...)`. For the union of direct and inherited grants: `GET /api/2.1/unity-catalog/effective-permissions/{securable_type}/{full_name}`; Python SDK: `w.grants.get_effective(...)`.)

Note that `SHOW GRANTS` does **not** include privileges granted by a GRANT policy. To see the full picture of `EXECUTE` access on a model, combine the output of `SHOW GRANTS` with the GRANT policies returned by `SHOW EFFECTIVE POLICIES` on its parent scope.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Best Practices

The following guidance is provided in the source documentation:^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- **Do not mix GRANT policies and direct grants for the same privilege.** For a given privilege on a securable, choose either GRANT policies or direct grants. Mixing the two on the same securable makes it harder to reason about who has access and complicates auditing.
- **Use direct grants for `USE CATALOG` and `USE SCHEMA`, and GRANT policies for `EXECUTE`.** GRANT policies currently support only the `EXECUTE` privilege on models. The prerequisite `USE` privileges must be granted directly.

### Limitations

- `SHOW GRANTS` does not reflect privileges granted by a GRANT policy.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `INFORMATION_SCHEMA` does not include GRANT policies.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- The `EXECUTE` privilege on models is the only privilege and securable type currently supported by GRANT policies (Beta). Non-supported privileges (e.g., `CREATE MODEL`, `APPLY TAG`) must be granted directly.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [GRANT Policy](/concepts/grant-policies-beta.md)
- [Direct Grant](/concepts/grant-policy-vs-direct-grant.md)
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md)
- SHOW GRANTS
- [SHOW EFFECTIVE POLICIES](/concepts/show-effective-policies.md)
- EXECUTE Privilege

### Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
