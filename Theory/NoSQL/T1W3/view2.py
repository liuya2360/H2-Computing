import pymongo, csv 
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("entertainment")
coll = db.get_collection("movies")

result = coll.find()
print('All documents in movie collection:')
for document in result:
    print(document)
print('Number of items in movie collection:', coll.count())

result = coll.find({'genre':{'$in':['adventure','comedy']}})
print('All movies with adventure or comedy genre inside:')
for document in result:
    print(document)

query2 = {}
