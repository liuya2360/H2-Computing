#Task 5.2

import pymongo
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.all_classes
coll = db.student_details 

while True:
    class_input = input("Please key in a valid class: ")
    cur = coll.find({"class": class_input})
    for row in cur:
        print(row["index_no"], row["name"])
    index = input("Please input a valid student id to add remarks:") 
    remarks = input("Please input the remarks:")
    coll.update_one({"index_no": index},{"$set": {"remarks": remarks}})
    stop = input("Do you want to add remarks for more students? [Y]es or [N]o")
    if stop.lower == "y":
        continue
    else:
        cur = coll.find({}, {"_id":0}) #, "class":1, "index_no":1, "name":1, "remarks":1})
        for row in cur:
            print(row)
        break 
