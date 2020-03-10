import sqlite3 

def open_DB(db): 
    connection = sqlite3.connect(db) 
    connection.row_factory = sqlite3.Row 
    return connection

con = open_DB("equipment.db") 

with open("MONITORS.txt") as f: 
    line = f.read() 
line = line.strip().split("\n")
for row in line: 
    row = row.strip().split(",") 
    #print(row)
    con.execute("INSERT INTO Device(SerialNumber, Type, Model, Location, DateOfPurchase, WrittenOff) VALUES (?,?,?,?,?,?)", (row[0], "Monitor", row[1], row[2], row[3], row[4])) 
    con.execute("INSERT INTO Monitor (SerialNumber, DateCleaned) VALUES (?,?)", (row[0], row[5])) 

with open("LAPTOPS.txt") as f: 
    line = f.read() 
line = line.strip().split("\n") 
for row in line: 
    row = row.strip().split(",") 
    con.execute("INSERT INTO Device(SerialNumber, Type, Model, Location, DateOfPurchase, WrittenOff) VALUES (?,?,?,?,?,?)", (row[0], "Laptop", row[1], row[2], row[3], row[4])) 
    con.execute("INSERT INTO Laptop(SerialNumber, WeightKg) VALUES (?,?)", (row[0], row[5]))

with open("PRINTERS.txt") as f: 
    line = f.read() 
line = line.strip().split("\n") 
for row in line: 
    row = row.strip().split(",") 
    con.execute("INSERT INTO Device(SerialNumber, Type, Model, Location, DateOfPurchase, WrittenOff) VALUES (?,?,?,?,?,?)", (row[0], "Laptop", row[1], row[2], row[3], row[4])) 
    con.execute("INSERT INTO Printer(SerialNumber, Toner, DateChanged) VALUES (?,?,?)", (row[0], row[5], row[6])) 

con.commit() 
con.close() 
