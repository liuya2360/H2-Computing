debug = False 

#Task 2.1 
with open("ENCRYPTED.TXT") as f:
    file = f.read()
file = file.strip().split('\n')

#Task 2.2 
def k2d(s, k):
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = 0
    if debug:
        print(s)            
    s = s.upper()
    for i in range(len(s)):
        res += mapping.index(s[i]) * pow(k, len(s)-i-1)
    return res 

#Task 2.3 
general_base = int(file[0][:2])
line_base = []
for i in range(2, len(file[0]), 5):
    temp = file[0][i:i+5]
    line_base.append(k2d(temp, general_base))

if debug: 
    print(line_base)
    
for i in range(1, len(file)):
    temp = ""
    for j in range(0, len(file[i]), 8):
        temp = temp+chr(k2d(file[i][j:j+8], line_base[i-1]))
    print(temp) 

#Task 2.4
def d2k(n, k):
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n:
        res = mapping[n%k] + res
        n //= k
    return res 

#Task 2.5 
