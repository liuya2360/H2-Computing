#Task 4.1
def hex2d(hex):
    mapping = "0123456789abcdef"
    value = 0
    for i in range(len(hex)):
        value += mapping.index(hex[i])* 16**(len(hex)-1-i)
    return value

#Task 4.2
def d2hex(d):
    mapping = "0123456789abcdef"
    result = ""
    while d > 0:
        result = mapping[d%16] + result
        d //= 16
    return result

#Task 4.3
def calCheckSum(hexa_list):
    checkSum = 0
    for i in hexa_list:
        checkSum += hex2d(i)
    return d2hex(checkSum%16)

#Task 4.4
fileHandle = open("hex_dump.txt")
line = fileHandle.read().split("\n")
fileHandle.close()
data = []
newFile = open("checksums_LiuYa_G1647704X.txt", "w")
newFile.close()
for row in line:
    if len(row) == 0:
        break
    temp = row.strip().split(",")
    data.append(temp[:])
    checkSum = calCheckSum(temp)
    while len(checkSum) < 2:
        checkSum = "0"+checkSum
    temp.append(checkSum)
    with open("checksums_LiuYa_G1647704X.txt", "a") as f:
        newRow = ",".join(temp)
        newRow = newRow + "\n"
        f.write(newRow)
        
checkSumColumn = []
for column in range(len(data[0])):
    temp = []
    for i in range(len(data)):
        temp.append(data[i][column])
    checkSum = calCheckSum(temp)
    while len(checkSum) < 2:
        checkSum = "0"+checkSum
    checkSumColumn.append(checkSum)
with open("checksums_LiuYa_G1647704X.txt", "a") as f:
    newRow = ",".join(checkSumColumn)
    newRow = newRow + "\n"
    f.write(newRow)
                
