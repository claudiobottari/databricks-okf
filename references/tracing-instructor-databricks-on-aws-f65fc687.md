---
title: Tracing Instructor | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/instructor
ingestedAt: "2026-06-18T08:17:17.320Z"
---

    import instructorfrom pydantic import BaseModelfrom openai import OpenAIimport mlflow# Use other autologging function e.g., mlflow.anthropic.autolog() if you are using Instructor with different LLM providersmlflow.openai.autolog()# Set up MLflow tracking on Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/instructor-demo")# Use Instructor as usualclass ExtractUser(BaseModel):    name: str    age: intclient = instructor.from_openai(OpenAI())res = client.chat.completions.create(    model="gpt-4o-mini",    response_model=ExtractUser,    messages=[{"role": "user", "content": "John Doe is 30 years old."}],)print(f"Name: {res.name}, Age:{res.age}")
