---
title: "Tutorial: Trace and analyze users and environments | Databricks on AWS"
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/add-context-to-traces-tutorial
ingestedAt: "2026-06-18T08:16:26.663Z"
---

This tutorial demonstrates adding context to traces in order to track and analyze users, sessions, and deployments.

*   In a simple chat app, you will use [`mlflow.update_current_trace()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace) to add custom metadata and tags to traces.
*   To analyze traces, you will use [`mlflow.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_traces) to extract relevant traces and compute statistics for users, sessions, environments, and app versions.

## Environment setup[​](#environment-setup "Direct link to Environment setup")

Install required packages:

*   `mlflow[databricks]`: Use the latest version of MLflow to get more features and improvements.
*   `openai`: This app will use the OpenAI API client to call Databricks-hosted models.

Python

    %pip install -qq --upgrade "mlflow[databricks]>=3.1.0" openaidbutils.library.restartPython()

Create an MLflow experiment. If you are using a Databricks notebook, you can skip this step and use the default notebook experiment. Otherwise, follow the [environment setup quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment) to create the experiment and connect to the MLflow Tracking server.

## Define and trace your application[​](#define-and-trace-your-application "Direct link to Define and trace your application")

The simple chat application below calls a [Databricks-hosted foundation model](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models) to answer user queries.

Tracing is done using:

*   `mlflow.openai.autolog()` to autolog OpenAI client calls
*   `@mlflow.trace` to trace the application logic in `my_app()`
*   `mlflow.update_current_trace()` to add context to traces within `my_app()`:
    *   User and session context: Query-specific information like user IDs can be passed to the application logic as arguments.
    *   Deployment context: Deployment-specific information like the environment or app version are passed to the application through environment variables, which simplifies configuration changes across deployments.

MLflow automatically populates some metadata in traces, but you can override the default values. You can also define custom metadata. The example below demonstrates both.

Python

    import mlflowimport osfrom databricks_openai import DatabricksOpenAImlflow.openai.autolog()@mlflow.tracedef my_app(user_id: str, session_id: str, message: str) -> str:    """Process a chat message with extra content logging for traces."""    # Add user and session context to the current trace.    # The @mlflow.trace decorator ensures there is an active trace.    mlflow.update_current_trace(        metadata={            "mlflow.trace.user": user_id,            "mlflow.trace.session": session_id,        },        tags={          "query_category": "chat",  # Example of a custom tag        },    )    app_environment = os.getenv("APP_ENVIRONMENT", "development")    mlflow.update_current_trace(        metadata={            # Override automatically populated metadata            "mlflow.source.type": app_environment,  # Override default LOCAL/NOTEBOOK            # Add custom metadata            "app_version": os.getenv("APP_VERSION", "1.0.0"),            "deployment_id": os.getenv("DEPLOYMENT_ID", "unknown"),        }    )    # The trace will capture the execution time, inputs, outputs, and any errors    # Your chat logic here    response = chat_completion(message)    return response# Basic chat logicdef chat_completion(message: str) -> str:    # Create an OpenAI client that is connected to Databricks-hosted LLMs    client = DatabricksOpenAI()    response = client.chat.completions.create(        model="databricks-claude-sonnet-4",        messages=[            {                "role": "system",                "content": "You are a helpful assistant. Give brief, 1-2 sentence responses.",            },            {                "role": "user",                "content": message,            },        ]    )    return response.choices[0].message.content

The application logic above takes user, session, and other metadata as function arguments. In a production application, the implementation might extract metadata from headers in a request object. For example, if the application is deployed as a [Databricks App](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/), then the app can [access HTTP headers with metadata](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/http-headers).

Next, simulate a few different users and sessions, each with one or more chat interactions. Set deployment information using environment variables.

Python

    # Set environment variables to log deployment-specific metadata with traces.os.environ["APP_ENVIRONMENT"] = "staging"os.environ["APP_VERSION"] = "1.0.0"os.environ["DEPLOYMENT_ID"] = "deployment-123"# Run the chat completion with user and session context to generate example traces:for session in range(2):  # 2 chat interactions per session for this user  result = my_app(      user_id="user-123",      session_id=f"session-abc-{session}",      message="What is MLflow and how does it help with GenAI?"  )  result = my_app(      user_id="user-123",      session_id=f"session-abc-{session}",      message="What is ML vs. AI?"  )os.environ["APP_VERSION"] = "1.1.0"os.environ["DEPLOYMENT_ID"] = "deployment-456"for session in range(2):  # 1 chat interaction per session for this user  result = my_app(      user_id="user-456",      session_id=f"session-def-{session}",      message="What is MLflow and how does it help with machine learning?"  )

## Search traces[​](#search-traces "Direct link to Search traces")

All of the analytics below are based on using `mlflow.search_traces()` to collect relevant traces for analysis:

Python

    import mlflowtraces = mlflow.search_traces()traces

Each trace is annotated with the additional context logged in the app, such as user IDs:

Python

    first_trace = traces.iloc[0]first_trace.trace_metadata['mlflow.trace.user']

## Analyze user behavior[​](#analyze-user-behavior "Direct link to Analyze user behavior")

First, analyze the behavior of a specific user.

Python

    import pandas as pdimport timedef analyze_user_behavior(user_id: str, days: int = 7):    """Analyze activity patterns for a specific user."""    cutoff_ms = int((time.time() - days * 86400) * 1000)    traces = mlflow.search_traces(        filter_string=f"metadata.`mlflow.trace.user` = '{user_id}' AND "                      f"trace.timestamp_ms > {cutoff_ms}",        order_by=["trace.timestamp_ms DESC"],    )    if len(traces) == 0:        print(f"No activity found for user {user_id}")        return    # Calculate key metrics    total_interactions = len(traces)    unique_sessions = set(row.trace_metadata.get("mlflow.trace.session", "") for index, row in traces.iterrows())    unique_sessions.discard("")    print(f"User {user_id} Activity Report ({days} days)")    print("=" * 50)    print(f"Total interactions: {total_interactions}")    print(f"Unique sessions: {len(unique_sessions)}")    # Daily activity    traces['date'] = pd.to_datetime(traces['request_time'], unit='ms').dt.date    daily_activity = traces.groupby('date').size()    print(f"\nDaily activity:")    print(daily_activity.to_string())    # Query categories    query_categories = traces['tags'].apply(lambda tags: tags.get('query_category'))    unique_categories = set(query_categories.dropna())    category_counts = query_categories.value_counts()    print(f"\nQuery categories:")    print(category_counts.to_string())    # Performance stats    print(f"\nPerformance:")    print(f"Average response time: {traces['execution_duration'].mean():.1f}ms")    print(f"Error rate: {(traces['state'] == 'ERROR').mean() * 100:.1f}%")    return traces

Python

    analyze_user_behavior(user_id="user-123")

Output

    User user-123 Activity Report (7 days)==================================================Total interactions: 4Unique sessions: 2Daily activity:date2025-12-12    4Query categories:tagschat    4Performance:Average response time: 2177.5msError rate: 0.0%

## Analyze session flow[​](#analyze-session-flow "Direct link to Analyze session flow")

A user may engage with your application for conversations with multiple turns. Analyzing the session turn-by-turn can help to illustrate the user's experience. Below, the conversation turns are put in order using trace timestamps.

Python

    def analyze_session_flow(session_id: str):    """Analyze conversation flow within a session."""    # Get all traces from a session, ordered chronologically    session_traces = mlflow.search_traces(        filter_string=f"metadata.`mlflow.trace.session` = '{session_id}'",        order_by=["timestamp ASC"]    )    # Build a timeline of the conversation    conversation_turns = []    for index, row in session_traces.iterrows():        conversation_turns.append({            "turn": index + 1,            "timestamp": int(row.request_time),            "duration_ms": int(row.execution_duration),            "status": str(row.state),            "response": row.response,        })    return conversation_turns

Python

    analyze_session_flow(session_id="session-abc-0")

Output

    [{'turn': 1,  'timestamp': 1765560306051,  'duration_ms': 2570,  'status': 'OK',  'response': 'MLflow is an open-source platform for managing the machine learning lifecycle, including experiment tracking, model packaging, and deployment. For GenAI, it helps by providing tools to track experiments with large language models, manage model versions, log prompts and responses, and deploy AI models at scale while maintaining reproducibility and governance.'}, {'turn': 2,  'timestamp': 1765560308943,  'duration_ms': 2644,  'status': 'OK',  'response': 'AI (Artificial Intelligence) is the broader field focused on creating machines that can perform tasks requiring human-like intelligence, while ML (Machine Learning) is a subset of AI that specifically uses algorithms to learn patterns from data without being explicitly programmed for each task. Think of AI as the goal and ML as one of the main methods to achieve it.'}]

## Analyze environments and versions[​](#analyze-environments-and-versions "Direct link to Analyze environments and versions")

Deployment metadata such as environment or app version can be analyzed similarly to users and sessions. Analyzing deployments can help to track improvements or degradations to quality, latency, or other important metrics as you iterate on your application.

Python

    traces = mlflow.search_traces()traces['app_version'] = traces['trace_metadata'].apply(lambda meta: meta.get('app_version'))traces['user_id'] = traces['trace_metadata'].apply(lambda meta: meta.get('mlflow.trace.user'))traces['app_environment'] = traces['trace_metadata'].apply(lambda meta: meta.get('mlflow.source.type'))interactions_per_version = traces.groupby('app_version').size()print(f"Interactions per app version:")print(interactions_per_version.to_string())users_per_version = traces.groupby('app_version')['user_id'].nunique()print(f"\nDistinct users per app version:")print(users_per_version.to_string())interactions_per_environment = traces.groupby('app_environment').size()print(f"\nInteractions per app environment:")print(interactions_per_environment.to_string())

Output

    Interactions per app version:app_version1.0.0    41.1.0    4Distinct users per app version:app_version1.0.0    11.1.0    1Interactions per app environment:app_environmentstaging    8

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Add context to traces](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/add-context-to-traces) - Learn more about adding custom metadata and tags to traces.
*   [Search traces programmatically](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/query-via-sdk) - Learn more about using [mlflow.search\_traces()](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_traces).
*   [Analyze traces](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/analyze-traces) - See other examples of trace analytics.

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Tutorial: Trace and analyze users and environments
