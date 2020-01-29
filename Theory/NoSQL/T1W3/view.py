import pymongo, csv 
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("entertainment")
coll = db.get_collection("movies")
result = coll.find()
print('All documents in movie collection:')
for document in result:
    print(document)
print("Number of items in movie collection:", coll.count())

result = coll.find({'genre':'adventure'})
print('All movies with adventure genre:')
for document in result:
    print(document)
    
query2 = {'genre':'adventure', 'year':{'$gt':2016}}
result = coll.find(query2)
print('All titles of movies with adventure genre after 2016:')
for document in result:
    print(" - " + document.get('title'))
print('There are', result.count(), 'movies in the list above.')
client.close() 
