---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ff85a1047127baac09676e60e57bfc638705eeb2cb3f165774afe16d33e8999
  pageDirectory: concepts
  sources:
    - evaluate-and-monitor-ai-agents-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-production-monitoring
    - MPM
    - MLflow 3 Production Monitoring
    - MLflow Production Monitoring for GenAI
    - MLflow Model Monitoring
    - MLflow Monitoring
  citations:
    - file: evaluate-and-monitor-ai-agents-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
    - file: |-
        configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md>

        ## Development Lifecycle Integration

        Production monitoring is part of a broader iterative workflow in MLflow 3:

        1. **Development**: Create and tune agents
    - file: define judges and scorers
    - file: |-
        evaluate using the evaluation harness.
        2. **Testing**: Run offline evaluations against curated datasets to validate quality before deployment.
        3. **Production**: Deploy the application with tracing enabled
    - file: apply the same judges and scorers to production traces
    - file: |-
        collect human feedback via the Review App.
        4. **Iteration**: Use insights from production monitoring to improve the agent
    - file: update prompts
    - file: or refine evaluation criteria
    - file: |-
        and begin the cycle again. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md>

        ## Related Concepts

        - [[MLflow GenAI Evaluation Harness|MLflow Evaluation Harness
title: MLflow Production Monitoring
description: Production-phase monitoring system that reuses the same judges and scorers from development evaluation to ensure consistent quality assessment
tags:
  - mlflow
  - monitoring
  - production
timestamp: "2026-06-19T10:23:32.440Z"
---

# MLflow Production Monitoring

**MLflow Production Monitoring** is the capability within [MLflow 3](/concepts/mlflow-3.md) to continuously assess the quality of GenAI agents, LLM applications, RAG systems, and other generative AI applications running in production environments. It enables teams to detect quality degradation, track performance over time, and maintain consistent evaluation standards from development through deployment.

## Overview

Production monitoring in MLflow builds upon [MLflow Tracing](/concepts/mlflow-tracing.md), which provides real-time trace logging across the development, testing, and production phases. While evaluation during development helps validate application quality before deployment, production monitoring provides ongoing assessment of application behavior in live environments. This continuous monitoring allows teams to detect issues such as response quality degradation, increased latency, or changes in user interaction patterns. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## How It Works

### Integration with Development Evaluation

A key design principle of MLflow Production Monitoring is consistency with development evaluation. The same [judges and scorers](/concepts/llm-judges-and-scorers.md) — both built-in and custom — that are used during development and testing can be reused in production monitoring. This ensures that quality metrics are measured consistently throughout the application lifecycle, eliminating discrepancies between pre-deployment evaluation and live monitoring. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### Trace-Based Monitoring

Production monitoring leverages the traces collected by [MLflow Tracing](/concepts/mlflow-tracing.md) during live application usage. Each trace captures the full execution path of an agent or LLM call, including inputs, outputs, intermediate reasoning steps, tool invocations, and their results. By applying judges and scorers to these production traces, MLflow provides ongoing quality assessment without requiring separate test infrastructure. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### Scheduled Scorers

Production monitoring can use scheduled scorers that automatically evaluate traces at defined intervals. These schedulers require a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) to be configured for the experiment to manage compute costs. If the workspace's default budget policy is disabled, a specific policy must be assigned to the experiment to avoid 403 PERMISSION_DENIED Serverless Budget Policy Error. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Key Features

### Reusable Evaluation Criteria

Judges and scorers defined during development can be directly applied to production traces, ensuring that the quality criteria used during testing remain the same in production. This eliminates the need to redefine evaluation logic for production environments. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### Continuous Quality Tracking

Production monitoring enables teams to track quality metrics over time, identify trends, and detect anomalies. By monitoring metrics such as response quality, relevance, safety, and tool call correctness, teams can quickly identify when an application's behavior has changed — for example, after a model update, prompt change, or tool modification. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

### Integration with Human Feedback

MLflow provides an integrated [Review App](/concepts/mlflow-review-app.md) for collecting human feedback on production traces. Domain experts can review agent responses, provide ratings, and annotate issues directly within the MLflow UI. This human feedback produces high-quality evaluation data that can be used for further iteration and improvement of the application. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md]

## Configuration

### Setting Up Production Monitoring

To enable production monitoring for a GenAI application:

1. Ensure [MLflow Tracing](/concepts/mlflow-tracing.md) is enabled for the application to capture production traces.
2. Define the judges and scorers to be used for evaluation, reusing those created during development when possible.
3. Configure scheduled scoring by setting a serverless budget policy on the experiment that manages the application's traces.
4. Deploy the application with the appropriate [MLflow SDK](/concepts/mlflow.md) version (at least `mlflow[databricks]>=3.1`).

### Budget Policy for Scheduled Workloads

For production monitoring workloads that run scheduled scorers, a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) must be assigned to the MLflow experiment. This policy controls resource allocation for serverless execution. If the workspace has disabled the default budget policy, each experiment must have a specific policy assigned. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md>

## Development Lifecycle Integration

Production monitoring is part of a broader iterative workflow in MLflow 3:

1. **Development**: Create and tune agents, define judges and scorers, evaluate using the evaluation harness.
2. **Testing**: Run offline evaluations against curated datasets to validate quality before deployment.
3. **Production**: Deploy the application with tracing enabled, apply the same judges and scorers to production traces, collect human feedback via the Review App.
4. **Iteration**: Use insights from production monitoring to improve the agent, update prompts, or refine evaluation criteria, and begin the cycle again. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md>

## Related Concepts

- [MLflow Evaluation Harness](/concepts/mlflow-genai-evaluation-harness.md) — Offline evaluation during development and testing
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Real-time trace logging across all phases
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers for quality assessment
- make_judge()|Make Judge API — Creating custom evaluation criteria
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing agent variants using shared judges
- Human Feedback and Expert Review — Collecting domain expert feedback for quality improvement
- [Review App](/concepts/mlflow-review-app.md) — UI for human review of production traces
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for deeper quality analysis
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Managing compute costs for production monitoring

## Sources

- evaluate-and-monitor-ai-agents-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [evaluate-and-monitor-ai-agents-databricks-on-aws.md](/references/evaluate-and-monitor-ai-agents-databricks-on-aws-edcafd11.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
3. configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md>

## Development Lifecycle Integration

Production monitoring is part of a broader iterative workflow in MLflow 3:

1. **Development**: Create and tune agents
4. define judges and scorers
5. evaluate using the evaluation harness.
2. **Testing**: Run offline evaluations against curated datasets to validate quality before deployment.
3. **Production**: Deploy the application with tracing enabled
6. apply the same judges and scorers to production traces
7. collect human feedback via the Review App.
4. **Iteration**: Use insights from production monitoring to improve the agent
8. update prompts
9. or refine evaluation criteria
10. and begin the cycle again. ^[evaluate-and-monitor-ai-agents-databricks-on-aws.md>

## Related Concepts

- [[MLflow GenAI Evaluation Harness|MLflow Evaluation Harness
