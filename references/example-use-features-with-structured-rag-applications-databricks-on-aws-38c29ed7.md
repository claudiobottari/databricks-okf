---
title: "Example: use features with structured RAG applications | Databricks on AWS"
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/rag
ingestedAt: "2026-06-18T08:10:33.409Z"
---

Retrieval-augmented generation, or RAG, is one of the most common approaches to building generative AI applications. Feature engineering in Unity Catalog supports structured RAG applications using online tables. You create an online table for the structured data that the RAG application needs and host it on a feature serving endpoint. The RAG application uses the feature serving endpoint to look up relevant data from the online table.

The typical steps are as follows:

1.  Create a feature serving endpoint.
2.  Create a LangChainTool that uses the endpoint to look up relevant data.
3.  Use the tool in the LangChain agent to retrieve relevant data.
4.  Create a model serving endpoint to host the LangChain application.

The following notebook illustrates how to use Databricks online tables and feature serving endpoints for retrieval augmented generation (RAG) applications.

#### Online tables with RAG applications demo notebook
