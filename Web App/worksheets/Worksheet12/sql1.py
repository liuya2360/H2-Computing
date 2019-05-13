import sqlite3 

con = sqlite3.connect("db1.db")

try: 
    con.execute("CREATE TABLE Book (ID INTEGER, title TEXT)")
except: 
    pass

while True: 
    operation = input("Please input operation type: [I]nsert, [D]elete, [E]nd: ")
    if operation.lower() == 'e': 
        break
    else: 
        id = input("Enter book id: ")
        if operation.lower() == 'i': 
            title = input("Enter book title: ")
            con.execute("INSERT INTO Book(ID, Title) VALUES (?,?)",(id, title))
        elif operation.lower() == 'd': 
            con.execute("DELETE FROM Book " + "WHERE ID=?",(id))
con.commit()

'''
#each row is retrieved as a dict mapping column names to values instead
con.row_factory = sqlite3.Row 
cursor = con.execute("SELECT ID, TITLE FROM BOOK")
for row in cursor: 
    print(row["title"])
    '''

#each row is retrieved as a list with index number 
cursor = con.execute("SELECT ID, TITLE FROM BOOK")
for row in cursor: 
    print(row[1])

con.commit()
con.close()