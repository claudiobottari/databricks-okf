---
title: Explore features and lineage (legacy) | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/workspace-feature-store/ui
ingestedAt: "2026-06-18T08:10:57.673Z"
---

With Databricks Workspace Feature Store, you can:

*   Search for feature tables by feature table name, feature, data source, or tag.
*   Control access to feature tables.
*   Identify the data sources used to create a feature table.
*   Identify models that use a particular feature.
*   Add a tag to a feature table.
*   Check feature freshness.

To access the Workspace Feature Store UI, in the sidebar, under **AI/ML**, click **Features**. A table lists all of the available feature tables, along with the features in the table and the following metadata:

*   Who created the feature table.
*   Data sources used to compute the feature table.
*   Online stores where the feature table has been published.
*   Scheduled jobs that compute the features in the feature table.
*   The last time a notebook or job wrote to the feature table.

![Feature store page](https://docs.databricks.com/aws/en/assets/images/feature-store-ui-14cd6020583d17242ddb0c0275b86222.png)

## Search and browse for feature tables[​](#search-and-browse-for-feature-tables "Direct link to Search and browse for feature tables")

Use the search box to search for feature tables. You can enter all or part of the name of a feature table, a feature, or a data source used for feature computation. You can also enter all or part of the key or value of a tag. Search text is case-insensitive.

![Feature search example](https://docs.databricks.com/aws/en/assets/images/feature-search-example-9b520100ccba30d2b3a935273adf8521.png)

## Control access to feature tables[​](#control-access-to-feature-tables "Direct link to Control access to feature tables")

See [Access control (legacy)](https://docs.databricks.com/aws/en/machine-learning/feature-store/workspace-feature-store/access-control).

## Track feature lineage and freshness[​](#track-feature-lineage-and-freshness "Direct link to Track feature lineage and freshness")

In the UI you can track both how a feature was created and where it is used. For example, you can track the raw data sources, notebooks, and jobs that were used to compute the features. You can also track the online stores where the feature is published, the models trained with it, the serving endpoints that access it, and the notebooks and jobs that read it.

Click the name of any feature table to display the feature table page.

On the feature table page, the **Producers** table provides information about all of the notebooks and jobs that write to this feature table so you can easily confirm the status of scheduled jobs and the freshness of the feature table.

![producers table](https://docs.databricks.com/aws/en/assets/images/producers-table-72cf0e89e441f1d0637c6a1b13689051.png)

The **Features** table lists all of the features in the table and provides links to the models, endpoints, jobs, and notebooks that use the feature.

![features table](https://docs.databricks.com/aws/en/assets/images/features-table-0f392167d9e5fde732562848b356a3fb.png)

To return to the main features UI page, click **Features** near the top of the page.

## Add a tag to a feature table[​](#add-a-tag-to-a-feature-table "Direct link to Add a tag to a feature table")

Tags are key-value pairs that you can create and use to [search for feature tables](#search-and-browse-for-feature-tables).

1.  On the feature table page, click ![Tag icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEsAAAAZCAYAAAB5CNMWAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAS6ADAAQAAAABAAAAGQAAAADG2PsQAAAEHUlEQVRYCe1XWShtbRh+HCc3IpJChnJhvEGGpAxFkQwZM9y5wQU3UhQZilyZpchQhDKXkAxX7ogypIxJIfOcsM5639qrvU/svdfy+x21v9prfcPzvt/6nu+dtpEgNhiaXgz80gtlADEDBrJkGIKBLANZMhiQAf0tA/spaHV1Nbq6urTqGBgYgJeXl1bMdy7+b2SFh4fDyclJOmt5eTl8fHwQExMjzdnb20v9f7Fj9F2lg6urKzIzM1FSUvIuL1TRGBkZvbtGk7rWVYL64lR4be93A3xTUxOqqqq0yX3J2vPzM+rr60FW6ObmhqSkJIyNjWnsdXx8jLKyMgQFBbFl1tbWYnh4GNHR0bi/v2fs09MTyO1DQkJYT0ZGBpaXlzX0KBl86Ibd3d04OjpCc3OzEr2KZOiC+vr6EBcXh/j4eMzNzaGwsBCWlpYIDg7G4+MjcnNzsb6+jsTERFhZWWFiYgIXFxdM1OvrK+9bWlrKJBOWZAcHB5GWlobZ2Vl8ytXJDf9ujY2NgouLC//EDxd2d3f/hnx6TPorKio09LS3twuiJUlzl5eX/A2VlZU8NzQ0xOORkREJc3p6KgQGBvL89fW18Pb2xv2CggIJc3JyIrS0tAgiydKcks67bqhuFpubm0hJSeFbUZ//in5WVhZiY2MhHg5bW1vY3t7mbcj1qG1sbPBbPSlYW1trJAmKcxQPx8fH0dHRgb29PRAmJycHHh4eLK/0oZMsUvzy8gLxxpTuobfc/Pw8xxlyOSKNYg01lXsRaeR6xsbGGjqJDPVWV1cHX19f1NTUIDIyEqGhoejt7VWHKOrrJMvR0RE9PT2IiIhQtIG+QldXV8jOzmYraG1txcLCApaWluDg4AATExNW4+7ujvPzcxBWva2trakP4ezszOQQ+UQYESy6PMc3DaDMgVayvL29MTMzA09PT5lq5cPJ7ailp6cjLCwMtra2HLQPDw8lZX5+ftynAH57e8sWR+42OTkpYW5ubjA1NYWDgwPY2dlxohBjIa+r3FgCy+x8mA1TU1P5NmTqUwwXAz7LUpVvamrKrt/Q0KChz9/fn7OhGKwxPT0trZGbkSVSIyssLi6GmZkZioqKYGNjg9HRUV4LCAjgt+KHkqzwX8i8lw3FMkAQrZmzGa23tbUJYjAX8vLypC0p24lJRxBLG6Gzs1PY398XxEAuZUMCrqyssBzpoB9ly/7+fkmH0s63VfAf3a54EI5L5ubmUqxSYXd2dtiiqNhUhQbCU112dnaGxcVFFZTfDw8PoELXwsJCY17p4J8jS9tB7u7uuDglTHJyMrsaFa5UpObn57OLapP/7NqPIosOS/8q6C/R6uoqB3mysKioKCQkJHyWC53yP44snSf6QoDW0uEL9/2Rqg1kybg2A1kGsmQwIAP6B1GoWkBNFigmAAAAAElFTkSuQmCC) if it is not already open. The tags table appears.
    
    ![tag table](https://docs.databricks.com/aws/en/assets/images/tags-open-2b92892f2d6833c4fac51ed029b0ae39.png)
    
2.  Click in the **Name** and **Value** fields and enter the key and value for your tag.
    
3.  Click **Add**.
    
    ![add tag](https://docs.databricks.com/aws/en/assets/images/tag-add-e7a0a94c7df96101259d3f82deb415fc.png)
    

### Edit or delete a tag[​](#edit-or-delete-a-tag "Direct link to Edit or delete a tag")

To edit or delete an existing tag, use the icons in the **Actions** column.

![tag actions](https://docs.databricks.com/aws/en/assets/images/tag-edit-or-delete-2a374d59a14e35d810bf70d2e1369a79.png)
