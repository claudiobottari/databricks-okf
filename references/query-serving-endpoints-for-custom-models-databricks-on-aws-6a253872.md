---
title: Query serving endpoints for custom models | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/score-custom-model-endpoints
ingestedAt: "2026-06-18T08:12:44.185Z"
---

In this article, learn how to format scoring requests for your served model, and how to send those requests to the model serving endpoint. The guidance is relevant to serving [custom models](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models), which Databricks defines as traditional ML models or customized Python models packaged in the MLflow format. Register the models in Unity Catalog or in the workspace model registry. Examples include scikit-learn, XGBoost, PyTorch, and Hugging Face transformer models. See [Deploy models using Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) for more information about this functionality and supported model categories.

For query requests for generative AI and LLM workloads, see [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models).

## Requirements[​](#requirements "Direct link to requirements")

*   A [model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).
*   For the MLflow Deployment SDK, MLflow 2.9 or above is required.
*   [Scoring request in an accepted format](#formats).
*   To send a scoring request through the REST API or MLflow Deployment SDK, you must have a Databricks API token.

## Querying methods and examples[​](#querying-methods-and-examples "Direct link to Querying methods and examples")

Model Serving provides the following options for sending scoring requests to served models:

### Pandas DataFrame scoring example[​](#pandas-dataframe-scoring-example "Direct link to Pandas DataFrame scoring example")

The following example assumes a `ENDPOINT_INVOCATION_URL` like `https://<databricks-instance>/serving-endpoints/<endpoint-name>/invocations`, where `<databricks-instance>` is the [name of your Databricks instance](https://docs.databricks.com/aws/en/workspace/workspace-details#workspace-instance-names-urls-and-ids), and a [Databricks REST API token](#required) called `DATABRICKS_API_TOKEN`.

See [Supported scoring formats](#formats).

*   REST API
*   MLflow Deployments SDK
*   PowerBI

Score a model accepting dataframe split input format.

Bash

    curl -X POST -u token:$DATABRICKS_API_TOKEN $ENDPOINT_INVOCATION_URL \  -H 'Content-Type: application/json' \  -d '{"dataframe_split": [{    "columns": ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],    "data": [[5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2]]    }]  }'

Score a model accepting tensor inputs. Tensor inputs should be formatted as described in [TensorFlow Serving's API documentation](https://www.tensorflow.org/tfx/serving/api_rest#request_format_2).

Bash

    curl -X POST -u token:$DATABRICKS_API_TOKEN $ENDPOINT_INVOCATION_URL \  -H 'Content-Type: application/json' \  -d '{"inputs": [[5.1, 3.5, 1.4, 0.2]]}'

### Tensor input example[​](#tensor-input-example "Direct link to Tensor input example")

The following example scores a model accepting tensor inputs. Tensor inputs should be formatted as described in [TensorFlow Serving's API docs](https://www.tensorflow.org/tfx/serving/api_rest#request_format_2). This example assumes a `ENDPOINT_INVOCATION_URL` like `https://<databricks-instance>/serving-endpoints/<endpoint-name>/invocations`, where `<databricks-instance>` is the [name of your Databricks instance](https://docs.databricks.com/aws/en/workspace/workspace-details#workspace-instance-names-urls-and-ids), and a [Databricks REST API token](#required) called `DATABRICKS_API_TOKEN`.

Bash

    curl -X POST -u token:$DATABRICKS_API_TOKEN $ENDPOINT_INVOCATION_URL \    -H 'Content-Type: application/json' \    -d '{"inputs": [[5.1, 3.5, 1.4, 0.2]]}'

## Supported scoring formats[​](#supported-scoring-formats "Direct link to supported-scoring-formats")

For custom models, Model Serving supports scoring requests in Pandas DataFrame or Tensor input.

### Pandas DataFrame[​](#pandas-dataframe "Direct link to Pandas DataFrame")

Requests should be sent by constructing a JSON-serialized Pandas DataFrame with one of the supported keys and a JSON object corresponding to the input format.

*   (Recommended)`dataframe_split` format is a JSON-serialized Pandas DataFrame in the `split` orientation.
    
    JSON
    
        {  "dataframe_split": {    "index": [0, 1],    "columns": ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],    "data": [      [5.1, 3.5, 1.4, 0.2],      [4.9, 3.0, 1.4, 0.2]    ]  }}
    
*   `dataframe_records` is JSON-serialized Pandas DataFrame in the `records` orientation.
    
    note
    
    This format does not guarantee the preservation of column ordering, and the `split` format is preferred over the `records` format.
    
    JSON
    
        {  "dataframe_records": [    {      "sepal length (cm)": 5.1,      "sepal width (cm)": 3.5,      "petal length (cm)": 1.4,      "petal width (cm)": 0.2    },    {      "sepal length (cm)": 4.9,      "sepal width (cm)": 3,      "petal length (cm)": 1.4,      "petal width (cm)": 0.2    },    {      "sepal length (cm)": 4.7,      "sepal width (cm)": 3.2,      "petal length (cm)": 1.3,      "petal width (cm)": 0.2    }  ]}
    

The response from the endpoint contains the output from your model, serialized with JSON, wrapped in a `predictions` key.

JSON

    {  "predictions": [0, 1, 1, 1, 0]}

### Tensor input[​](#tensor-input "Direct link to Tensor input")

When your model expects tensors, like a TensorFlow or Pytorch model, there are two supported format options for sending requests: `instances` and `inputs`.

If you have multiple named tensors per row, then you have to have one of each tensor for every row.

*   `instances` is a tensors-based format that accepts tensors in row format. Use this format if all the input tensors have the same 0-th dimension. Conceptually, each tensor in the instances list could be joined with the other tensors of the same name in the rest of the list to construct the full input tensor for the model, which would only be possible if all of the tensors have the same 0-th dimension.
    
    JSON
    
        { "instances": [1, 2, 3] }
    
    The following example shows how to specify multiple named tensors.
    
    JSON
    
        {  "instances": [    {      "t1": "a",      "t2": [1, 2, 3, 4, 5],      "t3": [        [1, 2],        [3, 4],        [5, 6]      ]    },    {      "t1": "b",      "t2": [6, 7, 8, 9, 10],      "t3": [        [7, 8],        [9, 10],        [11, 12]      ]    }  ]}
    
*   `inputs` send queries with tensors in columnar format. This request is different because there are actually a different number of tensor instances of `t2` (3) than `t1` and `t3`, so it is not possible to represent this input in the `instances` format.
    
    JSON
    
        {  "inputs": {    "t1": ["a", "b"],    "t2": [      [1, 2, 3, 4, 5],      [6, 7, 8, 9, 10]    ],    "t3": [      [        [1, 2],        [3, 4],        [5, 6]      ],      [        [7, 8],        [9, 10],        [11, 12]      ]    ]  }}
    

The response from the endpoint is in the following format.

JSON

    {  "predictions": [0, 1, 1, 1, 0]}

## Notebook example[​](#notebook-example "Direct link to Notebook example")

See the following notebook for an example of how to test your Model Serving endpoint with a Python model:

#### Test Model Serving endpoint notebook

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Monitor served models using Unity AI Gateway\-enabled inference tables](https://docs.databricks.com/aws/en/ai-gateway/inference-tables).
*   [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models).
*   [Debugging guide for Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-debug).
