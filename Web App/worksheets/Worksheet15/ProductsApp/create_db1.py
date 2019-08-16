import sqlite3 
con = sqlite3.connect("catalogue.db")
try: 
    con.execute("CREATE TABLE Products " + "(Name TEXT PRIMARY KEY, Description TEXT, Price REAL, Image TEXT )")
except Exception as err: 
    print(str(err)) 
import os 
home =  os.getcwd()
print(home)

products = []
fileHandle = open("ProductsApp/Products.txt") 
for row in fileHandle: 
    products.append(row.strip().split(","))
products.pop(0)
print(products)

for row in products: 
    name = row[0]
    description = row[1]
    price = float(row[2])
    image = row[3]
    try: 
        con.execute("INSERT INTO Products(Name, Description, Price, Image) VALUES (?,?,?,?)", (name, description, price, image))
    except Exception as err: 
        print(str(err), "error")
        continue 
    con.commit() 
con.close()