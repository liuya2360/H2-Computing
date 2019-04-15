from flask import Flask
from flask import render_template 
from flask import request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("form.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    w1 = float(request.form["weight1"])
    w2 = float(request.form["weight2"])
    m1 = float(request.form["mark1"])
    m2 = float(request.form["mark2"])

    score = m1*(w1/100)+m2*(w2/100)
    return render_template("resutl.html", form=request.form, score=score)

app.run()