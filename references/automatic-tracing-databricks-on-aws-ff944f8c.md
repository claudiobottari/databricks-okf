---
title: Automatic tracing | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/automatic
ingestedAt: "2026-06-18T08:16:30.329Z"
---

Add one line of code, [`mlflow.<library>.autolog()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.autolog) to automatically trace your generative AI app. Automatic tracing works with [20+ supported libraries and frameworks](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/) out of the box.

note

On serverless compute clusters, autologging for genAI tracing frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Databricks recommends MLflow 3 for the latest GenAI tracing capabilites.

Run the following in a Databricks notebook to install the `mlflow` package and integration package you want to use. This example uses OpenAI:

*   MLflow 3
*   MLflow 2.x

*   **mlflow\[databricks\]>=3.1**: Core MLflow functionality with GenAI features and Databricks connectivity.
*   **openai>=1.0.0**: Only required to run the [Basic Automatic Tracing Example](#basic-automatic-tracing-example) on this page (if using other LLM providers, install their respective SDKs instead).
*   **Additional libraries**: Install specific libraries for the integrations you want to use.

Install the basic requirements:

Python

    %pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0# Also install libraries you want to trace (langchain, anthropic, etc.)dbutils.library.restartPython()

### Configure credentials[​](#configure-credentials "Direct link to Configure credentials")

*   Databricks notebook
*   External environment

In a Databricks notebook, set any necessary LLM API keys:

Python

    import osos.environ["OPENAI_API_KEY"] = "your-api-key"# Add other provider keys as needed# os.environ["ANTHROPIC_API_KEY"] = "your-api-key"# os.environ["MISTRAL_API_KEY"] = "your-api-key"

## Automatic tracing example[​](#-automatic-tracing-example "Direct link to -automatic-tracing-example")

MLflow automatically traces [20+ supported frameworks](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/). Here's how to enable automatic tracing for OpenAI agents connecting to Databricks Foundation Model APIs.

Python

    import mlflowimport osfrom openai import OpenAI# Databricks Foundation Model APIs use Databricks authentication.mlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/databricks-sdk-autolog-example")# Enable auto-tracing for OpenAI (which will trace Databricks Foundation Model API calls)mlflow.openai.autolog()# Create OpenAI client configured for Databricksclient = OpenAI(    api_key=os.environ.get("DATABRICKS_TOKEN"),    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints")# Query Llama 4 Maverick using OpenAI clientresponse = client.chat.completions.create(    model="databricks-llama-4-maverick",    messages=[        {"role": "system", "content": "You are a helpful assistant."},        {"role": "user", "content": "What are the key features of MLflow Tracing?"}    ],    max_tokens=150,    temperature=0.7)print(response.choices[0].message.content)# Your calls to Databricks Foundation Model APIs are automatically traced!

## Auto-trace multiple frameworks[​](#auto-trace-multiple-frameworks "Direct link to Auto-trace multiple frameworks")

You can use auto-tracing for multiple frameworks in the same agent. See all of the [supported frameworks](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/).

The following code combines direct OpenAI API calls, LangChain chains, and custom logic in a single trace for easy debugging and monitoring.

Python

    %pip install --upgrade langchain langchain-openai

Python

    import mlflowimport openaifrom mlflow.entities import SpanTypefrom langchain_openai import ChatOpenAIfrom langchain_core.prompts import ChatPromptTemplate# Enable auto-tracing for both OpenAI and LangChainmlflow.openai.autolog()mlflow.langchain.autolog()# Create OpenAI clientclient = openai.OpenAI()@mlflow.trace(span_type=SpanType.CHAIN)def multi_provider_workflow(query: str):    # First, use OpenAI directly for initial processing    analysis = client.chat.completions.create(        model="gpt-4o-mini",        messages=[            {"role": "system", "content": "Analyze the query and extract key topics."},            {"role": "user", "content": query}        ]    )    topics = analysis.choices[0].message.content    # Then use LangChain for structured processing    llm = ChatOpenAI(model="gpt-4o-mini")    prompt = ChatPromptTemplate.from_template(        "Based on these topics: {topics}\nGenerate a detailed response to: {query}"    )    chain = prompt | llm    response = chain.invoke({"topics": topics, "query": query})    return response# Run the functionresult = multi_provider_workflow("Explain quantum computing")

## Combine manual and automatic tracing[​](#combine-manual-and-automatic-tracing "Direct link to combine-manual-and-automatic-tracing")

Use [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace) with auto-tracing to create unified traces for the following scenarios:

*   Multiple LLM calls in one workflow
*   Multi-agent systems with different providers
*   Custom logic between LLM calls

Python

    import mlflowimport openaifrom mlflow.entities import SpanTypemlflow.openai.autolog()# Create OpenAI clientclient = openai.OpenAI()@mlflow.trace(span_type=SpanType.CHAIN)def run(question):    messages = build_messages(question)    # MLflow automatically generates a span for OpenAI invocation    response = client.chat.completions.create(        model="gpt-4o-mini",        max_tokens=100,        messages=messages,    )    return parse_response(response)@mlflow.tracedef build_messages(question):    return [        {"role": "system", "content": "You are a helpful chatbot."},        {"role": "user", "content": question},    ]@mlflow.tracedef parse_response(response):    return response.choices[0].message.contentrun("What is MLflow?")

Running this code generates a single trace that combines the manual spans with the automatic OpenAI tracing:

![Mix of auto and manual tracing](https://docs.databricks.com/aws/en/assets/images/tracing-auto-manual-mix-683000e63e68335e6dbc94a234193b49.png)

## Advanced example: multiple LLM calls[​](#advanced-example-multiple-llm-calls "Direct link to Advanced example: multiple LLM calls")

The following example shows how automatic tracing captures multiple LLM calls in a single workflow.

This pattern is useful when your application needs to make sequential decisions, such as analyzing a query first and then generating a response based on that analysis.

Python

    import mlflowimport openaifrom mlflow.entities import SpanType# Enable auto-tracing for OpenAImlflow.openai.autolog()# Create OpenAI clientclient = openai.OpenAI()@mlflow.trace(span_type=SpanType.CHAIN)def process_user_query(query: str):    # First LLM call: Analyze the query    analysis = client.chat.completions.create(        model="gpt-4o-mini",        messages=[            {"role": "system", "content": "Analyze the user's query and determine if it requires factual information or creative writing."},            {"role": "user", "content": query}        ]    )    analysis_result = analysis.choices[0].message.content    # Second LLM call: Generate response based on analysis    if "factual" in analysis_result.lower():        # Use a different model for factual queries        response = client.chat.completions.create(            model="gpt-4o-mini",            messages=[                {"role": "system", "content": "Provide a factual, well-researched response."},                {"role": "user", "content": query}            ]        )    else:        # Use a different model for creative queries        response = client.chat.completions.create(            model="gpt-4o-mini",            messages=[                {"role": "system", "content": "Provide a creative, engaging response."},                {"role": "user", "content": query}            ]        )    return response.choices[0].message.content# Run the functionresult = process_user_query("Tell me about the history of artificial intelligence")

This creates one trace with:

*   Parent span for `process_user_query`
*   Two child spans for the OpenAI calls

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Automatic tracing integrations](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/) - Browse all 20+ supported libraries and frameworks
*   [Manual tracing with decorators](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/) - Add custom spans to capture business logic alongside auto-traced LLM calls
