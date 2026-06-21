---
title: Tracing PydanticAI | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/pydantic-ai
ingestedAt: "2026-06-18T08:17:34.875Z"
---

[PydanticAI](https://ai.pydantic.dev/) is a Python framework for building production-grade gen AI apps with strong typing and ergonomic APIs. It centers on Pydantic models to enforce structure and validation throughout agent workflows.

[MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) integrates with PydanticAI to record agent steps, tool calls, and model invocations with their typed inputs and outputs. Enable it with [`mlflow.pydantic_ai.autolog`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.pydantic_ai.html#mlflow.pydantic_ai.autolog).

note

On serverless compute clusters, autologging for genAI tracing frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace.

What this integration provides:

*   Agent calls with prompts, kwargs & output responses
*   LLM requests logging model name, prompt, parameters & response
*   Tool runs capturing tool name, arguments & usage metrics
*   MCP server calls & listings for tool-invocation tracing
*   Span metadata: latency, errors & run-ID linkage

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

To use MLflow Tracing with PydanticAI, you need to install MLflow and the relevant PydanticAI packages.

*   Development
*   Production

For development environments, install the full MLflow package with Databricks extras and PydanticAI:

Bash

    pip install --upgrade "mlflow[databricks]>=3.1" pydantic-ai openai

The full `mlflow[databricks]` package includes all features for local development and experimentation on Databricks.

note

MLflow 3 is recommended for the best tracing experience.

Before running the examples, you'll need to configure your environment:

**For users outside Databricks notebooks**: Set your Databricks environment variables:

Bash

    export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"export DATABRICKS_TOKEN="your-personal-access-token"

**For users inside Databricks notebooks**: These credentials are automatically set for you.

## Example usage[​](#example-usage "Direct link to Example usage")

Python

    import osfrom dataclasses import dataclassfrom typing import Anyfrom httpx import AsyncClientfrom pydantic_ai import Agent, ModelRetry, RunContext@dataclassclass Deps:    client: AsyncClient    weather_api_key: str | None    geo_api_key: str | Noneweather_agent = Agent(    # Switch to your favorite LLM    "google-gla:gemini-2.0-flash",    # 'Be concise, reply with one sentence.' is enough for some models (like openai) to use    # the below tools appropriately, but others like anthropic and gemini require a bit more direction.    system_prompt=(        "Be concise, reply with one sentence."        "Use the `get_lat_lng` tool to get the latitude and longitude of the locations, "        "then use the `get_weather` tool to get the weather."    ),    deps_type=Deps,    retries=2,    instrument=True,)@weather_agent.toolasync def get_lat_lng(    ctx: RunContext[Deps], location_description: str) -> dict[str, float]:    """Get the latitude and longitude of a location.    Args:        ctx: The context.        location_description: A description of a location.    """    if ctx.deps.geo_api_key is None:        return {"lat": 51.1, "lng": -0.1}    params = {        "q": location_description,        "api_key": ctx.deps.geo_api_key,    }    r = await ctx.deps.client.get("https://geocode.maps.co/search", params=params)    r.raise_for_status()    data = r.json()    if data:        return {"lat": data[0]["lat"], "lng": data[0]["lon"]}    else:        raise ModelRetry("Could not find the location")@weather_agent.toolasync def get_weather(ctx: RunContext[Deps], lat: float, lng: float) -> dict[str, Any]:    """Get the weather at a location.    Args:        ctx: The context.        lat: Latitude of the location.        lng: Longitude of the location.    """    if ctx.deps.weather_api_key is None:        return {"temperature": "21 °C", "description": "Sunny"}    params = {        "apikey": ctx.deps.weather_api_key,        "location": f"{lat},{lng}",        "units": "metric",    }    r = await ctx.deps.client.get(        "https://api.tomorrow.io/v4/weather/realtime", params=params    )    r.raise_for_status()    data = r.json()    values = data["data"]["values"]    # https://docs.tomorrow.io/reference/data-layers-weather-codes    code_lookup = {        1000: "Clear, Sunny",        1100: "Mostly Clear",        1101: "Partly Cloudy",        1102: "Mostly Cloudy",        1001: "Cloudy",        2000: "Fog",        2100: "Light Fog",        4000: "Drizzle",        4001: "Rain",        4200: "Light Rain",        4201: "Heavy Rain",        5000: "Snow",        5001: "Flurries",        5100: "Light Snow",        5101: "Heavy Snow",        6000: "Freezing Drizzle",        6001: "Freezing Rain",        6200: "Light Freezing Rain",        6201: "Heavy Freezing Rain",        7000: "Ice Pellets",        7101: "Heavy Ice Pellets",        7102: "Light Ice Pellets",        8000: "Thunderstorm",    }    return {        "temperature": f'{values["temperatureApparent"]:0.0f}°C',        "description": code_lookup.get(values["weatherCode"], "Unknown"),    }async def main():    async with AsyncClient() as client:        weather_api_key = os.getenv("WEATHER_API_KEY")        geo_api_key = os.getenv("GEO_API_KEY")        deps = Deps(            client=client, weather_api_key=weather_api_key, geo_api_key=geo_api_key        )        result = await weather_agent.run(            "What is the weather like in London and in Wiltshire?", deps=deps        )        print("Response:", result.output)# If you are running this on a notebookawait main()# Uncomment this is you are using an IDE or Python script.# asyncio.run(main())

Use PydanticAI as usual (agents, tools, and orchestrations). Traces will appear in the associated experiment.

## Connect to an MCP server[​](#connect-to-an-mcp-server "Direct link to Connect to an MCP server")

The following example below demonstrates how to run an MCP server using PydanticAI with MLflow tracing enabled. All tool invocation and listing operations are automatically captured as trace spans in the UI.

Python

    import mlflowimport asynciomlflow.set_tracking_uri("http://localhost:5000")mlflow.set_experiment("MCP Server")mlflow.pydantic_ai.autolog()from pydantic_ai import Agentfrom pydantic_ai.mcp import MCPServerStdioserver = MCPServerStdio(    "deno",    args=[        "run",        "-N",        "-R=node_modules",        "-W=node_modules",        "--node-modules-dir=auto",        "jsr:@pydantic/mcp-run-python",        "stdio",    ],)agent = Agent("openai:gpt-4o", mcp_servers=[server], instrument=True)async def main():    async with agent.run_mcp_servers():        result = await agent.run("How many days between 2000-01-01 and 2025-03-18?")    print(result.output)    # > There are 9,208 days between January 1, 2000, and March 18, 2025.# If you are running this on a notebookawait main()# Uncomment this is you are using an IDE or Python script.# asyncio.run(main())

## Token usage tracking[​](#token-usage-tracking "Direct link to Token usage tracking")

MLflow 3.2.0+ records token usage totals in trace info and per call in span attributes.

Python

    import mlflowlast_trace_id = mlflow.get_last_active_trace_id()trace = mlflow.get_trace(trace_id=last_trace_id)print(trace.info.token_usage)for span in trace.data.spans:    usage = span.get_attribute("mlflow.chat.tokenUsage")    if usage:        print(span.name, usage)

## Disable auto-tracing[​](#disable-auto-tracing "Direct link to Disable auto-tracing")

Disable with [`mlflow.pydantic_ai.autolog(disable=True)`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.pydantic_ai.html#mlflow.pydantic_ai.autolog) or globally with [`mlflow.autolog(disable=True)`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.autolog).
