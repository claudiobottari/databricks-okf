---
title: DELTA_SHARING_SECURABLE_DELETE_BLOCKED error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-sharing-securable-delete-blocked-error-class
ingestedAt: "2026-06-18T08:07:31.612Z"
---

[SQLSTATE: 55006](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-55-object-not-in-prerequisite-state)

`<securableType> <securableFullName>` cannot be deleted because it is being shared via OpenSharing.

## BY\_CLEAN\_ROOMS[​](#by_clean_rooms "Direct link to BY_CLEAN_ROOMS")

It is shared in clean rooms with central clean room ids: `<cleanRoomIds>`. If you just want to update a shared view, please use `ALTER VIEW` instead.

It is shared through the following shares: `<shareNames>`. If you just want to update a shared view, please use `ALTER VIEW` instead.

It is shared through the following shares: `<shareNames>`. It is shared in clean rooms with central clean room ids: `<cleanRoomIds>`. If you just want to update a shared view, please use `ALTER VIEW` instead.

## NO\_HINT[​](#no_hint "Direct link to NO_HINT")

If you just want to update a shared view, please use `ALTER VIEW` instead.
