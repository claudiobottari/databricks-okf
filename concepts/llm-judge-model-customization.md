---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8761db8f5dc911a6e3279325f23776ce5ecf1a81572a221561c77973e4caaad1
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-judge-model-customization
    - LJMC
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: LLM Judge Model Customization
description: The ability to change the underlying model powering a guidelines judge using the model argument with a provider/model-name format compatible with LiteLLM.
tags:
  - mlflow
  - model-configuration
  - litellm
timestamp: "2026-06-18T11:13:57.615Z"
---

# LLM Judge Model Customization

**LLM Judge Model Customization** refers to the ability to specify which underlying language model powers an LLM judge when evaluating GenAI outputs. By default, MLflow LLM judges use a pre-configured model, but you can override this to use a different model that better suits your evaluation needs.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Overview

LLM judges are AI-powered evaluators that assess GenAI application outputs against defined criteria. The judge model is the LLM that performs this evaluation. Customizing the judge model allows you to control the quality, cost, latency, and behavior of the evaluation process.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Specifying a Custom Judge Model

When creating an LLM judge, you can specify a custom model using the `model` argument. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

If you use `databricks` as the model provider, the model name is the same as the serving endpoint name.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Example: Custom Judge Model

```python
from mlflow.genai.scorers import Guidelines

clarity = Guidelines(
    name="clarity",
    guidelines=["The response must be clear, coherent, and concise"],
    model="databricks:/databricks-gpt-oss-120b",  # Custom judge model
)
```

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## When to Customize the Judge Model

Consider customizing the judge model when:

- **Different quality requirements**: Some evaluations may benefit from a more capable (and more expensive) model, while others can use a lighter model for faster, cheaper evaluation.
- **Regional compliance**: For European Union (EU) workspaces, LLM judges use models hosted in the EU. All other regions use models hosted in the US. Custom models can provide additional regional control.^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Partner-powered AI restrictions**: Disabling [Partner-powered AI features](/concepts/partner-powered-ai-features-on-databricks.md) prevents the LLM judge from calling partner-powered models. You can still use LLM judges by providing your own model.^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Trace-based evaluation**: [Trace-based Judges](/concepts/trace-based-judges.md) require a model specification because they analyze execution traces rather than just inputs and outputs.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Default Judge Models

By default, LLM judges use a pre-configured model that may be hosted by Databricks or a third-party provider. LLM judges might use third-party services to evaluate your GenAI applications, including Azure OpenAI operated by Microsoft. For Azure OpenAI, Databricks has opted out of Abuse Monitoring so no prompts or responses are stored with Azure OpenAI.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Considerations

- **Model availability**: The custom model must be deployed and accessible as a serving endpoint.
- **Performance**: Different models have different latency and throughput characteristics.
- **Cost**: More capable models typically incur higher inference costs.
- **Consistency**: Using the same judge model across evaluations ensures consistent scoring. In [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md), deploying the same judges across both runs ensures that differences in scores reflect changes in agent behavior rather than inconsistencies in the evaluation criteria.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers that evaluate agent quality
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [Guidelines LLM Judge](/concepts/guidelines-llm-judge.md) — Pass/fail natural language criteria evaluation
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for deeper quality analysis
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing agent variants with consistent judges
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
