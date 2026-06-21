---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1225f0294b401c3ad651230ac266fe3eafe1ea1234fdf3871671a6ad679eb9d5
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-governance-for-ml
    - UCGFM
    - Unity Catalog Governance for MLflow
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
    - file: best-practices-for-abac-policies-databricks-on-aws.md
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Unity Catalog Governance for ML
description: Unified governance of data, ML assets, model endpoints, and security across the ML lifecycle via Unity Catalog
tags:
  - governance
  - unity-catalog
  - mlops
timestamp: "2026-06-19T14:22:53.470Z"
---

```yaml
---
title: Unity Catalog Governance for ML
summary: Unified governance of data and ML assets, model endpoints, security, and administration via Unity Catalog, enabling a single governed approach across the ML lifecycle.
sources:
  - abac-grant-policies-for-models-beta-databricks-on-aws.md
  - best-practices-for-abac-policies-databricks-on-aws.md
  - code-based-scorer-reference-databricks-on-aws.md
  - admin-privileges-in-unity-catalog-databricks-on-aws.md
  - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:06:50.635Z"
updatedAt: "2026-06-18T11:06:50.635Z"
tags:
  - governance
  - unity-catalog
  - mlops
aliases:
  - unity-catalog-governance-for-ml
  - UCGFM
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Unity Catalog Governance for ML

**Unity Catalog Governance for ML** refers to the access control, tagging, and administrative mechanisms that Unity Catalog provides to govern machine learning assets, including registered models, model versions, and serving endpoints. These capabilities enable organizations to enforce fine-grained permissions, audit access, and maintain compliance across the ML lifecycle.

## Overview

Unity Catalog extends its governance framework to ML assets by treating models as first-class securable objects. Access is controlled through attribute-based [[ABAC GRANT Policy|ABAC GRANT policies]] that dynamically grant `EXECUTE` privileges based on governed or system tags. Admin roles—[[Account admin (Unity Catalog)|account admins]], [[Metastore Admin Role|metastore admin]]s, and [[Workspace Admin (Unity Catalog)|workspace admin]]s—manage metastores, workspaces, and permissions. Secure evaluation is supported through Databricks secrets accessible in custom scorers. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md, best-practices-for-abac-policies-databricks-on-aws.md, admin-privileges-in-unity-catalog-databricks-on-aws.md, concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Securable Objects for ML

Unity Catalog governs the following ML-related securable objects:

- **Registered models** – customer-registered MLflow Models (Unity Catalog–registered models).
- **Foundation models** – Databricks-hosted models in the `system.ai` schema (e.g., Anthropic, OpenAI, Llama).
- **Model versions** – individual versions of a registered model.
- **Serving endpoints** – real-time and batch inference endpoints managed through [[Model Serving]] and the [[Unity AI Gateway]].

Access to these objects is controlled by privileges such as `EXECUTE`, `CREATE MODEL`, `CREATE MODEL VERSION`, and `APPLY TAG`. Currently, only `EXECUTE` on models is supported by ABAC GRANT policies; other privileges must be granted directly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md, concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## ABAC Policies for Models

Unity Catalog uses **ABAC GRANT policies** (Beta) to dynamically grant `EXECUTE` on models. Unlike static `GRANT` statements that name specific objects, a GRANT policy evaluates a `WHEN` condition against tags on each model in its scope at every access check. Only models whose tags match the condition receive the privilege. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### How GRANT Policies Work

A GRANT policy is defined on a catalog or schema. It specifies:

- `TO` – principals (users or groups) to whom the privilege is granted.
- `EXCEPT` – principals to exclude.
- `GRANT EXECUTE FOR MODELS` – the privilege and securable type.
- `WHEN` – a condition using `has_tag_value()` or custom expressions on [[governed tags]] or [[system tags]].

The effective access on a model is the union of any applicable GRANT policies and any direct grants on the model or its parents. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Example: Production Model Access

```sql
CREATE POLICY grant_production_model_access
ON SCHEMA production.ml_models
COMMENT 'Grant EXECUTE on production MLflow models'
TO `analysts`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('lifecycle', 'production');
```

This policy grants `EXECUTE` only on models tagged `lifecycle = 'production'` in the `production.ml_models` schema. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Example: Foundation Model Access

```sql
CREATE POLICY grant_anthropic_foundation_models
ON SCHEMA system.ai
COMMENT 'Grant EXECUTE on Anthropic foundation models'
TO `data_scientists`
EXCEPT `contractors`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('ai.model_creator', 'anthropic');
```

Every model in `system.ai` with `ai.model_creator = 'anthropic'` automatically inherits the grant. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Admin Roles

Three admin roles govern Unity Catalog and ML assets:

- **Account admin (Unity Catalog)** – operates at the account level; creates and links metastores and workspaces, assigns administrative roles, and manages account-wide settings. Only account admins can assign the [[metastore|Metastore]] admin role. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- **Metastore admin** – manages metadata, ownership, and permissions within a Unity Catalog [[metastore|Metastore]]. Databricks recommends using a group for this role. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- **Workspace admin** – administers a single workspace, subject to restrictions set by the account admin (e.g., via `RestrictWorkspaceAdmins`). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

These roles collectively control the ability to create policies, assign permissions, and manage ML securable objects. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Tagging for ML

Tags are the foundation of ABAC for ML. Two types exist:

- **Governed tags** – customer-defined tags (e.g., `lifecycle`, `sensitivity`) with controlled values. Restricting tag creation and modification to authorized data stewards is essential because tags determine which policies apply. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **System tags** – predefined tags by Databricks (e.g., `ai.model_creator`). These are automatically applied to foundation models. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Taxonomy Best Practices

Use a small, consistent set of tag keys and values. For example, use a single `sensitivity` tag with values `public`, `internal`, `confidential`, `restricted` instead of overlapping tags like `is_sensitive` and `data_class`. Apply default restrictive tags (e.g., `classification: unverified`) to new objects until reviewed. ^[best-practices-for-abac-policies-databricks-on-aws.md]

Tag changes should be audited via the [[Audit Log System Table Requirements|audit log system table]]. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Secrets for Custom Scorers

Custom [[code-based scorers]] used in MLflow GenAI evaluation can securely retrieve credentials from [[Databricks Secret Scopes|Databricks secrets]]. This enables integration with external LLM endpoints (e.g., Azure OpenAI, AWS Bedrock) without hard-coding secrets. To access secrets inside a scorer, import the runtime module:

```python
from databricks.sdk.runtime import dbutils
api_key = dbutils.secrets.get(scope='my-scope', key='api-key')
```

This pattern works for both offline evaluation and production monitoring. ^[code-based-scorer-reference-databricks-on-aws.md]

## Best Practices

- **Scope policies at the highest applicable level** – catalog or schema, not individual models. This reduces policy count and ensures new models are automatically covered if their tags match. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Avoid policy sprawl** – start with a small number of broad policies and consolidate overlapping ones. Large numbers of policies and complex conditions slow authorization checks. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Use groups for `TO` and `EXCEPT`** – manage access by adding or removing group members without editing policies. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Audit both GRANT policies and direct grants** – effective privileges are the union of both. Use `SHOW EFFECTIVE POLICIES` and `SHOW GRANTS` to review. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Apply fallback tagging** – automatically tag unclassified objects with a restrictive default tag and create a policy that blocks access until reviewed. ^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Separate prerequisite permissions** – use direct grants for `USE CATALOG` and `USE SCHEMA`; use GRANT policies only for `EXECUTE` on models. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations

- Only `EXECUTE` on models is supported by GRANT policies. `CREATE MODEL`, `CREATE MODEL VERSION`, and `APPLY TAG` must be granted directly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- GRANT policies cannot be attached directly to models; only to catalogs or schemas. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `USE CATALOG` and `USE SCHEMA` prerequisites are not supported by GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `SHOW GRANTS` does not display privileges from GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Models with GRANT policies cannot be shared via [[Delta Sharing]]. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Deleting models or model versions is not covered by GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `INFORMATION_SCHEMA` does not include GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [[Unity Catalog]] – the unified governance platform
- MLflow Models – model securable objects
- [[ABAC GRANT Policy]] – dynamic privilege grants for models
- [[Governed Tags]] – customer-defined tags used in ABAC conditions
- [[System Tags]] – predefined Databricks tags
- [[Account admin (Unity Catalog)]] – highest-level admin role
- [[Metastore Admin Role|Metastore admin]] – metastore-level administration
- Workspace admin – workspace-level administration
- [[Row Filter Policies]] – content-based ABAC policies for tables
- [[Column Mask Policies]] – mask-based ABAC policies
- [[Code-based scorers]] – custom evaluation functions using secrets
- [[Unity AI Gateway]] – governance for model serving endpoints

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md
- best-practices-for-abac-policies-databricks-on-aws.md
- code-based-scorer-reference-databricks-on-aws.md
- admin-privileges-in-unity-catalog-databricks-on-aws.md
- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
```

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
2. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
3. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
4. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
5. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
