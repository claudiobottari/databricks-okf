---
title: Debug model serving timeouts | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-timeouts
ingestedAt: "2026-06-18T08:12:16.590Z"
---

This article describes the different timeouts you might encounter when using model serving endpoints and how to handle them. It covers model deployment timeouts, server-side timeouts, and client-side timeouts.

## Model deployment timeouts[​](#model-deployment-timeouts "Direct link to Model deployment timeouts")

When you deploy a model or update an existing deployment using Model Serving, the process might time out for a number of reasons. The **Events** tab of the model serving endpoint page records timeout messages. Search on **_"timed out"_** to find them.

note

The deployment process times out if the container build and model deployment exceed a certain duration that is dependent on the endpoint workload configuration. Check your configuration before deploying and compare it to previous successful deployments.

The container build has no hard limit, but retries up to 3 times. The deployment after the container is built will wait up to 30 minutes for CPU workloads, 60 minutes for GPU small or medium workloads, and 120 minutes for GPU large workloads before timing out.

![Model Serving Endpoint Events Tab](https://docs.databricks.com/aws/en/assets/images/model-serving-endpoint-events-tab-de9ed173c876cf1f950996697b33ce4b.png)

If you find a **"timed out"** message, navigate to the **Logs** tab and examine the build logs to determine the cause. Examples include library dependency issues, resource constraints, configuration issues and so on.

![Model Serving Endpoint Build Logs](https://docs.databricks.com/aws/en/assets/images/model-serving-endpoint-build-logs-01cec0c5ea01909dc30c965c950385ba.png)

See [Debug after container build failure](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-debug#build-fail).

## Server-side timeouts[​](#server-side-timeouts "Direct link to Server-side timeouts")

If your endpoint is healthy according to the **Events** and **Logs** tabs of your serving endpoint, but you experience timeouts when you make calls to the endpoint, the timeout might be on the server-side. The default timeout varies depending on the type of model serving endpoint. The following table shows the default server-side timeouts for requests sent to model serving endpoints.

To determine if you experienced a server-side timeout, see if your requests are timing out before or after the limits listed above.

*   If your request consistently fails at the limit, then it's likely a server-side timeout.
*   If your request fails earlier than the limit, it might be due to configuration issues.
    *   Check the service logs to determine if there are any other errors.
    *   Confirm that the model has worked locally, like from a notebook, or on previous requests on earlier versions.

## Client-side timeouts: MLflow configuration[​](#client-side-timeouts-mlflow-configuration "Direct link to Client-side timeouts: MLflow configuration")

Client-side timeouts typically return error messages that say **_"timed out"_** or **4xx Bad Request**. Common causes of these timeouts are from MLflow environment variables configurations. The following are the most common MLflow environment variables for timeouts. For the full list of timeout variables, see the [mlflow.environment\_variables documentation](https://mlflow.org/docs/latest/python_api/mlflow.environment_variables.html).

*   **MLFLOW\_HTTP\_REQUEST\_TIMEOUT**: Specifies the timeout in seconds for MLflow HTTP requests. Default timeout 120 seconds.
*   **MLFLOW\_HTTP\_REQUEST\_MAX\_RETRIES**: Specifies the maximum number of retries with exponential backoff for MLflow HTTP requests. Default is 7 seconds.

note

The HTTP request timeouts on the client-side are set to 120 seconds, which differs from the server-side's default timeout of 597 seconds for CPU and GPU serving endpoints. Adjust the MLflow environment variables accordingly if you expect your workload to exceed the 120-second client side timeout.

Do either of the following to determine if a timeout is caused by an MLflow environment variable configuration:

*   Test the model locally using sample inputs, like in a notebook, to confirm that it works as expected before you register the model and deploy it.
    *   Examine the time it takes to process the requests.
        *   If requests take longer than the default timeouts for MLflow environment variables or you get a **_"timed out"_** message in the notebook. Example **_"timed out"_** message:
        *   `Timed out while evaluating the model. Verify that the model evaluates within the timeout.`
*   Test the model serving endpoint using POST requests.
    *   Check the **Service Logs** for your endpoint or the inference tables if you enabled them.
        *   For inference table schema details, see [Unity AI Gateway\-enabled inference table schema](https://docs.databricks.com/aws/en/ai-gateway/inference-tables#schema).

### Configure MLflow environment variables[​](#configure-mlflow-environment-variables "Direct link to Configure MLflow environment variables")

Configure MLflow environment variables using the Serving UI or programmatically using Python.

*   Serving UI
*   Python

You can configure environment variables for a model deployment

1.  Select the endpoint that you want to configure an environment variable for.
2.  On the endpoint's page, select **Edit** on the top right.
3.  In **"Entity Details"**, expand **Advanced configuration** to add the relevant MLflow timeout environment variable.

See [Add plain text environment variables](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving#plain-text).

## Client-side timeouts: Third party client APIs[​](#client-side-timeouts-third-party-client-apis "Direct link to Client-side timeouts: Third party client APIs")

Client-side timeouts typically return error messages that say **_"timed out"_** or **4xx Bad Request**. Similar to MLflow configurations, third party client APIs can cause client-side timeouts depending on their configuration. These can impact model serving endpoints that consist of pipelines that use these third party client APIs. See [custom PyFunc models](https://docs.databricks.com/aws/en/machine-learning/model-serving/deploy-custom-python-code) and [PyFunc custom schema agents](https://docs.databricks.com/aws/en/generative-ai/agent-framework/author-agent-model-serving#custom-schema).

Similar to the MLflow configuration debugging instructions, do the following to determine if a timeout is caused by 3rd-party client APIs used in your model pipeline:

*   Test the model locally with sample inputs in a notebook.
    *   If you see a **_"timed out"_** message in the notebook, adjust any relevant parameters for the third party client's timeout window.
    *   Example **_"timed out"_** message: `APITimeoutError: Request timed out.`
*   Test the model serving endpoint using POST requests.
    *   Check the **Service Logs** for your endpoint or the inference tables if you enabled them.
        *   For inference table schema details, see [Unity AI Gateway\-enabled inference table schema](https://docs.databricks.com/aws/en/ai-gateway/inference-tables#schema).

### OpenAI client example[​](#openai-client-example "Direct link to OpenAI client example")

When you establish an [OpenAI client](https://github.com/openai/openai-python), you can configure the `timeout` parameter to change the maximum time before a request times out on the client-side. The default and maximum timeout for an OpenAI client is [10 minutes](https://community.openai.com/t/is-it-still-supported-to-set-a-request-timeout-for-request/1078461/3).

The following example highlights how to configure a 3rd-party client APIs timeout.

Python

    %pip install openaidbutils.library.restartPython()from openai import OpenAIimport os# How to get your Databricks token: https://docs.databricks.com/en/dev-tools/auth/pat.htmlDATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')client = OpenAI(    timeout=10, # Number of seconds before client times out    api_key=DATABRICKS_TOKEN,    base_url="<WORKSPACE_URL>/serving-endpoints")chat_completion = client.chat.completions.create(    messages=[        {            "role": "system",            "content": "You are an AI assistant"        },        {            "role": "user",            "content": "Tell me about Large Language Models."        }    ],    model="model_name",    max_tokens=256)

note

For the OpenAI client, you can get around the maximum timeout window by enabling [streaming](https://cookbook.openai.com/examples/how_to_stream_completions).

## Other timeouts[​](#other-timeouts "Direct link to Other timeouts")

### Idle endpoints warming up[​](#idle-endpoints-warming-up "Direct link to Idle endpoints warming up")

If an endpoint is [scaled to 0](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints) and it receives a request that warms it up, it could potentially lead to a client-side timeout if it takes too long to warm up. This can be a cause of timeouts in pipelines that leverage steps like calls to provisioned throughput endpoints or AI Search indices, as mentioned above.

### Connection timeout[​](#connection-timeout "Direct link to Connection timeout")

Connection timeouts are related to the time a client waits to establish a connection with the server. If the connection is not established within this time, the client cancels the attempt. It's important to be aware of the clients used in your model pipeline and check the service logs and inference tables of the Model Serving endpoint for any connection timeouts. The messaging varies by service.

*   For example, a [SocketTimeout](https://kb.databricks.com/dbsql/job-timeout-when-connecting-to-a-sql-endpoint-over-jdbc) (for a service reading/writing to a SQL endpoint over a JDBC connection) may look like the following:
    *   `jdbc:spark://<server-hostname>:443;HttpPath=<http-path>;TransportMode=http;SSL=1[;property=value[;property=value]];SocketTimeout=300`
*   To find these, look for error messages containing the term **_"timed out"_** or **_"timeout"_**.

### Rate limits[​](#rate-limits "Direct link to Rate limits")

Multiple requests made over the rate limit of an endpoint might lead to failure for additional requests. See [Resource and payload limits](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#resource-and-payload-limits) for rate limits based on endpoint types. For third party clients, Databricks recommends that you review the documentation of the third party client you are using.
