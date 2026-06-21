---
title: Configure a load test for custom model serving endpoints | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/configure-load-test
ingestedAt: "2026-06-18T08:11:45.437Z"
---

This article provides a load test notebook example and covers setup requirements, authentication, cluster configuration, and step-by-step instructions for running load tests to optimize endpoint performance.

The information in this article and the example files get you started on how to configure a load test for your Model Serving endpoint on Databricks.

For more information about load testing and related concepts, see [Load testing for serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/what-is-load-test).

## Requirements[​](#-requirements "Direct link to -requirements")

Download and import a copy of the following files and example notebook to your Databricks workspace:

*   [input.json](https://docs.databricks.com/aws/en/assets/files/input-1a0a09cd4a185dc0cacd8fca85001d3e.json)
    *   This file specifies the payload that is sent by all concurrent connections to your endpoint. If you're testing an endpoint which is senstive to the size of the payload, ensure the input payload is representative of how you expect the endpoint to be used. See [Test the payload](#test) for more guidance.
*   [fast-load-test.py](https://docs.databricks.com/aws/en/assets/files/fast-load-test-92daa527102b40d4972682e8302e95b6.py)
    *   This script is used by the **Locust load test** notebook to validate authentication token and read the input.json file contents.

#### Locust load test notebook

The above files and example notebook have been tested using the following cluster configuration:

*   Single node cluster
*   15.4 LTS ML runtime
*   Choose a CPU optimized instance. Databricks recommends an instance with at least 32 cores. Instances with more cores can generate higher queries or requests per second (RPS).

## Locust[​](#locust "Direct link to Locust")

[Locust](https://locust.io/) is an open source framework for load testing which is commonly used for evaluating production-grade endpoints. The locust framework allows you to modify various parameters, like number of client connections and how fast client connections spawn, while measuring your endpoint’s performance throughout the test. Locust is used for all of the example code as it standardizes and automates the approach.

Locust relies on CPU resources to run its tests. Depending on payload this facilitates roughly 4000 requests per second per CPU core. In the **Locust load test** notebook, the `--processes -1` flag has been set to allow Locust to auto-detect the number of CPU cores on your driver and fully utilize them.

Keep an eye on the Locust output. If Locust is being bottlenecked by the CPU, an output a message appears.

## Set up your environment[​](#set-up-your-environment "Direct link to Set up your environment")

The guidance in this section is meant be completed outside of the **Locust load test** notebook.

### Endpoint configuration[​](#endpoint-configuration "Direct link to Endpoint configuration")

The **Locust load test** notebook assumes your model is running on a CPU model serving endpoint. The calculations in this notebook assume you configured the following when you created your serving endpoint using the Serving UI. See [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).

*   Start with a “Small” (endpoint concurrency of 4) CPU endpoint. When you create your endpoint, ensure it has both a minimum and maximum concurrency of 4
*   Route optimization is enabled
*   Scale to Zero is disabled

### Service principal setup[​](#service-principal-setup "Direct link to Service principal setup")

In order to interact with the route-optimized endpoint, the Locust test needs to be able to generate OAuth tokens with permissions to query the endpoint. Follow these steps to prepare authentication:

1.  [Create a Databricks Service Principal](https://docs.databricks.com/aws/en/admin/users-groups/manage-service-principals#add-sp)
2.  Navigate to the Model Serving endpoint webpage, click “Permissions” and give the Service Principal “Can Query” level permissions.
3.  [Create a databricks secret scope](https://docs.databricks.com/aws/en/security/secrets/example-secret-workflow) named with two keys:
    1.  The ID of your Databricks service principal. For example: `service_principal_client_id` .
    2.  The client secret for the Databricks service principal. For example `service_principal_client_secret`.
4.  Put the client ID and client Secret of your service principal into a [Databricks secret](https://docs.databricks.com/aws/en/security/secrets/).

## Notebook setup[​](#notebook-setup "Direct link to Notebook setup")

The following sections describe how to set up your **Locust load test** notebook and the supporting files that you downloaded in the [Requirements](#required).

### Configure variables[​](#configure-variables "Direct link to Configure variables")

In your copy of the **Locust load test** notebook configure the following parameters:

### Specify a payload[​](#specify-a-payload "Direct link to Specify a payload")

Specify your payload into the `input.json` file alongside the **Locust load test** notebooks.

To ensure the validity of the load test results, it is important to consider the payload that should be sent by the Locust clients. Choose a payload that accurately represents the type of payload that you plan to send in production. For example, if your model is a fraud detection model on credit card transactions which will be evaluated in real time, like one transaction per request, ensure your payload represents only one typical transaction.

### Test the payload[​](#-test-the-payload "Direct link to -test-the-payload")

Test your payload by copying and pasting the full `input.json` data into the **Query** window on your Databricks Model Serving endpoint and ensuring your model is responding with the desired outputs.

To open the **Query** box for your endpoint:

1.  Navigate to the **Serving UI** in your Databricks workspace.
2.  Select the endpoint you want to use for load testing.
3.  In the top rightmost corner, select the dropdown menu next to the **Use** button.
4.  Select **Query**.

The model serving endpoint concurrency you need to achieve a certain percentile of latency scales linearly with the number of concurrent connections. This means you can test on a small endpoint and calculate the size endpoint you need in the end before performing a final test.

## Run the load test[​](#run-the-load-test "Direct link to Run the load test")

After your endpoint, notebooks, and payload are configured, you can begin to step through the notebook execution.  
The notebook runs a very short 30 second duration load test against your endpoint to ensure the endpoint is online and responding.

You can run a series of load tests with different amounts of client side concurrency in the **Locust load test** notebook. After completing the series of load tests, there are cells in the notebook that print the content of any request failures or exceptions, and create a plot of latency percentiles against client concurrency.

You are presented with a table of results and must make a selection. Select the row which best meets your latency requirements, and input the applications desired RPS. The notebook takes this user-supplied information and responds with a recommendation of how to size your endpoint to meet your RPS and latency goals.

After updating your Model Serving endpoint configuration to match the recommendations of the notebook, you can run the final load test of the notebook to ensure that the endpoint is meeting both latency and RPS requirements.
