---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5eb941f92477a52ee830e27d494ef69c843a188e2244430f3de7e56ff025d85
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-based-and-git-based-code-workflows
    - Git-based Code Workflows and Workspace-based
    - WAGCW
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: Workspace-based and Git-based Code Workflows
description: "Two code workflow modes supported by the AI Runtime CLI: sourcing code from Databricks workspaces or from git repositories."
tags:
  - databricks
  - workflow
  - mlops
timestamp: "2026-06-18T14:21:46.446Z"
---

# Workspace-based and git-based code workflows

**Workspace-based** and **git-based** code workflows are the two supported methods for defining how source code is provided to a workload when using the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`) on Databricks. Both workflows are configured via the `code_source` field in the [Workload YAML reference|workload YAML configuration](/concepts/workload-yaml-configuration.md), and each has distinct trade-offs regarding where code is stored, how it is versioned, and when it is pulled for execution. ^[ai-runtime-cli-databricks-on-aws.md]

## Workspace-based workflows

In a workspace-based workflow, the source code for a workload lives entirely inside the Databricks workspace file system (the Workspace files system). The code is referenced by a workspace path, and the job runs directly from that location without requiring an external git clone. ^[ai-runtime-cli-databricks-on-aws.md]

### Use case

Workspace-based workflows are best suited for users who want to keep their training code alongside their notebooks and other workspace artifacts, or who prefer not to manage a separate git repository for training jobs. The primary advantage is that there is no external repository to configure – the code is always inside the workspace and accessible immediately. ^[ai-runtime-cli-databricks-on-aws.md]

### Configuration

To use a workspace-based code source, set the `code_source` block in your YAML config as follows:

```yaml
code_source:
  type: workspace
  workspace:
    path: /Workspace/Users/me@example.com/my-project/train.py
```

The `path` value points to a file or directory inside the workspace file system. When the job runs, that path is replicated to the compute node and made available at `$CODE_SOURCE_PATH`. ^[ai-runtime-cli-databricks-on-aws.md]

### Best practices

- Use `$CODE_SOURCE_PATH` in your command rather than hard-coding the full workspace path. This makes the config easier to reuse across different workspaces. ^[ai-runtime-cli-databricks-on-aws.md]
- Keep the code source path stable. If you move the file in the workspace, update the YAML config to match. ^[ai-runtime-cli-databricks-on-aws.md]

## Git-based workflows

In a git-based workflow, the source code for a workload is pulled from a remote Git repository at submission time. The YAML config specifies a git repository URL, a branch or tag, and a path within the repository. When the job is submitted, the code is fetched from the specified repository state and made available to the compute node. ^[ai-runtime-cli-databricks-on-aws.md]

### Use case

Git-based workflows are ideal for teams that want to treat training jobs as code – checked into source control, reviewed in pull requests, and deployed from a specific commit or tag. The key benefit is that the exact version of the code that ran is always known from the git reference, and the same repository can be reused across multiple workspaces. ^[ai-runtime-cli-databricks-on-aws.md]

### Configuration

To use a git-based code source, set the `code_source` block in your YAML config as follows:

```yaml
code_source:
  type: git
  git:
    git_url: https://github.com/my-org/my-training-repo.git
    git_provider: github
    git_branch: main
    path: /train.py
```

Required fields: ^[ai-runtime-cli-databricks-on-aws.md]

- `git_url` – The full URL of the remote git repository.
- `git_provider` – The provider of the git repository (e.g., `github`, `gitlab`, `bitbucket_cloud`, `bitbucket_server`, `azure_devops_services`, or `aws_code_commit`).
- `git_branch` – The branch or tag to clone.

Optional fields: ^[ai-runtime-cli-databricks-on-aws.md]

- `path` – A sub-path within the repository to use as the code root. If omitted, the entire repository root is used.

### Authentication

Git-based workflows require authentication to clone the repository. Authentication is handled through the Databricks Git credentials configured in the workspace. If no git credentials are found, the workspace default credentials are used. If no default is configured either, the job fails at submission time. ^[ai-runtime-cli-databricks-on-aws.md]

### Best practices

- Pin to a specific commit or tag rather than a live branch. This ensures repeatable runs that are not affected by later pushes to the branch. ^[ai-runtime-cli-databricks-on-aws.md]
- Use `$CODE_SOURCE_PATH` in your command rather than hard-coding repository paths. ^[ai-runtime-cli-databricks-on-aws.md]

## Comparison

| Aspect | Workspace-based | Git-based |
|---|---|---|
| **Where code lives** | Inside the Databricks workspace | In an external git repository |
| **Version control** | Manual – you manage file versions | Automatic – tied to git commits and tags |
| **Setup** | No additional configuration | Requires git credentials in the workspace |
| **Reproducibility** | Relies on workspace file state | Relies on git ref – exact version always known |
| **Collaboration** | Single user or workspace-scoped | Team-wide – shared across workspaces via git |
| **When code is fetched** | At job start from the workspace | At submission time from the remote repository |

^[ai-runtime-cli-databricks-on-aws.md]

## Choosing a workflow

The right choice depends on how you work: ^[ai-runtime-cli-databricks-on-aws.md]

- **Workspace-based** – Choose this if you are prototyping, iterating quickly, or if your code is primarily notebook-based and you do not want to set up a separate repository.
- **Git-based** – Choose this if you want to treat training jobs as production code, enforce code review, or share code across multiple workspaces and users.

Both workflows are equally supported and can be used side by side in the same project. ^[ai-runtime-cli-databricks-on-aws.md]

## Related concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The CLI that submits and manages training workloads
- Workload YAML reference – Complete YAML configuration reference including all `code_source` options
- [AI Runtime](/concepts/ai-runtime.md) – The serverless GPU compute platform
- Workspace files – The Databricks file system for storing code and data
- Git integration in Databricks – Configuring git providers and credentials in the workspace
- Databricks Git credentials – Authentication for accessing remote git repositories

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
