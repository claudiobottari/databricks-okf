---
title: What is Ray on Databricks? | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ray/
ingestedAt: "2026-06-18T08:12:59.006Z"
---

[Ray](https://docs.ray.io/en/latest/index.html) is an open source framework for scaling Python applications. It includes libraries specific to AI workloads, making it especially suited for developing AI applications. Ray on Databricks lets you run Ray applications while getting all the platform benefits and features of Databricks.

With Ray 2.3.0 and above, you can create Ray clusters and run Ray applications on Apache Spark clusters with Databricks.

For information about getting started with machine learning on Ray, including tutorials and examples, see the [Ray documentation](https://docs.ray.io/en/latest/). For more information about the Ray and Apache Spark integration, see the [Ray on Spark API documentation](https://docs.ray.io/en/latest/cluster/vms/user-guides/community/spark.html#ray-on-spark-apis).

## What is Ray?[​](#what-is-ray "Direct link to What is Ray?")

Ray simplifies distributed systems by providing basic Python primitives to create distributed applications from scratch. For Python developers new to distributed systems, it offers the same ease of use as standard Python while managing orchestration, scheduling, and fault tolerance.

Ray and Apache Spark are complementary frameworks. Ray excels at logical parallelism, handling dynamic, compute-intensive tasks like machine learning and reinforcement learning. Apache Spark specializes in data parallelism, efficiently processing large datasets for tasks like ETL and data analytics. Together, they provide a powerful combination for both data processing and complex computation.

## Why run Ray on Databricks?[​](#why-run-ray-on-databricks "Direct link to why-run-ray-on-databricks")

Running Ray on Databricks allows you to leverage the breadth of the Databricks ecosystem, enhancing data processing and machine learning workflows with services and integrations that are not available in open source Ray. The benefits of running Ray within Databricks include:

*   **Unified platform**: Databricks provides a unified platform where you can run Ray applications alongside Apache Spark. This integration supports seamless data ETL operations, efficient data transfer, and powerful parallel computing within the same compute environment.
*   **Governance and control**: Get the benefits of lineage tracking, data versioning, and access control with Unity Catalog for all your data assets, files, models, and more, ensuring compliance and security.
*   **Infrastructure management**: Utilize infrastructure tools like the Databricks Terraform Provider and Databricks Asset Bundles to manage your clusters and jobs, ensuring streamlined operations and scalability.
*   **Managed Ray clusters**: Ray clusters are managed in the same execution environment as a running Apache Spark cluster. This ensures scalability, reliability, and ease of use without the need for complex infrastructure setup.
*   **Model Serving and monitoring**: Connect models trained with Ray Train to Model Serving for high-availability, low-latency deployments. Additionally, use data profiling to track model prediction quality and drift, ensuring consistent performance.
*   **Enhanced ML development**: Integrate with the fully managed Databricks MLflow service to track your model development, facilitating experiment management and reproducibility across your Ray applications.
*   **Automated workflows**: Use Lakeflow Jobs to automate your processes, creating production-ready pipelines that streamline your operations and reduce manual intervention.
*   **Code management and collaboration**: Manage your code efficiently with Databricks Git folders, enabling seamless Git integration for version control and collaborative development for your Ray application code.
*   **Efficient data access**: Connect Ray applications to Delta Lake, taking advantage of Databricks' wide ecosystem of data integrations to extend Ray's capabilities to a broader range of applications and outputs.

By running Ray on Databricks, you gain access to an integrated ecosystem that enhances your data processing, machine learning, and operational workflows.

## Use cases - machine learning and beyond[​](#use-cases---machine-learning-and-beyond "Direct link to Use cases - machine learning and beyond")

Ray is a versatile tool that extends the capabilities of Python beyond the limitations of DataFrame operations, making it ideal for highly customized and specialized distributed algorithms.

### Machine learning and deep learning[​](#machine-learning-and-deep-learning "Direct link to Machine learning and deep learning")

Leverage Ray's machine learning libraries to enhance your ML workflows:

*   **Hyperparameter tuning**: Optimize model performance with Ray Tune for performant and scalable hyperparameter search.
*   **Distributed deep learning training**: Scale deep learning models across multiple nodes with support for popular frameworks like PyTorch, TensorFlow, HuggingFace, and Keras. Ideal for training models for computer vision or large language models (LLMs).
*   **Traditional machine learning**: Use Ray to distribute training, evaluation, and batch inference for traditional ML models built with popular libraries such as scikit-learn or XGBoost.

### High-Performance Computing (HPC)[​](#high-performance-computing-hpc "Direct link to High-Performance Computing (HPC)")

Ray excels in distributing HPC workloads, making it suitable for:

*   **Mathematical computations**: Perform complex calculations in fields like physics, genomics, or finance using Ray Core for efficient parallel processing.
*   **Time series forecasting**: Scale your forecasting models, running estimates concurrently with forecasting packages such as Prophet or ARIMA.

### Data processing and feature engineering[​](#data-processing-and-feature-engineering "Direct link to Data processing and feature engineering")

Ray can also handle various data processing tasks:

*   **Computed features**: Complex compute-intensive feature engineering tasks can benefit from Ray's distributed computation architecture.
*   **Audio, image, and video processing**: Distribute and accelerate the processing of multimedia data, making it ideal for applications in speech recognition, image classification, and video analysis.

## Limitations[​](#limitations "Direct link to Limitations")

*   Ray on Apache Spark is supported for dedicated access mode, no isolation shared access mode, and jobs clusters only. A Ray cluster cannot be initiated on clusters using serverless-based runtimes. See [Access modes](https://docs.databricks.com/aws/en/compute/configure#access-modes).
*   Avoid running `%pip` to install packages on a running Ray cluster, as it will shut down the cluster. Instead, install libraries before initializing the cluster.
*   Using integrations that override the configuration from `ray.util.spark.setup_ray_cluster` can cause the Ray cluster to become unstable. Avoid over-subscribing Ray cluster resources in 3rd party applications.
*   If you encounter errors like `ncclInternalError: Internal check failed`, this indicates a problem with network communication among GPUs in your cluster. To resolve this error, add the following snippet in your training code to use the primary network interface.

Python

    import osos.environ["NCCL_SOCKET_IFNAME"] = "eth0"

See the other articles in this section.
