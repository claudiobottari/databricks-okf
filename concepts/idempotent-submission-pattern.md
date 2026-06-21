---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a37249d602d81c41e68f1c318884c2d250d8fb6a4eba26339f25625aae5443f7
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idempotent-submission-pattern
    - ISP
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: Idempotent Submission Pattern
description: Using the --idempotency-key flag with air run to safely retry submissions, returning the existing run if the same key was already used instead of creating a duplicate.
tags:
  - databricks
  - reliability
  - pattern
timestamp: "2026-06-19T22:03:21.008Z"
---

```markdown
---
title: Idempotent submission pattern
summary: Using --idempotency-key with air run to make submissions safely retryable, returning the existing run if the same key was previously used.
sources:
  - ai-runtime-cli-quickstart-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T13:57:38.352Z"
updatedAt: "2026-06-19T13:57:38.352Z"
tags:
  - databricks
  - cli
  - reliability
  - best-practice
aliases:
  - idempotent-submission-pattern
  - ISP
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Idempotent Submission Pattern

The **Idempotent submission pattern** ensures that submitting the same workload multiple times produces the same result — only one run is created, and subsequent submissions return the existing run instead of creating duplicates. This pattern is essential for reliable retry behavior in distributed training environments. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## How It Works

When submitting a workload with the AI Runtime CLI (`air`), you provide an **idempotency key** via the `--idempotency-key` flag. The system records this key and associates it with the resulting run. If the same key is used again, the existing run is returned rather than creating a new one. This prevents duplicate runs when automated retries occur. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Usage

```bash
air run --file train.yaml --idempotency-key my-unique-key
```

If `my-unique-key` has been used in a previous submission, the existing run ID is returned. If it is a new key, a fresh run is created and associated with that key. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related Concepts

- [[AI Runtime CLI]] – The command-line tool that implements this pattern.
- [[Workload YAML Configuration]] – The config file submitted with each run.
- Job Orchestration – Automated workflows that benefit from idempotent submission.
- [[MLflow Experiment Tracking]] – The system that captures run metadata; idempotent keys prevent duplicate entries in experiments.

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md
```

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
