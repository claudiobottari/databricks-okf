---
title: Workload YAML reference | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/cli/yaml-config
ingestedAt: "2026-06-18T08:08:19.316Z"
---

Beta

The AI Runtime CLI is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

This page is the reference for workload YAML configurations passed to `air run --file`.

note

The ground truth for YAML configuration is the in-CLI help. Run `air -h config` for the top-level view and `air -h config.<section>` (for example, `air -h config.environment`) for per-section detail.

## Minimal configuration[​](#minimal-configuration "Direct link to Minimal configuration")

YAML

    experiment_name: my-trainingenvironment:  dependencies:    - mlflowcompute:  num_accelerators: 1  accelerator_type: GPU_1xA10command: echo "Hello World"

Submit with:

Bash

    air run --file train.yaml -p profile

## Core concepts[​](#core-concepts "Direct link to Core concepts")

### Core fields[​](#core-fields "Direct link to Core fields")

Most training configurations include five components:

1.  `experiment_name`: Required. Creates or appends to an MLflow experiment.
2.  `environment`: Optional. Python dependencies and base environment.
3.  `compute`: Required. GPU resources (type and count).
4.  `command`: Required. The bash command or commands used to launch training.
5.  `code_source`: Optional. Path to your training code, made available remotely.

### Your first training job[​](#your-first-training-job "Direct link to Your first training job")

YAML

    experiment_name: simple-trainingenvironment:  dependencies:    - torch    - transformerscompute:  num_accelerators: 8  accelerator_type: GPU_8xH100code_source:  type: snapshot  snapshot:    root_path: /home/username/repocommand: torchrun --nproc_per_node=8 $CODE_SOURCE_PATH/train.py

In this configuration:

*   `experiment_name` creates an MLflow experiment named `simple-training` (or appends a new run if it already exists).
*   `environment` installs the listed Python dependencies (here, `torch` and `transformers`).
*   `compute` allocates one H100 node (8 H100 GPUs).
*   `code_source` uploads the folder `repo` to the node, available at `$CODE_SOURCE_PATH`.
*   `command` runs `train.py` via `torchrun` across the 8 H100 GPUs. The file lives at `/home/username/repo/train.py` locally.

## Common use cases[​](#common-use-cases "Direct link to Common use cases")

### Add environment variables[​](#add-environment-variables "Direct link to Add environment variables")

YAML

    experiment_name: training-with-envenvironment:  dependencies:    - torch    - transformersenv_variables:  BATCH_SIZE: '32'  LEARNING_RATE: '0.001'compute:  num_accelerators: 8  accelerator_type: GPU_8xH100code_source:  type: snapshot  snapshot:    root_path: /home/username/repo    git:      branch: maincommand: torchrun --nproc_per_node=8 train.py

### Use secrets (API keys, tokens)[​](#use-secrets-api-keys-tokens "Direct link to Use secrets (API keys, tokens)")

YAML

    experiment_name: training-with-secretsenvironment:  dependencies:    - torch    - transformerssecrets:  HF_TOKEN: 'my_scope/hf_token'  WANDB_API_KEY: 'my_scope/wandb'compute:  num_accelerators: 8  accelerator_type: GPU_8xH100code_source:  type: snapshot  snapshot:    root_path: /home/username/repo    git:      branch: maincommand: torchrun --nproc_per_node=8 train.py

Secrets use the format `scope/key` and must be configured in Databricks Secrets. See [Secret management](https://docs.databricks.com/aws/en/security/secrets/) for setup.

When sharing a YAML template, other users must create their own secrets or have access to the referenced secret.

## Python dependencies[​](#python-dependencies "Direct link to Python dependencies")

List your workload's Python dependencies as an inline list under `environment.dependencies`:

YAML

    environment:  version: '4'  dependencies:    - torch    - transformers

`environment.version` selects the [serverless GPU environment version](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/). It is optional and defaults to `"4"`.

### Dependency format[​](#dependency-format "Direct link to Dependency format")

The dependency list follows the [Databricks Base Environment Specification](https://docs.databricks.com/aws/en/admin/workspace-settings/base-environment#example-environment-specification). Each entry is a pip-style package spec (for example, `my-library==6.1`). The list also accepts the following entries:

*   **Requirements files**: a reference to an existing `requirements.txt` using `-r`, for example `-r '/Workspace/Shared/requirements.txt'`. Environment variables such as `$HOME` are expanded.
*   **Wheels**: an absolute path to a `.whl` file, for example `/Workspace/Shared/path/to/simplejson-3.19.3-py3-none-any.whl`.
*   **Index URLs**: an index URL, for example `--index-url https://pypi.org/simple`.

YAML

    environment:  version: '4'  dependencies:    - --index-url https://pypi.org/simple    - -r '/Workspace/Shared/requirements.txt'    - my-library==6.1    - /Workspace/Shared/path/to/simplejson-3.19.3-py3-none-any.whl

### Supported install flags[​](#supported-install-flags "Direct link to Supported install flags")

Dependencies are installed with [uv](https://docs.astral.sh/uv/). The following pip-style flags are supported as list entries:

*   **Applied to the whole install**: `--index-url`, `--extra-index-url`, and `--find-links` (`-f`) set or extend the package indexes.
*   **Applied to the dependency that follows them**: `--no-deps`, `--no-build-isolation`, `--no-cache-dir`, and `--force-reinstall`. Place the flag on its own line (or before the spec), followed by the dependency it applies to.

For example, to install `flash-attn` against the already-installed `torch` (no build isolation) and without resolving its own dependencies:

YAML

    environment:  version: '4'  dependencies:    - torch    - --no-build-isolation    - --no-deps    - flash-attn

note

`--trusted-host` is not supported. Because uv configures trust per index URL, use `--index-url` or `--extra-index-url` instead.

## Work with code sources[​](#work-with-code-sources "Direct link to Work with code sources")

The `code_source` block uploads local code so the training job can run it.

*   `root_path` is the local directory to snapshot. By default, `air` packages the working tree as-is (including any uncommitted changes) as a plain tarball.
*   To snapshot a pinned git version instead, add a `git:` block with a `branch` or `commit`. This requires `root_path` to be a git repository and enables version-aware snapshotting (caching, `git archive`).
*   For large repositories, `include_paths` lets you snapshot a subset.

### Minimal example[​](#minimal-example "Direct link to Minimal example")

YAML

    experiment_name: simple-trainingenvironment:  dependencies:    - torch    - transformerscompute:  num_accelerators: 8  accelerator_type: GPU_8xH100code_source:  type: snapshot  snapshot:    root_path: /home/username/repocommand: python $CODE_SOURCE_PATH/train.py

On the remote machine, the code is placed at `/databricks/code_source/<directory_name>`, where `<directory_name>` is the final path component of `root_path`. `$CODE_SOURCE_PATH` is set to that absolute path — use it in your command rather than hard-coding the location.

### Git repositories: pin by branch or commit[​](#git-repositories-pin-by-branch-or-commit "Direct link to Git repositories: pin by branch or commit")

For git repositories, add a `git:` block to pin the code version by branch or by commit SHA. `branch` and `commit` are mutually exclusive — specify exactly one within the block.

Pin to a branch (uses the local HEAD of that branch):

YAML

    code_source:  type: snapshot  snapshot:    root_path: /home/username/repo    git:      branch: main # Uses local HEAD of main (no remote fetch)command: train.sh

Pin to a commit SHA (exact reproducibility):

YAML

    code_source:  type: snapshot  snapshot:    root_path: /home/username/repo    git:      commit: abc1234567 # Pins specific commitcommand: train.sh

Key fields:

*   `root_path` (Required) — Local path to the root of your git repository.
*   `git.branch` (Optional) — Branch name. Uses local HEAD; no remote fetch. Mutually exclusive with `git.commit`.
*   `git.commit` (Optional) — Specific commit SHA. Mutually exclusive with `git.branch`.
*   `git.remote` (Optional) — Use the branch's remote HEAD instead of the local one. Set to `true` to auto-detect the remote, or to a remote name (for example, `upstream`) to fetch from a specific remote. Only valid with `git.branch`.

If you omit the `git:` block, `air` packages the working tree as a plain tarball, including any uncommitted changes — no extra field is required.

### Non-git directories[​](#non-git-directories "Direct link to Non-git directories")

You can snapshot directories that aren't git repositories. Omit the `git:` block — it requires `root_path` to be a git repository. Without it, there is no version caching; a fresh tarball is uploaded for every run.

YAML

    code_source:  type: snapshot  snapshot:    root_path: /home/username/my_projectcommand: $CODE_SOURCE_PATH/train.py

### Folder filtering with `include_paths`[​](#folder-filtering-with-include_paths "Direct link to folder-filtering-with-include_paths")

For large monorepos, snapshot only specific folders to reduce upload and download time and snapshot size:

YAML

    code_source:  type: snapshot  snapshot:    root_path: /home/username/repo    include_paths:      - research/models      - research/common      - research/configscommand: python $CODE_SOURCE_PATH/research/models/launch_training.py

Key points:

*   The field is optional. If omitted, the entire repository is included by default.
*   Paths must be relative to the repository root (no leading `/`).
*   `..` is not allowed; you cannot reference parent directories.

## Advanced features[​](#advanced-features "Direct link to Advanced features")

### Custom hyperparameters[​](#custom-hyperparameters "Direct link to Custom hyperparameters")

Pass structured configuration to your training script via `HYPERPARAMETERS_PATH`:

YAML

    experiment_name: parameterized-trainingenvironment:  dependencies:    - torch    - transformerscompute:  num_accelerators: 8  accelerator_type: GPU_8xH100code_source:  type: snapshot  snapshot:    root_path: /home/username/repo    git:      branch: maincommand: torchrun --nproc_per_node=8 train.pyparameters:  model:    name: 'gpt2'    hidden_size: 768  training:    batch_size: 32    learning_rate: 0.0001

Read them in your script:

Python

    import osimport yamlwith open(os.environ['HYPERPARAMETERS_PATH']) as f:    params = yaml.safe_load(f)learning_rate = params['training']['learning_rate']model_name = params['model']['name']

### Job reliability[​](#job-reliability "Direct link to Job reliability")

YAML

    experiment_name: reliable-trainingenvironment:  dependencies:    - torch    - transformerscompute:  num_accelerators: 8  accelerator_type: GPU_8xH100code_source:  type: snapshot  snapshot:    root_path: /home/username/repo    git:      branch: maincommand: torchrun --nproc_per_node=8 train.pymax_retries: 2timeout_minutes: 90

If the workload fails, it is retried twice. Each attempt has 90 minutes to complete — the total wall-clock budget is 90 × 3 = 270 minutes.

### Cost attribution[​](#cost-attribution "Direct link to Cost attribution")

Attach a workload to an existing budget policy via `usage_policy_id`. For setup, see [Attribute usage with serverless usage policies](https://docs.databricks.com/aws/en/admin/usage/budget-policies).

YAML

    experiment_name: my-trainingenvironment:  dependencies:    - mlflowcompute:  num_accelerators: 1  accelerator_type: GPU_1xA10command: echo "Hello World"usage_policy_id: abcd123-25b8-3e87-9a2c-f86eb19d101c

## Reference[​](#reference "Direct link to Reference")

### Core fields[​](#core-fields-1 "Direct link to Core fields")

### Supported GPU types[​](#supported-gpu-types "Direct link to Supported GPU types")

For accelerator capabilities and recommended use cases, see [Hardware options](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/#hardware-options).

### Optional fields[​](#optional-fields "Direct link to Optional fields")

**Environment configuration**

YAML

    environment:  version: '4'  dependencies:    - torch    - transformersenv_variables:  BATCH_SIZE: '32'secrets:  HF_TOKEN: 'my_scope/hf_token'

For the dependency format, supported install flags, and `environment.version`, see [Python dependencies](#python-dependencies).

**Code source configuration**

YAML

    code_source:  type: snapshot  snapshot:    root_path: /home/username/repo # REQUIRED — local path to repo or directory    git: # Optional (git repos only) — pin to a branch or commit      branch: main # Branch name; uses local HEAD unless 'remote' is set      # commit: abc1234567 # Mutually exclusive with 'branch'      remote: false # Optional — true to auto-detect remote HEAD, or a remote name string    include_paths: # Optional — filter included paths      - src/      - configs/

Field constraints:

*   `git.branch` and `git.commit` are mutually exclusive — specify exactly one within the `git:` block.
*   `git.remote` requires `git.branch` (it has no effect with `git.commit`).
*   If you omit the `git:` block, the working tree is packaged as a plain tarball, including any uncommitted changes.

**Custom parameters**

Passed to the workload via `HYPERPARAMETERS_PATH`:

YAML

    parameters:  model:    name: 'gpt2'    hidden_size: 768  training:    batch_size: 32

**MLflow run name**

YAML

    mlflow_run_name: 'experiment-001-baseline'

### Path resolution[​](#path-resolution "Direct link to Path resolution")

All paths in the workload YAML are relative to the workload YAML unless they are absolute paths.

Folder structure:

    /home/username/my-project/├── train.yaml└── scripts/    └── train.py

YAML configuration:

YAML

    experiment_name: my-trainingenvironment:  dependencies:    - torch    - transformerscompute:  num_accelerators: 8  accelerator_type: GPU_8xH100code_source:  type: snapshot  snapshot:    root_path: . # Relative to train.yaml    git:      branch: maincommand: torchrun --nproc_per_node=8 $CODE_SOURCE_PATH/scripts/train.py
