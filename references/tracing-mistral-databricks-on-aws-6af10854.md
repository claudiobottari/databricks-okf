---
title: Tracing Mistral | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/mistral
ingestedAt: "2026-06-18T08:17:26.194Z"
---

    import osfrom mistralai import Mistralimport mlflow# Turn on auto tracing for Mistral AI by calling mlflow.mistral.autolog()mlflow.mistral.autolog()# Set up MLflow tracking on Databricksmlflow.set_tracking_uri("databricks")mlflow.set_experiment("/Shared/mistral-demo")# Configure your API key.client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])# Use the chat complete method to create new chat.chat_response = client.chat.complete(    model="mistral-small-latest",    messages=[        {            "role": "user",            "content": "Who is the best French painter? Answer in one short sentence.",        },    ],)print(chat_response.choices[0].message)
