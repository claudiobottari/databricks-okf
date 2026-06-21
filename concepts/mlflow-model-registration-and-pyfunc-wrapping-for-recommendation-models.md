---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fecddef42b9d94f5ce4176d9fa0be82ecda32fd4b2e7f61b3084859c6cdad479
  pageDirectory: concepts
  sources:
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-model-registration-and-pyfunc-wrapping-for-recommendation-models
    - PyFunc Wrapping for Recommendation Models and MLflow Model Registration
    - MMRAPWFRM
  citations:
    - file: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
title: MLflow Model Registration and PyFunc Wrapping for Recommendation Models
description: Registering a trained two-tower model in MLflow with a PyFunc wrapper to simplify serving by converting dict inputs into prediction lists.
tags:
  - mlflow
  - model-serving
  - mlops
timestamp: "2026-06-19T10:16:46.421Z"
---

# MLflow Model Registration and PyFunc Wrapping for Recommendation Models

**MLflow Model Registration and PyFunc Wrapping** is the process of packaging a trained recommendation model (such as a two‑tower model) into an [MLflow](/concepts/mlflow.md) PyFunc and registering it in a [Unity Catalog](/concepts/unity-catalog.md) schema so that it can be served and used for real‑time inference. This approach transforms the model’s complex internal interface into a simple dictionary‑in / list‑out function, making deployment straightforward. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Why Wrap a Recommendation Model in PyFunc?

Two‑tower recommendation models, especially those built with TorchRec and [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md), expect inputs in a batch dictionary of tensors and return logits. For production serving, a simpler input format is often required – for example, a `Dict[str, List]` containing user IDs and movie IDs, with a `List[float]` as output (e.g., probabilities). The PyFunc wrapper bridges this gap. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Creating a PyFunc Wrapper

A custom Python model class is defined by subclassing `mlflow.pyfunc.PythonModel`. Below is the example `TwoTowerWrapper` from the source notebook:

```python
class TwoTowerWrapper(PythonModel):
    """
    MLflow PythonModel wrapper for TwoTower model that handles
    dictionary input and returns list outputs
    """
    def __init__(self, two_tower_model):
        self.two_tower_model = two_tower_model

    def predict(self, model_input: Dict[str, List]) -> List[float]:
        batch = {key: torch.tensor(value) for key, value in model_input.items()}
        if "label" not in batch:
            batch["label"] = torch.zeros(len(next(iter(batch.values()))))
        with torch.no_grad():
            output = self.two_tower_model(batch).cpu()
        output = torch.sigmoid(output)
        return output.tolist()
```

- The `__init__` method stores the underlying trained two‑tower model.
- The `predict` method converts the incoming dictionary of lists into a tensor batch, runs the model, applies a sigmoid activation, and returns the result as a Python list of floats.
- If the input dictionary does not contain a `"label"` key (as is typical during inference), a dummy label tensor is added to satisfy the model’s forward‑pass signature. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Logging the Model with Signature and Input Example

After defining the wrapper, the model is logged using `mlflow.pyfunc.log_model()`. Before logging, a signature is inferred from a small batch of test data using `mlflow.models.infer_signature()`. This signature documents the expected input schema and output type for serving. An `input_example` can also be provided. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

```python
signature = infer_signature(current_batch, current_output)
logged_model = mlflow.pyfunc.log_model(
    artifact_path="two_tower_pyfunc",
    python_model=pyfunc_two_tower_model,
    signature=signature,
    input_example=current_batch
)
```

## Registering the Model in Unity Catalog

The logged model is then registered in a Unity Catalog using `mlflow.register_model()`. The model is stored at a path of the form `<catalog>.<schema>.<model_name>`:

```python
uc_model_version = mlflow.register_model(
    f"models:/{logged_model.model_id}",
    name=f"{uc_catalog}.{uc_schema}.{model_name}"
)
```

After registration, the model is available in the Unity Catalog registry and can be used for batch inference or deployed to a serving endpoint. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Full Workflow

The typical workflow for a recommendation model trained on Databricks serverless GPU includes:

1. Train the two‑tower model using PyTorch Lightning and the `@distributed` decorator across 8×H100 GPUs.
2. Load the best checkpoint from MLflow (via `mlflow.pytorch.load_model`).
3. Instantiate the PyFunc wrapper with the loaded model.
4. Infer the model signature and log the wrapper model.
5. Register the logged model in Unity Catalog for deployment. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Related Concepts

- MLflow PyFunc – The Python function model flavor used for deployment.
- [Model Registration in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md) – Central model registry for Databricks.
- [Two‑Tower Recommendation Model](/concepts/two-tower-recommendation-model.md) – The underlying architecture.
- TorchRec – Library for large‑scale recommendation models.
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) – Framework for organizing training loops.
- [Serverless GPU Training on Databricks](/concepts/serverless-gpu-training-on-databricks.md) – Infrastructure for distributed GPU training.

## Sources

- distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md

# Citations

1. [distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md](/references/distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws-093d5979.md)
