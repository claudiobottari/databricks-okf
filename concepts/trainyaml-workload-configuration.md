---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a562cae23028edb22913872ef17046bf86c2a9a9d93b19ea10c7ee4e067372f5
  pageDirectory: concepts
  sources:
    - install-the-ai-runtime-cli-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - trainyaml-workload-configuration
    - TWC
    - YAML workload configuration
  citations:
    - file: filename.md
    - file: source-a.md
    - file: source-b.md
    - file: filename.md:START-END
    - file: filename.md#LSTART-LEND
    - file: install-the-ai-runtime-cli-databricks-on-aws.md
title: train.yaml Workload Configuration
description: A YAML configuration file used with the AI Runtime CLI to define machine learning workloads with inline dependencies.
tags:
  - configuration
  - yaml
  - workloads
timestamp: "2026-06-19T19:10:46.904Z"
---

You are a wiki author. Write a clear, well-structured markdown page about "train.yaml Workload Configuration".
Draw facts only from the provided source material.
Include a ## Sources section at the end listing the source document.
Suggest wikilinks to related concepts where appropriate.
Write in a neutral, informative tone. Be concise but thorough.

Source attribution: at the end of each prose paragraph, append a citation
marker showing which source file(s) the paragraph drew from.
^[filename.md] for single-source, ^[source-a.md, source-b.md] for multi-source.
When a single sentence makes a specific factual claim and you can identify the
exact line range it came from, you may use the claim-level form
^[filename.md:START-END] or ^[filename.md#LSTART-LEND] at the end of that
sentence — START and END are 1-indexed line numbers in the source file.
Paragraph-level citations remain the default; only switch to claim-level form
when it materially improves verifiability and the line range is unambiguous.
Place citations only at the end of prose paragraphs or sentences — not on
headings, list items, or code blocks.
Source filenames are visible as `--- SOURCE: filename.md ---` headers in the content below.

If a paragraph is your inference rather than a direct extraction, leave it
uncited — downstream lint rules will count uncited paragraphs as 'inferred'
to compute the page's provenance metadata.

--- SOURCE: install-the-ai-runtime-cli-databricks-on-aws.md ---

Source document is provided above — content is at the top of this message.

# train.yaml Workload Configuration

**train.yaml** is the primary configuration file format used by the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`) to define machine learning workloads on Databricks. After installing the CLI, users declare workloads, including dependencies and compute specifications, in a `train.yaml` config file. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Purpose

The `train.yaml` file serves as the central definition for training, evaluation, and inference workloads. Rather than specifying arguments and environment details on every command line invocation, users can define a workload once and run it repeatedly with simple CLI commands. The configuration includes details such as the Python environment, resource requirements, and the code to execute. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Usage

After authenticating the CLI against a Databricks workspace, users run workloads defined in `train.yaml` via commands like `air run` or `air list runs`. The file can specify inline dependencies or reference existing environments. ^[install-the-ai-runtime-cli-databricks-on-aws.md]

## Structure

While the full YAML reference documents every available field, the core `train.yaml` structure typically includes:

- **Dependencies**: Python packages required by the workload, specified inline.
- **Compute**: Resource requirements such as GPU type and count.
- **Entry point**: The script or module to execute.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line tool that reads and executes `train.yaml` configurations.
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) — The full specification of all fields available in `train.yaml`.
- Databricks CLI — Provides authentication profiles reused by the AI Runtime CLI.
- [AI Runtime](/concepts/ai-runtime.md) — The ML runtime environment on which workloads run.

## Sources

- install-the-ai-runtime-cli-databricks-on-aws.md

# Citations

1. filename.md
2. source-a.md
3. source-b.md
4. filename.md:START-END
5. filename.md#LSTART-LEND
6. [install-the-ai-runtime-cli-databricks-on-aws.md](/references/install-the-ai-runtime-cli-databricks-on-aws-22b6c9fd.md)
