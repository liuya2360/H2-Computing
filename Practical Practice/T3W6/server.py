from flask import Flask, render_template, request, redirect 
import sqlite3 

def open_DB(db): 
    connection = sqlite3.connect(db) 
    connection.row_factory = sqlite3.Row 
    return connection 

app = Flask("__name__") 

def hashPassword(passwordInput):
    asciiSum = 0 
    for i in range(len(passwordInput)): 
        asciiSum += ord(passwordInput[i]) 
    password = hex(asciiSum)
    return password

@app.route("/") 
def root(): 
    return render_template("loginPage.html")

@app.route("/login", methods=["POST"]) 
def login(): 
    con = open_DB("Portal.db") 
    cur = con.execute("SELECT * FROM User") 
    userInfo = cur.fetchall() 
    con.close() 
    loginID = request.form["loginID"]  
    password = request.form["password"] 
    validInput = False
    for i in range(len(userInfo)):
        if userInfo[i]["loginID"] == loginID: 
            if userInfo[i]["PasswordHash"] == hashPassword(password): 
                validInput = True 
                return f"<html><body><h2 style=\"color:red\">Successful login.</h2></body></html>"
                #return render_template("loginPage.html", loginMessage="Successful login.")  
    if not validInput: 
        return render_template("loginPage.html", loginMessage="Please re-enter login id and password.") 

app.run(debug=True)