---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b89f6adb1343cf4bedd0bc77e1b819a39970e02b5771c0434da6e8d72029f2b2
  pageDirectory: concepts
  sources:
    - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-retirement-and-migration-policy
    - Migration Policy and Model Retirement
    - MRAMP
  citations:
    - file: databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
title: Model Retirement and Migration Policy
description: Databricks publishes retirement dates for hosted models with recommended replacement models and migration guidance, including temporary traffic redirection periods.
tags:
  - databricks
  - model-lifecycle
  - operations
timestamp: "2026-06-19T09:52:28.750Z"
---

```yaml
---
title: Model Retirement and Migration Policy
summary: A lifecycle management policy for foundation models where deprecated models are retired on scheduled dates with recommended replacement models and migration guidance provided.
sources:
  - databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:39:29.703Z"
updatedAt: "2026-06-18T11:39:29.703Z"
tags:
  - model-lifecycle
  - governance
  - databricks
aliases:
  - model-retirement-and-migration-policy
  - Migration Policy and Model Retirement
  - MRAMP
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Model Retirement and Migration Policy

The **Model Retirement and Migration Policy** governs the lifecycle for Databricks-hosted foundation models in Foundation Model APIs that are scheduled for deprecation or removal. The policy defines retirement timelines, provides recommended replacement models, and specifies migration procedures to help customers transition smoothly to supported alternatives. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Retirement Announcements

When a model is scheduled for retirement, Databricks publishes a retirement date in the model's documentation. Some models also specify a separate deprecation period during which API calls are temporarily redirected to an alternative model before final removal. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Example: Google Gemini 3 Pro Preview

Google Gemini 3 Pro Preview is scheduled for retirement on March 26, 2026. To allow additional time for migration, between March 26, 2026 and June 7, 2026, API calls to Gemini 3 Pro are temporarily redirected to Gemini 3.1 Pro. The pricing for both models is identical during this period. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

### Example: Meta-Llama-3.1-405B-Instruct

Meta-Llama-3.1-405B-Instruct is scheduled for retirement on different dates depending on the workload type:

- **Pay-per-token workloads**: Starting February 15, 2026
- **Provisioned throughput workloads**: Starting May 15, 2026

^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Currently Retired Models

The following models are listed as retired in the documentation, with recommended replacement models:

| Retired Model | Retirement Date | Recommended Replacement | Migration Guidance |
|---------------|-----------------|------------------------|--------------------|
| OpenAI GPT-5.2 Codex | July 16, 2026 | See retired models documentation | See retired models documentation |
| OpenAI GPT-5.1 Codex Max | July 16, 2026 | See retired models documentation | See retired models documentation |
| OpenAI GPT-5.1 Codex Mini | July 16, 2026 | See retired models documentation | See retired models documentation |
| Google Gemini 3 Pro Preview | March 26, 2026 | Gemini 3.1 Pro Preview (temporary redirect to June 7, 2026) | See retired models documentation |
| Meta-Llama-3.1-405B-Instruct | February 15, 2026 (pay-per-token) / May 15, 2026 (provisioned throughput) | See retired models documentation | See retired models documentation |

^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Migration Procedure

While the specific migration steps depend on the retiring model and its replacement, the general procedure for migrating to a new model involves:

1. **Identify the retirement date** for your current model by reviewing the model's documentation page.
2. **Select a replacement model** from the recommended alternatives listed in the retired models documentation.
3. **Update your application code** to use the new model's endpoint name.
4. **Test the new model** with your workflows to ensure compatibility and performance meet expectations.
5. **Deploy the updated code** before the retirement date to avoid service disruption.

## Pay-per-Token vs. Provisioned Throughput Considerations

The retirement timeline may differ for pay-per-token and provisioned throughput workloads. For example, Meta-Llama-3.1-405B-Instruct has different retirement dates for each workload type, with provisioned throughput customers receiving an extended migration window. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

Additionally, provisioned throughput mode supports all models of a model architecture family, including fine-tuned and custom pre-trained models. This flexibility can simplify migration within the same architecture family when a specific model version is retired. ^[databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md]

## Related Concepts

- [[Foundation Model APIs]] — The API service hosting the supported models
- [[Databricks-hosted foundation models]] — The complete list of currently supported models
- [[Provisioned throughput Foundation Model APIs]] — Provisioned throughput mode for production workloads
- [[Model Serving]] — The serving infrastructure for deploying models
- Retired Models Documentation — The official documentation page for retired models and their replacements
- Compliance with Applicable Model Terms — Customer responsibilities when using foundation models

## Sources

- databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md
```

# Citations

1. [databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws.md](/references/databricks-hosted-foundation-models-available-in-foundation-model-apis-databricks-on-aws-8de78726.md)
