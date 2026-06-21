---
title: Set up your environment | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/environment
ingestedAt: "2026-06-18T08:08:25.745Z"
---

Public Preview

AI Runtime for single-node tasks is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types). The distributed training API for multi-GPU workloads remain in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

This page describes how to choose and configure a Python environment for AI Runtime, including environment caching behavior, custom module imports, and known limitations.

## What environment to use[​](#what-environment-to-use "Direct link to What environment to use")

AI Runtime offers two managed Python environments, the default base environment and the Databricks AI environment.

You can also use a [workspace base environment](https://docs.databricks.com/aws/en/compute/serverless/dependencies#base-environment) that a workspace admin has built for serverless GPU compute. See [Build for serverless GPU compute (AI Runtime)](https://docs.databricks.com/aws/en/admin/workspace-settings/base-environment#build-for-serverless-gpu-compute-ai-runtime).

### Default base environment (minimal environment)[​](#default-base-environment-minimal-environment "Direct link to default-base-environment-minimal-environment")

A minimal, stable environment containing only the required packages for AI Runtime operation. The environment includes `torch`, `cuda`, and `torchvision`, optimized for compatibility. For specific package versions, use `pip install` or pin necessary versions as needed.

Best for: Users who want full control over their dependency stack and prefer to install only what they need.

This is the default environment when you connect to a serverless GPU via AI Runtime.

For more details about package versions installed in different versions, see the release notes:

*   [GPU environment 5](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/five-gpu#base-environment)
*   [GPU environment 4](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/four-gpu#base-environment)

### Databricks AI environment[​](#databricks-ai-environment "Direct link to databricks-ai-environment")

Available in environment 4 and later. The AI environment is built on top of the default base environment with common runtime packages and packages specific to machine learning on GPUs. Pre-installed packages include:

*   PyTorch (with CUDA support)
*   Transformers (Hugging Face)
*   And additional ML/DL dependencies

Best for: ML practitioners who want a complete environment for training workloads, fine-tuning, and experimentation without manual dependency management.

To select: In the **Environment** side panel, choose **AI v5** or **AI v4** as your base environment.

For more details about package versions installed in different versions, see the release notes:

*   [AI environment 5](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/five-gpu#ai-environment)
*   [AI environment 4](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/four-gpu#ai-environment)

## Workspace base environments[​](#workspace-base-environments "Direct link to Workspace base environments")

A workspace admin can build a [workspace base environment](https://docs.databricks.com/aws/en/admin/workspace-settings/base-environment) for serverless GPU compute, which makes it available to all users in the workspace through the **Base environment** drop-down menu. For details, see [Build for serverless GPU compute (AI Runtime)](https://docs.databricks.com/aws/en/admin/workspace-settings/base-environment#build-for-serverless-gpu-compute-ai-runtime).

You can also configure your deep learning environment per project by starting from one of the provided base environments (default or Databricks AI) and installing additional packages programmatically using `%pip install` within your notebook or at the top of your training script:

Python

    %pip install datasets accelerate peft bitsandbytes

For more details, see [Add dependencies to the notebook](https://docs.databricks.com/aws/en/compute/serverless/dependencies#add-dependencies).

## Behavior[​](#behavior "Direct link to Behavior")

### When are environments cached?[​](#when-are-environments-cached "Direct link to When are environments cached?")

Environments are cached across sessions to speed up startup times. When you reconnect to AI Runtime with the same environment configuration, previously installed packages may be available from cache, reducing setup time.

However, cache behavior is not guaranteed, so always ensure your notebook includes the necessary `%pip install` commands for reproducibility.

### How do I import custom modules?[​](#how-do-i-import-custom-modules "Direct link to How do I import custom modules?")

You can import custom modules by placing them in `/Workspace/Shared` and adding the path to `sys.path`:

Python

    import syssys.path.append("/Workspace/Shared/my-project/src")from my_module import my_function

You can also upload module files as Workspace files and import them directly. For multi-user collaboration, store shared code in `/Workspace/Shared` rather than user-specific folders. For active development, use user-specific folders and push to a remote Git repository for version control.

## Limitations[​](#limitations "Direct link to Limitations")

The following capabilities are not available on AI Runtime:

*   **Spark functions**: You cannot import or use PySpark functions directly. AI Runtime is a Python-only environment; Spark is not available as a local runtime. However, Spark Connect is available for data loading. See [Load data on AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/dataloading).
*   **Databricks Runtime ML libraries**: Pre-installed packages are not a replacement for Databricks Runtime ML. Some ML libraries available in Databricks Runtime ML may not be pre-installed on AI Runtime.
*   **Private artifacts**: AI Runtime does support private artifacts in certain cases. Contact your account team for more details.
