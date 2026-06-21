---
title: Model Serving concepts | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/glossary
ingestedAt: "2026-06-18T08:11:59.947Z"
---

    POST /api/2.0/serving-endpoints{   "name":"multi-pt-model"   "config":   {      "served_entities":      [         {            "name":"meta_llama_v3_1_70b_instruct",            "entity_name":"system.ai.meta_llama_v3_1_70b_instruct",            "entity_version":"4",            "min_provisioned_throughput":0,            "max_provisioned_throughput":2400         },         {            "name":"meta_llama_v3_1_8b_instruct",            "entity_name":"system.ai.meta_llama_v3_1_8b_instruct",            "entity_version":"4",            "min_provisioned_throughput":0,            "max_provisioned_throughput":1240         }      ],      "traffic_config":      {         "routes":         [            {               "served_model_name":"meta_llama_v3_1_8b_instruct",               "traffic_percentage":"60"            },            {               "served_model_name":"meta_llama_v3_1_70b_instruct",               "traffic_percentage":"40"            }         ]      }   }}
