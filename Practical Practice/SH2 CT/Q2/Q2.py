import random 

def k2d(s, k): 
	s = s.lower()
	mapping = "0123456789abcdefghijklmnopqrstuvwxyz" 
	ans = 0 
	for i in range(len(s)): 
		ans += mapping.index(s[i]) * k ** (len(s)-i-1)
	return ans

fileHandle = open("ENCRYPTED.TXT") 
raw_data = [row.strip() for row in fileHandle] 
fileHandle.close()

general_base = int(raw_data[0][0:2]) 
base = [] 
while True: 
	if 2+len(base)*5 == len(raw_data[0]): 
		break 
	temp = raw_data[0][2+len(base)*5: 2+(len(base)+1)*5] 
	base.append(k2d(temp, general_base)) 

data = []
for i in range(len(raw_data)-1): 
	raw_row = raw_data[i+1] 
	new_row = ""
	while True: 
		if len(new_row)*8 == len(raw_row): 
			break 
		temp = raw_row[len(new_row)*8: (len(new_row)+1)*8] 
		new_row += (chr(k2d(temp, base[i])))
	data.append(new_row)
	
for row in data: 
	print(row) 

def d2k(n, k): 
	mapping = "0123456789abcdefghijklmnopqrstuvwxyz" 
	res = "" 
	while n > 0: 
		res = mapping[n%k] + res
		n //= k 
	res = res.upper()
	return res 

fileHandle = open("RAW.TXT")
raw_data = [row.strip() for row in fileHandle]
general_base = random.randint(2, 37) 
first_row = str(general_base)
base = []
for i in range(len(raw_data)): 
	base.append(random.randint(2, 32))
	new_base = d2k(base[i], general_base)
	while len(new_base) < 5: 
		new_base = '0' + new_base
	first_row = first_row + new_base

result = ""
result = result + first_row + "\n" 

for i in range(len(raw_data)): 
	new_row = "" 
	for j in range(len(raw_data[i])): 
		new_digit = d2k(ord(raw_data[i][j]), general_base) 
		while len(new_digit) < 8: 
			new_digit = '0' + new_digit 
		new_row = new_row + new_digit 
	new_row = new_row + "\n" 
	result = result + new_row 

with open("MY_RESULT.TXT", "w") as f: 
	f.write(result)