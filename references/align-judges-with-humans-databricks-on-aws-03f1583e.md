---
title: Align judges with humans | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/align-judges
ingestedAt: "2026-06-18T08:14:36.089Z"
---

Judge alignment teaches LLM judges to match human evaluation standards through systematic feedback. This process transforms generic evaluators into domain-specific experts that understand your unique quality criteria, improving agreement with human assessments by 30 to 50 percent compared to baseline judges.

The same alignment workflow applies to both [built-in judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/) (such as `RelevanceToQuery`, `Safety`, or `Correctness`) and [custom judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) created with `make_judge()`. Use alignment with built-in judges to adapt their generic criteria to your domain, or with custom judges to refine specialized evaluation logic.

Judge alignment follows a three-step workflow:

1.  **Generate initial assessments**: Use a built-in or custom judge to evaluate traces and establish a baseline.
2.  **Collect human feedback**: Domain experts review and correct judge assessments.
3.  **Align and deploy**: Invoke the judge's `align()` method to create a new judge that is more aligned with human feedback.

The system supports the optimizers that are available in the package [`mlflow.genai.judges.optimizers`](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/alignment/#alignment-optimizers).

## Requirements[​](#requirements "Direct link to Requirements")

*   MLflow 3.4.0 or above to use judge alignment features
    
    Python
    
        %pip install --upgrade "mlflow[databricks]>=3.4.0" databricks_openai dspydbutils.library.restartPython()
    
*   A judge to align. This can be a [built-in judge](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/) (for example, `RelevanceToQuery` or `Correctness`) or a [custom judge](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) created with [`make_judge()`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/).
    
*   The human feedback assessment name must exactly match the judge's `name` attribute. For built-in judges, this is the default snake\_case name (for example, `relevance_to_query` for `RelevanceToQuery`) unless you override it by passing `name=` when instantiating the class. For custom judges, it's the `name` you passed to `make_judge()` (for example, `product_quality`).
    
*   Alignment is not supported for session-level (multi-turn) judges such as `ConversationCompleteness`.
    

## Step 1: Set up the judge and generate traces[​](#step-1-set-up-the-judge-and-generate-traces "Direct link to Step 1: Set up the judge and generate traces")

Set up your initial judge and generate traces with assessments. You can achieve reasonable alignment with at least 10 traces, but 50-100 traces yield better results.

*   Built-in judge
*   Custom judge

Instantiate a built-in judge directly. Built-in judges expose a `name` attribute (the default is a snake\_case string such as `relevance_to_query`) that you'll use when logging human feedback in Step 2.

Python

    from mlflow.genai.scorers import RelevanceToQueryimport mlflow# Create or set an MLflow experiment for alignment.# Use a workspace path such as /Shared/<name> or /Users/<your-email>/<name>.experiment = mlflow.set_experiment("/Shared/relevance-alignment")experiment_id = experiment.experiment_id# Use a built-in judgeinitial_judge = RelevanceToQuery()

Define your application logic. The following example uses a [Databricks-hosted foundation model](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models) to generate a product description from a query. Replace this with your own application code:

Python

    import mlflowfrom databricks_openai import DatabricksOpenAI# Enable automatic tracing of OpenAI callsmlflow.openai.autolog()# Create an OpenAI client connected to Databricks-hosted LLMsclient = DatabricksOpenAI()model_name = "databricks-claude-sonnet-4"def generate_product_description(query: str) -> str:    response = client.chat.completions.create(        model=model_name,        messages=[            {                "role": "system",                "content": "You write concise, accurate product descriptions.",            },            {"role": "user", "content": query},        ],    )    return response.choices[0].message.content

Generate traces and run the judge. Use the judge's `name` attribute (for example, `relevance_to_query` for the built-in judge above, or `product_quality` for the custom judge above) as the feedback `name`:

Python

    # Generate traces for alignment (minimum 10, recommended 50+)for i in range(50):    query = f"Tell me about product {i}"    description = generate_product_description(query)    # Retrieve the ID of the most recent finished trace    trace_id = mlflow.get_last_active_trace_id()    trace = mlflow.get_trace(trace_id)    # Generate judge assessment    judge_result = initial_judge(trace=trace)    # Log judge feedback to the trace using the judge's name    mlflow.log_feedback(        trace_id=trace_id,        name=initial_judge.name,        value=judge_result.value,        rationale=judge_result.rationale,    )

## Step 2: Collect human feedback[​](#step-2-collect-human-feedback "Direct link to Step 2: Collect human feedback")

Collect human feedback to teach the judge your quality standards. Choose from the following approaches:

*   Databricks UI review
*   Programmatic feedback

Collect human feedback when:

*   You need domain experts to review outputs.
*   You want to iteratively refine feedback criteria.
*   You're working with a smaller dataset (< 100 examples).

Use the MLflow UI to manually review and provide feedback:

1.  Navigate to your MLflow experiment in the Databricks workspace.
2.  Click on the **Traces** tab to see traces.
3.  Review each trace and its judge assessment.
4.  Add human feedback using the UI's feedback interface.
5.  Ensure the feedback name matches your judge's `name` attribute exactly (for example, `relevance_to_query` for a built-in `RelevanceToQuery` instance or `product_quality` for the custom judge above).

### Best practices for feedback collection[​](#best-practices-for-feedback-collection "Direct link to Best practices for feedback collection")

*   **Diverse reviewers**: Include multiple domain experts to capture varied perspectives
*   **Balanced examples**: Include at least 30% negative examples (poor/fair ratings)
*   **Clear rationales**: Provide detailed explanations for ratings
*   **Representative samples**: Cover edge cases and common scenarios

## Step 3: Align and register the judge[​](#step-3-align-and-register-the-judge "Direct link to Step 3: Align and register the judge")

Once you have sufficient human feedback, align the judge. The same `align()` method is used for both built-in and custom judges.

*   Default optimizer (recommended)
*   Explicit optimizer

When you call [`align()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.judges.Judge.align) without specifying an optimizer, the MemAlign optimizer is used automatically:

Python

    # Retrieve traces with both judge and human assessmentstraces_for_alignment = mlflow.search_traces(    experiment_ids=[experiment_id],    max_results=100,    return_type="list")if len(traces_for_alignment) >= 10:    # Align the judge based on human feedback using the default optimizer    aligned_judge = initial_judge.align(traces_for_alignment)    # Register the aligned judge for production use.    # Use a new name to distinguish it from the original judge.    aligned_judge.register(        experiment_id=experiment_id,        name=f"{initial_judge.name}_aligned",        tags={"alignment_date": "2025-10-23", "num_traces": str(len(traces_for_alignment))}    )    print(f"Successfully aligned judge using {len(traces_for_alignment)} traces")else:    print(f"Insufficient traces for alignment. Found {len(traces_for_alignment)}, need at least 10")

## Enable detailed logging[​](#enable-detailed-logging "Direct link to Enable detailed logging")

To monitor the alignment process, enable debug logging for the optimizer:

Python

    import logging# Enable detailed logginglogging.getLogger("mlflow.genai.judges.optimizers.memalign").setLevel(logging.DEBUG)# Run alignment with verbose outputaligned_judge = initial_judge.align(traces_for_alignment)

## Validate alignment[​](#validate-alignment "Direct link to Validate alignment")

Validate that alignment improved the judge:

Python

    def test_alignment_improvement(    original_judge, aligned_judge, test_traces: list) -> dict:    """Compare judge performance before and after alignment."""    original_correct = 0    aligned_correct = 0    for trace in test_traces:        # Get human ground truth from trace assessments        feedbacks = trace.search_assessments(type="feedback")        human_feedback = next(            (f for f in feedbacks if f.source.source_type == "HUMAN"), None        )        if not human_feedback:            continue        # Get judge evaluations        # Judges can evaluate entire traces instead of individual inputs/outputs        original_eval = original_judge(trace=trace)        aligned_eval = aligned_judge(trace=trace)        # Check agreement with human        if original_eval.value == human_feedback.value:            original_correct += 1        if aligned_eval.value == human_feedback.value:            aligned_correct += 1    total = len(test_traces)    return {        "original_accuracy": original_correct / total,        "aligned_accuracy": aligned_correct / total,        "improvement": (aligned_correct - original_correct) / total,    }

## Create custom alignment optimizers[​](#create-custom-alignment-optimizers "Direct link to Create custom alignment optimizers")

For specialized alignment strategies, extend the [`AlignmentOptimizer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.judges.base.AlignmentOptimizer) base class:

Python

    from mlflow.genai.judges.base import AlignmentOptimizer, Judgefrom mlflow.entities.trace import Traceclass MyCustomOptimizer(AlignmentOptimizer):    """Custom optimizer implementation for judge alignment."""    def __init__(self, model: str = None, **kwargs):        """Initialize your optimizer with custom parameters."""        self.model = model        # Add any custom initialization logic    def align(self, judge: Judge, traces: list[Trace]) -> Judge:        """        Implement your alignment algorithm.        Args:            judge: The judge to be optimized            traces: List of traces containing human feedback        Returns:            A new Judge instance with improved alignment        """        # Your custom alignment logic here        # 1. Extract feedback from traces        # 2. Analyze disagreements between judge and human        # 3. Generate improved instructions        # 4. Return new judge with better alignment        # Example: Return judge with modified instructions        from mlflow.genai.judges import make_judge        improved_instructions = self._optimize_instructions(judge.instructions, traces)        return make_judge(            name=judge.name,            instructions=improved_instructions,            model=judge.model,        )    def _optimize_instructions(self, instructions: str, traces: list[Trace]) -> str:        """Your custom optimization logic."""        # Implement your optimization strategy        pass# Create your custom optimizercustom_optimizer = MyCustomOptimizer(model="your-model")# Use it for alignmentaligned_judge = initial_judge.align(traces_with_feedback, custom_optimizer)

## Limitations[​](#limitations "Direct link to Limitations")

*   Judge alignment does not support agent-based or expectation-based evaluation.

## Next steps[​](#next-steps "Direct link to Next steps")

*   Learn about [production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) to deploy aligned judges at scale.
*   See [code-based scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers) for complementary deterministic metrics.
*   Learn more about building customized judges in [this Databricks blog](https://www.databricks.com/blog/building-custom-llm-judges-ai-agent-accuracy).
