---
title: Tracing OpenAI Swarm | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/swarm
ingestedAt: "2026-06-18T08:17:42.320Z"
---

    import mlflowfrom swarm import Swarm, Agentimport os# Ensure your OPENAI_API_KEY is set in your environment# os.environ["OPENAI_API_KEY"] = "your-openai-api-key" # Uncomment and set if not globally configured# Calling the autolog API will enable trace logging by default.mlflow.openai.autolog()# Set up MLflow tracking to Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/openai-swarm-demo")# Define a simple multi-agent workflow using OpenAI Swarmclient = Swarm()def transfer_to_agent_b():    return agent_bagent_a = Agent(    name="Agent A",    instructions="You are a helpful agent.",    functions=[transfer_to_agent_b],)agent_b = Agent(    name="Agent B",    instructions="Only speak in Haikus.",)response = client.run(    agent=agent_a,    messages=[{"role": "user", "content": "I want to talk to agent B."}],)
