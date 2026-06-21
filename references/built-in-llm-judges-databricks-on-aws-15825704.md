---
title: Built-in LLM judges | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/
ingestedAt: "2026-06-18T08:14:51.171Z"
---

Built-in LLM judges are predefined [scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) that use Databricks-hosted LLMs to evaluate common quality dimensions of your GenAI application such as relevance, safety, groundedness, and correctness. Use them when you want to start evaluating quality quickly. For situations where you want more control over your judges, use [custom LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) or Python ([code-based scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers)).

For the complete list and detailed documentation, see the [MLflow predefined scorers documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/predefined/).

## Available judges[​](#available-judges "Direct link to Available judges")

Judge

Arguments

Requires ground truth

What it evaluates

[`RelevanceToQuery`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_context_relevant#relevance-to-query)

`inputs`, `outputs`

No

Is the response directly relevant to the user's request?

[`RetrievalRelevance`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_context_relevant#retrieval-relevance)

`inputs`, `outputs`

No

Is the retrieved context directly relevant to the user's request?

[`Safety`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_safe)

`inputs`, `outputs`

No

Is the content free from harmful, offensive, or toxic material?

[`RetrievalGroundedness`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_grounded)

`inputs`, `outputs`

No

Is the response grounded in the information provided in the context? Is the agent hallucinating?

[`Correctness`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_correct)

`inputs`, `outputs`, `expectations`

Yes

Is the response correct as compared to the provided ground truth?

[`RetrievalSufficiency`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_context_sufficient)

`inputs`, `outputs`, `expectations`

Yes

Does the context provide all necessary information to generate a response that includes the ground truth facts?

[`Guidelines`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/guidelines#prebuilt-guidelines-scorer)

`inputs`, `outputs`

No

Does the response meet specified natural language criteria?

[`ExpectationsGuidelines`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/guidelines#prebuilt-expectationsguidelines-scorer)

`inputs`, `outputs`, `expectations`

No (but needs guidelines in expectations)

Does the response meet per-example natural language criteria?

[`ToolCallCorrectness`](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/tool-call/correctness/)

`inputs`, `outputs`, `expectations`

Yes

Are the tool calls and arguments correct for the user query?

[`ToolCallEfficiency`](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/tool-call/efficiency/)

`inputs`, `outputs`

No

Are the tool calls efficient without redundancy?

## Multi-turn judges[​](#multi-turn-judges "Direct link to Multi-turn judges")

For conversational AI systems, MLflow provides judges that evaluate entire conversations rather than individual turns. These judges analyze the complete conversation history to assess quality patterns that emerge over multiple interactions.

Use multi-turn judges both for [evaluation during development](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-conversations) and for [monitoring in production](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring#use-multi-turn-judges).

For the complete list and detailed documentation, see the [MLflow predefined scorers documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/predefined/#multi-turn).

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Choose the LLM that powers a judge](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers#select-the-llm-that-powers-the-judge)
*   [Build a custom LLM judge](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) when built-in judges don't fit your use case
*   [Align judges with human feedback](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/align-judges) to improve accuracy on your domain
