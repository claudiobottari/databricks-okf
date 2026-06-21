---
title: Answer and context relevance judges | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_context_relevant
ingestedAt: "2026-06-18T08:14:55.886Z"
---

MLflow provides two built-in LLM judges to assess relevance in your GenAI applications. These judges help diagnose quality issues - if context isn't relevant, the generation step cannot produce a helpful response.

*   **`RelevanceToQuery`**: Evaluates if your app's response directly addresses the user's input.
*   **`RetrievalRelevance`**: Evaluates if each document returned by your app's retriever(s) is relevant.

For API details, see the MLflow documentation:

*   [`RelevanceToQuery`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.RelevanceToQuery)
*   [`RetrievalRelevance`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.RetrievalRelevance)

For detailed documentation and additional examples, see the [MLflow Relevance judges documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/rag/relevance/).

## Prerequisites for running the examples[​](#prerequisites-for-running-the-examples "Direct link to Prerequisites for running the examples")

1.  Install MLflow and required packages.
    
    Python
    
        %pip install --upgrade "mlflow[databricks]>=3.4.0" openai "databricks-connect>=16.1"dbutils.library.restartPython()
    
2.  Create an MLflow experiment by following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).
    

## `RelevanceToQuery` judge[​](#-relevancetoquery-judge "Direct link to -relevancetoquery-judge")

This scorer evaluates if your app's response directly addresses the user's input without deviating into unrelated topics.

You can invoke the scorer directly with a single input for testing, or pass it to `mlflow.genai.evaluate` for running full evaluation on a dataset.

**Requirements:**

*   **Trace requirements**: `inputs` and `outputs` must be on the Trace's root span

*   Invoke directly
*   Invoke with evaluate()

Python

    import mlflowfrom mlflow.genai.scorers import RelevanceToQueryassessment = RelevanceToQuery(name="my_relevance_to_query")(    inputs={"question": "What is the capital of France?"},    outputs="The capital of France is Paris.",)print(assessment)

## `RetrievalRelevance` judge[​](#retrievalrelevance-judge "Direct link to retrievalrelevance-judge")

This scorer evaluates if each document returned by your app's retriever(s) is relevant to the input request.

**Requirements:**

*   **Trace requirements**: The MLflow Trace must contain at least one span with `span_type` set to `RETRIEVER`

*   Invoke directly
*   Invoke with evaluate()

Python

    from mlflow.genai.scorers import retrieval_relevanceimport mlflow# Get a trace from a previous runtrace = mlflow.get_trace("<your-trace-id>")# Assess if each retrieved document is relevantfeedbacks = retrieval_relevance(trace=trace)print(feedbacks)

### RAG example[​](#rag-example "Direct link to RAG example")

Here's a complete example showing how to create a RAG application with a retriever and evaluate it:

Python

    import mlflowfrom mlflow.genai.scorers import RetrievalRelevancefrom mlflow.entities import Documentfrom typing import List# Define a retriever function with proper span type@mlflow.trace(span_type="RETRIEVER")def retrieve_docs(query: str) -> List[Document]:    # Simulated retrieval - in practice, this would query a vector database    if "capital" in query.lower() and "france" in query.lower():        return [            Document(                id="doc_1",                page_content="Paris is the capital of France.",                metadata={"source": "geography.txt"}            ),            Document(                id="doc_2",                page_content="The Eiffel Tower is located in Paris.",                metadata={"source": "landmarks.txt"}            )        ]    else:        return [            Document(                id="doc_3",                page_content="Python is a programming language.",                metadata={"source": "tech.txt"}            )        ]# Define your app that uses the retriever@mlflow.tracedef rag_app(query: str):    docs = retrieve_docs(query)    # In practice, you would pass these docs to an LLM    return {"response": f"Found {len(docs)} relevant documents."}# Create evaluation dataseteval_dataset = [    {        "inputs": {"query": "What is the capital of France?"}    },    {        "inputs": {"query": "How do I use Python?"}    }]# Run evaluation with RetrievalRelevance scorereval_results = mlflow.genai.evaluate(    data=eval_dataset,    predict_fn=rag_app,    scorers=[        RetrievalRelevance(            model="databricks:/databricks-gpt-oss-120b",  # Optional. Defaults to custom Databricks model.        )    ])

## Select the LLM that powers the judge[​](#select-the-llm-that-powers-the-judge "Direct link to Select the LLM that powers the judge")

By default, built-in judges use a Databricks-hosted LLM designed to perform GenAI quality assessments. You can change the judge model by using the `model` argument when you create the judge. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the model provider, the model name is the same as the serving endpoint name.

You can customize these judges by providing different judge models:

Python

    from mlflow.genai.scorers import RelevanceToQuery, RetrievalRelevance# Use different judge modelsrelevance_judge = RelevanceToQuery(    model="databricks:/databricks-gpt-5-mini"  # Or any LiteLLM-compatible model)retrieval_judge = RetrievalRelevance(    model="databricks:/databricks-claude-opus-4-5")# Use in evaluationeval_results = mlflow.genai.evaluate(    data=eval_dataset,    predict_fn=rag_app,    scorers=[relevance_judge, retrieval_judge])

## Interpret results[​](#interpret-results "Direct link to Interpret results")

The judge returns a `Feedback` object with:

*   **`value`**: "yes" if context is relevant, "no" if not
*   **`rationale`**: Explanation of why the judge found the context relevant or irrelevant

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Explore other built-in judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) - Learn about groundedness, safety, and correctness judges
*   [Create custom judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) - Build specialized judges for your use case
*   [Evaluate RAG applications](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app) - Apply relevance judges in comprehensive RAG evaluation
