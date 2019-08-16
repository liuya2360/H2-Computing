from flask import Flask, render_template, request, redirect
import sqlite3 

def open_DB(db): 
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row 
    return connection

app = Flask("__name__")

@app.route("/")
def root():
    con = open_DB('places.db')
    cur = con.execute("SELECT * FROM places")
    rows  = cur.fetchall()
    return render_template("main.html", places = rows)

@app.route("/add_location")
def show_add_location_form(): 
    return render_template("add_place.html")

@app.route("/submit", methods=["post"]) 
def submit_add_location():
    name = request.form["name"] 
    description = request.form["description"] 
    capacity = request.form["capacity"]
    availability = request.form["availability"] 
    if "image" in request.files: 
        image_file = request.file["image"]
        image_file_name = image_file.filename 
        image_file.save("static/images/"+image_file_name) 

    con = open_DB("places.db") 
    try: 
        con.execute("INSERT INTO places(Name, Description, Capacity, Availability, Image) VALUES (?,?,?,?,?,)",\
            (name, description, capacity, availability, image_file_name))
    except Exception as e: 
        print(str(e))
    con.commit()
    return redirect("/")

@app.route("/edit/<location>", methods=["GET"])
def edit_location(location): 
    try: 
        con = open_DB("places.db") 
        cur = con.cursor() 
        cur.execute("SELECT * FROM places where name=?", (location,)) 
        row = cur.fetchone() 
        con.close() 
    except Exception as e: 
        print(str(e))
    return render_template("edit_place.html", data = row)

@app.route("/edit/<location>", methods=["POST"])
def update_locaiton(locaiton): 
    image_file_name = "" 
    if "image" in request.files: 
        image_file = request.files["image"] 
        image_file_name = image_file.filename 
        image_file.save("ststic/image/"+image_file_name)
    try: 
        con = open_DB("places.db") 
        cur = con.cursor() 
        if request.form["submit"] == "update" and image_file_name == "": 
            cur.execute("UPDATE places set name=?, description=?, capability=?, availability=? where name=?",\
            (request.form["name"], request.form["description"], request.form["capacity"], request.form["availability"],\
                request.form["location"])) 
        elif request.form["submit"] == "update" and image_file_name != "": 
            cur.execute("UPDATE places set name=?, description=?, capability=?, availability=? where name=?",\
            (request.form["name"], request.form["description"], request.form["capacity"], request.form["availability"],\
                request.form["location"])) 
        elif request.form["submit"] == "delete": 
            cur.execute("DELETE FROM places where name=?", (locaiton,))
            msg = "Location Deleted. " 
            
        con.commit() 
        con.close() 
    except Exception as e: 
        print(str(e))
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)