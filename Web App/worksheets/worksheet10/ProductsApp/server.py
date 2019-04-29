from flask import Flask 
from flask import render_template 
from flask import request

fileHandle = open("products.txt")

products = []
for row in fileHandle:
    row = row.strip().split("|")
    products.append(row)
fileHandle.close()

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("products.html", products=products)

@app.route("/add")
def add_product():
    image_file_name = ""
    fileHandle = open("products.txt", "a")
    

    if "image" in request.files:
        image_file = request.files["image"]
        image_file_name = image_file.image_file_name 
        image_file.save("static/image/"+image_file_name)

app.run()
