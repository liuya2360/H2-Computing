#Task 1.1 
def k2d(k, l):
    mapping = "0123456789ABCDEF"
    res = 0
    l = l.upper() 
    for i in range(len(l)): 
        res += k ** (len(l)-1-i) * mapping.index(l[i])
    return res 

def hex2Str(data):
    data_formated = data.strip().split(" ") 
    res = []
    for i in data_formated:
        res.append(chr(k2d(16, i))) 
    return "".join(res)

#Task 1.2 
with open("ITEMS.TXT") as f:
    line = f.read()
raw_line = line.strip().split("\n") 
items = []
for row in raw_line:
    temp = hex2Str(row).strip().split(",")
    items.append([int(temp[0]), temp[1]])

items_dic = {items[i][0]: items[i][1] for i in range(len(items))}

#print(items)

#Task 1.3 
def mergeSort(array):
    if len(array) < 2:
        return array
    mid = len(array)//2
    return merge(mergeSort(array[:mid]), mergeSort(array[mid:]))

def merge(A, B):
    ret = []
    while len(A) and len(B):
        if A[0] < B[0]:
            ret.append(A[0])
            A.pop(0)
        else:
            ret.append(B[0])
            B.pop(0)
    if len(A) == 0:
        ret = ret + B
    else:
        ret = ret + A
    return ret

sorted_items = mergeSort(items)
#print(sorted_items) 

#Task 1.4
with open("CHARACTERS.TXT") as f:
    line = f.read()
raw_line = line.strip().split("\n")
characters = []
cnt = 0
prev_line = None
for row in raw_line:
    temp = hex2Str(row).strip().split(",")
    if cnt % 2 == 0:
        prev_line = temp
    else:
        temp_c = []
        for i in temp:
            temp_c.append(int(i))
        characters.append([prev_line, temp_c])
    cnt += 1
#print(characters) 

#Task 1.5
while True: 
    target = input("Please input a character name (enter EXIT to exit): ")
    if target == "EXIT":
        break 
    for i in range(len(characters)):
        if characters[i][0][0] == target:
            print(characters[i][0])
            item_list = characters[i][1] 
            for j in range(len(item_list)):
                print(items_dic[item_list[j]], end=" ")
            print() 
