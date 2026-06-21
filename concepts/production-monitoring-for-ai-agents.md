---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6eac9db7fe586c23d993ae4966a0e87682bf5a4e2bbe203754562ae961137235
  pageDirectory: concepts
  sources:
    - evaluate-and-monitor-ai-agents-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - production-monitoring-for-ai-agents
    - PMFAA
    - Production Monitoring for GenAI
    - Production monitoring for GenAI
    - production monitoring for GenAI
  citations:
    - file: evaluate-and-monitor-ai-agents-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Production Monitoring for AI Agents
description: Reusing the same judges and scorers from development in production to maintain consistent evaluation of AI application quality.
tags:
  - mlflow
  - monitoring
  - production
timestamp: "2026-06-18T12:12:38.610Z"
---

# Production Monitoring for AI Agents

**Production Monitoring for AI Agents** refers to the continuous measurement and assessment of AI agent quality, performance, and safety in live production environments. Unlike offline evaluation during development, production monitoring tracks agent behavior on real user interactions, enabling teams to detect regressions, identify quality issues, and maintain consistent performance over time.

## Overview

Production monitoring is a critical component of the AI agent lifecycle in [MLflow GenAI](/concepts/mlflow-3-for-genai.md). It extends the evaluation practices used during development into the production phase, reusing the same [judges](/concepts/llm-judges.md) and [[scorers]] to ensure consistent quality measurement across all stages of the application lifecycle. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

The monitoring component builds upon [MLflow Tracing](/concepts/mlflow-tracing.md), which provides real-time trace logging during production. These production traces can be evaluated using the same [LLM Judges](/concepts/llm-judges.md) and [Custom Judges](/concepts/custom-judges.md) that were developed and validated during offline testing. This consistency ensures that quality criteria defined during development remain applicable in production. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Key Capabilities

### Reuse of Evaluation Artifacts

A central principle of production monitoring is that the same judges and scorers used for offline evaluation can be deployed to production. This eliminates the need to redefine quality criteria or retrain evaluation models between development and production phases. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### Continuous Trace Analysis

Production monitoring leverages [MLflow Tracing](/concepts/mlflow-tracing.md) to continuously capture execution traces from live agent interactions. Each trace includes:

- User inputs (conversation history)
- Agent responses
- Tool invocations and their results
- Intermediate reasoning steps
- Execution timing and metadata

These traces are then scored by deployed judges in near real-time or in batch processing, providing ongoing quality metrics. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### Integration with Human Feedback

Domain experts can provide feedback on production agent outputs using the integrated [Review App](/concepts/mlflow-review-app.md), which supports live app testing for collecting expert annotations. This human feedback produces high-quality evaluation data that can be used for further iteration and improvement of the agent. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Workflow

The production monitoring workflow follows an iterative cycle:

1. **Deploy** the AI agent to production with [MLflow Tracing](/concepts/mlflow-tracing.md) enabled.
2. **Monitor** by continuously collecting traces from live interactions.
3. **Evaluate** production traces using the same judges and scorers defined during development.
4. **Collect feedback** from domain experts through the Review App.
5. **Iterate** by using production insights and human feedback to refine agent behavior, prompts, or tool configurations.
6. **Update** judges and evaluators as needed to align with evolving quality criteria.

This cycle mirrors the development-time evaluation loop but operates on live data, enabling continuous improvement. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Scheduled Scorers

Production monitoring can include scheduled scoring workflows that automatically evaluate agent performance on a regular cadence. These scheduled scorers run judges against production traces or synthetic evaluation sets to provide ongoing quality dashboards. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

**Important:** Scheduled scorers require a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) to be configured on the MLflow experiment. If the default serverless budget policy is disabled and no alternative policy is assigned, scheduled scoring will fail with a 403 PERMISSION_DENIED error. See 403 PERMISSION_DENIED Serverless Budget Policy Error for resolution steps. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Differences Between Development and Production Monitoring

| Aspect | Development Evaluation | Production Monitoring |
|--------|----------------------|----------------------|
| Data source | Synthetic or curated test datasets | Real user interactions |
| Frequency | On-demand, per iteration | Continuous or scheduled |
| Judges | Same as production (reusable) | Same as development (reusable) |
| Feedback loop | Iterative development | Real-time alerts + iterative updates |
| Scale | Small to moderate | Large scale, potentially streaming |

## Best Practices

### Start with Offline Evaluation

Before deploying production monitoring, establish a robust baseline using offline evaluation with representative datasets. Validate that your judges produce reliable scores that align with human expert assessments. See Align judges with human feedback for guidance. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Monitor for Regressions

Production monitoring should detect when agent quality degrades compared to the baseline. Set up alerts for significant drops in key metrics, such as issue resolution rates or adherence to expected behaviors. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### Ensure Budget Policy Configuration

For scheduled monitoring workflows that create serverless workloads, verify that the MLflow experiment has a valid serverless budget policy assigned. Without this, production monitoring tasks may fail silently. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Use A/B Testing in Production

Production monitoring can support [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) by deploying different agent variants to user segments and comparing judge scores across variants. This enables data-driven decisions about configuration changes. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Document the Monitoring Configuration

Record the exact judges, scorers, thresholds, and alerting rules used in production monitoring. This documentation ensures reproducibility and helps teams understand what quality dimensions are being measured. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Example: Production Monitoring Workflow

```python
# Production monitoring configuration (simplified)
import mlflow

# 1. Enable tracing for the production agent
mlflow.genai.tracing.enable()

# 2. Deploy judges for production scoring
# (Judges created during development are reused here)

# 3. Configure scheduled scoring on the experiment
# Serverless budget policy must be set on the experiment
mlflow.set_experiment_tag(
    experiment_id="<production-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<policy-id>",
)

# 4. Production traces are automatically collected and scored
# Human feedback is collected through the Review App
```

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The platform providing evaluation and monitoring capabilities
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Real-time trace logging for development, testing, and production
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers for evaluating agent quality
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing agent variants using consistent judges
- Human Feedback Alignment — Improving judge accuracy with expert annotations
- [Review App](/concepts/mlflow-review-app.md) — Tool for collecting human expert feedback on agent outputs
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Required for scheduled scoring workloads
- 403 PERMISSION_DENIED Serverless Budget Policy Error — Troubleshooting scheduled scorer failures
- [Evaluation Harness](/concepts/evaluation-harness.md) — The offline evaluation framework

## Sources

- evaluate-and-monitor-ai-agents-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [evaluate-and-monitor-ai-agents-databricks-on-aws.md](/references/evaluate-and-monitor-ai-agents-databricks-on-aws-edcafd11.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
3. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
