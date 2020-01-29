import pymongo
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("entertainment")
coll = db.get_collection("movies")
coll.insert_one({"_id":1, "title":"Johnny Maths", "genre":"comedy"})
coll.insert_one({"title":"Star Walls", "genre":"science fiction"})
coll.insert_one({"title":"Detection"})  #no genre
list_to_add = []
list_to_add.append({"title":"Badman", "genre":"adventure", "year":2015})
list_to_add.append({"title":"Averages", "genre":["science fiction","adventure"], "year":2017})
list_to_add.append({"title":"Octopus Man", "genre":"adventure", "year":2017})
list_to_add.append({"title":"Fantastic Bees", "genre":"adventure", "year":2018})
list_to_add.append({"title":"Underground", "genre":"horror", "year":2014})
coll.insert_many(list_to_add)
c = db.collection_names("entertainment")
print ("Collections in entertainment database: ",c)
client.close()
