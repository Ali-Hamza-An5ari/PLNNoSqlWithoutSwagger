

# Creating Collection
To insert the documents for the 18 sports into the Azure Cosmos DB using the SQL API, you'd have to use the CreateDocumentAsync function provided by the .NET SDK (as of my last training cut-off in September 2021).

Unfortunately, Azure Cosmos DB's SQL API doesn't support the direct insertion of documents using SQL-like syntax. You have to use one of the supported SDKs (like .NET, Java, Python, Node.js, etc.) to perform these operations.

For example, in C# (.NET SDK), you would use code similar to the following to insert documents:
```
CosmosClient client = new CosmosClient("<Your Connection String Here>");
Database database = client.GetDatabase("SportsScoresDB");
Container container = database.GetContainer("SCORES");

dynamic document1 = new
{
    id = "001",
    sport = "Soccer",
    match_id = "001",
    teams = new[] {
        new { name = "Team A", goals = 2 },
        new { name = "Team B", goals = 1 },
    },
    date = DateTime.Now
};

ItemResponse<dynamic> response = await container.CreateItemAsync(document1);

```
You'd repeat the creation of document and CreateItemAsync for each sport document you need to insert.

If you want to use SQL-like queries for data manipulation, you can consider using MongoDB API while creating the Cosmos DB account. It allows the insertion of documents using SQL-like syntax. But it is still necessary to use the supported SDKs to execute these commands.

Note that the Azure Cosmos DB's SQL API is mostly for querying the data (read operations), and not for data manipulation (write operations). For write operations, you'd use the methods provided by the SDKs.

Finally, remember to replace `"<Your Connection String Here>"` with your actual Cosmos DB connection string, which you can find in the 'Keys' section of your Cosmos DB account on the Azure portal.
