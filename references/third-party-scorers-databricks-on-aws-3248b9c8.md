---
title: Third-party scorers | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/third-party-scorers/
ingestedAt: "2026-06-18T08:15:31.789Z"
---

MLflow integrates with popular open-source evaluation frameworks so that you can use their specialized metrics as scorers alongside [built-in LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers) and [code-based scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers). Third-party scorers plug directly into [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate), giving you access to a broad library of evaluation metrics through a single, unified interface.

## Why use third-party scorers[​](#why-use-third-party-scorers "Direct link to Why use third-party scorers")

Third-party scorers are useful when you need:

*   **Specialized metrics** not covered by built-in judges, such as agent plan quality, jailbreak detection, or BLEU/ROUGE text comparison scores.
*   **Framework-specific strengths** from libraries your team already uses, without changing your evaluation workflow.
*   **Combined evaluation** across multiple frameworks in a single `mlflow.genai.evaluate()` call, with results visualized together in the MLflow UI.

## Available integrations[​](#available-integrations "Direct link to Available integrations")

Each integration wraps a third-party framework's metrics as MLflow scorers. Install the framework's package, import the scorer, and pass it to `mlflow.genai.evaluate()`.

Integration

When to use:

[DeepEval scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/third-party-scorers/deep-eval)

You need the broadest metric coverage across RAG, agents, conversational AI, and safety. DeepEval offers specialized scorers for agent plan quality, step efficiency, multi-turn conversation completeness, and role adherence that other frameworks don't provide.

[RAGAS scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/third-party-scorers/ragas)

You need deep RAG evaluation with fine-grained context metrics (precision, recall, utilization, noise sensitivity), agent goal accuracy, or deterministic text comparison scores like BLEU, ROUGE, and semantic similarity without LLM calls.

[Arize Phoenix scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/third-party-scorers/phoenix)

You need a lightweight, focused set of scorers for hallucination detection, relevance assessment, toxicity identification, QA correctness, or summarization quality.

[TruLens scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/third-party-scorers/trulens)

You need to analyze agent execution traces with goal-plan-action alignment metrics like logical consistency, execution efficiency, plan adherence, and tool selection.

[Guardrails AI scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/third-party-scorers/guardrails)

You need rule-based output validation that runs without LLM calls, such as toxicity detection, PII scanning, jailbreak detection, secrets detection, or gibberish identification.

## Quick example[​](#quick-example "Direct link to Quick example")

The following example combines scorers from two different frameworks in a single evaluation:

Python

    import mlflowfrom mlflow.genai.scorers.deepeval import AnswerRelevancyfrom mlflow.genai.scorers.guardrails import ToxicLanguageeval_dataset = [    {        "inputs": {"query": "What is MLflow?"},        "outputs": "MLflow is an open-source platform for managing ML and GenAI workloads.",    },]results = mlflow.genai.evaluate(    data=eval_dataset,    scorers=[        AnswerRelevancy(threshold=0.7, model="databricks:/databricks-gpt-5-mini"),        ToxicLanguage(threshold=0.7),    ],)

## When to use third-party vs. built-in scorers[​](#when-to-use-third-party-vs-built-in-scorers "Direct link to When to use third-party vs. built-in scorers")

Start with [built-in LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers#built-in-judges) for common evaluation needs like correctness, groundedness, and safety. Add third-party scorers in the following situations:

*   You already use these libraries in your workflows and want to take advantage of other MLflow features.
*   You need metrics for a specific domain that built-in judges don't cover, such as agent step efficiency or conversation completeness.
*   You need deterministic, non-LLM evaluation metrics like BLEU scores, exact match, or regex pattern matching.
*   You need rule-based validators that run without LLM calls, such as PII detection or secrets scanning.
