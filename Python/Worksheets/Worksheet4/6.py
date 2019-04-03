import os
home = os.getcwd()

for i in os.lisdir():
	end = i[len(i)-5:]
	if end == ".calc":
		file_handle = open("i")
		operation = file_handle.read().split("\n")
		for row in operation:
			
