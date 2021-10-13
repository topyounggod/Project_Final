from pymongo import MongoClient
cluster = "mongodb+srv://young:PKzh8aqQ8yFB30PC@cluster0.ieeta.mongodb.net/Project_Younghun?retryWrites=true&w=majority"
client = MongoClient(cluster)
print(client.list_database_names())
db = client.Project_Younghun
print(db.list_collection_names())
