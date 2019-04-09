from flask import Flask #class
from flask import render_template 
from flask import request

app = Flask(__name__)

@app.route("/")  #decorator function
def root():
    return render_template("form1.html")

@app.route("/submit", methods=["POST","GET"])
def calculate():
    
    output = "Hello, " + request.form["name"]
    return output

app.run()