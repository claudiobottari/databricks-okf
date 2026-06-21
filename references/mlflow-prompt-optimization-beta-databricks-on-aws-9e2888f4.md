---
title: MLflow Prompt Optimization (beta) | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/automatically-optimize-prompts
ingestedAt: "2026-06-18T08:16:11.532Z"
---

Beta

This feature is currently in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

MLflow offers the [`mlflow.genai.optimize_prompts()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.optimize_prompt) API, which enables you to automatically improve your prompts using evaluation metrics and training data. This feature allows you to enhance prompt effectiveness across any agent framework by applying prompt optimization algorithms, reducing manual effort and ensuring consistent quality.

MLflow supports the [GEPA](https://arxiv.org/abs/2507.19457) optimization algorithm through the [`GepaPromptOptimizer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.optimize.GepaPromptOptimizer) researched and validated by the [Databricks AI Research Team](https://www.databricks.com/blog/building-state-art-enterprise-agents-90x-cheaper-automated-prompt-optimization). GEPA iteratively refines prompts using LLM-driven reflection and automated feedback, leading to systematic and data-driven improvements.

## Key benefits[​](#key-benefits "Direct link to Key benefits")

*   **Automatic Improvement**: Optimizes prompts based on evaluation metrics without manual tuning.
*   **Data-Driven Optimization**: Uses your training data and custom scorers to guide optimization.
*   **Framework Agnostic**: Works with any agent framework, providing broad compatibility.
*   **Joint Optimization**: Enable the simultaneous refinement of multiple prompts for best overall performance.
*   **Flexible Evaluation**: Provides support for custom scorers and aggregation function.
*   **Version Control**: Automatically registers optimized prompts in MLflow Prompt Registry.
*   **Extensible**: Plug in custom optimization algorithms by extending the base class.

Version Requirements

The `optimize_prompts` API requires **MLflow >= 3.5.0**.

## Prompt optimization example[​](#prompt-optimization-example "Direct link to Prompt optimization example")

See [Optimize prompts tutorial](https://docs.databricks.com/aws/en/mlflow3/genai/tutorials/examples/prompt-optimization-quickstart) for a simple example of prompt optimization.

The API produces an improved prompt that performs better on your evaluation criteria.

### Example: Simple Prompt → Optimized Prompt[​](#example-simple-prompt--optimized-prompt "Direct link to Example: Simple Prompt → Optimized Prompt")

**Before Optimization:**

Text

    Answer this question: {{question}}

**After Optimization:**

Text

    Answer this question: {{question}}.Focus on providing precise,factual information without additional commentary or explanations.1. **Identify the Subject**: Clearly determine the specific subjectof the question (e.g., geography, history)and provide a concise answer.2. **Clarity and Precision**: Your response should be a single,clear statement that directly addresses the question.Do not add extra details, context, or alternatives.3. **Expected Format**: The expected output should be the exact answerwith minimal words where appropriate.For instance, when asked about capitals, the answer shouldsimply state the name of the capital city,e.g., "Tokyo" for Japan, "Rome" for Italy, and "Paris" for France.4. **Handling Variations**: If the question contains multipleparts or variations, focus on the primary query and answer it directly. Avoid over-complication.5. **Niche Knowledge**: Ensure that the responses are based oncommonly accepted geographic and historical facts,as this type of information is crucial for accuracy in your answers.Adhere strictly to these guidelines to maintain consistencyand quality in your responses.

For a complete explanation, see the [MLflow documentation](https://mlflow.org/docs/latest/genai/prompt-registry/optimize-prompts/)

## Advanced usage[​](#advanced-usage "Direct link to Advanced usage")

See the following guides for advanced use cases,

*   [Optimize prompts using custom scorers](https://docs.databricks.com/aws/en/mlflow3/genai/tutorials/examples/custom-scorers)
*   [Optimize multiple prompts together](https://docs.databricks.com/aws/en/mlflow3/genai/tutorials/examples/multi-prompt-optimization)

## Common use cases[​](#common-use-cases "Direct link to Common use cases")

The following sections provide example code for common use cases.

### Improving accuracy[​](#improving-accuracy "Direct link to Improving accuracy")

Optimize prompts to produce more accurate outputs:

Python

    from mlflow.genai.scorers import Correctnessresult = mlflow.genai.optimize_prompts(    predict_fn=predict_fn,    train_data=dataset,    prompt_uris=[prompt.uri],    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-gpt-5"),    scorers=[Correctness(model="databricks:/databricks-claude-sonnet-4-5")],)

### Optimize for safeness[​](#optimize-for-safeness "Direct link to Optimize for safeness")

Ensure outputs are safe:

Python

    from mlflow.genai.scorers import Safetyresult = mlflow.genai.optimize_prompts(    predict_fn=predict_fn,    train_data=dataset,    prompt_uris=[prompt.uri],    optimizer=GepaPromptOptimizer(reflection_model="databricks:/databricks-claude-sonnet-4-5"),    scorers=[Safety(model="databricks:/databricks-claude-sonnet-4-5")],)

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

The following sections provide troubleshooting guidance for common errors.

### Issue: Optimization takes too long[​](#issue-optimization-takes-too-long "Direct link to Issue: Optimization takes too long")

**Solution**: Reduce dataset size or reduce the optimizer budget:

Python

    # Use fewer examplessmall_dataset = dataset[:20]# Use faster model for optimizationoptimizer = GepaPromptOptimizer(    reflection_model="databricks:/databricks-gpt-5-mini", max_metric_calls=100)

### Issue: No improvement observed[​](#issue-no-improvement-observed "Direct link to Issue: No improvement observed")

**Solution**: Check your evaluation metrics and increase dataset diversity as follows:

*   Ensure scorers accurately measure what you care about.
*   Increase training data size and diversity.
*   Try to modify optimizer configurations.
*   Verify that the form of outputs matches expectations.

### Issue: Prompts not being used[​](#issue-prompts-not-being-used "Direct link to Issue: Prompts not being used")

**Solution**: Ensure `predict_fn` calls `mlflow.entities.model_registry.PromptVersion.format`:

Python

    # ✅ Correct - loads from registrydef predict_fn(question: str):    prompt = mlflow.genai.load_prompt(f"prompts:/{prompt_location}@latest)    return llm_call(prompt.format(question=question))# ❌ Incorrect - hardcoded promptdef predict_fn(question: str):    return llm_call(f"Answer: {question}")

## Next steps[​](#next-steps "Direct link to Next steps")

To learn more about the API, see [Optimize Prompts (Beta)](https://mlflow.org/docs/latest/genai/prompt-registry/optimize-prompts/).

To learn more about tracing and evaluation for GenAI applications, see the following articles:

*   [MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/)
*   [Agent Evaluation](https://docs.databricks.com/aws/en/generative-ai/agent-evaluation/)
