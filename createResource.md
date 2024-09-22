#Azure Cosmos DB for NoSQL

To create an Azure Cosmos DB for NoSQL, follow the steps below:

Create a new resource: Click on the Create a resource button on the homepage of the Azure portal.

Select Azure Cosmos DB: In the New window, search for Azure Cosmos DB and select it.

Click on Create: In the Azure Cosmos DB window, click on the Create button.

Fill out the form:

Subscription: Choose the Azure subscription that you want to use for this DB.
Resource Group: You can either create a new resource group or use an existing one.
Account Name: Enter a unique name to identify your Cosmos DB account.
API: Choose Core (SQL) for the API (Azure Cosmos DB's API for MongoDB could also be used depending on your preference).
Location: Choose a location for your Cosmos DB.
Capacity mode: Choose either Provisioned throughput or Serverless depending on your needs.
Apply Free Tier Discount: If applicable, you can choose to apply the free tier discount.
Account Type: Choose Non-Production or Production depending on your needs.
Version: Choose the Version 3.6 or Version 4.0 for MongoDB API.

**Note:** The form will validate your inputs and if everything is correct, you should see a green Validation passed message at the top of the form.

Review + create: After filling out the form, click on the Review + create button at the bottom of the page. This will take you to a new page where you can review your settings.

Create: If everything looks correct, click on the Create button at the bottom of the page. Azure will now deploy your Cosmos DB. This may take a few minutes.

Navigate to your Cosmos DB account: Once your Cosmos DB has been deployed, you can navigate to it by clicking on Go to resource.

Create a new database: Inside your Cosmos DB account, click on New Container. You'll need to specify the Database id (you can create a new one), the Container id (this will be the name of your collection), and the Partition key. If you followed the schema suggested in the previous sections, you could use /sport as the partition key.

Adding data to your collection: To add data to your collection, select the Items tab in your container, then click on New Item. You can then paste in the JSON for a new document and click on Save.

Remember, Cosmos DB is a powerful, fully-managed NoSQL database service provided by Azure. It provides a range of features including turnkey global distribution, automatic scaling of throughput, and multiple well-defined consistency models.

Before you create any production-level databases, make sure you understand the pricing model and have configured the appropriate settings for your use case.

## Create Database
Continuing from where we left off:

Add a Container: After your Cosmos DB account has been created, you'll be taken to the Azure Cosmos DB account page. On the left side, you'll see a 'Data Explorer' tab. Click on this.

Create New Database: In the 'Data Explorer' tab, click the 'New Container' button. This will open a new pane where you can create your new database and container.

Enter Database Details:

Database id: Click on 'Create new', then enter a unique name for your database in the text field.
Provision database throughput: Depending on your needs, you may want to provision throughput at the database level. If not, leave this unchecked.
Container id: Enter a unique name for the container you're creating. If we're following the previous examples, you could name it "SCORES".
Partition key: Enter the property that should be used as the partition key. For the examples we've been working with, "/sport" could be a good choice, as it will evenly distribute data across various sports.
Create Container: Click on the 'OK' button at the bottom of the pane. This will create your database and container, and take you back to the 'Data Explorer' page.

You've now created a container within an Azure Cosmos DB database!

Now you're ready to start adding documents to your container. You can use the Items tab in the Data Explorer to create new items, query your data, modify existing items, and more.

Remember that while Azure Cosmos DB is fully managed, it's also quite powerful and flexible. You should understand its pricing model and throughput provisioning features to make sure you're using it effectively and efficiently. If you're using it in a production application, it's also important to consider security and compliance requirements, and to monitor and troubleshoot your database as necessary.

## 
For partition key selection, it's crucial to consider the nature of queries and updates that the application will perform. The partition key should evenly distribute the workload across multiple partitions, which allows the system to scale horizontally.

Considering the sports scoring data we've worked with, the "sport" field could be a good choice for the partition key. As the data for different sports is likely to be distributed fairly evenly, using "sport" as the partition key would allow the system to balance the load across multiple partitions. Furthermore, if the application frequently needs to fetch or update scores for a specific sport, having "sport" as the partition key would make these operations more efficient, as they would only need to operate on a single partition.

Here's the database details:

- Database id: "SportsScoresDB"
- Provision database throughput: Unchecked (You can check it depending on your requirements and expected workload)
- Container id: "SCORES"
- Partition key: "/sport"

Please note that Azure Cosmos DB also provides a feature called "synthetic partition keys". This feature allows you to create a partition key that combines multiple properties of your JSON documents. For example, if the application frequently needs to update scores for specific matches, you could create a synthetic partition key combining "sport" and "match_id" to distribute data more evenly and make updates more efficient.

Unique keys in Cosmos DB provide developers with the ability to add an extra layer of data integrity to the system by ensuring the uniqueness of one or more values per logical partition.

In our case, it would make sense to use the match_id as a unique key, because every match in any sport should have a unique identifier. This ensures that no two matches, even in the same sport, will have the same identifier.

So in the Unique keys field, you would add ["/match_id"].

This will ensure that within each logical partition (each unique sport, in our case), every document must have a unique match_id. It's important to note that unique keys in Cosmos DB ensure uniqueness within a logical partition, not across all documents in a container. In this context, you can have two documents with the same match_id as long as they are in different logical partitions (different sports).

Please note that defining unique key policies can have performance implications, and unique key constraints can impact the throughput of write operations. So they should be used judiciously based on the requirements of the application.

