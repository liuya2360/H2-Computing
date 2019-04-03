file_handle = open("INTEGER.TXT", "a")

while True:
	user_input = input("Please input an integer:")
	if user_input == "exit":
		break
	try:
		rational_number = float(user_input)
		if rational_number % 1 == 0:
			file_handle.write(str(int(rational_number))+"\n")
		else:
			raise ValueError
	except ValueError:
		print("Please enter an INTEGER.")