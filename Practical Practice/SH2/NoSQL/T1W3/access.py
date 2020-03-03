import pymongo
client = pymongo.MongoClient("127.0.0.1", 27017)
databases = client.database_names()
print("The databases in the MongoDB server are:")
print(databases)
client.close() 
