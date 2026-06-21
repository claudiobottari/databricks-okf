---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5854074ef2db119e6299385eaa4a33e1772ac4837d19a65d50227f5e475dcf5d
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-foundation-model-endpoints
    - DFME
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Databricks Foundation Model Endpoints
description: Databricks-hosted model endpoints accessed via 'databricks:/' URIs for use as evaluation judges
tags:
  - Databricks
  - LLM
  - deployment
timestamp: "2026-06-18T14:27:52.802Z"
---

# Databricks Foundation Model Endpoints

**Databricks Foundation Model Endpoints** are serverless serving endpoints that host Databricks-managed foundation models — including models from providers such as Anthropic, Meta, and Mistral — alongside original Databricks models. These endpoints allow users to perform inference using pre-trained models without provisioning dedicated GPU infrastructure. The endpoints are cataloged under the `system.ai` schema in Unity Catalog and are accessed via SQL or the Databricks SDK. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Scope and Securability

Foundation Model Endpoints are securable objects in Unity Catalog. The principal ability to invoke an endpoint is controlled by the `EXECUTE` privilege. Administrators can grant `EXECUTE` on individual endpoints, or use **ABAC GRANT policies** to dynamically grant `EXECUTE` based on [Governed Tags](/concepts/governed-tags.md). For example, a policy can grant `EXECUTE` on all models bearing the system tag `ai.model_creator = 'anthropic'` without requiring a separate grant for each new model that Databricks adds. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Access Control via ABAC GRANT Policies

Because Foundation Model Endpoints are registered as models in the `system.ai` schema, they are subject to the same ABAC GRANT policy mechanism as customer-registered models. A GRANT policy attached to the `system.ai` schema (or its parent catalog) can selectively grant `EXECUTE` to principals whose role matches a tag condition. The following example grants `EXECUTE` on all Anthropic-hosted foundation models to the `data_scientists` group, excluding `contractors`: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

```sql
CREATE POLICY grant_anthropic_foundation_models
ON SCHEMA system.ai
COMMENT 'Grant EXECUTE on Anthropic foundation models'
TO `data_scientists`
EXCEPT `contractors`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('ai.model_creator', 'anthropic');
```

The equivalent access using direct grants would require one statement per model, reissued as Databricks adds new Anthropic models. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Usage in MLflow GenAI Evaluation

Foundation Model Endpoints are commonly used as the inference target for [Custom Judges](/concepts/custom-judges.md) created with the `make_judge()` API. When defining a judge, the `model` parameter can reference a Databricks foundation model endpoint using the `databricks:/` scheme, for example `databricks:/databricks-gpt-5-mini`. This allows the judge to rate agent outputs by querying the hosted model rather than deploying a separate inference endpoint. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where Foundation Model Endpoints are registered
- [ABAC GRANT Policies](/concepts/abac-grant-policy.md) — Attribute-based policies that dynamically control `EXECUTE` on endpoints
- [Governed Tags](/concepts/governed-tags.md) — Tags used in GRANT policy conditions to scope endpoint access
- [System Tags](/concepts/system-tags.md) — Predefined tags such as `ai.model_creator`
- [Custom Judges](/concepts/custom-judges.md) — LLM-based evaluators that consume foundation model endpoints
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The evaluation and monitoring framework that interacts with endpoints

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
