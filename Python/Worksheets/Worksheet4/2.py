from random import randint
for i in range(100):
	name = "" 
	name = name + str(randint(0,9))
	name = name + ".txt"
	try:
		fileHandle = open(name)
		data = fileHandle.read()
		print(data)
		fileHandle.close()
	except:
		continue