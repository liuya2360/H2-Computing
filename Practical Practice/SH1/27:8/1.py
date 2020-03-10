#linear search of a string 
def search(s, x):
    for i in range(len(s)): 
        if s[i] == x: 
            return i 
    return -1 

print(search("abcd", "a"))
print(search("abcd", "b")) 
print(search("abcd", "c"))
print(search("abcd", "")) 
print(search("abcd", "e"))
print(search("aaa", "a"))