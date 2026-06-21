---
title: Tracing CrewAI | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/crewai
ingestedAt: "2026-06-18T08:17:03.052Z"
---

![CrewAI Tracing using autolog](https://assets.docs.databricks.com/_static/images/mlflow3/tracing/crewai-tracing.gif)

[CrewAI](https://www.crewai.com/) is an open-source framework for orchestrating role-playing, autonomous AI agent.

[MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) provides automatic tracing capability for [CrewAI](https://www.crewai.com/), an open source framework for building multi-agent applications. By enabling auto tracing for CrewAI by calling the [`mlflow.crewai.autolog`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.crewai.html#mlflow.crewai.autolog) function, MLflow will capture nested traces for CrewAI workflow execution and log them to the active MLflow Experiment.

Python

    import mlflowmlflow.crewai.autolog()

note

On serverless compute clusters, autologging for genAI tracing frameworks is not automatically enabled. You must explicitly enable autologging by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace.

MLflow trace automatically captures the following information about CrewAI agents:

*   Tasks and Agent who executes each task
*   Every LLM calls with input prompts, completion responses, and various metadata
*   Memory load and writes operations
*   Latency of each operation
*   Any exception if raised

note

On serverless compute clusters, autologging is not automatically enabled. You must explicitly call `mlflow.crewai.autolog()` to enable automatic tracing for this integration.

note

Currently, MLflow CrewAI integration only support tracing for synchronous task execution. Asynchronous task and kickoff are not supported right now.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

To use MLflow Tracing with CrewAI, you need to install MLflow and the `crewai` library (which includes `crewai_tools`).

*   Development
*   Production

For development environments, install the full MLflow package with Databricks extras and `crewai`:

Bash

    pip install --upgrade "mlflow[databricks]>=3.1" crewai

The full `mlflow[databricks]` package includes all features for local development and experimentation on Databricks.

note

MLflow 3 is highly recommended for the best tracing experience with CrewAI.

Before running the examples, you'll need to configure your environment:

**For users outside Databricks notebooks**: Set your Databricks environment variables:

Bash

    export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"export DATABRICKS_TOKEN="your-personal-access-token"

**For users inside Databricks notebooks**: These credentials are automatically set for you.

**API Keys**: Ensure any necessary LLM provider API keys are configured. For production use, use [AI Gateway or Databricks secrets](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/#secure-api-key-management) instead of hardcoded values:

Bash

    export OPENAI_API_KEY="your-openai-api-key"export SERPER_API_KEY="your-serper-api-key"# Add other provider keys as needed

### Example Usage[​](#example-usage "Direct link to Example Usage")

First, enable auto-tracing for CrewAI, and optionally create an MLflow experiment to write traces to. This helps organizing your traces better.

Python

    import mlflowimport os# Ensure your API keys (e.g., OPENAI_API_KEY, SERPER_API_KEY) are set in your environment# os.environ["OPENAI_API_KEY"] = "your-openai-key"# os.environ["SERPER_API_KEY"] = "your-serper-key"# Turn on auto tracing by calling mlflow.crewai.autolog()mlflow.crewai.autolog()# Set up MLflow tracking to Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/crewai-demo")

Next, define a multi-agent workflow using CrewAI. The following example defines a trip planner agent that uses web search capability as a tool.

Python

    from crewai import Agent, Crew, Taskfrom crewai.knowledge.source.string_knowledge_source import StringKnowledgeSourcefrom crewai_tools import SerperDevTool, WebsiteSearchToolfrom textwrap import dedentcontent = "Users name is John. He is 30 years old and lives in San Francisco."string_source = StringKnowledgeSource(    content=content, metadata={"preference": "personal"})search_tool = WebsiteSearchTool()class TripAgents:    def city_selection_agent(self):        return Agent(            role="City Selection Expert",            goal="Select the best city based on weather, season, and prices",            backstory="An expert in analyzing travel data to pick ideal destinations",            tools=[                search_tool,            ],            verbose=True,        )    def local_expert(self):        return Agent(            role="Local Expert at this city",            goal="Provide the BEST insights about the selected city",            backstory="""A knowledgeable local guide with extensive information        about the city, it's attractions and customs""",            tools=[search_tool],            verbose=True,        )class TripTasks:    def identify_task(self, agent, origin, cities, interests, range):        return Task(            description=dedent(                f"""                Analyze and select the best city for the trip based                on specific criteria such as weather patterns, seasonal                events, and travel costs. This task involves comparing                multiple cities, considering factors like current weather                conditions, upcoming cultural or seasonal events, and                overall travel expenses.                Your final answer must be a detailed                report on the chosen city, and everything you found out                about it, including the actual flight costs, weather                forecast and attractions.                Traveling from: {origin}                City Options: {cities}                Trip Date: {range}                Traveler Interests: {interests}            """            ),            agent=agent,            expected_output="Detailed report on the chosen city including flight costs, weather forecast, and attractions",        )    def gather_task(self, agent, origin, interests, range):        return Task(            description=dedent(                f"""                As a local expert on this city you must compile an                in-depth guide for someone traveling there and wanting                to have THE BEST trip ever!                Gather information about key attractions, local customs,                special events, and daily activity recommendations.                Find the best spots to go to, the kind of place only a                local would know.                This guide should provide a thorough overview of what                the city has to offer, including hidden gems, cultural                hotspots, must-visit landmarks, weather forecasts, and                high level costs.                The final answer must be a comprehensive city guide,                rich in cultural insights and practical tips,                tailored to enhance the travel experience.                Trip Date: {range}                Traveling from: {origin}                Traveler Interests: {interests}            """            ),            agent=agent,            expected_output="Comprehensive city guide including hidden gems, cultural hotspots, and practical travel tips",        )class TripCrew:    def __init__(self, origin, cities, date_range, interests):        self.cities = cities        self.origin = origin        self.interests = interests        self.date_range = date_range    def run(self):        agents = TripAgents()        tasks = TripTasks()        city_selector_agent = agents.city_selection_agent()        local_expert_agent = agents.local_expert()        identify_task = tasks.identify_task(            city_selector_agent,            self.origin,            self.cities,            self.interests,            self.date_range,        )        gather_task = tasks.gather_task(            local_expert_agent, self.origin, self.interests, self.date_range        )        crew = Crew(            agents=[city_selector_agent, local_expert_agent],            tasks=[identify_task, gather_task],            verbose=True,            memory=True,            knowledge={                "sources": [string_source],                "metadata": {"preference": "personal"},            },        )        result = crew.kickoff()        return resulttrip_crew = TripCrew("California", "Tokyo", "Dec 12 - Dec 20", "sports")result = trip_crew.run()

### Disable auto-tracing[​](#disable-auto-tracing "Direct link to Disable auto-tracing")

Auto tracing for CrewAI can be disabled globally by calling `mlflow.crewai.autolog(disable=True)` or `mlflow.autolog(disable=True)`.
