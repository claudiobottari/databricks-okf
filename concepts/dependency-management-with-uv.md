---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 88d4d5be9f8863809fd32ee030defba780a6c968530165e56a7f40fef92bba69
  pageDirectory: concepts
  sources:
    - workload-yaml-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dependency-management-with-uv
    - DMWU
    - Dependency Management
    - Dependency management
  citations:
    - file: workload-yaml-reference-databricks-on-aws.md
title: Dependency Management with uv
description: Python dependency specification for AI Runtime workloads using `environment.dependencies`, supporting pip-style specs, requirements files, wheels, index URLs, and install flags, all installed via the uv package manager.
tags:
  - dependencies
  - python
  - uv
timestamp: "2026-06-19T23:27:45.834Z"
---

# Dependency Management with uv

**Dependency Management with uv** refers to the use of [uv](https://docs.astral.sh/uv/), a fast Python package installer and resolver, as the underlying tool for installing Python dependencies in [AI Runtime CLI](/concepts/ai-runtime-cli.md) workloads on Databricks. When a workload YAML specifies Python dependencies, the system uses uv to perform the installation rather than pip. ^[workload-yaml-reference-databricks-on-aws.md]

## How uv Is Used

In the [Workload YAML reference|workload YAML configuration](/concepts/workload-yaml-configuration.md), dependencies are declared under `environment.dependencies` as an inline list. These dependencies are installed using uv when the workload is submitted. Users do not need to install or configure uv themselves; it is the default package installer in the [AI Runtime CLI](/concepts/ai-runtime-cli.md) environment. ^[workload-yaml-reference-databricks-on-aws.md]

```yaml
environment:
  version: '4'
  dependencies:
    - torch
    - transformers
```

## Supported Dependency Formats

The dependency list follows the Databricks Base Environment Specification. Each entry is a pip-style package specifier (for example, `my-library==6.1`). The following entry types are supported: ^[workload-yaml-reference-databricks-on-aws.md]

- **Package specifications**: Standard pip-style package names with optional version constraints, such as `torch` or `transformers>=4.0`.
- **Requirements files**: A reference to an existing `requirements.txt` file using the `-r` flag, for example `-r '/Workspace/Shared/requirements.txt'`. Environment variables such as `$HOME` are expanded.
- **Wheels**: An absolute path to a `.whl` file, for example `/Workspace/Shared/path/to/simplejson-3.19.3-py3-none-any.whl`.
- **Index URLs**: A custom package index URL using `--index-url`, for example `--index-url https://pypi.org/simple`.

```yaml
environment:
  version: '4'
  dependencies:
    - --index-url https://pypi.org/simple
    - -r '/Workspace/Shared/requirements.txt'
    - my-library==6.1
    - /Workspace/Shared/path/to/simplejson-3.19.3-py3-none-any.whl
```

^[workload-yaml-reference-databricks-on-aws.md]

## Supported Install Flags

uv supports several pip-style install flags that can be included as list entries in the dependencies section: ^[workload-yaml-reference-databricks-on-aws.md]

**Flags applied to the whole install:**
- `--index-url` — Set the primary package index URL
- `--extra-index-url` — Add an additional package index URL
- `--find-links` (`-f`) — Specify a directory or URL to search for packages

**Flags applied to the dependency that follows them:**
- `--no-deps` — Do not install package dependencies
- `--no-build-isolation` — Install against the already-installed environment (do not isolate builds)
- `--no-cache-dir` — Do not use cache
- `--force-reinstall` — Force reinstallation of packages

For example, to install `flash-attn` against the already-installed `torch` without build isolation or dependency resolution: ^[workload-yaml-reference-databricks-on-aws.md]

```yaml
environment:
  version: '4'
  dependencies:
    - torch
    - --no-build-isolation
    - --no-deps
    - flash-attn
```

## Unsupported Flags

The `--trusted-host` flag is not supported with uv. Because uv configures trust per index URL, users should use `--index-url` or `--extra-index-url` instead to specify trusted package sources. ^[workload-yaml-reference-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line interface for managing serverless GPU workloads on Databricks
- Workload YAML reference — Complete reference for [Workload YAML Configuration](/concepts/workload-yaml-configuration.md)
- Python dependencies — How dependencies are specified in Databricks environments
- Databricks Base Environment Specification — The specification governing environment definitions
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute infrastructure for running GPU workloads

## Sources

- workload-yaml-reference-databricks-on-aws.md

# Citations

1. [workload-yaml-reference-databricks-on-aws.md](/references/workload-yaml-reference-databricks-on-aws-d459ba00.md)
