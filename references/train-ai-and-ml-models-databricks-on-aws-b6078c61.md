---
title: Train AI and ML models | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/
ingestedAt: "2026-06-18T08:13:16.649Z"
---

Databricks offers flexible compute solutions tailored to different machine learning needs, ranging from managed cluster runtimes to fully serverless GPU environments.

*   *   [AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/)
    *   Serverless GPU compute environment optimized for custom single-node and multi-node deep learning workloads.
*   *   [Databricks Runtime for Machine Learning](https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml)
    *   Classic compute environment with pre-built libraries for classic machine learning and deep learning workloads.

## AI Runtime (Preview)[​](#ai-runtime-preview "Direct link to AI Runtime (Preview)")

[AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/) is a specialized offering within the Databricks serverless ecosystem. It is optimized for custom single-node and multi-node deep learning workloads, such as fine-tuning LLMs or training computer vision models. For an overview of how [serverless compute](https://docs.databricks.com/aws/en/getting-started/high-level-architecture#serverless-compute-plane) fits into the Databricks architecture, see [Serverless workspace architecture](https://docs.databricks.com/aws/en/getting-started/high-level-architecture#serverless-workspace-architecture).

Key features include:

*   **Instant availability**: Removes the need to manage underlying cluster infrastructure, allowing you to connect a notebook directly to serverless GPU resources.
*   **High-performance hardware**: Provides access to A10 GPUs for cost-effective tasks and H100 GPUs for large-scale AI workloads.
*   **Managed environments**: Offers a default base environment for full customization or an AI environment pre-loaded with common ML packages like Transformers and Ray.
*   **Flexible scaling**: Supports distributed training across multiple GPUs and nodes.

## Databricks Runtime for Machine Learning[​](#databricks-runtime-for-machine-learning "Direct link to databricks-runtime-for-machine-learning")

[Databricks Runtime for Machine Learning](https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml) is a specialized runtime that automates the creation of compute resources with pre-built infrastructure. It is designed for users who want a comprehensive, ready-to-use environment for both classic machine learning and deep learning.

Key features include:

*   **Pre-installed libraries**: Includes popular libraries like PyTorch, TensorFlow, and XGBoost, which receive frequent updates and optimized support.
*   **Compute versatility**: Supports both CPU and GPU-based instance types, including AWS Graviton for improved price-to-performance.
*   **Optimization**: Offers integration with Photon to accelerate Spark SQL, DataFrames, and feature engineering tasks.
*   **Access control**: Requires dedicated access mode for secure data access through Unity Catalog.
