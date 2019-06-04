from flask import Flask, render_template, request, redirect
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

@app.route("/product")
def show_product_form():
    return render_template("product_frm.html")

@app.route("/add", methods=["POST"])
def add_product(): 
    name = request.form["name"]
    price = request.form["price"]
    description = request.form["description"]
    if "image" in request.files: 
        image_file = request.files["image"]
        image_file_name = image_file.filename 
        image_file.save("static/images/" + image_file_name) 

    con = sqlite3.connect("catalogue.db") 
    try: 
        con.execute("INSERT INTO Products(Name, Description, Price, Image) VALUES (?,?,?,?)", (name, description, price, image_file_name))
    except Exception as err: 
        print(str(err), "error") 
    con.commit() 

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

