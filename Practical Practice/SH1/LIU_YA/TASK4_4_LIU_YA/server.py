from flask import Flask, render_template, request 
import sqlite3 

def open_DB(db): 
    connection = sqlite3.connect(db) 
    connection.row_factory = sqlite3.Row 
    return connection 

app = Flask("__name__") 

@app.route("/") 
def root(): 
    location = request.form["location"]
    return render_template("") 