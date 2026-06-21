---
title: Migrate to MLflow 3 from Agent Evaluation | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/agent-eval-migration
ingestedAt: "2026-06-18T08:14:26.750Z"
---

Agent Evaluation is now integrated with MLflow 3 on Databricks. The Agent Evaluation SDK methods are now exposed through the `mlflow[databricks]>=3.1` SDK, under the [`mlflow.genai`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html) namespace. MLflow 3 introduces:

*   **Refreshed UI** that mirrors all SDK functionality
*   **New SDK** [`mlflow.genai`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html) with simplified APIs for running evaluation, human labeling, and managing evaluation datasets
*   **Enhanced tracing** with a production-scale trace ingestion backend that provides real-time observability
*   **Streamlined human feedback** collection
*   **Improved LLM judges** as built-in scorers

This guide helps you migrate from Agent Evaluation (MLflow 2.x with `databricks-agents<1.0`) to MLflow 3. This detailed guide is also available in a [quick reference](https://docs.databricks.com/aws/en/mlflow3/genai/agent-eval-migration-reference) format.

important

MLflow 3 with Agent Evaluation only works on Managed MLflow, not open source MLflow. View the [managed vs. open source MLflow page](https://docs.databricks.com/aws/en/mlflow3/genai/overview/oss-managed-diff) to understand the differences between managed and open source MLflow in more depth.

## Migration checklist[​](#migration-checklist "Direct link to Migration checklist")

Get started by using this checklist. Each item links to details in sections below.

### [Evaluation API](#evaluation-api-migration)[​](#evaluation-api "Direct link to evaluation-api")

*   [Update imports from `databricks.agents` to `mlflow.genai.*`](#evaluation-import-updates)
*   [Convert `@metric` decorators to `@scorer`](#custom-metrics-to-scorers-migration)
    *   [Update custom metric/scorer function signatures](#scorer-changes)
*   [Replace `mlflow.evaluate()` with `mlflow.genai.evaluate()`](#evaluation-api-migration)
    *   [Update parameter names (`model` → `predict_fn`, `extra_metrics` → `scorers`)](#evaluation-api-changes)
    *   [Update data field names (`request` → `inputs`, `response` → `outputs`, `expected*` → `expectations`)](#data-field-mapping)
    *   [Replace `evaluator_config` with scorer-level configuration](#llm-judges-migration)
    *   [Update result access to use `mlflow.search_traces()`](#accessing-evaluation-results)

### [LLM judges](#llm-judges-migration)[​](#llm-judges "Direct link to llm-judges")

*   [Replace direct judge calls with predefined scorers where possible](#predefined-judge-scorers)
*   [Update `judges.guideline_adherence()` to `judges.meets_guidelines()` or `Guidelines()` scorer](#guideline-adherence-migration)
*   [Update judge function parameter names to match new API](#llm-judges-migration)
*   [Consider using `ExpectationsGuidelines()` for ground-truth based guidelines](#migrating-expectation-guidelines)

### [Human feedback](#human-feedback-migration)[​](#human-feedback "Direct link to human-feedback")

*   [Update labeling session and review app imports to `mlflow.genai.labeling`](#human-feedback-migration)
*   [Update label schema imports to `mlflow.genai.label_schemas`](#labeling-api-changes)
*   [Update logic for syncing feedback to datasets](#syncing-feedback-to-datasets)

### Common pitfalls to avoid[​](#common-pitfalls-to-avoid "Direct link to Common pitfalls to avoid")

*   Remember to update data field names in your DataFrames
*   Remember that `model_type="databricks-agent"` is no longer needed
*   Ensure custom scorers return valid values ("yes"/"no" for pass/fail)
*   Use `search_traces()` instead of accessing result tables directly
*   Update any hardcoded namespace references in your code
*   **Remember to explicitly specify all scorers** - MLflow 3 does not automatically run judges
*   Convert `global_guidelines` from config to explicit `Guidelines()` scorers

## Evaluation API migration[​](#-evaluation-api-migration "Direct link to -evaluation-api-migration")

### Import updates[​](#-import-updates "Direct link to -import-updates")

The list below summarizes imports to update, with details and examples in each subsection below.

Python

    # Old importsfrom mlflow import evaluatefrom databricks.agents.evals import metricfrom databricks.agents.evals import judges# New importsfrom mlflow.genai import evaluatefrom mlflow.genai.scorers import scorerfrom mlflow.genai import judges# For predefined scorers:from mlflow.genai.scorers import (    Correctness, Guidelines, ExpectationsGuidelines,    RelevanceToQuery, Safety, RetrievalGroundedness,    RetrievalRelevance, RetrievalSufficiency)

### From `mlflow.evaluate()` to `mlflow.genai.evaluate()`[​](#from-mlflowevaluate-to-mlflowgenaievaluate "Direct link to from-mlflowevaluate-to-mlflowgenaievaluate")

The core evaluation API has moved to a dedicated GenAI namespace with cleaner parameter names.

**Key API changes:**

**Data field mapping:**

#### Example: Basic evaluation[​](#example-basic-evaluation "Direct link to Example: Basic evaluation")

**MLflow 2.x:**

Python

    import mlflowimport pandas as pdeval_data = [        {            "request":  "What is MLflow?",            "response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models.",            "expected_response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models.",        },        {            "request":  "What is Databricks?",            "response": "Databricks is a unified analytics platform.",            "expected_response": "Databricks is a unified analytics platform for big data and AI.",        },    ]# Note: By default, MLflow 2.x runs all applicable judges automaticallyresults = mlflow.evaluate(    data=eval_data,    model=my_agent,    model_type="databricks-agent",    evaluator_config={        "databricks-agent": {            # Optional: limit to specific judges            # "metrics": ["correctness", "safety"],            # Optional: add global guidelines            "global_guidelines": {                "clarity": ["Response must be clear and concise"]            }        }    })# Access resultseval_df = results.tables['eval_results']

**MLflow 3.x:**

Python

    import mlflowimport pandas as pdfrom mlflow.genai.scorers import Guidelineseval_data = [        {            "inputs": {"request": "What is MLflow?"},            "outputs": {                "response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models."            },            "expectations": {                "expected_response":                    "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models.",            },        },        {            "inputs": {"request": "What is Databricks?"},            "outputs": {"response": "Databricks is a unified analytics platform."},            "expectations": {                "expected_response":                    "Databricks is a unified analytics platform for big data and AI.",            },        },    ]# Define guidelines for scorerguidelines = {    "clarity": ["Response must be clear and concise"],    # supports str or list[str]    "accuracy": "Response must be factually accurate",}print("Running evaluation with mlflow.genai.evaluate()...")with mlflow.start_run(run_name="basic_evaluation_test") as run:    # Run evaluation with new API    # Note: Must explicitly specify which scorers to run (no automatic selection)    results = mlflow.genai.evaluate(        data=eval_data,        scorers=[            Correctness(),  # Requires expectations.expected_response            RelevanceToQuery(),  # No ground truth needed            Guidelines(name="clarity", guidelines=guidelines["clarity"]),            Guidelines(name="accuracy", guidelines=guidelines["accuracy"]),            # ExpectationsGuidelines(),            # Add more scorers as needed: Safety(), RetrievalGroundedness(), etc.        ],    )# Access results using search_tracestraces = mlflow.search_traces(        run_id=results.run_id,)

### Accessing evaluation results[​](#-accessing-evaluation-results "Direct link to -accessing-evaluation-results")

In MLflow 3, evaluation results are stored as traces with assessments. Use `mlflow.search_traces()` to access detailed results:

Python

    # Access results using search_tracestraces = mlflow.search_traces(    run_id=results.run_id,)# Access assessments for each tracefor trace in traces:    assessments = trace.info.assessments    for assessment in assessments:        print(f"Scorer: {assessment.name}")        print(f"Value: {assessment.value}")        print(f"Rationale: {assessment.rationale}")

### Evaluating an MLflow LoggedModel[​](#evaluating-an-mlflow-loggedmodel "Direct link to Evaluating an MLflow LoggedModel")

In MLflow 2.x, you could pass a logged MLflow model (such as a PyFunc model or one logged by [Custom Agents](https://docs.databricks.com/aws/en/generative-ai/agent-framework/author-agent-model-serving)) directly to `mlflow.evaluate()`. In MLflow 3.x, you need to wrap the model in a predict function to handle parameter mapping.

This wrapper is necessary because `mlflow.genai.evaluate()` expects a predict function that accepts the keys in the `inputs` dict from your dataset as keyword arguments, while most logged models accept a single input parameter (e.g., `model_inputs` for PyFunc models or similar interfaces for LangChain models).

The predict function serves as a translation layer between the evaluation framework's named parameters and the model's expected input format.

Python

    import mlflowfrom mlflow.genai.scorers import Safety# Make sure to load your logged model outside of the predict_fn so MLflow only loads it once!model = mlflow.pyfunc.load_model("models:/chatbot/staging")def evaluate_model(question: str) -> dict:    return model.predict({"question": question})results = mlflow.genai.evaluate(    data=[{"inputs": {"question": "Tell me about MLflow"}}],    predict_fn=evaluate_model,    scorers=[Safety()])

### Custom metrics to scorers migration[​](#-custom-metrics-to-scorers-migration "Direct link to -custom-metrics-to-scorers-migration")

Custom evaluation functions (`@metric`) now use the `@scorer` decorator with a simplified signature.

**Key changes:**

#### Example: Pass/fail scorer[​](#example-passfail-scorer "Direct link to Example: Pass/fail scorer")

**MLflow 2.x:**

Python

    from databricks.agents.evals import metric@metricdef response_length_check(request, response, expected_response=None):    """Check if response is within acceptable length."""    length = len(response)    return "yes" if 50 <= length <= 500 else "no"# Use in evaluationresults = mlflow.evaluate(    data=eval_data,    model=my_agent,    model_type="databricks-agent",    extra_metrics=[response_length_check])

**MLflow 3.x:**

Python

    import mlflowfrom mlflow.genai.scorers import scorer# Sample agent function@mlflow.tracedef my_agent(request: str):    """Simple mock agent for testing - MLflow 3 expects dict input"""    responses = {        "What is MLflow?": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models.",        "What is Databricks?": "Databricks is a unified analytics platform.",    }    return {"response": responses.get(request, "I don't have information about that.")}@scorerdef response_length_check(inputs, outputs, expectations=None, traces=None):    """Check if response is within acceptable length."""    length = len(outputs)    return "yes" if 50 <= length <= 500 else "no"# Use in evaluationresults = mlflow.genai.evaluate(    data=eval_data,    predict_fn=my_agent,    scorers=[response_length_check])

#### Example: Numeric scorer with Assessment[​](#example-numeric-scorer-with-assessment "Direct link to Example: Numeric scorer with Assessment")

**MLflow 2.x:**

Python

    from databricks.agents.evals import metric, Assessmentdef calculate_similarity(response, expected_response):    return 1@metricdef semantic_similarity(response, expected_response):    """Calculate semantic similarity score."""    # Your similarity logic here    score = calculate_similarity(response, expected_response)    return Assessment(        name="semantic_similarity",        value=score,        rationale=f"Similarity score based on embedding distance: {score:.2f}"    )

**MLflow 3.x:**

Python

    from mlflow.genai.scorers import scorerfrom mlflow.entities import Feedback@scorerdef semantic_similarity(outputs, expectations):    """Calculate semantic similarity score."""    # Your similarity logic here    expected = expectations.get("expected_response", "")    score = calculate_similarity(outputs, expected)    return Feedback(        name="semantic_similarity",        value=score,        rationale=f"Similarity score based on embedding distance: {score:.2f}"    )

## LLM judges migration[​](#-llm-judges-migration "Direct link to -llm-judges-migration")

### Key differences in judge behavior[​](#key-differences-in-judge-behavior "Direct link to Key differences in judge behavior")

**Automatic judge selection:**

**MLflow 2.x automatic judge selection:**

*   Without ground truth: runs `chunk_relevance`, `groundedness`, `relevance_to_query`, `safety`, `guideline_adherence`
*   With ground truth: also runs `context_sufficiency`, `correctness`

**MLflow 3.x explicit scorer selection:**

*   You must explicitly list scorers you want to run
*   More control but requires being explicit about evaluation needs

### Migration paths[​](#migration-paths "Direct link to Migration paths")

MLflow 3 provides two ways to use LLM judges:

1.  **Predefined scorers** - Ready-to-use scorers that wrap judges with automatic trace parsing
2.  **Direct judge calls** - Call judges directly within custom scorers for more control

### Controlling which judges run[​](#controlling-which-judges-run "Direct link to Controlling which judges run")

#### Example: Specifying judges to run[​](#example-specifying-judges-to-run "Direct link to Example: Specifying judges to run")

**MLflow 2.x (limiting default judges):**

Python

    import mlflow# By default, runs all applicable judges# Use evaluator_config to limit which judges runresults = mlflow.evaluate(    data=eval_data,    model=my_agent,    model_type="databricks-agent",    evaluator_config={        "databricks-agent": {            # Only run these specific judges            "metrics": ["groundedness", "relevance_to_query", "safety"]        }    })

**MLflow 3.x (explicit scorer selection):**

Python

    from mlflow.genai.scorers import (    RetrievalGroundedness,    RelevanceToQuery,    Safety)# Must explicitly specify which scorers to runresults = mlflow.genai.evaluate(    data=eval_data,    predict_fn=my_agent,    scorers=[        RetrievalGroundedness(),        RelevanceToQuery(),        Safety()    ])

### Comprehensive migration example[​](#comprehensive-migration-example "Direct link to Comprehensive migration example")

This example shows migrating an evaluation that uses multiple judges with custom configuration:

**MLflow 2.x:**

Python

    from databricks.agents.evals import judges, metricimport mlflow# Custom metric using judge@metricdef check_no_pii(request, response, retrieved_context):    """Check if retrieved context contains PII."""    context_text = '\n'.join([c['content'] for c in retrieved_context])    return judges.guideline_adherence(        request=request,        guidelines=["The context must not contain personally identifiable information."],        guidelines_context={"retrieved_context": context_text}    )# Define global guidelinesglobal_guidelines = {    "tone": ["Response must be professional and courteous"],    "format": ["Response must use bullet points for lists"]}# Run evaluation with multiple judgesresults = mlflow.evaluate(    data=eval_data,    model=my_agent,    model_type="databricks-agent",    evaluator_config={        "databricks-agent": {            # Specify subset of built-in judges            "metrics": ["correctness", "groundedness", "safety"],            # Add global guidelines            "global_guidelines": global_guidelines        }    },    # Add custom judge    extra_metrics=[check_no_pii])

**MLflow 3.x:**

Python

    from mlflow.genai.scorers import (    Correctness,    RetrievalGroundedness,    Safety,    Guidelines,    scorer)from mlflow.genai import judgesimport mlflow# Custom scorer using judge@scorerdef check_no_pii(inputs, outputs, traces):    """Check if retrieved context contains PII."""    # Extract retrieved context from trace    retrieved_context = traces.data.spans[0].attributes.get("retrieved_context", [])    context_text = '\n'.join([c['content'] for c in retrieved_context])    return judges.meets_guidelines(        name="no_pii",        context={            "request": inputs,            "retrieved_context": context_text        },        guidelines=["The context must not contain personally identifiable information."]    )# Run evaluation with explicit scorersresults = mlflow.genai.evaluate(    data=eval_data,    predict_fn=my_agent,    scorers=[        # Built-in scorers (explicitly specified)        Correctness(),        RetrievalGroundedness(),        Safety(),        # Global guidelines as scorers        Guidelines(name="tone", guidelines="Response must be professional and courteous"),        Guidelines(name="format", guidelines="Response must use bullet points for lists"),        # Custom scorer        check_no_pii    ])

### Migrating to predefined judge scorers[​](#-migrating-to-predefined-judge-scorers "Direct link to -migrating-to-predefined-judge-scorers")

MLflow 3 provides predefined scorers that wrap the LLM judges, making them easier to use with `mlflow.genai.evaluate()`.

#### Example: Correctness judge[​](#example-correctness-judge "Direct link to Example: Correctness judge")

**MLflow 2.x:**

Python

    from databricks.agents.evals import judges, metric@metricdef check_correctness(request, response, expected_response):    """Check if response is correct."""    return judges.correctness(        request=request,        response=response,        expected_response=expected_response    )# Use in evaluationresults = mlflow.evaluate(    data=eval_data,    model=my_agent,    model_type="databricks-agent",    extra_metrics=[check_correctness])

**MLflow 3.x (Option 1: Using predefined scorer):**

Python

    from mlflow.genai.scorers import Correctness# Use predefined scorer directlyresults = mlflow.genai.evaluate(    data=eval_data,    predict_fn=my_agent,    scorers=[Correctness()])

**MLflow 3.x (Option 2: Custom scorer with judge):**

Python

    from mlflow.genai.scorers import scorerfrom mlflow.genai import judges@scorerdef check_correctness(inputs, outputs, expectations):    """Check if response is correct."""    return judges.correctness(        request=inputs,        response=outputs,        expected_response=expectations.get("expected_response", "")    )# Use in evaluationresults = mlflow.genai.evaluate(    data=eval_data,    predict_fn=my_agent,    scorers=[check_correctness])

#### Example: Safety judge[​](#example-safety-judge "Direct link to Example: Safety judge")

**MLflow 2.x:**

Python

    from databricks.agents.evals import judges, metric@metricdef check_safety(request, response):    """Check if response is safe."""    return judges.safety(        request=request,        response=response    )

**MLflow 3.x:**

Python

    from mlflow.genai.scorers import Safety# Use predefined scorerresults = mlflow.genai.evaluate(    data=eval_data,    predict_fn=my_agent,    scorers=[Safety()])

#### Example: Relevance judge[​](#example-relevance-judge "Direct link to Example: Relevance judge")

**MLflow 2.x:**

Python

    from databricks.agents.evals import judges, metric@metricdef check_relevance(request, response):    """Check if response is relevant to query."""    return judges.relevance_to_query(        request=request,        response=response    )

**MLflow 3.x:**

Python

    from mlflow.genai.scorers import RelevanceToQuery# Use predefined scorerresults = mlflow.genai.evaluate(    data=eval_data,    predict_fn=my_agent,    scorers=[RelevanceToQuery()])

#### Example: Groundedness judge[​](#example-groundedness-judge "Direct link to Example: Groundedness judge")

**MLflow 2.x:**

Python

    from databricks.agents.evals import judges, metric@metricdef check_groundedness(response, retrieved_context):    """Check if response is grounded in context."""    context_text = '\n'.join([c['content'] for c in retrieved_context])    return judges.groundedness(        response=response,        context=context_text    )

**MLflow 3.x:**

Python

    from mlflow.genai.scorers import RetrievalGroundedness# Use predefined scorer (automatically extracts context from trace)results = mlflow.genai.evaluate(    data=eval_data,    predict_fn=my_agent,    scorers=[RetrievalGroundedness()])

### Migrating guideline adherence to meets\_guidelines[​](#-migrating-guideline-adherence-to-meets_guidelines "Direct link to -migrating-guideline-adherence-to-meets_guidelines")

The `guideline_adherence` judge has been renamed to `meets_guidelines` with a cleaner API.

**MLflow 2.x:**

Python

    from databricks.agents.evals import judges, metric@metricdef check_tone(request, response):    """Check if response follows tone guidelines."""    return judges.guideline_adherence(        request=request,        response=response,        guidelines=["The response must be professional and courteous."]    )@metricdef check_policies(request, response, retrieved_context):    """Check if response follows company policies."""    context_text = '\n'.join([c['content'] for c in retrieved_context])    return judges.guideline_adherence(        request=request,        guidelines=["Response must comply with return policy in context."],        guidelines_context={            "response": response,            "retrieved_context": context_text        }    )

**MLflow 3.x (Option 1: Using predefined Guidelines scorer):**

Python

    from mlflow.genai.scorers import Guidelines# For simple guidelines that only need request/responseresults = mlflow.genai.evaluate(    data=eval_data,    predict_fn=my_agent,    scorers=[        Guidelines(            name="tone",            guidelines="The response must be professional and courteous."        )    ])

**MLflow 3.x (Option 2: Custom scorer with meets\_guidelines):**

Python

    from mlflow.genai.scorers import scorerfrom mlflow.genai import judges@scorerdef check_policies(inputs, outputs, traces):    """Check if response follows company policies."""    # Extract retrieved context from trace    retrieved_context = traces.data.spans[0].attributes.get("retrieved_context", [])    context_text = '\n'.join([c['content'] for c in retrieved_context])    return judges.meets_guidelines(        name="policy_compliance",        guidelines="Response must comply with return policy in context.",        context={            "request": inputs,            "response": outputs,            "retrieved_context": context_text        }    )

#### Example: Migrating ExpectationsGuidelines[​](#-example-migrating-expectationsguidelines "Direct link to -example-migrating-expectationsguidelines")

When you want to set guidelines for each example in your evaluation set, such as requiring that certain topics are covered, or that the response follows a specific style, use the `ExpectationsGuidelines` scorer in MLflow 3.x.

**MLflow 2.x:**

In MLflow 2.x, you would implement guidelines as follows:

Python

    import pandas as pdeval_data = {    "request": "What is MLflow?",    "response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models.",    "guidelines": [        ["The response must mention these topics: platform, observability, testing"]    ],}eval_df = pd.DataFrame(eval_data)mlflow.evaluate(    data=eval_df,    model_type="databricks-agent",    evaluator_config={        "databricks-agent": {"metrics": ["guideline_adherence"]}    })

**MLflow 3.x:**

In MLflow 3.x, you organize evaluation data differently. Each entry in your evaluation data should have an `expectations` key, and inside that, you can include fields like `guidelines`.

Here's what your evaluation data might look like:

Python

    eval_data = [    {        "inputs": {"input": "What is MLflow?"},        "outputs": {"response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models."},        "expectations": {            "guidelines": [                "The response should mention the topics: platform, observability, and testing."            ]        }    }]

Then, use the `ExpectationsGuidelines` scorer:

Python

    import mlflowfrom mlflow.genai.scorers import ExpectationsGuidelinesexpectations_guideline = ExpectationsGuidelines()# Use predefined scorerresults = mlflow.genai.evaluate(    data=eval_data,  # Make sure each row has expectations.guidelines    predict_fn=my_app,    scorers=[        expectations_guideline    ])

tip

If you need to check for specific factual content (e.g., "MLflow is open-source"), use the Correctness scorer with an `expected_facts` field instead of guidelines. See [Correctness judge](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/is_correct).

### Replicating MLflow 2.x automatic judge behavior[​](#replicating-mlflow-2x-automatic-judge-behavior "Direct link to Replicating MLflow 2.x automatic judge behavior")

To replicate MLflow 2.x behavior of running all applicable judges, explicitly include all scorers:

**MLflow 2.x (automatic):**

Python

    # Automatically runs all applicable judges based on dataresults = mlflow.evaluate(    data=eval_data,  # Contains expected_response and retrieved_context    model=my_agent,    model_type="databricks-agent")

**MLflow 3.x (explicit):**

Python

    from mlflow.genai.scorers import (    Correctness, RetrievalSufficiency,  # Require ground truth    RelevanceToQuery, Safety, RetrievalGroundedness, RetrievalRelevance  # No ground truth)# Manually specify all judges you want to runresults = mlflow.genai.evaluate(    data=eval_data,    predict_fn=my_agent,    scorers=[        # With ground truth judges        Correctness(),        RetrievalSufficiency(),        # Without ground truth judges        RelevanceToQuery(),        Safety(),        RetrievalGroundedness(),        RetrievalRelevance(),    ])

### Direct judge usage[​](#direct-judge-usage "Direct link to Direct judge usage")

You can still call judges directly for testing:

Python

    from mlflow.genai import judges# Test a judge directly (same in both versions)result = judges.correctness(    request="What is MLflow?",    response="MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models.",    expected_response="MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models.")print(f"Judge result: {result.value}")print(f"Rationale: {result.rationale}")

## Human feedback migration[​](#-human-feedback-migration "Direct link to -human-feedback-migration")

### Labeling sessions and schemas[​](#-labeling-sessions-and-schemas "Direct link to -labeling-sessions-and-schemas")

The Review App functionality has moved from `databricks.agents` to `mlflow.genai.labeling`.

**Namespace changes:**

#### Example: Creating a labeling session[​](#example-creating-a-labeling-session "Direct link to Example: Creating a labeling session")

**MLflow 2.x:**

Python

    from databricks.agents import review_appimport mlflow# Get review appmy_app = review_app.get_review_app()# Create custom label schemaquality_schema = my_app.create_label_schema(    name="response_quality",    type="feedback",    title="Rate the response quality",    input=review_app.label_schemas.InputCategorical(        options=["Poor", "Fair", "Good", "Excellent"]    ))# Create labeling sessionsession = my_app.create_labeling_session(    name="quality_review_jan_2024",    agent="my_agent",    assigned_users=["user1@company.com", "user2@company.com"],    label_schemas=[        review_app.label_schemas.EXPECTED_FACTS,        "response_quality"    ])# Add traces for labelingtraces = mlflow.search_traces(run_id=run_id)session.add_traces(traces)

**MLflow 3.x:**

Python

    import mlflowimport mlflow.genai.labeling as labelingimport mlflow.genai.label_schemas as schemas# Create custom label schemaquality_schema = schemas.create_label_schema(    name="response_quality",    type=schemas.LabelSchemaType.FEEDBACK,    title="Rate the response quality",    input=schemas.InputCategorical(        options=["Poor", "Fair", "Good", "Excellent"]    ),    overwrite=True)# Previously built in schemas must be created before use# However, constant for their names are provided to ensure your schemas work with built-in scorersexpected_facts_schema = schemas.create_label_schema(    name=schemas.EXPECTED_FACTS,    type=schemas.LabelSchemaType.EXPECTATION,    title="Expected facts",    input=schemas.InputTextList(max_length_each=1000),    instruction="Please provide a list of facts that you expect to see in a correct response.",    overwrite=True)# Create labeling sessionsession = labeling.create_labeling_session(    name="quality_review_jan_2024",    assigned_users=["user1@company.com", "user2@company.com"],    label_schemas=[        schemas.EXPECTED_FACTS,        "response_quality"    ])# Add traces for labelingtraces = mlflow.search_traces(    run_id=session.mlflow_run_id)session.add_traces(traces)# Get review app URLapp = labeling.get_review_app()print(f"Review app URL: {app.url}")

### Syncing feedback to datasets[​](#-syncing-feedback-to-datasets "Direct link to -syncing-feedback-to-datasets")

**MLflow 2.x:**

Python

    # Sync expectations back to datasetsession.sync(to_dataset="catalog.schema.eval_dataset")# Use dataset for evaluationdataset = spark.read.table("catalog.schema.eval_dataset")results = mlflow.evaluate(    data=dataset,    model=my_agent,    model_type="databricks-agent")

**MLflow 3.x:**

Python

    from mlflow.genai import datasetsimport mlflow# Sample agent function@mlflow.tracedef my_agent(request: str):    """Simple mock agent for testing - MLflow 3 expects dict input"""    responses = {        "What is MLflow?": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models.",        "What is Databricks?": "Databricks is a unified analytics platform.",    }    return {"response": responses.get(request, "I don't have information about that.")}# Sync expectations back to datasetsession.sync(to_dataset="catalog.schema.eval_dataset")# Use dataset for evaluationdataset = datasets.get_dataset("catalog.schema.eval_dataset")results = mlflow.genai.evaluate(    data=dataset,    predict_fn=my_agent)

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [MLflow 3 GenAI Evaluation Guide](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app)
*   [Custom Scorers Documentation](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers)
*   [Human Feedback with labeling sessions](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/concepts/labeling-sessions)
*   [Predefined Judge Scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers)
*   [MLflow Tracing Guide](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/)

For additional support during migration, consult the MLflow documentation or reach out to your Databricks support team.
