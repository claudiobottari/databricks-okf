---
title: Best practices for deep learning on Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/dl-best-practices
ingestedAt: "2026-06-18T08:13:25.768Z"
---

This article includes tips for deep learning on Databricks and information about built-in tools and libraries designed to optimize deep learning workloads such as the following:

*   [Delta](https://docs.databricks.com/aws/en/delta/) to load data
*   [Optuna](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/#optuna-overview) to parallelize training
*   [Pandas UDFs](https://docs.databricks.com/aws/en/udf/pandas) for inference

Databricks provides pre-built deep learning infrastructure with Databricks Runtime for Machine Learning, which includes the most common deep learning libraries like TensorFlow, PyTorch, and Keras. It also has built-in, pre-configured GPU support including drivers and supporting libraries.

Databricks Runtime ML also includes all of the capabilities of the Databricks workspace, such as cluster creation and management, library and environment management, code management with Databricks Git folders, automation support including Lakeflow Jobs and APIs, and integrated MLflow for model development tracking and model deployment and serving.

## Resource and environment management[​](#resource-and-environment-management "Direct link to Resource and environment management")

Databricks helps you to both customize your deep learning environment and keep the environment consistent across users.

### Customize the development environment[​](#customize-the-development-environment "Direct link to Customize the development environment")

With Databricks Runtime, you can customize your development environment at the notebook, cluster, and job levels.

*   Use [notebook-scoped Python libraries](https://docs.databricks.com/aws/en/libraries/notebooks-python-libraries) or [notebook-scoped R libraries](https://docs.databricks.com/aws/en/libraries/notebooks-r-libraries) to use a specific set or version of libraries without affecting other cluster users.
*   [Install libraries at the cluster level](https://docs.databricks.com/aws/en/libraries/cluster-libraries) to standardize versions for a team or a project.
*   Set up a Databricks [job](https://docs.databricks.com/aws/en/jobs/) to ensure that a repeated task runs in a consistent, unchanging environment.

### Use cluster policies[​](#use-cluster-policies "Direct link to Use cluster policies")

You can create [cluster policies](https://docs.databricks.com/aws/en/admin/clusters/policies) to guide data scientists to the right choices, such as using a Single Node cluster for development and using an autoscaling cluster for large jobs.

### Consider A100 GPUs for deep learning workloads[​](#consider-a100-gpus-for-deep-learning-workloads "Direct link to Consider A100 GPUs for deep learning workloads")

A100 GPUs are an efficient choice for many deep learning tasks, such as training and tuning large language models, natural language processing, object detection and classification, and recommendation engines.

*   Databricks supports A100 GPUs on all clouds. For the complete list of supported GPU types, see [Supported instance types](https://docs.databricks.com/aws/en/compute/gpu#gpu-list).
*   A100 GPUs usually have limited availability. Contact your cloud provider for resource allocation, or consider reserving capacity in advance.

### GPU scheduling[​](#gpu-scheduling "Direct link to GPU scheduling")

To maximize your GPUs for distributed deep learning training and inference, optimize GPU scheduling. See [GPU scheduling](https://docs.databricks.com/aws/en/compute/gpu#gpu-scheduling).

## Best practices for loading data[​](#best-practices-for-loading-data "Direct link to Best practices for loading data")

Cloud data storage is typically not optimized for I/O, which can be a challenge for deep learning models that require large datasets. Databricks Runtime ML includes [Delta Lake](https://docs.databricks.com/aws/en/delta/) to optimize data throughput for deep learning applications.

Databricks recommends using Delta Lake tables for data storage. Delta Lake simplifies ETL and lets you access data efficiently. Especially for images, Delta Lake helps optimize ingestion for both training and inference. The [reference solution for image applications](https://docs.databricks.com/aws/en/machine-learning/reference-solutions/images-etl-inference) provides an example of optimizing ETL for images using Delta Lake.

For very large datasets that do not fit in memory, use streaming approaches:

*   [PyTorch IterableDataset](https://docs.pytorch.org/docs/stable/data.html#iterable-style-datasets) for custom streaming logic.
*   [Hugging Face datasets](https://huggingface.co/docs/datasets/stream) with streaming for datasets hosted on the Hub or in volumes.
*   [Ray Data](https://docs.ray.io/en/latest/data/data.html) for distributed batch data processing.

## Best practices for training deep learning models[​](#best-practices-for-training-deep-learning-models "Direct link to Best practices for training deep learning models")

Databricks recommends using [Databricks Runtime for Machine Learning](https://docs.databricks.com/aws/en/machine-learning/) and [MLflow tracking](https://docs.databricks.com/aws/en/mlflow/tracking) and [autologging](https://docs.databricks.com/aws/en/mlflow/databricks-autologging) for all model training.

### Start with a Single Node cluster[​](#start-with-a-single-node-cluster "Direct link to Start with a Single Node cluster")

A [Single Node](https://docs.databricks.com/aws/en/compute/configure#single-node) (driver only) [GPU cluster](https://docs.databricks.com/aws/en/compute/gpu) is typically fastest and most cost-effective for deep learning model development. One node with 4 GPUs is likely to be faster for deep learning training that 4 worker nodes with 1 GPU each. This is because distributed training incurs network communication overhead.

A Single Node cluster is a good option during fast, iterative development and for training models on small- to medium-size data. If your dataset is large enough to make training slow on a single machine, consider moving to multi-GPU and even distributed compute.

### Use TensorBoard and cluster metrics to monitor the training process[​](#use-tensorboard-and-cluster-metrics-to-monitor-the-training-process "Direct link to Use TensorBoard and cluster metrics to monitor the training process")

TensorBoard is preinstalled in Databricks Runtime ML. You can use it within a notebook or in a separate tab. See [TensorBoard](https://docs.databricks.com/aws/en/machine-learning/train-model/tensorboard) for details.

Cluster metrics are available in all Databricks runtimes. You can examine network, processor, and memory usage to inspect for bottlenecks. See [cluster metrics](https://docs.databricks.com/aws/en/compute/clusters-manage#metrics) for details.

### Optimize performance for deep learning[​](#optimize-performance-for-deep-learning "Direct link to Optimize performance for deep learning")

You can, and should, use deep learning performance optimization techniques on Databricks.

#### Early stopping[​](#early-stopping "Direct link to Early stopping")

Early stopping monitors the value of a metric calculated on the validation set and stops training when the metric stops improving. This is a better approach than guessing at a good number of epochs to complete. Each deep learning library provides a native API for early stopping; for example, see the EarlyStopping callback APIs for [TensorFlow/Keras](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/EarlyStopping) and for [PyTorch Lightning](https://pytorch-lightning.readthedocs.io/latest/common/early_stopping.html). For an example notebook, see [TensorFlow Keras example notebook](https://docs.databricks.com/aws/en/machine-learning/train-model/tensorflow#tensorflow-keras-example-notebook).

#### Batch size tuning[​](#batch-size-tuning "Direct link to Batch size tuning")

Batch size tuning helps optimize GPU utilization. If the batch size is too small, the calculations cannot fully use the GPU capabilities. You can use [cluster metrics](https://docs.databricks.com/aws/en/compute/clusters-manage#metrics) to view GPU metrics.

Adjust the batch size in conjunction with the learning rate. A good rule of thumb is, when you increase the batch size by n, increase the learning rate by sqrt(n). When tuning manually, try changing batch size by a factor of 2 or 0.5. Then continue tuning to optimize performance, either manually or by testing a variety of hyperparameters using an automated tool like [Optuna](#optuna).

#### Transfer learning[​](#transfer-learning "Direct link to Transfer learning")

With transfer learning, you start with a previously trained model and modify it as needed for your application. Transfer learning can significantly reduce the time required to train and tune a new model. See [Featurization for transfer learning](https://docs.databricks.com/aws/en/machine-learning/preprocess-data/transfer-learning-tensorflow) for more information and an example.

### Move to distributed training[​](#move-to-distributed-training "Direct link to Move to distributed training")

Databricks Runtime ML includes TorchDistributor, DeepSpeed and Ray to facilitate the move from single-node to distributed training.

### TorchDistributor[​](#torchdistributor "Direct link to TorchDistributor")

TorchDistributor is an open-source module in PySpark that facilitates distributed training with PyTorch on Spark clusters, that allows you to launch PyTorch training jobs as Spark jobs. See [Distributed training with TorchDistributor](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/spark-pytorch-distributor).

#### Optuna[​](#optuna "Direct link to Optuna")

[Optuna](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/#optuna-overview) provides adaptive hyperparameter tuning for machine learning.

## Best practices for inference[​](#best-practices-for-inference "Direct link to Best practices for inference")

This section contains general tips about using models for inference with Databricks.

*   To minimize costs, consider both CPUs and inference-optimized GPUs such as the Amazon EC2 G4 and G5 instances. There is no clear recommendation, as the best choice depends on model size, data dimensions, and other variables.

*   Use [MLflow](https://docs.databricks.com/aws/en/mlflow/) to simplify deployment and model serving. MLflow can log any deep learning model, including custom preprocessing and postprocessing logic. [Models in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/) or models registered in the [Workspace Model Registry](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/workspace-model-registry) can be deployed for batch, streaming, or online inference.

### Online serving[​](#online-serving "Direct link to Online serving")

The best option for low-latency serving is online serving behind a REST API. Databricks provides [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) for online inference. Model Serving provides a unified interface to deploy, govern, and query AI models and supports serving the following:

*   [Custom models](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models). These are Python models packaged in the MLflow format. Examples include scikit-learn, XGBoost, PyTorch, and Hugging Face transformer models.
*   State-of-the-art open models made available by [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/). These models are curated foundation model architectures that support optimized inference. For example, base models like Meta-Llama-3.3-70B-Instruct, GTE-Large, and Gemma-3-12B are available for immediate use with **pay-per-token** pricing. For workloads that require performance guarantees and fine-tuned model variants, you can deploy them with **provisioned throughput**.
*   [External models](https://docs.databricks.com/aws/en/generative-ai/external-models/). These are models that are hosted outside of Databricks. For example, generative AI models like, OpenAI's GPT-4, Anthropic's Claude, and others. Endpoints that serve these models can be centrally governed and customers can establish rate limits and access control for them.

Alternatively, MLflow provides [APIs](https://mlflow.org/docs/latest/python_api/index.html) for deploying to various managed services for online inference, as well as [APIs for creating Docker containers](https://mlflow.org/docs/latest/cli.html#mlflow-models-build-docker) for custom serving solutions.

### Batch and streaming inference[​](#batch-and-streaming-inference "Direct link to Batch and streaming inference")

Batch and streaming scoring supports high-throughput, low-cost scoring at latencies as low as minutes. For more information, see [Deploy models for batch inference and prediction](https://docs.databricks.com/aws/en/machine-learning/model-inference/).

*   If you expect to access data for inference more than once, consider creating a preprocessing job to ETL the data into a Delta Lake table before running the inference job. This way, the cost of ingesting and preparing the data is spread across multiple reads of the data. Separating preprocessing from inference also allows you to select different hardware for each job to optimize cost and performance. For example, you might use CPUs for ETL and GPUs for inference.
*   Use [Spark Pandas UDFs](https://docs.databricks.com/aws/en/udf/pandas) to scale batch and streaming inference across a cluster.
    *   When you log a model from Databricks, MLflow automatically provides inference code to [apply the model as a pandas UDF](https://docs.databricks.com/aws/en/mlflow/runs#code-snippets-for-prediction).
    *   You can also optimize your inference pipeline further, especially for large deep learning models. See the [reference solution for image ETL](https://docs.databricks.com/aws/en/machine-learning/reference-solutions/images-etl-inference) for an example.
