---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 90fa8f6d61eeb79c0b09f78f27b5c78fdd33ea5f1a6d584ef8d28f454bbc0f28
  pageDirectory: concepts
  sources:
    - mlflow-3-deep-learning-workflow-databricks-on-aws.md
    - track-and-compare-models-using-mlflow-logged-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-loggedmodel
    - MLflow Logged Models
    - MLflow LoggedModels
    - MLflow search_logged_models
    - Track and Compare Models Using MLflow Logged Models
    - Track and compare models using MLflow Logged Models
  citations:
    - file: track-and-compare-models-using-mlflow-logged-models-databricks-on-aws.md
    - file: mlflow-3-deep-learning-workflow-databricks-on-aws.md
    - file: track-and-compre-models-using-mlflow-logged-models-databricks-on-aws.md
title: MLflow LoggedModel
description: A tracked model artifact in MLflow 3 that represents a specific checkpoint or version of a model, with associated metrics, parameters, and metadata.
tags:
  - mlflow
  - model-tracking
  - deep-learning
timestamp: "2026-06-19T19:36:29.428Z"
---

# MLflow LoggedModel

**MLflow LoggedModel** is a core entity introduced in [MLflow 3](/concepts/mlflow-3.md) that tracks a model’s progress throughout its lifecycle. When you train a model, calling `mlflow.<model-flavor>.log_model()` creates a `LoggedModel` that ties together all critical information — metadata, metrics, parameters, and the code used to generate the model — under a unique ID. The `LoggedModel` object persists across different environments and can be registered to the [Unity Catalog](/concepts/unity-catalog.md) model registry, making information about the model from all MLflow experiments and workspaces available in a single location.^[track-and-compare-models-using-mlflow-logged-models-databricks-on-aws.md]

## Improved tracking for gen AI and deep learning models

Generative AI and deep learning workflows especially benefit from the granular tracking that LoggedModels provides. For **gen AI**, LoggedModels can capture git commits or sets of parameters as dedicated objects that can then be linked to traces and metrics generated during evaluation and deployment, such as reviewer feedback data. For **deep learning**, training creates multiple checkpoints (snapshots of the model’s state at a particular point); MLflow creates a separate `LoggedModel` for each checkpoint, containing the model’s metrics and performance data. This allows efficient comparison and evaluation of checkpoints to identify the best-performing models.^[track-and-compare-models-using-mlflow-logged-models-databricks-on-aws.md]

## Creation

To create a LoggedModel, use the same `log_model()` API that existing MLflow workloads use. The code snippet below shows logging a LangChain agent for a gen AI workflow:

```python
model_info = mlflow.langchain.log_model(
  lc_model=chain,
  name="basic_chain",
  params={
    "temperature": 0.1,
    "max_tokens": 2000,
    "prompt_template": str(prompt)
  },
  model_type="agent",
  input_example={"messages": "What is MLflow?"},
)
logged_model = mlflow.get_logged_model(model_info.model_id)
print(logged_model.model_id, logged_model.params)
```

For deep learning and traditional ML workflows, the same pattern applies: use `mlflow.<flavor>.log_model()` within an [MLflow Run](/concepts/mlflow-run.md). The LoggedModel entity is linked to its name and parameters automatically.^[track-and-compare-models-using-mlflow-logged-models-databricks-on-aws.md]

An end‑to‑end example for deep learning is available in the [MLflow 3 deep learning workflow notebook](/concepts/mlflow-3-deep-learning-workflow.md). It runs a PyTorch training job that logs a checkpoint every 10 epochs, with each checkpoint tracked as a separate LoggedModel. The notebook logs the model accuracy as a metric for each checkpoint.^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

After creating a LoggedModel, you can start an evaluation job and link metrics to it by providing the unique `model_id`:

```python
with mlflow.start_run() as evaluation_run:
  eval_dataset = mlflow.data.from_pandas(df=eval_df, name="eval_dataset")
  result = mlflow.evaluate(
    model=f"models:/{logged_model.model_id}",
    data=eval_dataset,
    model_type="databricks-agent"
  )
  mlflow.log_metrics(
    metrics=result.metrics,
    dataset=eval_dataset,
    model_id=logged_model.model_id
  )
```

^[track-and-compare-models-using-mlflow-logged-models-databricks-on-aws.md]

## View models and track progress

You can view LoggedModels in the workspace UI:

1. Go to the **Experiments** tab in your workspace.
2. Select an experiment.
3. Select the **Models** tab.

This page contains all LoggedModels associated with the experiment, along with their metrics, parameters, and artifacts. You can generate charts to track metrics across models.^[track-and-compare-models-using-mlflow-logged-models-databricks-on-aws.md]

From the **Models** tab, you can register a model version to Unity Catalog by clicking the model name, then the **Register model** button in the upper‑right corner. It can take a few minutes for a model to appear in the UI after registration.^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

### Models tab vs. Catalog Explorer model version page

The **Models** tab on the MLflow experiment page and the model version page in [Catalog Explorer](/concepts/catalog-explorer.md) show similar information but serve different roles:

- The **Models** tab presents the results of logged models from a single experiment on one page. Its Charts tab provides visualizations to help you compare models and select the best versions to register to Unity Catalog for possible deployment.
- The model version page in Catalog Explorer gives an overview of all model performance and evaluation results across linked environments (workspaces, endpoints, experiments). This is useful for monitoring and deployment, especially when used with [deployment jobs](/concepts/mlflow-deployment-jobs.md). The evaluation task in a deployment job creates additional metrics that appear on this page.^[mlflow-3-deep-learning-workflow-databricks-on-aws.md]

## Search and filter Logged Models

You can search and filter LoggedModels in the UI by their attributes, parameters, tags, and metrics. Filters can include dataset‑specific metric performance: only models with matching metric values on the given datasets are returned. If dataset filters are provided without metric filters, models with *any* metrics on those datasets are returned.^[track-and-compre-models-using-mlflow-logged-models-databricks-on-aws.md]

**Filterable attributes:**

- `model_id`
- `model_name`
- `status`
- `artifact_uri`
- `creation_time` (numeric)
- `last_updated_time` (numeric)

**Operators:** For string‑like attributes, parameters, and tags: `=`, `!=`, `IN`, `NOT IN`. For numeric attributes and metrics: `=`, `!=`, `>`, `<`, `>=`, `<=`.

### Search Logged Models programmatically

```python
# Get a LoggedModel by ID
mlflow.get_logged_model(model_id="<my-model-id>")

# Get all accessible LoggedModels
mlflow.search_logged_models()

# Get all with a specific name
mlflow.search_logged_models(filter_string="model_name = '<my-model-name>'")

# Get all created within a time range
mlflow.search_logged_models(
  filter_string="creation_time >= <start> AND creation_time <= <end>"
)

# Get all with a specific param value
mlflow.search_logged_models(filter_string="params.<param_name> = '<param_value>'")

# Get all with specific tag values
mlflow.search_logged_models(
  filter_string="tags.<tag_name> IN ('<value1>', '<value2>')"
)

# Get all with a metric value above a threshold on a specific dataset, ordered
mlflow.search_logged_models(
  filter_string="metrics.<metric_name> >= <metric_value>",
  datasets=[{"dataset_name": "<name>", "dataset_digest": "<digest>"}],
  order_by=[
    {
      "field_name": "metrics.<metric_name>",
      "dataset_name": "<name>",
      "dataset_digest": "<digest>"
    }
  ]
)
```

^[track-and-compare-models-using-mlflow-logged-models-databricks-on-aws.md]

### Search runs by model inputs and outputs

You can search runs that have a particular LoggedModel as an input or output using the model ID:

```python
mlflow.search_runs(filter_string="models.model_id = '<my-model-id>'")
```

^[track-and-compare-models-using-mlflow-logged-models-databricks-on-aws.md]

## Next steps

- [MLflow 3 Deep Learning Workflow](/concepts/mlflow-3-deep-learning-workflow.md) — example notebook showing checkpoint logging.
- [MLflow 3 traditional ML workflow](/concepts/mlflow-3-traditional-ml-workflow.md) — example notebook for classical ML.
- Model Registry improvements with MLflow 3 — details on registering LoggedModels.
- [MLflow 3 Deployment Jobs](/concepts/mlflow-3-deployment-jobs.md) — deploying models with evaluation tasks.

## Sources

- track-and-compare-models-using-mlflow-logged-models-databricks-on-aws.md
- mlflow-3-deep-learning-workflow-databricks-on-aws.md

# Citations

1. [track-and-compare-models-using-mlflow-logged-models-databricks-on-aws.md](/references/track-and-compare-models-using-mlflow-logged-models-databricks-on-aws-232408a8.md)
2. [mlflow-3-deep-learning-workflow-databricks-on-aws.md](/references/mlflow-3-deep-learning-workflow-databricks-on-aws-71fc96e5.md)
3. track-and-compre-models-using-mlflow-logged-models-databricks-on-aws.md
