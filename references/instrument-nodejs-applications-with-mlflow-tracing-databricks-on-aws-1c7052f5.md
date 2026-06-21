---
title: Instrument Node.js applications with MLflow Tracing | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/typescript-sdk
ingestedAt: "2026-06-18T08:16:41.693Z"
---

[MLflow's TypeScript SDK](https://www.npmjs.com/package/mlflow-tracing) brings [MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) capabilities to TypeScript and JavaScript applications. Add production-ready observability to your GenAI applications with minimal code changes and leverage Databricks' powerful analytics and monitoring platform.

## Requirements[​](#requirements "Direct link to Requirements")

tip

Databricks recommends installing the latest version of the MLflow Tracing TypeScript SDK when developing Node.js applications with tracing.

To instrument your Node.js applications with MLflow Tracing, install the following:

*   `mlflow-tracing` from the [npm registry](https://www.npmjs.com/package/mlflow-tracing)
*   Node.js 14 or above
*   A Databricks workspace with access to MLflow Experiments

For automatic tracing with OpenAI, you also need:

*   `mlflow-openai` from the [npm registry](https://www.npmjs.com/package/mlflow-openai)

## Set up the SDK[​](#set-up-the-sdk "Direct link to Set up the SDK")

### Install the package[​](#install-the-package "Direct link to Install the package")

Install the package from the [npm registry](https://www.npmjs.com/package/mlflow-tracing):

Bash

    npm install mlflow-tracing

### Create an MLflow Experiment[​](#create-an-mlflow-experiment "Direct link to Create an MLflow Experiment")

1.  Open your Databricks workspace.
2.  In the left sidebar, under **AI/ML**, click **Experiments**.
3.  At the top of the Experiments page, click **GenAI apps & agents**.
4.  Click the ![Info icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTcuMjUgMTAuNVY3LjVIOC43NVYxMC41SDcuMjVaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDVDOC40MTQyMSA1IDguNzUgNS4zMzU3OSA4Ljc1IDUuNzVDOC43NSA2LjE2NDIxIDguNDE0MjEgNi41IDggNi41QzcuNTg1NzkgNi41IDcuMjUgNi4xNjQyMSA3LjI1IDUuNzVDNy4yNSA1LjMzNTc5IDcuNTg1NzkgNSA4IDVaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNOCAxNEMxMS4zMTM3IDE0IDE0IDExLjMxMzcgMTQgOEMxNCA0LjY4NjI5IDExLjMxMzcgMiA4IDJDNC42ODYyOSAyIDIgNC42ODYyOSAyIDhDMiAxMS4zMTM3IDQuNjg2MjkgMTQgOCAxNFpNOCAxMi41QzEwLjQ4NTMgMTIuNSAxMi41IDEwLjQ4NTMgMTIuNSA4QzEyLjUgNS41MTQ3MiAxMC40ODUzIDMuNSA4IDMuNUM1LjUxNDcyIDMuNSAzLjUgNS41MTQ3MiAzLjUgOEMzLjUgMTAuNDg1MyA1LjUxNDcyIDEyLjUgOCAxMi41WiIgZmlsbD0iIzZGNkY2RiIvPgo8L3N2Zz4K) icon next to the experiment name to find the experiment ID and note it down.

![create experiment](https://docs.databricks.com/aws/en/assets/images/genai-apps-agents-tile-2fc67b2799a4b6aa281a90a2dae81c95.png)

### Configure authentication[​](#configure-authentication "Direct link to Configure authentication")

Choose one of the following authentication methods:

*   Environment Variables
*   .env File

1.  In your MLflow Experiment, click the ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) icon > **Log traces locally** > click **Generate API Key**.
2.  Copy and run the generated code in your terminal:

Bash

    export DATABRICKS_TOKEN=<databricks-personal-access-token>export DATABRICKS_HOST=https://<workspace-name>.cloud.databricks.com

### Initialize the SDK[​](#initialize-the-sdk "Direct link to Initialize the SDK")

In your Node.js application, initialize the SDK with the experiment ID:

TypeScript

    import * as mlflow from 'mlflow-tracing';mlflow.init({  trackingUri: 'databricks',  experimentId: '<your-experiment-id>',});

## Automatic Tracing[​](#automatic-tracing "Direct link to Automatic Tracing")

Add one line of code to automatically trace supported libraries. MLflow Tracing TypeScript SDK currently supports automatic tracing for OpenAI SDK.

To use automatic tracing for OpenAI, install [`mlflow-openai`](https://www.npmjs.com/package/mlflow-openai) package:

Bash

    npm install mlflow-openai

Then, wrap the OpenAI client with the [`tracedOpenAI`](https://www.npmjs.com/package/mlflow-openai) function:

TypeScript

    import * as mlflow from 'mlflow-tracing';// Initialize the tracing SDKmlflow.init({  trackingUri: 'databricks',  experimentId: '<your-experiment-id>',});import { OpenAI } from 'openai';import { tracedOpenAI } from 'mlflow-openai';// Wrap the OpenAI client with the tracedOpenAI functionconst client = tracedOpenAI(new OpenAI());// Invoke the client as usualconst response = await client.chat.completions.create({  model: 'gpt-4o-mini',  messages: [    { role: 'system', content: 'You are a helpful weather assistant.' },    { role: 'user', content: "What's the weather like in Seattle?" },  ],});

## Manual Tracing[​](#manual-tracing "Direct link to Manual Tracing")

### Tracing a function with the `trace` API[​](#tracing-a-function-with-the-trace-api "Direct link to tracing-a-function-with-the-trace-api")

The `trace` API is useful when you want to trace a function.

*   Named function
*   Anonymous function

TypeScript

    import * as mlflow from 'mlflow-tracing';const getWeather = async (city: string) => {  return `The weather in ${city} is sunny`;};// Wrap the function with mlflow.trace to create a traced functionconst tracedGetWeather = mlflow.trace(getWeather, { name: 'get-weather' });// Invoke the traced function as usualconst result = await tracedGetWeather('San Francisco');

On the invocation of the traced function, MLflow will automatically create a span that captures:

*   Input arguments
*   Return value
*   Exception information if thrown
*   Latency

### Capturing nested function calls[​](#capturing-nested-function-calls "Direct link to Capturing nested function calls")

If you trace nested functions, MLflow will generate a trace with multiple spans, where the span structure captures the nested function calls.

TypeScript

    const sum = mlflow.trace(  (a: number, b: number) => {    return a + b;  },  { name: 'sum' },);const multiply = mlflow.trace(  (a: number, b: number) => {    return a * b;  },  { name: 'multiply' },);const computeArea = mlflow.trace(  (a: number, b: number, h: number) => {    const sumOfBase = sum(a, b);    const area = multiply(sumOfBase, h);    return multiply(area, 0.5);  },  { name: 'compute-area' },);computeArea(1, 2, 3);

The trace will look like this:

    - compute-area  - sum (a=1, b=2)  - multiply (a=3, b=3)  - multiply (a=9, b=0.5)

### Tracing a class method with the `@trace` API[​](#tracing-a-class-method-with-the-trace-api "Direct link to tracing-a-class-method-with-the-trace-api")

TypeScript version 5.0+ supports decorators. MLflow Tracing supports this syntax to trace class methods easily. MLflow will automatically create a span that captures:

*   Input arguments
*   Return value
*   Exception information if thrown
*   Latency

TypeScript

    import * as mlflow from 'mlflow-tracing';class MyClass {  @mlflow.trace({ spanType: mlflow.SpanType.LLM })  generateText(prompt: string) {    return "It's sunny in Seattle!";  }}const myClass = new MyClass();myClass.generateText("What's the weather like in Seattle?");

### Tracing a block of code with the `withSpan` API[​](#tracing-a-block-of-code-with-the-withspan-api "Direct link to tracing-a-block-of-code-with-the-withspan-api")

The `withSpan` API is useful when you want to trace a block of code, not a function.

TypeScript

    import * as mlflow from 'mlflow-tracing';const question = "What's the weather like in Seattle?";const result = await mlflow.withSpan(  async (span: mlflow.Span) => {    return "It's sunny in Seattle!";  },  // Pass name, span type, and inputs as options.  {    name: 'generateText',    spanType: mlflow.SpanType.TOOL,    inputs: { prompt: question },  },);

### Create and End a Span Explicitly[​](#create-and-end-a-span-explicitly "Direct link to Create and End a Span Explicitly")

To get more control over the span lifecycle, you can create and end a span explicitly.

TypeScript

    import * as mlflow from 'mlflow-tracing';const span = mlflow.startSpan({  name: 'generateText',  spanType: mlflow.SpanType.LLM,  inputs: { prompt: question },});span.end({  outputs: { answer: "It's sunny in Seattle!" },  status: 'OK',});

## Grouping Traces by Users and Sessions[​](#grouping-traces-by-users-and-sessions "Direct link to Grouping Traces by Users and Sessions")

Many real-world applications use sessions to maintain multi-turn user interactions. On the other hand, traces are often generated per-request. MLflow supports grouping traces by user sessions to help you understand an end-user's journey and identify issues. See [Add context to traces](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/add-context-to-traces) guide for more details.

## Full-stack example application[​](#full-stack-example-application "Direct link to Full-stack example application")

Check out the [full-stack example](https://github.com/mlflow/mlflow/tree/main/examples/mlflow-tracing/typescript-openai) for a complete example of how to use the MLflow Tracing TypeScript SDK in a Node.js application.

## Next steps[​](#next-steps "Direct link to Next steps")

See the following pages:

*   [Debug and observe your app](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/) - Use the Trace UI to analyze your application's behavior and performance
*   [Evaluate app quality](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app) - Leverage your traces to systematically assess and improve application quality
*   [Production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) - Track quality metrics in real-time in production
