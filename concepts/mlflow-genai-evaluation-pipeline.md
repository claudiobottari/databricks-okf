---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 50837fe9803bfedce8431d1b9f1656338b3c63c0e2ad0e690c13a57cf16f91e9
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluation-pipeline
    - MGEP
  citations:
    - file: correctness-judge-databricks-on-aws.md
    - file: code-based-scorer-reference-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: MLflow GenAI Evaluation Pipeline
description: The workflow for evaluating GenAI applications using MLflow, combining evaluation datasets, built-in or custom scorers/judges, and the mlflow.genai.evaluate() function to produce quality assessments.
tags:
  - mlflow
  - genai
  - evaluation
  - pipeline
timestamp: "2026-06-18T11:12:29.935Z"
---

# MLflow GenAI Evaluation Pipeline

The **MLflow GenAI Evaluation Pipeline** is the end-to-end workflow for assessing the quality of generative AI applications within the MLflow ecosystem. It encompasses offline evaluation using built-in or custom judges, production monitoring through registered scorers, and the governance controls needed to secure model access and serverless workloads.^[correctness-judge-databricks-on-aws.md, code-based-scorer-reference-databricks-on-aws.md, configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md, abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Components

### Experiment Setup

Every evaluation begins with an MLflow experiment. The experiment serves as the organizational unit for runs, traces, and results. You must create an experiment and connect your environment to it before running evaluations.^[correctness-judge-databricks-on-aws.md]

### Scorers – Built-in Judges

MLflow provides built-in LLM judges, such as `Correctness`, that compare an application's response against ground‑truth facts. The `Correctness` judge returns a `Feedback` object with a `value` of `"yes"` or `"no"` and a detailed `rationale`. By default, built-in judges use a Databricks-hosted LLM, but you can customize the judge model using the `model` argument with a `provider:/model-name` format (e.g., `databricks:/databricks-gpt-5-mini`).^[correctness-judge-databricks-on-aws.md]

### Scorers – Custom Code-Based Scorers

For domain‑specific evaluation, you can define a code-based scorer using the `@scorer` decorator. The scorer function receives a `Trace` object and returns a `Feedback`. Scorers can securely access Databricks secrets by importing `dbutils` from `databricks.sdk.runtime`. This allows integration with external LLM endpoints (e.g., Azure OpenAI, AWS Bedrock) without hard‑coding credentials.^[code-based-scorer-reference-databricks-on-aws.md]

### Running Offline Evaluation

Use `mlflow.genai.evaluate()` to run a batch evaluation. You provide a dataset with `inputs`, `outputs`, and optional `expectations` (such as `expected_facts` or `expected_response`), and a list of scorers. The function executes each scorer on every example and collects results.^[correctness-judge-databricks-on-aws.md]

## Production Monitoring

After offline validation, you can register a custom scorer with `scorer.register()` and start it with `sampling_config = ScorerSamplingConfig(sample_rate=...)`. This deploys the scorer as a scheduled serverless workload that continuously evaluates production traces. The same secret‑access pattern used in offline evaluation works unchanged in production.^[code-based-scorer-reference-databricks-on-aws.md]

## Security and Governance

### Serverless Budget Policy

Scheduled scorers and other serverless workloads (e.g., synthetic evaluation set generation, agent evaluation) must have a valid serverless budget policy assigned to the MLflow experiment. If the workspace’s default budget policy is disabled and no experiment‑level policy is set, MLflow returns a `403 PERMISSION_DENIED` error. To resolve this, set the `mlflow.workload_creation_policy_id` tag on the experiment, either through the UI or the API (`mlflow.set_experiment_tag()`). Users and service principals must have permission to use the chosen policy.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### ABAC GRANT Policies for Model Access

GRANT policies (Beta) can dynamically grant the `EXECUTE` privilege on MLflow models based on governed tags. This controls which principals can invoke a model during evaluation or production scoring. Policies are attached at the catalog or schema level and can include `TO` and `EXCEPT` clauses. To audit effective access, use `SHOW EFFECTIVE POLICIES` and `SHOW GRANTS`. Best practices include using groups rather than individual users, and avoiding mixing GRANT policies with direct grants for the same privilege.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Tagging Governance

Consistent tagging is critical for both ABAC policies and data classification. Establish a small, controlled vocabulary (e.g., `sensitivity` with values `public`, `internal`, `confidential`) and restrict tag modification to authorized data stewards. Use automation to apply a default restrictive tag (like `classification: unverified`) to new objects until they are reviewed.^[best-practices-for-abac-policies-databricks-on-aws.md]

## Workflow Summary

1. **Create an experiment** and set the serverless budget policy if needed.  
2. **Prepare evaluation data** with inputs, outputs, and expectations.  
3. **Select or build scorers** – use built-in judges like `Correctness` or write custom `@scorer` functions.  
4. **Run offline evaluation** with `mlflow.genai.evaluate()`.  
5. **Register the scorer** for production monitoring.  
6. **Govern model access** with ABAC GRANT policies and secret management.  

## Sources

- correctness-judge-databricks-on-aws.md  
- code-based-scorer-reference-databricks-on-aws.md  
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md  
- abac-grant-policies-for-models-beta-databricks-on-aws.md  
- best-practices-for-abac-policies-databricks-on-aws.md  

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md)  
- [Correctness Judge](/concepts/correctness-judge.md)  
- [Code-based Scorers](/concepts/code-based-scorers.md)  
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md)  
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md)  
- [Governed Tags](/concepts/governed-tags.md)  
- [Production Monitoring](/concepts/production-monitoring.md)

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
2. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
3. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
4. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
5. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
