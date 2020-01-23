#T1W1 Revision 

#repeatedly request a file name 
while True: 
	try: 
		filename = input("Please input a valid file name: ")
		with open(filename) as f: 
			line = f.read() 
		break 
	except: 
		print("Invalid input") 
		
#read the file to count the total number of lines in the file 
line = line.strip().split("\n") 
num_lines = len(line) 
num_items = [] 
for row in line: 
	row = row.split(",") 
	num_items.append(str(len(row))) 

with open("LOG.TXT", "w") as f: 
	f.write("Statistics for:" + str(filename) + "\n") 
	f.write("Total lines:" + str(num_lines) + "\n") 
	separator = "," 
	f.write("Items per Line:" + separator.join(num_items) +"\n") 
