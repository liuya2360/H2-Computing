word = ["zero","one","two","three","four","five","six","seven","eight","nine"]

def it_print(s):
	for number in s:
		print(word[int(number)], end = " ")

s = input()

for number in s:
	print(word[int(number)], end = " ")
	
print("")