#using the strategy of separate chaining with doubly-linked linked lists to resolve collision 
class Node(): 
    def __init__(self, data): 
        self.data = data 
        self.prev = None 
        self.next = None 
    
    def __str__(self): 
        return str(self.data) 
    
class DLLL(): 
    def __init__(self): 
        self.first = None
    
    def insert(self, data): 
        if self.first == None: 
            self.first = Node(data)
        else: 
            Newnode = Node(data) 
            current = self.first
            while current.next != None: 
                current = current.next
            current.next = Newnode
            current.next.prev = current 
        
    def delete(self, data): 
        if self.first == None: 
            return False 
        else: 
            current = self.first
            while current != None and current.data != data: 
                current = current.next 
            if current == None: 
                return False 
            else: 
                current.prev.next = current.next 
                current.next.prev = current.prev 
                return True 
    
    def exists(self, data): 
        if self.first = None: 
            return False 
        else: 
            current = self.first 
            while current != None and current.data != data: 
                current = current.next
            if current == None: 
                return False 
            else: 
                return True 

    def print(self): 
        current = self.first
        while current != None: 
            print(current)
            current = current.next 

class HashTable():
    def __init__(self, size): 
        self._size = size 
        self._array = [DLLL() for i in range(size)]

    def hash(self, data):
        return hash(data)%self._size 
    
    def isFull(self): 
        for i in range(self._size): 
            if self._array[i].first == None: 
                return False 
        return True 

    def isEmpty(self): 
        for i in range(self._size): 
            if self._array[i].first != None: 
                return False 
        return True 
    
    def insert(self, data): 
        target = self.hash(data)
        self._array[target].insert(data)
    
    def exists(self, data): 
        target = self.hash(data)
        return self._array[target].exists(data)
    
    def delete(self, data): 
        target = self.hash(data) 
        return self._array[target].delete(data) 
    
    def print(self): 
        for i in range(self._size):
            if self._array[i].first != None: 
                self._array[i].print()

t = HashTable(5)
print(t.isEmpty())
t.insert(1)
t.insert(2)
print(t.isEmpty())
print(t.isFull())
t.insert(3)
t.insert(4)
t.insert(5)
print(t.isFull())
print("Hash table: ")
t.print()