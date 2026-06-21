---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21382c878a3ef4ec639b91453233974036aeb47370d4ce58f8f3dcbeaf78b8dd
  pageDirectory: concepts
  sources:
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-serverless-gpu-for-deep-learning
    - DSGFDL
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Databricks Serverless GPU for Deep Learning
description: A cloud compute environment on Databricks that provides on-demand GPU acceleration (e.g., 1xA10) for training deep learning models without managing infrastructure.
tags:
  - databricks
  - gpu
  - cloud-computing
  - deep-learning
timestamp: "2026-06-19T10:37:13.730Z"
---

# Databricks Serverless GPU for Deep Learning

**Databricks Serverless GPU for Deep Learning** provides on-demand, clusterless GPU compute for training and inference workloads. It eliminates the need to manage infrastructure — users simply select the Serverless GPU option from the notebook **Connect** dropdown, configure the accelerator and runtime version, and start running deep learning code. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Setting Up Serverless GPU Compute

To use Serverless GPU:

1. Open a notebook and click the **Connect** dropdown.
2. Select **Serverless GPU**.
3. Open the **Environment** side panel.
4. Set **Accelerator** to the desired GPU type (e.g., `1xA10`).
5. Choose an AI runtime version (e.g., **AI v5**).

After configuration, the notebook automatically provisions GPU resources when code execution begins. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Environment Configuration

Deep learning libraries are installed via `%pip` inside the notebook. After installation, the Python environment must be restarted with `dbutils.library.restartPython()` to activate the new packages. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

```python
%pip install -q --upgrade gluonts[torch] wget
dbutils.library.restartPython()
```

For persisting model checkpoints, use a [Unity Catalog](/concepts/unity-catalog.md) volume path. The checkpoint directory is specified as a UC volume path (e.g., `/Volumes/<catalog>/<schema>/<volume>/<model_name>`) and created with `os.makedirs`. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Verifying GPU Resources

Before training, verify GPU availability with standard PyTorch commands:

```python
import torch
assert torch.cuda.is_available(), 'Need GPU compute'
print(f"Number of GPUs: {torch.cuda.device_count()}")
print(f"Total GPU RAM: {torch.cuda.get_device_properties(0).total_memory / (1024**3):.2f} GB")
```

The `nvidia-smi` system command displays GPU hardware details. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Running Deep Learning Workloads

Serverless GPU supports a variety of deep learning frameworks and libraries. A typical workflow is probabilistic time series forecasting using [GluonTS](/concepts/gluonts.md). The notebook example:

- Loads electricity consumption data (15‑minute intervals from 370 clients).
- Resamples to hourly intervals.
- Splits into training and test sets with rolling windows for backtesting.
- Trains a [DeepAR](/concepts/deepar.md) model (a recurrent neural network for probabilistic forecasting).
- Generates predictions with 90% confidence intervals and evaluates metrics (MASE, RMSE, quantile losses).

On a single `1xA10` accelerator, training 10 epochs takes approximately 60 seconds. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

Model checkpoints can be saved after each epoch and later restored to resume training. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Supported Accelerators

Serverless GPU offers multiple accelerator choices. Documented types include `1xA10` (NVIDIA A10 GPU). For the complete list and availability, consult the Supported GPU Types on Databricks documentation. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

For larger workloads, [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) is available across all clouds. A100 GPUs are an efficient choice for training large language models, NLP, object detection, and recommendation engines, but capacity may be limited — contacting the cloud provider for reservation is recommended. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Best Practices

- Use the appropriate accelerator size for the model. Start with a smaller GPU (e.g., A10) for prototyping and scale to A100s for production training.
- Store model artifacts and checkpoints in Unity Catalog volumes for governance and reproducibility.
- Refer to the official Databricks documentation on [serverless GPU compute best practices](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability) and [troubleshooting](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/guides) for optimization tips. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Related Concepts

- [GluonTS](/concepts/gluonts.md) – Probabilistic time series forecasting library
- [DeepAR](/concepts/deepar.md) – Recurrent neural network model for forecasting
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)
- [Unity Catalog](/concepts/unity-catalog.md) – Governance and storage for models and data
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre‑configured runtime with GPU support
- GPU Scheduling – Optimising GPU utilisation for distributed training
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md) – General guidance for workflows

## Sources

- forecasting-time-series-with-gluonts-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
2. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
