---
title: User-defined functions in Databricks Connect for Scala | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/udf
ingestedAt: "2026-06-18T08:06:55.536Z"
---

note

This article covers Databricks Connect for Databricks Runtime 14.1 and above.

[Databricks Connect for Scala](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/scala/) supports running user-defined functions (UDFs) on Databricks clusters from your local development environment.

This page describes how to execute user-defined functions with Databricks Connect for Scala.

For the Python version of this article, see [User-defined functions in Databricks Connect for Python](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/udf).

## Upload compiled class and JARs[​](#upload-compiled-class-and-jars "Direct link to Upload compiled class and JARs")

For UDFs to work, the compiled classes and JARs must be uploaded to the cluster using the `addCompiledArtifacts()` API.

The following Scala program sets up a simple UDF that squares values in a column.

Scala

    import com.databricks.connect.DatabricksSessionimport org.apache.spark.sql.SparkSessionimport org.apache.spark.sql.functions.{col, udf}object Main {  def main(args: Array[String]): Unit = {    val spark = getSession()    val squared = udf((x: Long) => x * x)    spark.range(3)      .withColumn("squared", squared(col("id")))      .select("squared")      .show()    }  }  def getSession(): SparkSession = {    if (sys.env.contains("DATABRICKS_RUNTIME_VERSION")) {      // On a Databricks cluster — reuse the active session      SparkSession.active    } else {      // Locally with Databricks Connect — upload local JARs and classes      DatabricksSession        .builder()        .addCompiledArtifacts(          Main.getClass.getProtectionDomain.getCodeSource.getLocation.toURI        )        .getOrCreate()    }  }}

`Main.getClass.getProtectionDomain.getCodeSource.getLocation.toURI` points to the same location as the project's compiled output (for example, target/classes or the built JAR). All compiled classes are uploaded to Databricks, not just `Main`.

    target/scala-2.13/classes/├── com/│   ├── examples/│   │   ├── Main.class│   │   └── MyUdfs.class│   └── utils/│       └── Helper.class

When the Spark session is already initialized, further compiled classes and JARs can be uploaded using the `spark.addArtifact()` API.

note

When uploading JARs, all transitive dependency JARs must be included for upload. The APIs do not perform any automatic detection of transitive dependencies.

### UDFs with third-party dependencies[​](#udfs-with-third-party-dependencies "Direct link to UDFs with third-party dependencies")

If you've added a Maven dependency in `build.sbt` that is used in a UDF but isn't available on the Databricks cluster, for example:

    // In build.sbtlibraryDependencies += "org.apache.commons" % "commons-text" % "1.10.0"

Scala

    // In your codeimport org.apache.commons.text.StringEscapeUtils// ClassNotFoundException thrown during UDF execution of this function on the server sideval escapeUdf = udf((text: String) => {  StringEscapeUtils.escapeHtml4(text)})

Use `spark.addArtifact()` with `ivy://` to download dependencies from Maven:

1.  Add the `oro` library to your `build.sbt` file
    
        libraryDependencies ++= Seq(  "org.apache.commons" % "commons-text" % "1.10.0" % Provided,  "oro" % "oro" % "2.0.8"  // Required for ivy:// to work)
    
2.  Add the artifact after creating the session with the `addArtifact()` API:
    
    Scala
    
        def getSession(): SparkSession = {  if (sys.env.contains("DATABRICKS_RUNTIME_VERSION")) {    SparkSession.active  } else {    val spark = DatabricksSession.builder()      .addCompiledArtifacts(Main.getClass.getProtectionDomain.getCodeSource.getLocation.toURI)      .getOrCreate()    // Convert Maven coordinates to ivy:// format    // From: "org.apache.commons" % "commons-text" % "1.10.0"    // To:   ivy://org.apache.commons:commons-text:1.10.0    spark.addArtifact("ivy://org.apache.commons:commons-text:1.10.0")    spark  }}
    

## Typed Dataset APIs[​](#typed-dataset-apis "Direct link to Typed Dataset APIs")

Typed Dataset APIs allow one to run transformations such as `map()`, `filter()`, `mapPartitions()`, and aggregations on resulting datasets. Uploading the compiled class and JARs to the cluster using the `addCompiledArtifacts()` API also applies to these, so your code must behave differently depending on where it runs:

*   **Local development** with Databricks Connect: Upload artifacts to the remote cluster.
*   **Deployed on Databricks** running on the cluster: No need to upload anything because classes are already there.

The following Scala application uses the `map()` API to modify a number in a result column to a prefixed string.

Scala

    import com.databricks.connect.DatabricksSessionimport org.apache.spark.sql.SparkSessionimport org.apache.spark.sql.functions.{col, udf}object Main {  def main(args: Array[String]): Unit = {    val sourceLocation = getClass.getProtectionDomain.getCodeSource.getLocation.toURI    val spark = DatabricksSession.builder()      .addCompiledArtifacts(sourceLocation)      .getOrCreate()    spark.range(3).map(f => s"row-$f").show()  }}

## External JAR dependencies[​](#external-jar-dependencies "Direct link to External JAR dependencies")

If you’re using a private or third-party library that isn't on the cluster:

Scala

    import com.mycompany.privatelib.DataProcessor// ClassNotFoundException thrown during UDF execution of this function on the server sideval myUdf = udf((data: String) => {  DataProcessor.process(data)})

Upload external JARs from your `lib/` folder when creating the session:

Scala

    def getSession(): SparkSession = {  if (sys.env.contains("DATABRICKS_RUNTIME_VERSION")) {    SparkSession.active  } else {    val builder = DatabricksSession.builder()      .addCompiledArtifacts(Main.getClass.getProtectionDomain.getCodeSource.getLocation.toURI)     // Add all JARs from lib/ folder     val libFolder = new java.io.File("lib")     builder.addCompiledArtifacts(libFolder.toURI)   builder.getOrCreate()  }}

This automatically uploads all JARs in your lib/ directory to Databricks when running locally.

## Projects with multiple modules[​](#projects-with-multiple-modules "Direct link to Projects with multiple modules")

In a multi-module SBT project, `getClass.getProtectionDomain.getCodeSource.getLocation.toURI` only returns the current module's location. If your UDF uses classes from other modules, you'll get `ClassNotFoundException`.

    my-project/├── module-a/  (main application)├── module-b/  (utilities - module-a depends on this)

Use `getClass` from a class in each module to get all their location and upload them separately:

Scala

    // In module-a/src/main/scala/Main.scalaimport com.company.moduleb.DataProcessor  // From module-bdef getSession(): SparkSession = {  if (sys.env.contains("DATABRICKS_RUNTIME_VERSION")) {    SparkSession.active  } else {    // Get location using a class FROM module-a    val moduleALocation = Main.getClass      .getProtectionDomain.getCodeSource.getLocation.toURI    // Get location using a class FROM module-b    val moduleBLocation = DataProcessor.getClass      .getProtectionDomain.getCodeSource.getLocation.toURI    DatabricksSession.builder()      .addCompiledArtifacts(moduleALocation)  // Upload module-a      .addCompiledArtifacts(moduleBLocation)  // Upload module-b      .getOrCreate()  }}

## Limitations[​](#limitations "Direct link to limitations")

*   Support for UDFs on serverless compute always follows the initial corresponding minor release of Databricks Connect. For supported versions, see the [version compatibility table](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/requirements#versions).
