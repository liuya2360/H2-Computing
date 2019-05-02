from flask import Flask 
from flask import render_template 
from flask import request
import os

print(os.getcwd())

fileHandle = open("products.txt")

products = []
for row in fileHandle:
    row = row.strip().split("|")
    products.append(row)

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("products.html", products=products)

app.run()
