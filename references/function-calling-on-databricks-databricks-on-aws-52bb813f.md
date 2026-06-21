---
title: Function calling on Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/function-calling
ingestedAt: "2026-06-18T08:11:58.479Z"
---

This article describes function calling and how to use it as part of your generative AI application workflows. Databricks Function Calling is OpenAI-compatible and is only available during model serving as part of [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/) and serving endpoints that serve [external models](https://docs.databricks.com/aws/en/generative-ai/external-models/).

## What is function calling?[​](#what-is-function-calling "Direct link to What is function calling?")

Function calling provides a way for you to control the output of LLMs, so they generate structured responses more reliably. When you use a function call, you describe functions in the API call by describing the function arguments using a JSON schema. The LLM itself does not call these functions, but instead it creates a JSON object that users can use to call the functions in their code.

For function calling on Databricks, the basic sequence of steps are as follows:

1.  Call the model using the submitted query and a set of functions defined in the `tools` parameter.
2.  The model decides whether or not to call the defined functions. When the function is called, the content is a JSON object of strings that adheres to your custom schema.
3.  Parse the strings into JSON in your code, and call your function with the provided arguments if they exist.
4.  Call the model again by appending the structured response as a new message. The structure of the response is defined by the functions you previously provided in `tools`. From here, the model summarizes the results and sends that summary to the user.

## When to use function calling[​](#when-to-use-function-calling "Direct link to When to use function calling")

The following are example use cases for function calling:

*   Create assistants that can answer questions by calling other APIs. For example, you can define functions like `send_email(to: string, body: string)` or `current_weather(location: string, unit: 'celsius' | 'fahrenheit')`.
*   Define and use API calls based on natural language. Like taking the statement, “Who are my top customers?” and making that into an API call named, `get_customers(min_revenue: int, created_before: string, limit: int)` and calling that API.

For batch inference or data processing tasks, like converting unstructured data into structured data. Databricks recommends using [structured outputs](https://docs.databricks.com/aws/en/machine-learning/model-serving/structured-outputs).

## Supported models[​](#supported-models "Direct link to supported-models")

The following table lists the supported models and which model serving feature makes each model available. See [Applicable model terms](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models) for these models.

*   For models made available by Foundation Model APIs, see [Foundation Model APIs limits](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#fmapi-limits) for region availability.
*   For models made available by External models, see [Region availability](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#regions) for region availability.

important

*   Meta-Llama-3.1-405B-Instruct will be retired as noted below. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.
    
    *   Starting February 15, 2026, this model is not available for pay-per-token workloads.
    *   Starting May 15, 2026, this model is not available for provisioned throughput workloads.
*   Starting December 11, 2024, Meta-Llama-3.3-70B-Instruct replaces support for Meta-Llama-3.1-70B-Instruct in Foundation Model APIs pay-per-token endpoints.
    
*   Google Gemini 3 Pro will be retired on March 26, 2026. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.
    
    *   To allow more time for migration, between March 26, 2026 and June 7, 2026, API calls to Gemini 3 Pro will be temporarily redirected to Gemini 3.1 Pro. The pricing for both models is identical.

:::

## Use function calling[​](#-use-function-calling "Direct link to -use-function-calling")

To use function calling with your generative AI application, you must provide function `parameters` and a `description`.

The default behavior for `tool_choice` is `"auto"`. This lets the model decide which functions to call and whether to call them.

You can customize the default behavior depending on your use case. The following are your options:

*   Set `tool_choice: "required"`. In this scenario, the model always calls one or more functions. The model selects which function or functions to call.
*   Set `tool_choice: {"type": "function", "function": {"name": "my_function"}}`. In this scenario, the model calls only a specific function.
*   Set `tool_choice: "none"` to disable function calling and have the model only generate a user-facing message.

The following is a single turn example using the OpenAI SDK and its `tools` parameter. See [Chat Completions API](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/api-reference#chat) for additional syntax details.

important

During Public Preview, function calling on Databricks is optimized for single turn function calling.

Python

    import osimport jsonfrom openai import OpenAIDATABRICKS_TOKEN = os.environ.get('YOUR_DATABRICKS_TOKEN')DATABRICKS_BASE_URL = os.environ.get('YOUR_DATABRICKS_BASE_URL')client = OpenAI(  api_key=DATABRICKS_TOKEN,  base_url=DATABRICKS_BASE_URL  )tools = [  {    "type": "function",    "function": {      "name": "get_current_weather",      "description": "Get the current weather in a given location",      "parameters": {        "type": "object",        "properties": {          "location": {            "type": "string",            "description": "The city and state, e.g. San Francisco, CA"          },          "unit": {            "type": "string",            "enum": [              "celsius",              "fahrenheit"            ]          }        }      }    }  }]messages = [{"role": "user", "content": "What is the current temperature of Chicago?"}]response = client.chat.completions.create(    model="databricks-meta-llama-3-3-70b-instruct",    messages=messages,    tools=tools,    tool_choice="auto",)print(json.dumps(response.choices[0].message.model_dump()['tool_calls'], indent=2))

This parameter also supports [Computer Use (beta)](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) for Claude models.

### JSON schema[​](#json-schema "Direct link to JSON schema")

Foundation Model APIs broadly support function definitions accepted by OpenAI. However, using a simpler JSON schema for function call definitions results in higher quality function call JSON generation. To promote higher quality generation, Foundation Model APIs only support a subset of [JSON schema specifications](https://json-schema.org/specification).

The following function call definition keys are not supported:

*   Regular expressions using `pattern`.
*   Complex nested or schema composition and validation using: `anyOf`, `oneOf`, `allOf`, `prefixItems`, or `$ref`.
*   Lists of types except for the special case of `[type, “null”]` where one type in the list is a valid JSON type and the other is `"null"`

Additionally, the following limitations apply:

*   The maximum number of keys specified in the JSON schema is `16`.
*   Foundation Model APIs does not enforce length or size constraints for objects and arrays.
    *   This includes keywords like `maxProperties`, `minProperties`, and `maxLength`.
*   Heavily nested JSON schemas result in lower quality generation. If possible, try flattening the JSON schema for better results.

## Token usage[​](#token-usage "Direct link to Token usage")

Prompt injection and other techniques are used to enhance the quality of tool calls. Doing so impacts the number of input and output tokens consumed by the model, which in turn results in billing implications. The more tools you use, the more your input tokens increase.

## Limitations[​](#limitations "Direct link to Limitations")

The following are limitations for function calling during Public Preview:

*   For multi-turn function calling Databricks recommends the [supported Claude models](#function-calling-models).
*   If using Llama 4 Maverick, the current function calling solution is optimized for single turn function calls. Multi-turn function calling is supported during the preview, but is under development.
*   Parallel function calling is not supported.
*   The maximum number of functions that can be defined in `tools` is 32 functions.
*   For provisioned throughput support, function calling is only supported on new endpoints. You cannot add function calling to previously created endpoints.
*   For Google Gemini endpoints, the `id` field on `function_call` and `function_response` is not supported.

## Notebook example[​](#notebook-example "Direct link to Notebook example")

See the following notebook for detailed function calling examples

#### Function calling example notebook
