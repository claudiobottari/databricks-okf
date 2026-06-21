---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 366506b8d5bba0529301253bd11823641e255eb558182b9964da36f8932461cc
  pageDirectory: concepts
  sources:
    - foundation-model-apis-limits-and-quotas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - foundation-model-retirement-and-migration-policy
    - Migration Policy and Foundation Model Retirement
    - FMRAMP
  citations:
    - file: foundation-model-apis-limits-and-quotas-databricks-on-aws.md
title: Foundation Model Retirement and Migration Policy
description: Policies and timelines for retired foundation models including migration guidance and temporary re-routing strategies.
tags:
  - model-retirement
  - migration
  - foundation-models
timestamp: "2026-06-18T12:25:47.749Z"
---

# Foundation Model Retirement and Migration Policy

**Foundation Model Retirement and Migration Policy** refers to Databricks' lifecycle management process for deprecating and removing foundation models from [Foundation Model APIs](/concepts/foundation-model-apis.md). Models reach end-of-life when newer, more capable versions are available or when the underlying model provider discontinues support. The policy provides timelines, replacement guidance, and migration procedures to help users transition between model versions.

## Retirement Timeline and Process

When a foundation model is scheduled for retirement, Databricks announces a deprecation date followed by a final retirement date. During the deprecation period, the model remains available for use. After the retirement date, API calls to the retired model may be temporarily redirected to a recommended replacement, or the model may be fully removed. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

For example, Meta-Llama-3.1-405B-Instruct was retired starting February 15, 2026, and Gemini 3 Pro Preview was retired starting March 26, 2026. To allow additional migration time for Gemini 3 Pro, between March 26, 2026 and June 7, 2026, API calls were temporarily redirected to Gemini 3.1 Pro. The pricing for both models was identical during this period. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Recommended Replacement Models

For each retired model, Databricks documents a recommended replacement model. Users should review the replacement model's capabilities, pricing, and any migration considerations before updating their applications. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Migration Guidance

### Identifying Dependencies

Before migrating, identify all code and configuration that references the retired model. This includes:

- API calls using the model name or endpoint
- [MLflow](/concepts/mlflow.md) model registrations and deployments
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) configurations
- [Production Monitoring](/concepts/production-monitoring.md) schedules

### Updating API Endpoints

Update your application code to point to the replacement model's endpoint. Databricks recommends testing the replacement model with representative workloads before fully transitioning production traffic. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

### Handling Temporary Redirects

When API calls are temporarily redirected to a replacement model (as occurred with Gemini 3 Pro to Gemini 3.1 Pro), Databricks recommends updating your application code to use the replacement model directly to avoid relying on redirection behavior. The model pricing may be identical during the redirection period. ^[foundation-model-apis-limits-and-quotas-databricks-on-aws.md]

## Best Practices

- **Monitor model lifecycle announcements.** Stay informed about upcoming retirements through Databricks release notes and documentation updates.
- **Test replacement models early.** Begin evaluating replacement models during the deprecation period to ensure they meet your quality and performance requirements.
- **Update configuration progressively.** Start by migrating non-production environments, then move to production once testing is complete.
- **Document model versions used.** Maintain records of which foundation model versions your applications depend on, including any version-specific behavior or tuning.
- **Plan for rate limit differences.** Replacement models may have different rate limits for tokens per minute (ITPM, OTPM) and queries per hour. Review the Foundation Model APIs limits and quotas for the replacement model and adjust your application accordingly.

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service that hosts foundation models
- Foundation Model APIs limits and quotas — Rate limits and quotas for pay-per-token and provisioned throughput endpoints
- MLflow Models — Model management and deployment framework
- [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) — Dedicated capacity option for production workloads
- Retired models policy — The formal policy governing model retirement procedures
- Model Serving limits and regions — Additional limits and regional availability information

## Sources

- foundation-model-apis-limits-and-quotas-databricks-on-aws.md

# Citations

1. [foundation-model-apis-limits-and-quotas-databricks-on-aws.md](/references/foundation-model-apis-limits-and-quotas-databricks-on-aws-f7287590.md)
