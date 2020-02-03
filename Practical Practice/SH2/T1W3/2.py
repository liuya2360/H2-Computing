#Q2

#Task 1
def strHash(data):
    res = 0
    for i in range(len(data)):
        res += ord(data[len(data)-i-1])*(i+1)
    return res

#Task 2
hashTable = []
size = None

def insert(
