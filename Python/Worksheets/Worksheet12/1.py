class HashTable():
    def __init__(self, size):
        self._array = [None for i in range(size)]
        self._size = size 

    def hash(self, data):
        return hash(data) % self._size

    def isFull(self):
        for i in range(self._size): 
            if self._array[i] == None: 
                return False
        return True 
    
    def isEmpty(self):
        for i in range(self._size):
            if self._array[i] != None: 
                return False
        return True 
    
    def insert(self, data): 
        target = self.hash(data) 
        end = target 
        while self._array[target] != None:
            target = (target+1)%self._size
            if target == end:
                print("Hash tabel is full. ")
                return 
        self._array[target] = data 
    
    def exist(self, data): 
        target = self.hash(data) 
        end = target 
        while self._array[target] != data: 
            target = (target+1)%self._size 
            if target == end: 
                return False 
        return True 
    
    def delete(self, data):
        target = self.hash(data) 
        end = target 
        while self._array[target] != data:
            target = (target+1)%self._size 
            if target == end: 
                return False 
        self._array[target] = None 
        return True 
    
    def print(self):
        for i in range(self._size):
            if self._array[i] != None: 
                print(self._array[i]) 
