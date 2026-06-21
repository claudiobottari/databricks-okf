---
title: Foundation model REST API reference | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/api-reference
ingestedAt: "2026-06-18T08:11:01.058Z"
---

This article provides general API information for Databricks Foundation Model APIs and the models they support. The Foundation Model APIs are designed to be similar to OpenAI's REST API to make migrating existing projects easier. Both the pay-per-token and provisioned throughput endpoints accept the same REST API request format.

## Endpoints[​](#endpoints "Direct link to endpoints")

Foundation Model APIs supports pay-per-token endpoints and provisioned throughput endpoints.

A preconfigured endpoint is available in your workspace for each pay-per-token supported model, and users can interact with these endpoints using HTTP POST requests. See [Supported foundation models on Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-model-overview) for supported models.

Provisioned throughput endpoints can be [created using the API or the Serving UI](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis). These endpoints support multiple models per endpoint for A/B testing, as long as both served models expose the same API format. For example, both models are chat models. See [POST /api/2.0/serving-endpoints](https://docs.databricks.com/api/workspace/servingendpoints/create) for endpoint configuration parameters.

Requests and responses use JSON, the exact JSON structure depends on an endpoint's task type. Chat and completion endpoints support streaming responses.

## Usage[​](#usage "Direct link to usage")

Responses include a `usage` sub-message which reports the number of tokens in the request and response. The format of this sub-message is the same across all task types.

For models like `databricks-meta-llama-3-3-70b-instruct` a user prompt is transformed using a prompt template before being passed into the model. For pay-per-token endpoints, a system prompt might also be added. `prompt_tokens` includes all text added by our server.

## Responses API[​](#responses-api "Direct link to responses-api")

important

The Responses API is only compatible with OpenAI models.

The Responses API enables multi-turn conversations with a model. Unlike Chat Completions, the Responses API uses `input` instead of `messages`.

### Responses API request[​](#responses-api-request "Direct link to Responses API request")

**Unsupported parameters**: The following parameters are not supported by Databricks and will return a 400 error if specified:

*   `background` - Background processing is not supported
*   `store` - Stored responses is not supported
*   `conversation` - Conversation API is not supported
*   `service_tier` - Service tier selection is managed by Databricks

#### `ResponsesInput`[​](#responsesinput "Direct link to responsesinput")

The `input` field accepts either a string or a list of input message objects with role and content.

#### `ResponsesContentBlock`[​](#responsescontentblock "Direct link to responsescontentblock")

Content blocks define the type of content in input and output messages. The content block type is determined by the `type` field.

##### `InputText`[​](#inputtext "Direct link to inputtext")

##### `OutputText`[​](#outputtext "Direct link to outputtext")

##### `InputImage`[​](#inputimage "Direct link to inputimage")

##### `InputFile`[​](#inputfile "Direct link to inputfile")

##### `FunctionCall`[​](#functioncall "Direct link to functioncall")

##### `FunctionCallOutput`[​](#functioncalloutput "Direct link to functioncalloutput")

##### `CustomToolCall`[​](#customtoolcall "Direct link to customtoolcall")

Returned in the response `output` array when a custom tool is called. Unlike function calls, custom tool calls return plain text `input` instead of JSON `arguments`.

##### `CustomToolCallOutput`[​](#customtoolcalloutput "Direct link to customtoolcalloutput")

Use this input type to provide the result of a custom tool call back to the model in a multi-turn conversation.

#### `StreamOptions`[​](#streamoptions "Direct link to streamoptions")

Configuration for streaming responses. Only used when `stream: true`.

#### `TextConfig`[​](#textconfig "Direct link to textconfig")

Configuration for text output, including structured outputs.

#### `ResponsesFormatObject`[​](#responsesformatobject "Direct link to responsesformatobject")

Specifies the output format for text responses.

The `json_schema` object has the same structure as [JsonSchemaObject](#json-schema) documented in the Chat Completions API.

#### `ReasoningConfig`[​](#reasoningconfig "Direct link to reasoningconfig")

Configuration for reasoning behavior in reasoning models (o-series and gpt-5 models).

#### `ToolObject`[​](#toolobject "Direct link to toolobject")

See [Function calling on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/function-calling).

note

The Responses API supports the following tool types: `function`, `custom`, `mcp`, `image_generation`, `shell`. Custom tools and grammar-based output formats are only available with GPT-5 series models (`gpt-5`, `gpt-5.1`, `gpt-5.2`).

#### `CustomToolObject`[​](#customtoolobject "Direct link to customtoolobject")

Custom tools allow the model to return arbitrary string output instead of JSON-formatted function arguments. This is useful for code generation, applying patches, or other use cases where structured JSON is not required.

note

Custom tools are only supported with GPT-5 series models (`gpt-5`, `gpt-5.1`, `gpt-5.2`) through the Responses API.

**Example custom tool:**

JSON

    {  "type": "custom",  "name": "code_exec",  "description": "Executes arbitrary Python code. Return only valid Python code."}

**Example custom tool with grammar:**

JSON

    {  "type": "custom",  "name": "apply_patch",  "description": "Apply a patch to create or modify files.",  "format": {    "type": "grammar",    "definition": "start: begin_patch hunk end_patch\nbegin_patch: \"*** Begin Patch\" LF\n...",    "syntax": "lark"  }}

When a custom tool is called, the response contains a `custom_tool_call` output item with plain text `input` instead of JSON `arguments`.

#### `CustomFormat`[​](#customformat "Direct link to customformat")

Grammar-based output formats are only supported with GPT-5 series models.

#### `FunctionObject`[​](#functionobject "Direct link to functionobject")

#### `ToolChoiceObject`[​](#toolchoiceobject "Direct link to toolchoiceobject")

See [Function calling on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/function-calling).

### Responses API response[​](#responses-api-response "Direct link to Responses API response")

For non-streaming requests, the response is a single response object. For streaming requests, the response is a `text/event-stream` where each event is a response chunk.

#### `ResponsesMessage`[​](#responsesmessage "Direct link to responsesmessage")

Message objects in the `output` field containing the model's response content.

#### `Error`[​](#error "Direct link to error")

Error information when a response fails.

#### `IncompleteDetails`[​](#incompletedetails "Direct link to incompletedetails")

Details about why a response is incomplete.

## Chat Completions API[​](#chat-completions-api "Direct link to chat-completions-api")

The Chat Completions API enables multi-turn conversations with a model. The model response provides the next `assistant` message in the conversation. See [POST /serving-endpoints/{name}/invocations](https://docs.databricks.com/api/workspace/servingendpoints/query) for querying endpoint parameters.

### Chat request[​](#chat-request "Direct link to Chat request")

#### `ChatMessage`[​](#chatmessage "Direct link to chatmessage")

The `system` role can only be used once, as the first message in a conversation. It overrides the model's default system prompt.

#### `ContentItem`[​](#contentitem "Direct link to contentitem")

`ContentItem` is one of the following content types: `TextContent`, `ReasoningContent`, `DocumentContent`, or `ImageContent`

##### `TextContent`[​](#-textcontent "Direct link to -textcontent")

The citations fields are as follows:

##### `ImageContent`[​](#-imagecontent "Direct link to -imagecontent")

ImageURL fields are below:

##### `ReasoningContent`[​](#-reasoningcontent "Direct link to -reasoningcontent")

###### `TextSummary`[​](#-textsummary "Direct link to -textsummary")

###### `EncryptedTextSummary`[​](#-encryptedtextsummary "Direct link to -encryptedtextsummary")

##### `DocumentContent`[​](#-documentcontent "Direct link to -documentcontent")

DocumentContent is only for requests.

###### `Source`[​](#-source "Direct link to -source")

##### `FileContent`[​](#-filecontent "Direct link to -filecontent")

File fields are below:

#### `ToolCall`[​](#toolcall "Direct link to toolcall")

A tool call action suggestion by the model. See [Function calling on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/function-calling).

#### `FunctionCallCompletion`[​](#functioncallcompletion "Direct link to functioncallcompletion")

**Note**: `ToolChoiceObject`, `ToolObject`, and `FunctionObject` are defined in the [Responses API section](#tool-choice) and are shared between both APIs.

#### `ResponseFormatObject`[​](#responseformatobject "Direct link to responseformatobject")

See [Structured outputs on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/structured-outputs).

#### `JsonSchemaObject`[​](#jsonschemaobject "Direct link to jsonschemaobject")

See [Structured outputs on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/structured-outputs).

### Chat response[​](#chat-response "Direct link to chat-response")

For non-streaming requests, the response is a single chat completion object. For streaming requests, the response is a `text/event-stream` where each event is a completion chunk object. The top-level structure of completion and chunk objects is almost identical: only `choices` has a different type.

#### `ChatCompletionChoice`[​](#chatcompletionchoice "Direct link to chatcompletionchoice")

#### `ChatCompletionChunk`[​](#chatcompletionchunk "Direct link to chatcompletionchunk")

## Embeddings API[​](#embeddings-api "Direct link to embeddings-api")

Embedding tasks map input strings into embedding vectors. Many inputs can be batched together in each request. See [POST /serving-endpoints/{name}/invocations](https://docs.databricks.com/api/workspace/servingendpoints/query) for querying endpoint parameters.

### Embedding request[​](#embedding-request "Direct link to Embedding request")

Instructions are optional and highly model specific. For instance the BGE authors recommend no instruction when indexing chunks and recommend using the instruction `"Represent this sentence for searching relevant passages:"` for retrieval queries. The Qwen3-Embedding authors recommend a task-specific instruction such as `"Given a web search query, retrieve relevant passages that answer the query"` for retrieval queries, and no instruction when embedding retrieval documents. Other models like Instructor-XL support a wide range of instruction strings.

### Embeddings response[​](#embeddings-response "Direct link to Embeddings response")

#### `EmbeddingObject`[​](#embeddingobject "Direct link to embeddingobject")

## Completions API[​](#completions-api "Direct link to completions-api")

Text completion tasks are for generating responses to a single prompt. Unlike Chat, this task supports batched inputs: multiple independent prompts can be sent in one request. See [POST /serving-endpoints/{name}/invocations](https://docs.databricks.com/api/workspace/servingendpoints/query) for querying endpoint parameters.

### Completion request[​](#completion-request "Direct link to Completion request")

### Completion response[​](#completion-response "Direct link to Completion response")

#### `CompletionChoice`[​](#completionchoice "Direct link to completionchoice")

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Databricks Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/)
*   [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models)

*   [Databricks-hosted foundation models available in Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models)
