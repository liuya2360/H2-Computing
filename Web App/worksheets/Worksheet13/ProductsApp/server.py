from flask import Flask, render_template, request
## DB boiler plates 
import sqlite3 
def open_DB(db): 
    connection = sqlite3.connect(db) 
    connection.row_factory = sqlite3.Row # return a library instead of a tuple 
    return connection 

app = Flask("__name__")

@app.route("/")
def root():
    con = open_DB('catalogue.db') 
    #to display the items in ascending order of price 
    cur = con.execute("SELECT * FROM Products ORDER BY price") 
    rows = cur.fetchall() 
    con.close() 
    return render_template("products.html", products = rows) 

@app.route("/add_product")
def add_product():
    return render_template("product_frm.html")

@app.route("/submit", methods=["POST"])
def submit(): 
    name = request.form["name"]
    price = request.form["price"]
    description = request.form["description"]
    image = request.form["image"]

    con = sqlite3.connect("catalogue.db") 
    try: 
        con.execute("INSERT INTO Products(Name, Description, Price, Image) VALUES (?,?,?,?)", (name, description, price, image))
    except Exception as err: 
        print(str(err), "error") 
    con.commit() 
    con = open_DB('catalogue.db') 
    #to display the items in ascending order of price 
    cur = con.execute("SELECT * FROM Products ORDER BY price") 
    rows = cur.fetchall() 
    con.close()
    return render_template("products.html", products = rows) 
    
    


if __name__ == "__main__":
    app.run(debug=True)

