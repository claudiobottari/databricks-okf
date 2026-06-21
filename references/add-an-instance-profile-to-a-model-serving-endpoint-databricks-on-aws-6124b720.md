---
title: Add an instance profile to a model serving endpoint | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/add-model-serving-instance-profile
ingestedAt: "2026-06-18T08:11:43.889Z"
---

This article demonstrates how to attach an instance profile to a model serving endpoint. Doing so allows customers to access any AWS resources from the model permissible by the instance profile. Learn more about [instance profiles](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile).

## Requirements[​](#requirements "Direct link to Requirements")

*   [Create an instance profile](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile).
    
*   [Add an instance profile to Databricks](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile#add-instance-profile).
    
    *   If you have an instance profile already configured for serverless SQL, be sure to change the access policies so that your models have the right access policy to your resources.
*   Model serving endpoints run on serverless compute. Your instance profile's IAM role must have a trust relationship configured for serverless compute. If you see the error "IAM role does not have the required trust relationship," see [Confirm or set up an AWS instance profile to use with your serverless SQL warehouses](https://docs.databricks.com/aws/en/admin/sql/data-access-configuration#aws-instance-profile-setup) for setup instructions.
    

## Add an instance profile during endpoint creation[​](#add-an-instance-profile-during-endpoint-creation "Direct link to Add an instance profile during endpoint creation")

When you [create a model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints) you can add an instance profile to the endpoint configuration.

note

The endpoint creator's permission to an instance profile is validated at endpoint creation time.

*   From the Serving UI, you can add an instance profile in **Advanced configurations**:
    
    ![Create a model serving endpoint](https://docs.databricks.com/aws/en/assets/images/add-instance-profile-85d7ec40a687ac01fbd4cf84183f725b.png)
    
*   For programmatic workflows, use the `instance_profile_arn` field when you create an endpoint to add an instance profile.
    
    Bash
    
        POST /api/2.0/serving-endpoints{  "name": "feed-ads",  "config":{  "served_entities": [{    "entity_name": "ads1",    "entity_version": "1",    "workload_size": "Small",    "scale_to_zero_enabled": true,    "instance_profile_arn": "arn:aws:iam::<aws-account-id>:instance-profile/<instance-profile-name-1>"    }]  }}
    

## Update an existing endpoint with an instance profile[​](#update-an-existing-endpoint-with-an-instance-profile "Direct link to Update an existing endpoint with an instance profile")

You can also update an existing model serving endpoint configuration with an instance profile with the `instance_profile_arn` field.

Bash

    PUT /api/2.0/serving-endpoints/{name}/config{  "served_entities": [{    "entity_name": "ads1",    "entity_version": "2",    "workload_size": "Small",    "scale_to_zero_enabled": true,    "instance_profile_arn": "arn:aws:iam::<aws-account-id>:instance-profile/<instance-profile-name-2>"  }]}

## Limitations[​](#limitations "Direct link to Limitations")

The following limitations apply:

*   STS temporary security credentials are used to authenticate data access. It can't bypass any network restriction.
*   If customers edit the instance profile IAM role from the **Settings** of the Databricks UI, endpoints running with the instance profile continue to use the old IAM role until the endpoint updates.
*   If customers delete an instance profile from the **Settings** of the Databricks UI and that profile is used in running endpoints, the running endpoint is not impacted.

For general model serving endpoint limitations, see [Model Serving limits and regions](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits).

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Look up features](https://docs.databricks.com/aws/en/machine-learning/feature-store/fs-authentication) using the same instance profile that you added to the serving endpoint.
*   [Configure access to resources from model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving).
