debug = False 

#Task 1 
import os 
home = os.getcwd() 
templates_path = os.path.join(home, "templates") 
if not os.path.exists(templates_path): 
    os.mkdir(templates_path)

#read in the instructions from the user 

#enter the title of the web page 
title_message = "Please enter the title for the web page: "
while True: 
    title = input(title_message) 
    if len(title) != 0: 
        break 
    else: 
        title_message = "Please enter a valid title:  "
if debug: 
    print("title: "+title)

#enter the inputs of the web form 
input_list = []
input_type = ['t','b','i'] 
input_type_list = [] 
url = []
input_message = "Please enter the input name (input [END] to end):  "
while True: 
    temp = input(input_message) 
    if temp == "END": 
        break 
    elif temp == "": 
        input_message = "Please enter a valid input name (input [END] to end):  "
        continue 
    else: 
        input_list.append(temp) 
        new_input = temp 
        input_type_message = "Please enter the input type ([t]ext, [b]utton, OR [i]mage):  "
        while True: 
            temp = input(input_type_message) 
            if temp in input_type: 
                input_type_list.append(input_type.index(temp)) 
                if temp == "b": 
                    #input the html to submit to 
                    url_temp = input("Please enter the URL to submit the form to:  ")
                    if debug: 
                        print("url: ", url_temp) 
                    url.append(url_temp)
                else: 
                    url.append("")
                break 
            else: 
                input_type_message = "Please enter a valid input type:  [t]ext, [b]utton, [f]ile, OR [i]mage" 
if debug: 
    print("input list:", input_list) 
    print("input type list:", input_type_list)
    print("url list:", url)

'''
#input the html to submit to 
url = input("Please enter the URL to submit the form to:  ")
if debug: 
    print("url: ", url) 
'''

#generate the html file 
#begining of the html
html_1 = "<!DOCTYPE html>\n<html>\n    <head>\n        <title>"

#insert title (between html_1 and html_2) 

html_2 = "</title>\n        <style>"
#insert the internal css formatting 
css_format = ""

html_3 = "</style>\n    </head>\n    <body>\n"

#insert the main form
form = "        <form action=\"/submit\" method=\"post\" enctype=\"multipart/form-data\">\n"
input_html_1 = "            <div>\n             <label for=\"" #insert the name of the input 
input_html_2 = "\">" #insert the name of the input 
input_html_3 = "</label>\n              <input type=\"" #insert the type depending on the input type> 
input_html_4 = "\" name=\"" #input the name of the input 
input_html_5 = "\">\n           </div>\n"
#insert all the text and image input
for i in range(len(input_list)): 
    if input_type[input_type_list[i]] == 'b': 
        continue 
    temp = "" 
    temp = input_html_1 + input_list[i] + input_html_2 + input_list[i] + input_html_3 
    if input_type[input_type_list[i]] == 'i': 
        temp = temp + "file"
    else: 
        temp = temp + "text"
    temp = temp + input_html_4 + input_list[i] + input_html_5 
    form = form + temp 
#insert all the button input 
for i in range(len(input_list)): 
    if input_type[input_type_list[i]] != 'b': 
        continue 
    temp = "            <div>\n                <button type=\"submit\" name=\"" + input_list[i] + "\" value=\"" + input_list[i] + "\">" + input_list[i] + "</button>\n            </div>\n"
    #html code for button and link it to the url
    form = form + temp 
form = form + "        </form>\n"


html_4 = "    </body>\n</html>"
#end of the html 

os.chdir(templates_path)
with open(title+".html", "w") as f: 
    f.write(html_1 + title + html_2 + css_format + html_3 + form + html_4) 
os.chdir(home)

#----------------------------------------------

#Task 2 

#write the python/flask/SQL code to process the form and insert records 

python_code = ""

#import library 
import_lib = "from flask import Flask, render_template, request, redirect, url_for \n\
import sqlite3 \n\n" 

#define the app 
define_app = "app = Flask(\"__name__\")\n\n"

#connect to database
connect_to_database = "def open_DB(db): \n    connection = sqlite3.connect(db) \n    connection.row_factory = sqlite3.Row \n    return connection\n\n"

#create sql table 
'''
create_table = "        create_table = \"CREATE TABLE `" + title + "` (\\n"
for i in range(len(input_list)): 
    create_table = create_table + "`" + input_list[i]+ "`	" + "TEXT"
    if i != len(input_list)-1: 
        create_table = create_table + ",\\n "
    else: 
        create_table = create_table + "\\n"
create_table = create_table + ");\""
create_table = create_table + "\n        cur.execute(create_table) \n\n"
'''
create_table = "CREATE TABLE `" + title + "` (\n"
for i in range(len(input_list)): 
    if input_type_list[i] == input_type.index("b"): 
        continue 
    create_table = create_table + "`" + input_list[i]+ "`	" + "TEXT"
    if i != len(input_list)-1: 
        create_table = create_table + ",\n "
    else: 
        create_table = create_table + "\n"
create_table = create_table + ");"
if debug: 
    print(create_table)
import sqlite3
def open_DB(db): 
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row 
    return connection
con = open_DB("table.db") 
cur = con.cursor()
cur.execute(create_table) 
con.commit() 
con.close() 

#root() and extract data from database 
root = "@app.route(\"/\") \n\
def root(): \n\
    con = open_DB('table.db') \n\
    cur = con.cursor()\n\
    try:\n \
        cur.excecute(\"SELECT * FROM " + title + "\")\n\
    except: \n\
        pass \n"\
    + "    con.commit()\n\
    con.close()\n\
    return render_template(\""+ title +".html\") \n\n"

#submit() 
submit = "@app.route(\"/submit\", methods=[\"POST\"]) \n\
def submit(): \n\
    image_file_name = ""\n"
if input_type.index("i") in input_type_list: 
    if debug: 
        print("image found")
    image_name = input_list[input_type_list.index(input_type.index("i"))]
    submit = submit + "    if \"" + image_name + "\" in request.files: \n\
        image_file = request.files[\""+ image_name +"\"] \n\
        image_file_name = image_file.filename \n\
        image_file.save(\"static/image/\"+image_file_name) \n"
submit = submit + "    try: \n\
        con = open_DB('table.db') \n\
        cur = con.cursor() \n\
        #generate SQL insert statement \n"
if input_type.index("i") in input_type_list: 
    submit = submit + "        if request.form[\"submit\"] == \"submit\" and image_file_name != \"\": \n\
            con.execute(\"INSERT INTO " + title + "(" + input_list[input_type_list.index(input_type.index("i"))]+") VALUES (?)\", (image_file_name,)) \n" 

for i in range(len(input_list)): 
    if input_type_list[i] == input_type.index("i"): 
        continue 
    elif input_type_list[i] == input_type.index("b"): 
        continue 
    submit = submit + "        con.execute(\"INSERT INTO " + title+ "(" + input_list[i]+") VALUES (?)\", (request.form[\"" + input_list[i] +"\"],))\n"

submit = submit + "        #execute and commmit \n\
        con.commit() \n\
        con.close() \n\
    except Exception as e: \n\
        print(str(e)) \n\
    return redirect(\""+ url[input_type_list.index(input_type.index("b"))] + "\") \n\n"

#run the app 
run_app = "if __name__ == \"__main__\": \n\
    app.run(debug=True)\n" 

#combine the code
python_code = import_lib + define_app + connect_to_database + root + submit + run_app

with open("server.py","w") as f: 
    f.write(python_code)