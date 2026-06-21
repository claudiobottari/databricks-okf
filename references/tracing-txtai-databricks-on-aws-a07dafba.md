---
title: Tracing txtai | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/txtai
ingestedAt: "2026-06-18T08:17:44.469Z"
---

![txtai Tracing via autolog](https://docs.databricks.com/aws/en/assets/images/txtai-rag-tracing-507199b924f1c7ed180e0d940758e2dc.png)

[txtai](https://github.com/neuml/txtai?tab=readme-ov-file) is an all-in-one embeddings database for semantic search, LLM orchestration and language model workflows.

[MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) provides automatic tracing capability for txtai. Auto tracing for txtai can be enabled by calling the [`mlflow.autolog`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=autolog#mlflow.autolog) function, MLflow will capture traces for LLM invocation, embeddings, AI Search, and log them to the active MLflow Experiment.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

To use MLflow Tracing with txtai, you need to install MLflow, the `txtai` library, and the `mlflow-txtai` extension.

*   Development
*   Production

For development environments, install the full MLflow package with Databricks extras, `txtai`, and `mlflow-txtai`:

Bash

    pip install --upgrade "mlflow[databricks]>=3.1" txtai mlflow-txtai

The full `mlflow[databricks]` package includes all features for local development and experimentation on Databricks.

note

MLflow 3 is highly recommended for the best tracing experience with txtai.

Before running the examples, you'll need to configure your environment:

**For users outside Databricks notebooks**: Set your Databricks environment variables:

Bash

    export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"export DATABRICKS_TOKEN="your-personal-access-token"

**For users inside Databricks notebooks**: These credentials are automatically set for you.

**API Keys**: Ensure your LLM provider API keys are set:

Bash

    export OPENAI_API_KEY="your-openai-api-key"# Add other provider keys as needed if using txtai with different models

### Basic Example[​](#basic-example "Direct link to Basic Example")

The first example traces a [Textractor pipeline](https://neuml.github.io/txtai/pipeline/data/textractor/).

note

On serverless compute clusters, autologging for genAI tracing frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace.

Python

    import mlflowfrom txtai.pipeline import Textractorimport os# Ensure any necessary LLM provider API keys are set in your environment if Textractor uses one# For example, if it internally uses OpenAI:# os.environ["OPENAI_API_KEY"] = "your-openai-key"# Enable MLflow auto-tracing for txtaimlflow.txtai.autolog()# Set up MLflow tracking to Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/txtai-demo")# Define and run a simple Textractor pipeline.textractor = Textractor()textractor("https://github.com/neuml/txtai")

![txtai Textractor Tracing via autolog](https://docs.databricks.com/aws/en/assets/images/txtai-textractor-tracing-15f2e1b268fc3fc4921c06e5e9a87cd8.png)

### Retrieval Augmented Generation (RAG)[​](#retrieval-augmented-generation-rag "Direct link to Retrieval Augmented Generation (RAG)")

The next example traces a [RAG pipeline](https://neuml.github.io/txtai/pipeline/text/rag/).

Python

    import mlflowfrom txtai import Embeddings, RAGimport os# Ensure your LLM provider API key (e.g., OPENAI_API_KEY for the Llama model via some services) is set# os.environ["OPENAI_API_KEY"] = "your-key" # Or HUGGING_FACE_HUB_TOKEN, etc.# Enable MLflow auto-tracing for txtaimlflow.txtai.autolog()# Set up MLflow tracking to Databricks if not already configured# mlflow.set_tracking_uri("databricks")# mlflow.set_experiment("/Shared/txtai-rag-demo")wiki = Embeddings()wiki.load(provider="huggingface-hub", container="neuml/txtai-wikipedia-slim")# Define prompt templatetemplate = """Answer the following question using only the context below. Only include informationspecifically discussed.question: {question}context: {context} """# Create RAG pipelinerag = RAG(    wiki,    "hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4",    system="You are a friendly assistant. You answer questions from users.",    template=template,    context=10,)rag("Tell me about the Roman Empire", maxlength=2048)

![txtai Rag Tracing via autolog](https://docs.databricks.com/aws/en/assets/images/txtai-rag-tracing-507199b924f1c7ed180e0d940758e2dc.png)

### Agent[​](#agent "Direct link to Agent")

The last example runs a [txtai agent](https://neuml.github.io/txtai/agent/) designed to research questions on astronomy.

Python

    import mlflowfrom txtai import Agent, Embeddingsimport os# Ensure your LLM provider API key (e.g., OPENAI_API_KEY for the Llama model via some services) is set# os.environ["OPENAI_API_KEY"] = "your-key" # Or HUGGING_FACE_HUB_TOKEN, etc.# Enable MLflow auto-tracing for txtaimlflow.txtai.autolog()# Set up MLflow tracking to Databricks if not already configured# mlflow.set_tracking_uri("databricks")# mlflow.set_experiment("/Shared/txtai-agent-demo")def search(query):    """    Searches a database of astronomy data.    Make sure to call this tool only with a string input, never use JSON.    Args:        query: concepts to search for using similarity search    Returns:        list of search results with for each match    """    return embeddings.search(        "SELECT id, text, distance FROM txtai WHERE similar(:query)",        10,        parameters={"query": query},    )embeddings = Embeddings()embeddings.load(provider="huggingface-hub", container="neuml/txtai-astronomy")agent = Agent(    tools=[search],    llm="hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4",    max_iterations=10,)researcher = """{command}Do the following. - Search for results related to the topic. - Analyze the results - Continue querying until conclusive answers are found - Write a Markdown report"""agent(    researcher.format(        command="""Write a detailed list with explanations of 10 candidate stars that could potentially be habitable to life."""    ),    maxlength=16000,)

![txtai Agent Tracing via autolog](https://docs.databricks.com/aws/en/assets/images/txtai-agent-tracing-f69f47a9de38c40814ea985887782850.png)

### More Information[​](#more-information "Direct link to More Information")

For more examples and guidance on using txtai with MLflow, please refer to the [MLflow txtai extension documentation](https://github.com/neuml/mlflow-txtai/tree/master)

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Understand tracing concepts](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/tracing-101) - Learn how MLflow captures and organizes trace data for RAG and agent workflows
*   [Debug and observe your app](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/) - Use the Trace UI to analyze your txtai application's behavior
*   [Evaluate your app's quality](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app) - Set up quality assessment for your semantic search and RAG applications
