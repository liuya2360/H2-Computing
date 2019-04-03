fileHandle = open("WORDS.TXT")
data = fileHandle.read().split("\n")

cnt_row = 0
word = ""
number = None
max_word = []
max_number = -1
#print(data)
for row in data:
	#print(row)
	if cnt_row % 2 == 0:
		try:
			word = str(row.strip())
			#print(word)
			cnt_row += 1
		except:
			continue
	else:
		try:
			number = int(row.strip())
			#print(number)
			cnt_row += 1
			if number > max_number:
				max_number = number
				max_word = []
				max_word.append(word)
			elif number == max_number:
				max_word.append(word)
		except:
			continue

for each_word in max_word:
	print(each_word)