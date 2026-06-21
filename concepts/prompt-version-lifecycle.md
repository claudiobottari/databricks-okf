---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73657d716e4f1b6859be66afd897afdebf16896f83cbe28a29f9fc5ba940f55e
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - prompt-version-lifecycle
    - PVL
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Prompt Version Lifecycle
description: "The end-to-end workflow for prompt management: creating versions, evaluating against datasets, selecting the best performer, and deploying to production using aliases."
tags:
  - lifecycle
  - deployment
  - genai
timestamp: "2026-06-19T18:41:09.698Z"
---

# Prompt Version Lifecycle

The **Prompt Version Lifecycle** describes the stages a prompt version goes through from creation to production deployment and ongoing monitoring. Managing this lifecycle systematically is essential for building reliable GenAI applications and agents.

## Overview

A prompt version begins as a registered template in the [Prompt Registry](/concepts/prompt-registry.md) and progresses through evaluation, comparison, deployment, and monitoring stages. The lifecycle framework ensures that prompt changes are tracked, tested, and deployed in a controlled manner. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Lifecycle Stages

### 1. Creation and Registration

Each prompt version is created by registering a template in the Prompt Registry with a meaningful commit message. The registry stores the template string, version number, and metadata. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

Best practice is to **start simple** with basic prompts and iteratively improve based on evaluation results. Each registration should include a commit message documenting why changes were made. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### 2. Evaluation

Prompt versions are evaluated using [MLflow's evaluation framework](/concepts/mlflow-genai-evaluation-framework.md) (`mlflow.genai.evaluate()`). Evaluation requires:
- An evaluation dataset containing input examples and expected facts
- One or more [[scorers]] to measure performance
- A prediction function that loads and formats the prompt version

A consistent evaluation dataset should be used across all versions for fair comparison. The dataset should include edge cases and challenging examples. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

Custom [judges](/concepts/llm-judges.md) can be created using `make_judge()` to evaluate specific criteria, such as format compliance or domain-specific requirements. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### 3. Comparison and Selection

Results from evaluation runs are compared across multiple prompt versions using metrics such as:
- Correctness (coverage of expected facts)
- Format compliance (e.g., sentence count requirements)
- Composite scores (weighted combinations of individual metrics)

Composite scoring allows teams to weight different criteria based on application priorities. The best performing version is selected for deployment based on evaluation results. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### 4. Deployment

After selecting the best performing version, it is deployed to production using [aliases in the Prompt Registry](/concepts/prompt-registry.md). Aliases (such as `"production"` or `"staging"`) allow applications to reference a prompt by its logical role rather than a specific version number. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### 5. Production Monitoring

The lifecycle includes continued evaluation after deployment. Prompt degradation should be monitored over time, triggering re-evaluation and potential version updates when performance drops. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Best Practices

| Practice | Description |
|----------|-------------|
| **Start simple** | Begin with basic prompts and iteratively improve based on results |
| **Use consistent datasets** | Evaluate all versions against the same data for fair comparison |
| **Track everything** | Log prompt versions, evaluation results, and deployment decisions |
| **Test edge cases** | Include challenging examples in evaluation datasets |
| **Monitor production** | Continue evaluating after deployment to catch degradation |
| **Document changes** | Use meaningful commit messages for each version |

^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Common Workflow

1. Register a new prompt version with a commit message
2. Build or update the evaluation dataset with expected facts
3. Create or update scorers and judges for relevant criteria
4. Run evaluation against the new version (and existing versions for comparison)
5. Compare metrics across versions using composite scores or individual metrics
6. Select the best performing version and promote it via aliases
7. Deploy the application pointing to the alias
8. Monitor production performance and return to step 1 when degradation is detected

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md)
- [Prompt Version Management](/concepts/prompt-version-management.md)
- [MLflow evaluation harness](/concepts/mlflow-genai-evaluation-harness.md)
- [Scorers and judges](/concepts/scorers-and-llm-judges.md)
- Aliases and deployment
- [GenAI application lifecycle](/concepts/genai-application-evaluation-lifecycle.md)

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
