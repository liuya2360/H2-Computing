from flask import Flask, render_template, request, redirect

app = Flask("__name__")

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    result1 = request.form["result1"]
    result2 = request.form["result2"]
    result3 = request.form["result3"]
    result4 = request.form["result4"]
    result_gp = request.form["result_gp"]
    result_pw = request.form["result_pw"]
    mapping = {"A": 20, "B": 17.5, "C": 15, "D": 12.5, "E": 10, "S": 5, "U": 0} 
    score = mapping[result1] + mapping[result2] + mapping[result3] + \
            0.5*(mapping[result4] + mapping[result_gp] + mapping[result_pw])
    try: 
        result_mt = request.form["result_mt"]
        score += 0.5 * mapping[result_mt]
        score = score/10*9
    except:
        pass
    return render_template("result.html", score=score)

app.run() 
