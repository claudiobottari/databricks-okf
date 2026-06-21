---
title: Query with the Google Gemini API | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/query-gemini-api
ingestedAt: "2026-06-18T08:12:33.363Z"
---

    from google import genaifrom google.genai import typesimport osDATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')client = genai.Client(    api_key="databricks",    http_options=types.HttpOptions(        base_url="https://example.staging.cloud.databricks.com/serving-endpoints/gemini",        headers={            "Authorization": f"Bearer {DATABRICKS_TOKEN}",        },    ),)response = client.models.generate_content(    model="databricks-gemini-2-5-pro",    contents=[        types.Content(            role="user",            parts=[types.Part(text="What is a mixture of experts model?")],        ),    ],    config=types.GenerateContentConfig(        max_output_tokens=256,    ),)print(response.text)
