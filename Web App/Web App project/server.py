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

@app.route("/add_place")
def add_place(): 
    return render_template("add_place.html")

@app.route("/submit", methods=["post"]) 
def submit():
    return  redirect("/")

if __name__ == "__main__":
    app.run(debug=True)