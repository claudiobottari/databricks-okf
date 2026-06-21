---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aac87f8d7f6520acbf3176c4d044efa25d5a8f9aa1b6ebda3a1cd082118083c5
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - config-override-and-dry-run-patterns
    - Dry-Run Patterns and Config Override
    - COADP
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: Config Override and Dry-Run Patterns
description: Common CLI patterns for overriding YAML configuration fields at submission time and validating configurations without actually submitting a job using --dry-run.
tags:
  - databricks
  - cli
  - configuration
  - testing
timestamp: "2026-06-19T22:03:51.233Z"
---

## Config Override and Dry-Run Patterns

**Config Override and Dry-Run Patterns** are two CLI workflow patterns used with the [AI Runtime CLI](/concepts/ai-runtime-cli.md) to validate and modify job configurations before or during submission without needing to edit the YAML file directly. These patterns improve safety, reduce repeat submissions, and simplify iterative tuning of training jobs. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Dry-Run Pattern

The dry-run pattern validates a configuration without actually submitting the workload. It is useful for checking syntax, field correctness, and overall config validity before committing to a run. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Use `--dry-run` with the `air run` command:

```bash
air run --file train.yaml --dry-run
```

This flag evaluates the YAML config, checks that all required fields (e.g., `experiment_name`, `compute`, `command`) are present and correctly structured, but does not start any [MLflow Run](/concepts/mlflow-run.md) or create any cloud resources. The output includes any validation errors or a success message. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Config Override Pattern

The config override pattern lets you change specific fields in the YAML config at the command line without modifying the file. This is useful for adjusting compute resources, timeout limits, or other parameters across different runs. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

Use `--override` with the `air run` command:

```bash
air run --file train.yaml --override compute.num_accelerators=32 timeout_minutes=120
```

The override syntax uses dot-separated paths to reference YAML fields (e.g., `compute.num_accelerators`, `timeout_minutes`). Multiple overrides can be specified in a single command, separated by spaces. Overrides are applied before the config is used for submission. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

### Idempotency Key Pattern (Related)

The `--idempotency-key` flag makes submissions safely retryable by ensuring that if the same key has been used before, the existing run is returned instead of creating a new one. This is related to the dry-run and override patterns as a further safeguard against accidental duplicate submissions. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

```bash
air run --file train.yaml --idempotency-key my-unique-key
```

### Use Cases

- **Dry-run**: Validate YAML config after editing, before submitting a long-running job.
- **Override**: Tune `compute.num_accelerators`, `timeout_minutes`, or other fields without editing the file.
- **Idempotency**: Prevent accidental duplicate submissions when a command is re-run.

### Related Concepts

- [AI Runtime CLI Command Reference](/concepts/ai-runtime-cli-commands.md)
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md)
- [MLflow Experiment](/concepts/mlflow-experiment.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)

### Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
