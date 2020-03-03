import pymongo, json 

#Task 1
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("demo")
db.drop_collection("heroes") 

with open("heroes.json") as f:
    data = json.load(f)


db["heroes"].insert_many(data)
result = db["heroes"].find()
for row in result:
    print(row)

#Task 2
heroes = db.get_collection("heroes")
results = heroes.find({'Publisher':'Marvel Comics'})
for row in results:
    print(row['name'])
results = heroes.find({'Gender':'Female', 'weight':{'$lt': 0}})
for row in results:
    print(row['name'])

#Task 3
results = heroes.find({'Race':'-'})
for row in results:
    row.update({'$unset':'Race'})
    print(row)

#for row in heroes.find({'$nin':'Race'}):
for row in heroes.find():
    if 'Race' not in row: 
        print(row) 

client.close() 

