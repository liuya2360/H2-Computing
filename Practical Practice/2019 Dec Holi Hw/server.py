from flask import Flask, render_template, request, redirect, url_for 
import sqlite3 

app = Flask("__name__")

def open_DB(db): 
    connection = sqlite3.connect(db) 
    connection.row_factory = sqlite3.Row 
    return connection

@app.route("/") 
def root(): 
    con = open_DB('table.db') 
    cur = con.cursor()
    try:
         cur.excecute("SELECT * FROM test50")
    except: 
        pass 
    con.commit()
    con.close()
    return render_template("test50.html") 

@app.route("/submit", methods=["POST"]) 
def submit(): 
    if "image" in request.files: 
        image_file = request.files["image"] 
        image_file_name = image_file.filename 
        image_file.save("static/image/"+image_file_name) 
    try: 
        con = open_DB('table.db') 
        cur = con.cursor() 
        #generate SQL insert statement 
        if request.form["submit"] == "submit" and image_file_name != "": 
            con.execute("INSERT INTO test50(image) VALUES (?)", (image_file_name,)) 
        con.execute("INSERT INTO test50(name) VALUES (?)", (request.form["name"],))
        print(image_file_name)
        print(name)
        #execute and commmit 
        con.commit() 
        con.close() 
    except Exception as e: 
        print(str(e)) 
    return redirect("/") 

if __name__ == "__main__": 
    app.run(debug=True)
