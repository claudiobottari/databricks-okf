---
title: Install Databricks Connect for Scala | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/install
ingestedAt: "2026-06-18T08:06:43.010Z"
---

note

This article covers Databricks Connect for Databricks Runtime 13.3 LTS and above.

This article describes how to install the Databricks Connect for Scala client. See [Databricks Connect for Scala](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/).

## Requirements[​](#requirements "Direct link to requirements")

Before installing Databricks Connect, make sure your workspace and local environment meet the requirements. See [Databricks Connect usage requirements](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements).

## Install the Databricks Connect client[​](#install-the-databricks-connect-client "Direct link to install-the-databricks-connect-client")

This section describes how to install the Databricks Connect client with `sbt`, Maven, or Gradle.

### Add a reference to the Databricks Connect client[​](#add-a-reference-to-the-databricks-connect-client "Direct link to Add a reference to the Databricks Connect client")

To set up the Databricks Connect client, first add a reference to the client. In your Scala project's build file such as `build.sbt` for `sbt`, `pom.xml` for Maven, or `build.gradle` for Gradle, add the following reference to the Databricks Connect client. Replace the version number with the version of the Databricks Connect library that matches the Databricks Runtime version on your cluster. You can find the Databricks Connect library version numbers in the [Maven central repository (for Databricks Runtime 16.4 LTS and below)](https://central.sonatype.com/artifact/com.databricks/databricks-connect/versions) or the [Maven central repository (for Databricks Runtime 17.0 and above)](https://central.sonatype.com/artifact/com.databricks/databricks-connect_2.13/versions).

*   Sbt
*   Maven
*   Gradle

    libraryDependencies += "com.databricks" % "databricks-connect" % "14.0.0"

Or for Databricks Connect 17.0 and above:

    libraryDependencies += "com.databricks" %% "databricks-connect" % "17.3.+"

## Next steps[​](#next-steps "Direct link to Next steps")

After you have installed Databricks Connect, you need to configure a connection to Databricks. See [Compute configuration for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config).
