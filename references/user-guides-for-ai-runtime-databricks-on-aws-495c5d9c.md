---
title: User guides for AI Runtime | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides
ingestedAt: "2026-06-18T08:09:16.845Z"
---

Public Preview

AI Runtime for single-node tasks is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types). The distributed training API for multi-GPU workloads remain in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

This page includes migration information, links to example notebooks, and troubleshooting information.

## Migrating classic GPU workloads to serverless[​](#migrating-classic-gpu-workloads-to-serverless "Direct link to Migrating classic GPU workloads to serverless")

If you are moving an existing deep learning workload from a classic Databricks cluster (with Databricks Runtime ML) to serverless (with AI Runtime), follow these steps:

1.  **Replace cluster-dependent code.** Remove any references to Spark-based distributed training (for example, `TorchDistributor`) and replace them with the `@distributed` decorator from `serverless_gpu`.
2.  **Update data loading.** Replace direct DBFS paths with Unity Catalog volumes paths (`/Volumes/...`). Replace local Spark DataFrame operations with Spark Connect. For streaming file-based data from volumes, use `UCVolumeDataset` from `serverless_gpu.data`. See [Load data on AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/dataloading).
3.  **Reinstall dependencies.** Do not rely on Databricks Runtime ML pre-installed libraries. Add explicit `%pip install` commands for all required packages.
4.  **Update checkpoint paths.** Move checkpoints from DBFS or local storage to Unity Catalog volumes (`/Volumes/<catalog>/<schema>/<volume>/...`). For distributed checkpointing, use `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data`, which stage I/O through local NVMe. See [Model checkpointing](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability#model-checkpointing).
5.  **Update MLflow configuration.** Ensure experiment names use absolute paths and configure run names so they can be easily restarted.
6.  **Test interactively first.** Validate your workload in an interactive notebook before scheduling it as a job.

## Track usage and costs[​](#track-usage-and-costs "Direct link to Track usage and costs")

You can monitor your AI Runtime GPU spend by querying the billable usage system table (`system.billing.usage`). The following query returns total usage for serverless GPU workloads:

SQL

    SELECT  SUM(usage_quantity)FROM  system.billing.usageWHERE  product_features.serverless_gpu IS NOT NULL

For more information about the billable usage table schema, see [Billable usage system table reference](https://docs.databricks.com/aws/en/admin/system-tables/billing).

AI Runtime charges per GPU hour on the Model Training SKU at the following prices:

*   H100 on demand: $7.00/GPU hour (US East)
*   A10 on demand: $2.50/GPU hour (US East)

## Example notebooks[​](#example-notebooks "Direct link to Example notebooks")

The following categories of example notebooks are available to help you get started:

For the full list, see [AI Runtime example notebooks](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/).

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

Genie Code can help diagnose and suggest fixes for library installation errors. See [Use Genie Code to debug compute environment errors](https://docs.databricks.com/aws/en/compute/troubleshooting/#debug).

The error typically arises when there is a mismatch in the NumPy versions used during the compilation of a dependent package and the NumPy version currently installed in the runtime environment. This incompatibility often occurs due to changes in NumPy's C API and is particularly noticeable from NumPy 1.x to 2.x. This error indicates that the Python package installed in the notebook may have changed the NumPy version.

**Recommended solution:**

Check the NumPy version in the runtime and ensure it is compatible with your packages. See the Serverless GPU Compute release notes for [environment 4](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/four-gpu#installed-libraries) and [environment 3](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/three-gpu#installed-libraries) for information on preinstalled Python libraries. If you have a dependency on a different version of NumPy, add that dependency to your compute environment.

### PyTorch cannot find libcudnn when installing torch[​](#pytorch-cannot-find-libcudnn-when-installing-torch "Direct link to PyTorch cannot find libcudnn when installing torch")

When you install a different version of `torch`, you might see the error: `ImportError: libcudnn.so.9: cannot open shared object file: No such file or directory`. This is because torch only searches for the cuDNN library in the local path.

**Recommended solution:**

Reinstall the dependencies by adding `--force-reinstall` when installing `torch`:

Python

    %pip install torch --force-reinstall
