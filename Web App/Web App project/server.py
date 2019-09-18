from flask import Flask, render_template, request, redirect, url_for
import sqlite3 

def open_DB(db): 
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row 
    return connection

app = Flask("__name__")

@app.route("/", methods=["GET", "POST"])
def root(): 
    #return render_template("login.html", error="") 
    if request.method == "GET": 
        return render_template("login.html")
    else: 
        con = open_DB("places.db") 
        cur = con.cursor() 
        userExist = "This username already exist. Please try a new one. "
        userNotExist = "This user does not exist. Please input a valid username. "
        incorrectPass = "Incorrect password. Please try again. "
        if request.form["submit"] == "register": 
            id = request.form["userId"] 
            password = request.form["password"]
            if id == "" or password == "": 
                return render_template("login.html", error="Invalid Input. Please try again. ")
            #print(id) 
            #print(password) 
            try: 
                cur.execute("SELECT id FROM users WHERE id=?",(id,)) 
                row = cur.fetchall()
                if len(row) == 0:
                    try: 
                        cur.execute("INSERT INTO users(id, password) VALUES(?,?)",(id, password)) 
                        con.commit() 
                        con.close() 
                        return render_template("successLogin.html")
                    except Exception as e: 
                        print(e) 
                else: 
                    return render_template("login.html", error=userExist)
            except Exception as e: 
                print(e)  
        else: 
            id = request.form["userId"] 
            password = request.form["password"] 
            try: 
                cur.execute("SELECT id FROM users WHERE id=?",(id,)) 
                row = cur.fetchall() 
                if len(row) == 0: 
                    return render_template("login.html", error=userNotExist) 
                else: 
                    try: 
                        cur.execute("SELECT * FROM users WHERE id=?",(id,)) 
                        row = cur.fetchone() 
                        print(row["password"]) 
                        print(password) 
                        if row["password"] == password: 
                            return render_template("successLogin.html") 
                        else: 
                            print(incorrectPass)
                            return render_template("login.html", error=incorrectPass)
                    except Exception as e: 
                        print(e)
            except Exception as e: 
                print(e) 
    return redirect("/")

@app.route("/home")
def home():
    con = open_DB('places.db')
    cur = con.execute("SELECT * FROM places")
    rows  = cur.fetchall()
    return render_template("main.html", places = rows)

@app.route("/add_location")
def show_add_location_form(): 
    return render_template("add_place.html")

@app.route("/submit", methods=["POST"]) 
def submit_add_location():
    name = request.form["name"] 
    description = request.form["description"] 
    capacity = request.form["capacity"]
    availability = request.form["availability"] 
    con = open_DB("places.db") 
    if "image" in request.files: 
        image_file = request.files["image"]
        image_file_name = image_file.filename 
        image_file.save("static/images/"+image_file_name) 
        try: 
            con.execute("INSERT INTO places(Name, Description, Capacity, Availability, Image) VALUES (?,?,?,?,?)",\
                (name, description, capacity, availability, image_file_name))
        except Exception as e: 
            print(str(e))
    else: 
        try: 
            con.execute("INSERT INTO places(Name, Description, Capacity, Availability) VALUES (?,?,?,?)",\
                (name, description, capacity, availability))
        except Exception as e: 
            print(str(e))
    con.commit()
    con.close()
    return redirect("/home")

@app.route("/view_location/<location>", methods=["GET", "POST"])
def view_location(location): 
    linked_locations = []
    try: 
        con = open_DB("places.db") 
        cur = con.cursor() 
        cur.execute("SELECT * FROM places where name=?", (location,)) 
        row = cur.fetchone() 
        cur.execute("SELECT location2 from link where location1=?", (location,))
        linked_locations = cur.fetchall() 
        con.close() 
    except Exception as e: 
        print(str(e))
    exitFlag = len(linked_locations) 
    return render_template("view_place.html", place = row, linked_locations=linked_locations, exitFlag=exitFlag) 

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
    return render_template("edit_place.html", place = row) 

@app.route("/edit/<location>", methods=["POST"])
def update_location(location): 
    image_file_name = "" 
    if "image" in request.files: 
        image_file = request.files["image"] 
        image_file_name = image_file.filename 
        image_file.save("static/images/"+image_file_name)
    try: 
        con = open_DB("places.db") 
        cur = con.cursor() 
        if request.form["submit"] == "update" and image_file_name == "": 
            cur.execute("UPDATE places set name=?, description=?, capacity=?, availability=? where name=?",\
                 (request.form["name"], request.form["description"], request.form["capacity"],\
                      request.form["availability"], request.form["name"])) 
        elif request.form["submit"] == "update" and image_file_name != "": 
            cur.execute("UPDATE places set name=?, description=?, capacity=?, availability=?, image=? where name=?)",\
                 (request.form["name"], request.form["description"], request.form["capacity"],\
                      request.form["availability"], request.form["image"], request.form["name"])) 
        elif request.form["submit"] == "delete": 
            cur.execute("DELETE FROM link WHERE location1 = ? OR location2 = ?", (location, location))
            cur.execute("DELETE FROM places where name=?", (location,))
            msg = "Location Deleted. "
        con.commit() 
        con.close() 
    except Exception as e: 
        print(str(e))
    try: 
        con = open_DB("places.db") 
        cur = con.cursor() 
        cur.execute("SELECT * FROM places where name=?", (location,)) 
        row = cur.fetchone() 
        con.close() 
    except Exception as e: 
        print(str(e))
    if request.form["submit"] == "delete": 
        return redirect("/home")
    return render_template("view_place.html", place = row) 

@app.route("/add_link", methods=["GET"]) 
def show_add_link(): 
    try: 
        con = open_DB("places.db") 
        cur = con.cursor() 
        cur.execute("SELECT name FROM places") 
        location_list = cur.fetchall() 
        con.commit() 
        con.close()
    except Exception as e: 
        print(str(e)) 
    return render_template("add_link.html", location_list=location_list) 

@app.route("/add_link", methods=["POST"]) 
def add_link(): 
    try: 
        con = open_DB("places.db") 
        cur = con.cursor() 
        if request.form["submit"] == "update": 
            cur.execute("INSERT INTO link (location1, location2) VALUES (?,?)",\
                (request.form["location_1"], request.form["location_2"]))
            cur.execute("INSERT INTO link (location1, location2) VALUES (?,?)",\
                (request.form["location_2"], request.form["location_1"]))
        con.commit() 
        con.close()
    except Exception as e: 
        print(str(e)) 
    return redirect("/home")

@app.route("/view_location/<location>", methods=["GET", "POST"])
def change_location(): 
    return 0
    #return url_for(view_location(target_locaiton)) 
    #return redirect(url_for(view_location), location=target_locaiton)

if __name__ == "__main__":
    app.run(debug=True)