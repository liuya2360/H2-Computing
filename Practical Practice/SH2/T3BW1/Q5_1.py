#Task 5.1 
import csv
import pymongo

with open("STUDENTLIST.txt") as f: 
    reader = csv.reader(f) 
    line = [row for row in reader]
    #print(line) 
    
#connect to MongoDB 
client = pymongo.MongoClient('127.0.0.1', 27017) 
db = client.all_classes 
#print(db.list_collection_names())
try: 
    db.student_details.drop() 
except: 
    pass 
coll = db.student_details 

for row in line: 
    student = {'class': row[0], 'index_no': row[1], 'name': row[2]} 
    coll.insert_one(student) 
