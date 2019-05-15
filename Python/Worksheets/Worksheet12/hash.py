class HashTable():
    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(size)] 

    def hash(self, data): 
        return hash(data) % self.size 
    
    def insert(self, data, key): 
        target = self.hash(key) 
        end = target 
        while self.array[target] != None: 
            target = (target+1) % self.size 
            if target == end: 
                print("Hash table full. Cannot insert")
                return 
        self.array[target] = (key, data)

    def delete(self, key):
        target = self.hash(key) 
        end = target 
        while self.array[target][0] != key: 
            target = (target+1) % self.size 
            if target == end: 
                return False 
        self.array[target] = None 
        return True 
    
    def search(self, key): 
        target = self.hash(key) 
        end = target
        while self.array[target][0] != key: 
            target = (target+1) % self.size 
            if target == end: 
                return False: 
        return self.array[target][1]
    
    def print(self): 
        for i in range(self.size): 
            if self.array[i] != None: 
                print("{0:10}{0:10}".format(i, self.array[i]))