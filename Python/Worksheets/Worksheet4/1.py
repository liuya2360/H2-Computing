numbers = [x for x in range(1000)]
i = 0
while True:
	try:
		print(str(numbers[i]))
		i += 1
	except:
		break