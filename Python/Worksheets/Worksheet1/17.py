day = int(input("Day born? "))
month = int(input("Month born? "))
year = int(input("Year born? "))
yy = year % 100
century = year // 100

bday = (day + (month+1)//5 + yy + yy//4 + century//4 - 2*century) % 7
w = ["Saterday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print("Your birthday fell on: " + w[bday])
