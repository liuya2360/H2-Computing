debug = False

quan = int(input("Input a quantity: "))
m = input("Select either length, area or volume: ")
a = input("Select the base unit of measurement (mm, cm, m, km): ")
b = input("Select which base unit of measurement to convert to (mm, cm, m, km): ")

power = 0
if m == " length":
    power = 1
elif m == "area":
    power = 2
elif m == "volume":
    power = 3
    
a_p = 0
if a == "mm":
    a_p = 1
elif a == "cm":
    a_p = 2
elif a == "m":
    a_p = 4
elif a == "km":
    a_p = 8
b_p = 0
if b == "mm":
    b_p = 1
elif b == "cm":
    b_p = 2
elif b == "m":
    b_p = 4
elif b == "km":
    b_p = 8

if debug:
    print("power", power)
    print("a_p", a_p)
    print("b_p", b_p)

print(str(quan)+" "+a+"^"+str(power)+" = "+str(quan*(10**(a_p-b_p))**power)+" "+b+"^"+str(power))
