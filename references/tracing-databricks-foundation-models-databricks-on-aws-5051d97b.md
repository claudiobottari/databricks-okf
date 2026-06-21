---
title: Tracing Databricks Foundation Models | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/databricks-foundation-models
ingestedAt: "2026-06-18T08:17:05.235Z"
---

[MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) provides automatic tracing capability for Databricks Foundation Models. Since Databricks Foundation Models use an OpenAI-compatible API, you can enable auto tracing by calling the `mlflow.openai.autolog` function, and MLflow will capture traces for LLM invocation and log them to the active MLflow Experiment.

Python

    import mlflowmlflow.openai.autolog()

MLflow trace automatically captures the following information about Databricks Foundation Model calls:

*   Prompts and completion responses
*   Latencies
*   Model name and endpoint
*   Additional metadata such as `temperature`, `max_tokens`, if specified
*   Function calling if returned in the response
*   Any exception if raised

note

On serverless compute clusters, autologging is not automatically enabled. You must explicitly call `mlflow.openai.autolog()` to enable automatic tracing for this integration.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

To use MLflow Tracing with Databricks Foundation Models, you need to install MLflow and the OpenAI SDK (since Databricks Foundation Models use an OpenAI-compatible API).

*   Development
*   Production

For development environments, install the full MLflow package with Databricks extras and the OpenAI SDK:

Bash

    pip install --upgrade "mlflow[databricks]>=3.1" openai

The full `mlflow[databricks]` package includes all features for local development and experimentation on Databricks.

note

MLflow 3 is highly recommended for the best tracing experience with Databricks Foundation Models.

Before running the examples, you'll need to configure your environment:

**For users outside Databricks notebooks**: Set your Databricks environment variables:

Bash

    export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"export DATABRICKS_TOKEN="your-personal-access-token"

**For users inside Databricks notebooks**: These credentials are automatically set for you.

## Supported APIs[​](#supported-apis "Direct link to Supported APIs")

MLflow supports automatic tracing for the following Databricks Foundation Model APIs:

To request support for additional APIs, please open a [feature request](https://github.com/mlflow/mlflow/issues) on GitHub.

## Basic Example[​](#basic-example "Direct link to Basic Example")

Python

    import mlflowimport osfrom openai import OpenAI# Databricks Foundation Model APIs use Databricks authentication.# Enable auto-tracing for OpenAI (which will trace Databricks Foundation Model API calls)mlflow.openai.autolog()# Set up MLflow tracking to Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/databricks-foundation-models-demo")# Create OpenAI client configured for Databricksclient = OpenAI(    api_key=os.environ.get("DATABRICKS_TOKEN"),    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints")messages = [    {        "role": "user",        "content": "What is the capital of France?",    }]response = client.chat.completions.create(    model="databricks-llama-4-maverick",    messages=messages,    temperature=0.1,    max_tokens=100,)

![Databricks Foundation Models Trace](https://docs.databricks.com/aws/en/assets/images/databricks-foundation-models-trace-70bf0df386e819678fd7ef5e50b992ce.png)

## Streaming[​](#streaming "Direct link to Streaming")

MLflow Tracing supports streaming API of Databricks Foundation Models. With the same setup of auto tracing, MLflow automatically traces the streaming response and renders the concatenated output in the span UI.

Python

    import mlflowimport osfrom openai import OpenAI# Enable auto-tracing for OpenAI (which will trace Databricks Foundation Model API calls)mlflow.openai.autolog()# Set up MLflow tracking to Databricks if not already configured# mlflow.set_tracking_uri("databricks")# mlflow.set_experiment("/Shared/databricks-streaming-demo")# Create OpenAI client configured for Databricksclient = OpenAI(    api_key=os.environ.get("DATABRICKS_TOKEN"),    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints")stream = client.chat.completions.create(    model="databricks-llama-4-maverick",    messages=[        {"role": "user", "content": "Explain the benefits of using Databricks Foundation Models"}    ],    stream=True,  # Enable streaming response)for chunk in stream:    print(chunk.choices[0].delta.content or "", end="")

![Databricks Foundation Models Streaming Trace](https://docs.databricks.com/aws/en/assets/images/databricks-foundation-models-trace-stream-9805a5ccb04f2075368ebaf7cc9113fe.png)

## Function Calling[​](#function-calling "Direct link to Function Calling")

MLflow Tracing automatically captures function calling response from Databricks Foundation Models. The function instruction in the response will be highlighted in the trace UI. Moreover, you can annotate the tool function with the `@mlflow.trace` decorator to create a span for the tool execution.

The following example implements a simple function calling agent using Databricks Foundation Models and MLflow Tracing.

Python

    import jsonimport osfrom openai import OpenAIimport mlflowfrom mlflow.entities import SpanType# Enable auto-tracing for OpenAI (which will trace Databricks Foundation Model API calls)mlflow.openai.autolog()# Set up MLflow tracking to Databricks if not already configured# mlflow.set_tracking_uri("databricks")# mlflow.set_experiment("/Shared/databricks-function-agent-demo")# Create OpenAI client configured for Databricksclient = OpenAI(    api_key=os.environ.get("DATABRICKS_TOKEN"),    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints")# Define the tool function. Decorate it with `@mlflow.trace` to create a span for its execution.@mlflow.trace(span_type=SpanType.TOOL)def get_weather(city: str) -> str:    if city == "Tokyo":        return "sunny"    elif city == "Paris":        return "rainy"    return "unknown"tools = [    {        "type": "function",        "function": {            "name": "get_weather",            "parameters": {                "type": "object",                "properties": {"city": {"type": "string"}},            },        },    }]_tool_functions = {"get_weather": get_weather}# Define a simple tool calling agent@mlflow.trace(span_type=SpanType.AGENT)def run_tool_agent(question: str):    messages = [{"role": "user", "content": question}]    # Invoke the model with the given question and available tools    response = client.chat.completions.create(        model="databricks-llama-4-maverick",        messages=messages,        tools=tools,    )    ai_msg = response.choices[0].message    # If the model requests tool call(s), invoke the function with the specified arguments    if tool_calls := ai_msg.tool_calls:        for tool_call in tool_calls:            function_name = tool_call.function.name            if tool_func := _tool_functions.get(function_name):                args = json.loads(tool_call.function.arguments)                tool_result = tool_func(**args)            else:                raise RuntimeError("An invalid tool is returned from the assistant!")            messages.append(                {                    "role": "tool",                    "tool_call_id": tool_call.id,                    "content": tool_result,                }            )        # Send the tool results to the model and get a new response        response = client.chat.completions.create(            model="databricks-llama-4-maverick", messages=messages        )    return response.choices[0].message.content# Run the tool calling agentquestion = "What's the weather like in Paris today?"answer = run_tool_agent(question)

![Databricks Foundation Models Function Calling Trace](https://docs.databricks.com/aws/en/assets/images/databricks-foundation-models-trace-function-calling-7b31fa0cf9da6448bab7623fd35b0da6.png)

## Available Models[​](#available-models "Direct link to Available Models")

Databricks Foundation Models provides access to a variety of state-of-the-art models including Llama, Anthropic, and other leading foundation models.

For the complete and most up-to-date list of available models and their model IDs, please refer to the [Databricks Foundation Models documentation](https://docs.databricks.com/en/machine-learning/foundation-models/index.html).

## Disable auto-tracing[​](#disable-auto-tracing "Direct link to Disable auto-tracing")

Auto tracing for Databricks Foundation Models can be disabled globally by calling `mlflow.openai.autolog(disable=True)` or `mlflow.autolog(disable=True)`.
