---
title: Genie Code for agent observability and evaluation | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/genie-code
ingestedAt: "2026-06-18T08:15:49.267Z"
---

Genie Code provides a natural language interface for understanding, debugging, and improving your GenAI applications within MLflow. It has read access to everything in your experiment, from traces, prompts, and datasets to evaluation runs, scorers, and labeling sessions — so you can explore your observability and evaluation data conversationally instead of writing queries or navigating multiple UI pages.

To get started, click the Genie Code icon in the top-right of your workspace while viewing an experiment.

![Genie Code for agent observability and evaluation](https://assets.docs.databricks.com/_static/images/mlflow3-genai/genie-code-mlflow-demo.gif)

## Capabilities[​](#capabilities "Direct link to Capabilities")

Genie Code can help you with a wide range of observability and evaluation tasks, including:

*   **Trace analysis and debugging**: Investigate failing traces, find errors, examine span trees, pinpoint root causes, analyze latency, and identify bottlenecks in your agent's execution flow. Deep-dive into any trace to inspect its full span hierarchy, including inputs, outputs, metadata, and token usage at every step.
*   **Metrics and performance**: Compute latency percentiles (P50/P95/P99), track error rates and throughput over time, analyze token usage patterns and costs, and compare performance across different time periods or filters.
*   **Quality and evaluations**: Review assessment scores from human feedback, LLM judges, and programmatic checks. Inspect evaluation datasets, check registered scorers and their configurations, and get help setting up `mlflow.genai.evaluate()` with the right scorers.
*   **Labeling and review**: View labeling sessions and who's assigned to review traces, and inspect labeling schemas to understand feedback criteria such as ratings, comments, and expectations.
*   **Prompt registry**: Browse prompts in Unity Catalog, view templates, versions, and aliases.
*   **Instrumentation guidance**: Get help adding tracing to your code with `autolog()`, `@mlflow.trace`, or manual spans, with runnable code snippets you can paste directly into Databricks notebooks.

## Example questions[​](#example-questions "Direct link to Example questions")

Here are some things you can ask Genie Code:

*   "Help me discover issues with my agent's tool calling in the traces for this experiment over the last 3 hours"
*   "Identify cases where users get frustrated in the conversations with my agent"
*   "Which sessions have the lowest user feedback scores, and what went wrong in those conversations?"
*   "What are the most common failure patterns in my traces this past week, and what scorers should I add to catch them?"
*   "Which spans consume the most tokens across all my traces?"
*   "Find traces where the retriever returned no results but the agent still tried to answer"
*   "Help me set up evaluation for my RAG agent with the right scorers"

## Requirements[​](#requirements "Direct link to Requirements")

To use Genie Code for agent observability and evaluation, your workspace needs the following:

*   Partner-powered AI features enabled for both the account and workspace. See [Partner-powered AI features](https://docs.databricks.com/aws/en/databricks-ai/partner-powered).
*   Your workspace must be in a supported region. Genie Code is a [Designated Service](https://docs.databricks.com/aws/en/resources/designated-services) that uses Geos to manage data residency. See [Geo availability of Genie Code features](https://docs.databricks.com/aws/en/genie-code/#geo-availability).

## Next steps[​](#next-steps "Direct link to Next steps")

*   [MLflow Tracing - GenAI observability](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) — Learn about MLflow Tracing for end-to-end observability.
*   [Evaluate and monitor AI agents](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/) — Set up evaluation and monitoring for your GenAI agents.
*   [Get started: MLflow 3 for GenAI](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/) — Get started with MLflow 3 for GenAI.
