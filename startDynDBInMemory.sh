# Start DB in memory - nothing will be saved to disk
cd DynamoDB && java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb -inMemory
