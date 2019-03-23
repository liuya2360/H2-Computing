Q19 = True
Q20 = False

#Q19
while Q19:
    raw = input("Value? ")
    sf = int(input("Sig. Figs.? "))

    value = float(raw)
    sign = 1

    if value < 0:
        value = -value
        sign = -sign
    
    # let value = 0.x * 10 ** offset
    offset = 0
    if value < 0.1:
        while value < 0.1:
            value = value * 10
            offset -= 1
    if value > 1:
        while value >= 1:
            value = value / 10
            offset += 1

    value = round(value, sf) * 10 ** offset * sign
    if value % 1 == 0:
        value = int(value)
    value = str(value)

    valueLen = len(value)
    if "-"  in value:
        valueLen -= 1
    if "." in value:
        valueLen -= 1
    if offset < 0:
        valueLen -= abs(offset)
        valueLen -= 1 # for "0" in "0."
    extraZeros = max(0, sf - valueLen)

    if extraZeros > 0:
        if "." not in value:
            value = value + "."
    value = value + "0" * extraZeros

    print("The value " + raw + " to " + str(sf) + \
          " SF is: " + value)



#Q20
while Q20:
    pass























