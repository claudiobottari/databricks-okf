---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b11730ab5a4d8e083186a37301b443e0b9f49c7d28801ce3b7b04422627c1f0c
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-beta-limitations
    - GPBL
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy Beta Limitations
description: "Current Beta constraints: only EXECUTE on models is supported, policies attach at catalog/schema level only, SHOW GRANTS does not reflect policy-granted privileges, and Delta Sharing is incompatible."
tags:
  - unity-catalog
  - beta
  - limitations
timestamp: "2026-06-19T13:50:19.404Z"
---

```markdown
---
title: GRANT Policy Beta Limitations
summary: Current Beta limitations including only EXECUTE privilege on models, no attachment at model level, SHOW GRANTS not reflecting policy grants, no INFORMATION_SCHEMA support, and incompatibility with Delta Sharing.
sources:
  - abac-grant-policies-for-models-beta-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T08:47:57.686Z"
updatedAt: "2026-06-19T08:47:57.686Z"
tags:
  - limitations
  - unity-catalog
  - beta
  - databricks
aliases:
  - grant-policy-beta-limitations
  - GPBL
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# GRANT Policy Beta Limitations

**GRANT Policy Beta Limitations** describes the known restrictions and unsupported features of [[Auditing Direct Grants and ABAC GRANT Policies|ABAC GRANT policies for models|ABAC GRANT policies]] during the Beta phase. These policies dynamically grant `EXECUTE` on models based on governed tags, but the current release is limited in privilege scope, attachment level, and integration with certain Databricks tools. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Overview

ABAC GRANT policies are in Beta on Databricks. During Beta, they can only grant the `EXECUTE` privilege on models, and only when attached at the catalog or schema level. Additional privileges and securable object types are planned for future releases. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

The Beta limitations mean that some access control patterns that work with other ABAC policy types (such as row filters or column masks) are not yet available for GRANT policies. Administrators must understand these limitations to avoid incomplete access configurations. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Specific Limitations

The following limitations apply to GRANT policies in Beta: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- **Privilege scope**: Only `EXECUTE` on models is supported. Privileges like `CREATE MODEL`, `CREATE MODEL VERSION`, and `APPLY TAG` are not covered by GRANT policies and must be granted directly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Prerequisite permissions ignored**: `USE SCHEMA` and `USE CATALOG`—which a user needs to reach a model—are not granted by GRANT policies and must be assigned separately. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Attachment scope**: A policy can only be attached to a catalog or a schema, not directly to a model. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **No visibility in `SHOW GRANTS`**: Privileges granted via a GRANT policy are not returned by the `SHOW GRANTS` command. Administrators must use `SHOW EFFECTIVE POLICIES` to see these grants. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Not included in `INFORMATION_SCHEMA`**: GRANT policies do not appear in the `INFORMATION_SCHEMA` views. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Model deletion not covered**: Deleting a model or a model version is not governed by GRANT policies. See [[Alias-based model lifecycle in Unity Catalog|Manage model lifecycle in Unity Catalog]] for deletion procedures. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Delta Sharing unsupported**: Models that have GRANT policies defined on them cannot be shared via [[Delta Sharing]]. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Policy Quotas

GRANT policies have dedicated quotas that are separate from the quotas for [[row filter and column mask policies]]. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [[ABAC GRANT policies]] – Core concept and usage patterns.
- [[Unity Catalog]] – The governance framework for these policies.
- [[Governed Tags]] – The tag system used in policy conditions.
- [[Row Filters and Column Masks]] – Alternative ABAC policy types with different limitations.

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md
```

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
