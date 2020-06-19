#Q2
#Task 2.1
def CheckDigits(iban):
    #step 1 + 2
    temp = iban[:2] + "00" 
    iban = iban + temp
    iban = iban[4:]
    
    #step 3
    i = 0 
    while True: 
        if iban[i].isalpha():
            iban = iban[:i] + str(ord(iban[i])-55) + iban[i+1:]
        i += 1
        if i >= len(iban):
            break 
    
    #step 4 - 6
    iban = int(iban)
    result = 98 - iban % 97
    
    return str(result)  

print(CheckDigits("GB00WEST12345698765432")) 
print(CheckDigits("GB00NWBK60161331926819"))
print(CheckDigits("GB00LOYD30952013145983")) 


#Task 2.2
def ValidateIBAN(iban):
    #step 1
    temp = iban[:4]
    iban = iban + temp
    iban = iban[4:]

    #step 2
    i = 0 
    while True: 
        if iban[i].isalpha():
            iban = iban[:i] + str(ord(iban[i])-55) + iban[i+1:]
        i += 1
        if i >= len(iban):
            break 

    #step 3 
    iban = int(iban)
    if iban % 97 == 1:
        return True
    else:
        return False

def CheckIBAN():
    with open("TRANSACTIONS.TXT") as f:
        line = f.read()
    data = line.strip().split("\n")
    for row in range(len(data)):
        iban = data[row][:22]
        if ValidateIBAN(iban):
            print(iban + " OK")
        else:
            corrCheckDigits = CheckDigits(iban)
            print("Invalid. Expected check digids: {}".format(corrCheckDigits))
            data[row] = data[row][:2] + corrCheckDigits + data[row][4:]
    with open("TRANSACTIONS.TXT", "w") as f:
        line = "\n".join(data)
        f.write(line)

CheckIBAN() 

#Task 2.4
def UpdateBalance():
    with open("ACCOUNTS.TXT") as f:
        line = f.read()
    line = line.strip().split("\n")
    balance = {}
    for row in line:
        iban = row[:22]
        name = row[22:37]
        num = row[37:]
        name = name.replace(" ", "")
        
