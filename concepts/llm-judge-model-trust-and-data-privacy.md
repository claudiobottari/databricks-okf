---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d21c2b75156968539c3145049f34a4fed2274f8b63e5e420cc96f922f0b24949
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-judge-model-trust-and-data-privacy
    - Data Privacy and LLM Judge Model Trust
    - LJMTADP
    - Data Privacy and Compliance
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: LLM Judge Model Trust and Data Privacy
description: Operational and trust considerations for LLM judges, including third-party model hosting (Azure OpenAI), regional data residency, abuse monitoring opt-out, and restrictions on using judge outputs for model training.
tags:
  - llm-evaluation
  - privacy
  - trust
  - compliance
timestamp: "2026-06-18T14:47:32.899Z"
---

Here is the wiki page for "LLM Judge Model Trust and Data Privacy".

---

## LLM Judge Model Trust and Data Privacy

**LLM Judge Model Trust and Data Privacy** refers to the set of considerations, data handling practices, and governance choices associated with using [Large Language Model (LLM)](/concepts/large-language-models-llms-on-databricks.md)-based judges—such as [Guidelines judges](/concepts/guidelines-llm-judges.md)—to evaluate [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications. It addresses how judge model outputs are handled, where they are processed, and the contractual and privacy implications of using third-party model providers versus customer-hosted models.

### Overview

LLM judges are specialized models used to score the quality of Generative AI outputs against criteria like compliance rules, style/tone, or [factual accuracy](/concepts/correctness-scorer-for-factual-accuracy.md). Because these judges are themselves LLMs, they may process prompts and responses on third-party infrastructure. Understanding which model powers the judge, where that model is hosted, and what data protections apply is essential for Data Governance in regulated environments. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Model Providers

The model used by a judge can be either a **partner-powered model** or a **customer-provided model**.

- **Partner-powered models**: By default, Databricks LLM judges use models from third-party providers such as Azure OpenAI. Databricks has opted out of Microsoft's Abuse Monitoring for Azure OpenAI, so no prompts or responses are stored by the provider for that purpose. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Customer-provided models**: You can specify a custom model by using the `model` argument in the judge definition. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. For Databricks-hosted models, use `databricks` as the provider and the [serving endpoint](/concepts/serving-endpoint-acls.md) name as the model name. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Data Handling

- **Location of processing**: For workspaces in the European Union (EU), LLM judges use models hosted in the EU. All other regions use models hosted in the US. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Abuse monitoring**: For Azure OpenAI, Databricks has opted out of Abuse Monitoring, meaning no prompts or responses are stored with Azure OpenAI. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Disabling partner-powered models**: Disabling [Partner-powered AI features](/concepts/partner-powered-ai-features-on-databricks.md) prevents the LLM judge from calling partner-powered models. You can still use LLM judges by providing your own model. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Usage Restrictions on Judge Outputs

LLM judges are intended to help customers evaluate their GenAI agents and applications. **LLM judge outputs should not be used to train, improve, or fine-tune an LLM.** ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Trust Considerations

- **Transparency**: Because the judge is an LLM, its evaluation decisions are not purely rule-based; they are subject to the same model biases and behavior as the application being evaluated. This means judge outputs require careful review and validation against [Human feedback](/concepts/mlflow-human-feedback-collection.md) for sensitive or high-stakes evaluations. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Auditability**: When using a partner-powered judge, the provider's data storage practices differ from when using a customer-provided model. Choosing a model with a known data handling policy (e.g., a Databricks-hosted model) can simplify audit compliance. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Best Practices

To ensure trust and data privacy when using LLM judges:

1. **Review the provider's data handling policy** before selecting a judge model, especially if your data contains Personally Identifiable Information (PII) or sensitive business data.
2. **Prefer Databricks-hosted models** for workloads where data must not leave the workspace's region or where you require full control over model data storage. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
3. **Disable partner-powered AI features** if your compliance requirements prohibit any third-party processing of your evaluation data. You can still use LLM judges with a custom model. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
4. **Do not use judge outputs for model training.** LLM judge outputs are not intended for training, improving, or fine-tuning an LLM. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Related Concepts

- [Guidelines LLM Judge](/concepts/guidelines-llm-judge.md)
- [LLM Judge](/concepts/llm-judges.md)
- [Custom Judge](/concepts/custom-judges.md)
- Data Governance
- [AI Governance](/concepts/ai-governance.md)
- [Model Serving](/concepts/model-serving.md)
- [Partner-powered AI Features](/concepts/partner-powered-ai-features-on-databricks.md)

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
