import pymongo
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("entertainment")
coll = db.get_collection("movies")

title = input("Please input the title of the movie: ")
year = int(input("Please input the year of the movie: "))

coll.insert_one({"title":title, "year":year}) 
