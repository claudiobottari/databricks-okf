---
title: Query interruptions with Databricks Connect | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/queries
ingestedAt: "2026-06-18T08:06:33.354Z"
---

note

This article covers Databricks Connect for Databricks Runtime 14.0 and above.

This article describes how to handle asynchronous queries and interruptions with Databricks Connect. Databricks Connect enables you to connect popular IDEs, notebook servers, and custom applications to Databricks clusters. See [Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/).

## Query execution interruptions[​](#query-execution-interruptions "Direct link to Query execution interruptions")

For Databricks Connect for Databricks Runtime 14.0 and above, query execution is more resilient to network and other interrupts when executing long running queries. When the client program receives an interruption or the process is paused (up to 5 minutes) by the operating system, such as when the laptop lid is shut, the client reconnects to the running query. This also allows queries to run for longer times (previously only 1 hour).

Databricks Connect now also comes with the ability to interrupt running queries, if desired, such as for cost saving.

*   Python
*   Scala

The following Python program interrupts a long running query by using the `interruptTag()` API.

Python

    from databricks.connect import DatabricksSessionfrom time import sleepimport threadingsession = DatabricksSession.builder.getOrCreate()def thread_fn():  sleep(5)  session.interruptTag("interrupt-me")# All subsequent DataFrame queries that use session will have this tag.session.addTag("interrupt-me")t = threading.Thread(target=thread_fn).start()df = <a long running DataFrame query>df.show()t.join()

## Long-lived sessions[​](#long-lived-sessions "Direct link to Long-lived sessions")

note

Long-lived sessions are supported in Databricks Connect version 16.4 and above on serverless compute.

When you use Databricks Connect with serverless compute, after the default idle timeout a best effort is made to preserve your session. When you reconnect, Databricks attempts to automatically restore your session, including configurations, temporary views, UDFs, temporary variables, and uploaded files.

This is useful for sessions with commands that need state to survive periods of inactivity, such as setting configurations, registering UDFs, creating temporary views, or uploading files. Without this, an idle timeout would require you to re-run all of those setup commands before resuming work.

### Limitations[​](#limitations "Direct link to Limitations")

*   Long-lived sessions are only supported on serverless compute. They are not supported on standard or dedicated compute.
*   Session recovery after idle timeout is best-effort and not guaranteed. If your session cannot be restored, a new session is started.
*   Sessions that accumulate a large amount of state may exceed the size limit, after which state is no longer preserved. Reconnecting after this threshold starts a new session.
*   Preserved state expires after two days of inactivity. If your session is idle longer than this, reconnecting starts a new session.
*   Streaming query state and SQL scripts that use `EXECUTE IMMEDIATE` are not preserved across reconnects.
