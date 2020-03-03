import pymongo, csv 
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("entertainment")
coll = db.get_collection("users")

with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        coll.insert_one({"name":row[0], "age":row[1]})
client.close() 
