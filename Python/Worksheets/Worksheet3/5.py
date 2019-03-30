import re

file = open("shakespeare-romeo-48.txt")

text = []
for row in file:
	row = row.lower()
	row =  re.findall(r"[\w']+", row)
	for i in row:
		text.append(i)

l = dict()
for i in text:
	if i in l.keys():
		l[i] += 1
	else: 
		l[i] = 1

file.close()

l_keys = list(l.keys())
#print(l_keys[:10])

file_out = open("R&J_WORD_FREQS.TXT", "w")
for i in range(len(l)):
	line = l_keys[i]
	line += ": " + str(l[l_keys[i]])
	file_out.write(line+"\n")

file_out.close()