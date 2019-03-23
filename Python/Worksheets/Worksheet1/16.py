c_10 = int(input("Enter the number of 10-cent coins inserted: "))
c_20 = int(input("Enter the number of 20-cent coins inserted: "))
c_50 = int(input("Enter the number of 50-cent coins inserted: "))
c_1 = int(input("Enter the number of 1-dollar coins inserted: "))
price = float(input("Please enter the price of the drink, i.e., 0.8 or 1.2: ")) * 100
total = c_10 * 10 +  c_20 * 20 + c_50 * 50 + c_1 * 100
print("Total inserted: $" + str(total))

cnt_1 = 0
cnt_50 = 0
cnt_20 = 0
cnt_10 = 0

total -= price
print("The machine returns a total of $" + str(total) + ", in the form of : ")

'''
print(total)
while(total > 1.0):
	total -= 1.0
	print(total)
	cnt_1 += 1
while(total > 0.5):
	total -= 0.5
	cnt_50 += 1
while(total > 0.2):
	total -= 0.2
	cnt_20 += 1
while(total > 0.1):
	total -= 0.1
	cnt_10 += 1
'''

cnt_1 = total // 100
total %= 100
cnt_50 = total // 50
total %= 50
cnt_20 = total // 20
total %= 20
cnt_10 = total // 10
total %= 10

print(str(int(cnt_1)) + " X 1-dollar coin(s)")
print(str(int(cnt_50)) + " X 50-cent coin(s)")
print(str(int(cnt_20)) + " X 20-cent coin(s)")
print(str(int(cnt_10)) + " X 10-cent coin(s)")
