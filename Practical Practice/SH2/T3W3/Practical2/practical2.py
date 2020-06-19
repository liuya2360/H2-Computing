## Start Coding : You have 45 mins
## Task 4:
#Task 4.1 
while True: 
  userinput = input("Please input an integer in the range 1 to 20: ") 
  
  if int(userinput) < 21 and int(userinput) > 0: 
    break 

def RomanNumeral(n): 
  res = ""
  '''
  for i in range(n//50): 
    res = res+"L"
  n -= n%50

  if n == 40: 
    res = "XL"+res 
    return res 
  '''
  if n == 4:
    return "IV"

  if n == 9: 
    res = "IX"+res 
    return res 

  for i in range(n//10): 
    res = res+"X" 
    n %= 10 
  
  if n >= 5: 
    res = res+"V" 
    n -= 5 

  for i in range(n): 
    res = res+"I" 

  return res 

print(RomanNumeral(int(userinput)))

#Task 4.3
seq = {0: "first", 1: "second"}
userinput = [None for i in range(2)]
check = {"I": 1, "V":5, "X":10}
for i in range(2):
  while True:
    temp = input("Please input" + seq[i] + "Roman numeral number between 1 and 20")
    
