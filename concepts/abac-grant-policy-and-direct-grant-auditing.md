---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b64d540ce3db2146af8b534c659b1dc627f1df39ca513e16255980367f66c8f7
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-grant-policy-and-direct-grant-auditing
    - Direct Grant Auditing and ABAC GRANT Policy
    - AGPADGA
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: ABAC GRANT Policy and Direct Grant Auditing
description: Effective privileges on a data object are the union of both direct grants and ABAC GRANT policies, requiring auditors to check both surfaces to avoid hidden unintended permissions.
tags:
  - abac
  - auditing
  - security
timestamp: "2026-06-19T09:08:58.716Z"
---

Here is the wiki page for "ABAC GRANT Policy and Direct Grant Auditing", written based solely on the provided source material.

---

## ABAC GRANT Policy and Direct Grant Auditing

**ABAC GRANT Policy and Direct Grant Auditing** refers to the practice of reviewing both direct privilege grants and [ABAC GRANT Policies](/concepts/abac-grant-policies.md) together to ensure a complete understanding of a user's effective permissions on a data object. Because a user's effective privileges are the union of both mechanisms, auditing only one surface can leave unintended permissions undetected. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Overview

In Unity Catalog, access to data objects can be granted through two distinct mechanisms:

- **Direct grants**: Explicit privileges assigned to a user or group on a specific object (e.g., `GRANT SELECT ON TABLE`).
- **ABAC GRANT policies (Beta)**: Dynamic policies that grant privileges based on tag-based conditions, evaluated at query time.

A user's effective privileges on a data object are the union of both direct grants and ABAC GRANT policies. When reviewing access, it is essential to check both surfaces. Auditing only one can hide unintended permissions. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Auditing Best Practices

- **Audit both surfaces together**: Always review direct grants and ABAC GRANT policies in conjunction. Do not rely on one alone to determine who has access to what. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Use system tables**: Audit tag changes and grant changes regularly using the [audit log system table](/concepts/audit-log-system-table-requirements.md) to track modifications over time. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Document policies and grants**: Maintain clear documentation of which ABAC GRANT policies exist, which tags they reference, and which direct grants are in place. This helps teams understand the full governance model without inspecting each policy individually. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Related Concepts

- [ABAC GRANT policies for models (Beta)](/concepts/abac-grant-policies.md) — The specific ABAC policy type that dynamically grants privileges.
- Direct grants — Explicit privilege assignments on securable objects.
- [Effective privileges](/concepts/effective-privileges-union-model.md) — The combined set of permissions from all grant mechanisms.
- [Audit log system table](/concepts/audit-log-system-table-requirements.md) — System table for tracking governance changes.
- [Governed Tags](/concepts/governed-tags.md) — The attributes used in ABAC policy conditions.

### Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
