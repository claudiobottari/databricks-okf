---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd9be62876a50d904ee4b71b60d4b43d8e52e6402dae2ec3b49c5c10c52bda87
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code-source-snapshot-pattern
    - CSSP
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: Code source snapshot pattern
description: Pattern for uploading local training code to AI Runtime via code_source.snapshot configuration, where $CODE_SOURCE_PATH resolves to the remote upload directory.
tags:
  - databricks
  - code-deployment
  - training
timestamp: "2026-06-19T13:56:49.649Z"
---

```markdown
# Code source snapshot pattern

The **code source snapshot pattern** is a method for defining a code upload strategy in the [[AI Runtime CLI]] [[workload-yaml-configuration|Workload YAML Configuration]]. It tells the CLI to package a local directory—often the project root—and upload it to the remote compute node so that the training script can be executed there. This pattern is the recommended way to supply user code for serverless GPU jobs. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Configuration

To use the snapshot pattern, set the `code_source` block inside the workload YAML file as follows:

```yaml
code_source:
  type: snapshot
  snapshot:
    root_path: .
```

- `type: snapshot` declares the snapshot pattern.
- `snapshot.root_path` specifies the local directory to upload. The value `.` uploads the entire current working directory.

The full YAML config typically also includes an `environment` block with dependencies and a `command` that references the uploaded code. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Behavior

When a workload is submitted with the snapshot pattern, the CLI:

1. Installs the Python dependencies listed in the `environment.dependencies` block.
2. Uploads the directory indicated by `snapshot.root_path` (along with the config file and any supporting files) to the remote serverless GPU node.
3. Resolves the environment variable `$CODE_SOURCE_PATH` to the absolute path of the uploaded code on the remote node.

The user's command (e.g., `python $CODE_SOURCE_PATH/train.py`) is then executed on that node. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Best practices

Databricks recommends using `$CODE_SOURCE_PATH` instead of hardcoding a path to the uploaded code. This ensures portability across different environments and avoids path mismatches. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Related concepts

- [[AI Runtime CLI]] – The command-line interface that consumes the snapshot pattern.
- Workload YAML reference – Full documentation of all configurable fields in the YAML specification.
- [[Serverless Environment Versioning|Serverless GPU environment versions]] – The `environment.version` field used alongside the code source.

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md
```

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
