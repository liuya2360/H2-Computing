import pymongo, json 
client = pymongo.MongoClient("127.0.0.1", 27017)
with open('data.json') as file:
    data = json.load(file) 
client['entertainment']['moreusers'].insert_many(data)
client.close() 
