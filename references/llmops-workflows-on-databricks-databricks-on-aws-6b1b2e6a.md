---
title: LLMOps workflows on Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/mlops/llmops
ingestedAt: "2026-06-18T08:11:34.131Z"
---

This article complements [MLOps workflows on Databricks](https://docs.databricks.com/aws/en/machine-learning/mlops/mlops-workflow) by adding information specific to LLMOps workflows. For more details, see [The Big Book of MLOps](https://www.databricks.com/resources/ebook/the-big-book-of-mlops).

## How does the MLOps workflow change for LLMs?[​](#how-does-the-mlops-workflow-change-for-llms "Direct link to How does the MLOps workflow change for LLMs?")

LLMs are a class of natural language processing (NLP) models that have significantly surpassed their predecessors in size and performance across a variety of tasks, such as open-ended question answering, summarization, and execution of instructions.

Development and evaluation of LLMs differs in some important ways from traditional ML models. This section briefly summarizes some of the key properties of LLMs and the implications for MLOps.

## Commonalities between MLOps and LLMOps[​](#commonalities-between-mlops-and-llmops "Direct link to Commonalities between MLOps and LLMOps")

Many aspects of MLOps processes do not change for LLMs. For example, the following guidelines also apply to LLMs:

*   Use separate environments for development, staging, and production.
*   Use Git for version control.
*   Manage model development with MLflow, and use [Models in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/) to manage the model lifecycle.
*   Store data in a lakehouse architecture using Delta tables.
*   Your existing CI/CD infrastructure should not require any changes.
*   The modular structure of MLOps remains the same, with pipelines for featurization, model training, model inference, and so on.

## Reference architecture diagrams[​](#reference-architecture-diagrams "Direct link to Reference architecture diagrams")

This section uses two LLM-based applications to illustrate some of the adjustments to the [reference architecture of traditional MLOps](https://docs.databricks.com/aws/en/machine-learning/mlops/mlops-workflow). The diagrams show the production architecture for 1) a retrieval-augmented generation (RAG) application using a third-party API, and 2) a RAG application using a self-hosted fine-tuned model. Both diagrams show an optional vector database — this item can be replaced by directly querying the LLM through the Model Serving endpoint.

### RAG with a third-party LLM API[​](#rag-with-a-third-party-llm-api "Direct link to RAG with a third-party LLM API")

The diagram shows a production architecture for a RAG application that connects to a third-party LLM API using Databricks External Models.

![third-party LLM using external model](https://docs.databricks.com/aws/en/assets/images/llmops-rag-3p-fe920f2390a4eb5a216dd39d389d61d4.png)

### RAG with a fine-tuned open source model[​](#rag-with-a-fine-tuned-open-source-model "Direct link to rag-with-a-fine-tuned-open-source-model")

The diagram shows a production architecture for a RAG application that fine-tunes an open source model.

![fine-tune LLM based on open source model](https://docs.databricks.com/aws/en/assets/images/llmops-rag-fine-tune-24a137f9f37a64e788f0e2c138161efb.png)

## LLMOps changes to MLOps production architecture[​](#llmops-changes-to-mlops-production-architecture "Direct link to LLMOps changes to MLOps production architecture")

This section highlights the major changes to the MLOps reference architecture for LLMOps applications.

### Model hub[​](#model-hub "Direct link to Model hub")

LLM applications often use existing, pretrained models selected from an internal or external model hub. The model can be used as-is or fine-tuned.

Databricks includes a selection of high-quality, pre-trained foundation models in Unity Catalog and in Databricks Marketplace. You can use these pre-trained models to access state-of-the-art AI capabilities, saving you the time and expense of building your own custom models. For details, see [Access generative AI and LLM models from Unity Catalog](https://docs.databricks.com/aws/en/generative-ai/pretrained-models).

### Vector index[​](#vector-index "Direct link to Vector index")

Some LLM applications use vector indexes for fast similarity searches, for example to provide context or domain knowledge in LLM queries. Databricks provides an integrated AI Search functionality that lets you use any Delta table in Unity Catalog as an index. The AI Search index automatically syncs with the Delta table. For details, see [AI Search](https://docs.databricks.com/aws/en/ai-search/ai-search).

You can create a model artifact that encapsulates the logic to retrieve information from an AI Search index and provides the returned data as context to the LLM. You can then log the model using the MLflow LangChain or PyFunc model flavor.

### Fine-tune LLM[​](#fine-tune-llm "Direct link to Fine-tune LLM")

Because LLM models are expensive and time-consuming to create from scratch, LLM applications often fine-tune an existing model to improve its performance in a particular scenario. In the reference architecture, fine-tuning and model deployment are represented as distinct Lakeflow Jobs. Validating a fine-tuned model before deploying is often a manual process.

Databricks provides Foundation Model Fine-tuning, which lets you use your own data to customize an existing LLM to optimize its performance for your specific application. For details, see [Foundation Model Fine-tuning](https://docs.databricks.com/aws/en/large-language-models/foundation-model-training/).

### Model serving[​](#model-serving "Direct link to Model serving")

In the RAG using a third-party API scenario, an important architectural change is that the LLM pipeline makes external API calls, from the Model Serving endpoint to internal or third-party LLM APIs. This adds complexity, potential latency, and additional credential management.

Databricks provides Model Serving, which provides a unified interface to deploy, govern, and query AI models. For details, see [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/).

### Human feedback in monitoring and evaluation[​](#human-feedback-in-monitoring-and-evaluation "Direct link to Human feedback in monitoring and evaluation")

Human feedback loops are essential in most LLM applications. Human feedback should be managed like other data, ideally incorporated into monitoring based on near real-time streaming.

The MLflow review app helps you gather feedback from human reviewers. For details, see [Human feedback in MLflow](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/).
