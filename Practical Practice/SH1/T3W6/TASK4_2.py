import sqlite3 
con = sqlite3.connect("Portal.db") 

userInfo = []
with open("USERS.TXT") as fileHandle: 
    firstRow =  True 
    for row in fileHandle: 
        if firstRow: 
            firstRow = False 
            continue 
        else: 
            row = row.strip().split(',') 
            userInfo.append(row)

def hashPassword(passwordInput):
    asciiSum = 0 
    for i in range(len(passwordInput)): 
        asciiSum += ord(passwordInput[i]) 
    password = hex(asciiSum)
    return password

passwordDefault = "19SH07njc" 
passwordDefault = hashPassword(passwordDefault)
print(passwordDefault)

for i in range(len(userInfo)): 
    con.execute("INSERT INTO User(Name, LoginID, PasswordHash) VALUES (?,?,?)", (userInfo[i][0], userInfo[i][2], passwordDefault))
    con.commit() 
    con.close() 