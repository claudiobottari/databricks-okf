---
title: Web search on Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/web-search
ingestedAt: "2026-06-18T08:12:54.256Z"
---

This page describes web search on Databricks and how to use it to ground model responses with real-time information from the web. Web search is available for Gemini and OpenAI foundation models served through [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/), and for Anthropic models through [Model Context Protocol (MCP)](https://docs.databricks.com/aws/en/generative-ai/mcp/external-mcp).

## What is web search?[​](#what-is-web-search "Direct link to What is web search?")

Web search allows foundation models to retrieve up-to-date information from the internet during response generation. When web search is enabled, the model can search the web to find relevant information and incorporate it into its response. This is useful for questions about current events, recent data, or any topic where real-time information improves the response.

## Use web search[​](#use-web-search "Direct link to Use web search")

How you enable web search depends on the model provider and API you use:

*   **Gemini models**: Use the `google_search` parameter with the [Chat Completions API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models) or the [Google Gemini API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-gemini-api).
*   **OpenAI models**: Use the `web_search` tool with the [OpenAI Responses API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-openai-responses).
*   **Anthropic models**: Use a web search MCP server such as [You.com](https://marketplace.databricks.com/details/32d5b7b6-0fab-4bba-9c57-5de23dd58996/Youcom_Youcom-MCP-The-1-AI-Web-Search-API) from Databricks Marketplace.

important

Web search for OpenAI models is only available through the Responses API. It is not supported through the Chat Completions API.

### Gemini models with the Chat Completions API[​](#gemini-models-with-the-chat-completions-api "Direct link to Gemini models with the Chat Completions API")

To enable web search for Gemini models using the Chat Completions API, pass `google_search` as a top-level parameter in the request body.

*   Python
*   REST API

Python

    import osfrom openai import OpenAIDATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')DATABRICKS_BASE_URL = os.environ.get('DATABRICKS_BASE_URL')client = OpenAI(    api_key=DATABRICKS_TOKEN,    base_url=DATABRICKS_BASE_URL)response = client.chat.completions.create(    model="databricks-gemini-2-5-pro",    messages=[        {"role": "user", "content": "What are the best Italian restaurants in San Francisco?"}    ],    extra_body={"google_search": {}})print(response.choices[0].message.content)

### Gemini models with the Google Gemini API[​](#gemini-models-with-the-google-gemini-api "Direct link to Gemini models with the Google Gemini API")

To enable web search using the [Google Gemini API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-gemini-api), pass `google_search` as a tool.

*   Python
*   REST API

Python

    from google import genaifrom google.genai import typesimport osDATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')client = genai.Client(    api_key="databricks",    http_options=types.HttpOptions(        base_url="https://example.staging.cloud.databricks.com/serving-endpoints/gemini",        headers={            "Authorization": f"Bearer {DATABRICKS_TOKEN}",        },    ),)response = client.models.generate_content(    model="databricks-gemini-2-5-pro",    contents=[        types.Content(            role="user",            parts=[types.Part(text="What are the best Italian restaurants in San Francisco?")],        ),    ],    config=types.GenerateContentConfig(        tools=[types.Tool(google_search=types.GoogleSearch())],    ),)print(response.text)

### OpenAI models with the Responses API[​](#openai-models-with-the-responses-api "Direct link to OpenAI models with the Responses API")

To enable web search for OpenAI models, pass `web_search` as a tool using the [OpenAI Responses API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-openai-responses).

*   Python
*   REST API

Python

    import osfrom openai import OpenAIDATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')DATABRICKS_BASE_URL = os.environ.get('DATABRICKS_BASE_URL')client = OpenAI(    api_key=DATABRICKS_TOKEN,    base_url=DATABRICKS_BASE_URL)response = client.responses.create(    model="databricks-gpt-5",    input=[        {"role": "user", "content": "What are the best Italian restaurants in San Francisco?"}    ],    tools=[{"type": "web_search"}])print(response.output_text)

### Anthropic models with MCP[​](#anthropic-models-with-mcp "Direct link to Anthropic models with MCP")

Anthropic's native web search tool is not available through Databricks Foundation Model APIs. Instead, you can add web search to Anthropic models using the [Model Context Protocol (MCP)](https://docs.databricks.com/aws/en/generative-ai/mcp/external-mcp) with a search provider such as You.com.

#### Set up the You.com MCP server[​](#set-up-the-youcom-mcp-server "Direct link to Set up the You.com MCP server")

1.  Navigate to **Marketplace > Agents > MCP Servers** in your Databricks workspace.
2.  Search for **You.com** and click **Install**.
3.  Configure the connection:

*   **Connection name**: Enter a name (for example, `youcom_web_search`).
*   **Bearer token**: Enter your You.com API key.

4.  Click **Install**.
5.  Grant **USE CONNECTION** privileges to appropriate users or groups under **Catalog > Connections > \[your connection\] > Permissions**.

After setup, the MCP server is available as a tool in AI Playground, agents, and other MCP-compatible clients. The proxy endpoint URL for your connection is:

    https://<workspace_host>.databricks.com/api/2.0/mcp/external/<connection_name>

#### Use with Claude Code[​](#use-with-claude-code "Direct link to Use with Claude Code")

If you use Claude Code with Databricks Foundation Model APIs, add the You.com MCP server to enable web search:

Bash

    claude mcp add youcom-search \  --transport http \  --url "https://<workspace_host>.databricks.com/api/2.0/mcp/external/<connection_name>" \  --header "Authorization: Bearer <your-databricks-pat>"

Verify the server was added with `claude mcp list`.

Alternatively, add the server directly to `~/.claude.json`:

JSON

    {  "mcpServers": {    "youcom-search": {      "type": "http",      "url": "https://<workspace_host>.databricks.com/api/2.0/mcp/external/<connection_name>",      "headers": {        "Authorization": "Bearer <your-databricks-pat>"      }    }  }}

## Supported models[​](#supported-models "Direct link to Supported models")

Web search is supported on all Gemini and OpenAI pay-per-token foundation models. See [Databricks-hosted foundation models available in Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models) for region availability.

### Gemini models[​](#gemini-models "Direct link to Gemini models")

*   `databricks-gemini-3-1-pro`
*   `databricks-gemini-3-1-flash-lite`
*   `databricks-gemini-3-pro`
*   `databricks-gemini-3-flash`
*   `databricks-gemini-2-5-pro`
*   `databricks-gemini-2-5-flash`

### OpenAI models[​](#openai-models "Direct link to OpenAI models")

*   `databricks-gpt-5-5-pro`
*   `databricks-gpt-5-5`
*   `databricks-gpt-5-4`
*   `databricks-gpt-5-4-mini`
*   `databricks-gpt-5-4-nano`
*   `databricks-gpt-5-3-codex`
*   `databricks-gpt-5-2`
*   `databricks-gpt-5-2-codex`
*   `databricks-gpt-5-1`
*   `databricks-gpt-5-1-codex-max`
*   `databricks-gpt-5-1-codex-mini`
*   `databricks-gpt-5`
*   `databricks-gpt-5-mini`
*   `databricks-gpt-5-nano`

### Anthropic models (via MCP)[​](#anthropic-models-via-mcp "Direct link to Anthropic models (via MCP)")

Web search via MCP is supported on all Anthropic foundation models that support tool use.

*   `databricks-claude-sonnet-4-6`
*   `databricks-claude-sonnet-4-5`
*   `databricks-claude-opus-4-7`
*   `databricks-claude-opus-4-6`
*   `databricks-claude-opus-4-5`
*   `databricks-claude-opus-4-1`
*   `databricks-claude-sonnet-4`

## Limitations[​](#limitations "Direct link to Limitations")

*   Web search is only available on pay-per-token foundation model endpoints. Provisioned throughput endpoints do not support web search.
*   External models do not support web search through Databricks.
*   Web search is not available for workspaces with HIPAA/BAA compliance enabled because web search queries are sent to external search services that are not HIPAA-compliant.
*   Web search results depend on the model's ability to formulate search queries and synthesize results. Response quality may vary.

*   For OpenAI models, web search is only available through the Responses API. The Chat Completions API does not support web search for OpenAI models.
*   Web search for Gemini models is not available when cross-region processing is disabled. Gemini does not support in-geo search processing, so any workspace with data residency enforcement is ineligible.
*   Web search for OpenAI models is not available when cross-region processing is disabled, unless the workspace is in an eligible geo (Americas or Europe). OpenAI supports in-geo search processing in these regions.

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Function calling on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/function-calling).
*   [Query a chat model](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models).

*   [Query with the OpenAI Responses API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-openai-responses).
*   [Query with the Google Gemini API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-gemini-api).
