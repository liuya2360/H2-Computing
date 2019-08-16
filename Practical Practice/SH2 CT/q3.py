class Node(): 
    def __init__(self, data):
        self.data = data 
        self.link1 = None 
        self.link2 = None 

    def print(self): 
        print("DATA: " + str(self.data) + "; LINK1: " + str(self.link1) + "; LINK2: " + str(self.link2))

class DLLNode(Node): 
    def __init__(self): 
        self.prev = self.link1 
        self.next = self.link2
    
    def print(self): 
        print("DLL.DATA: " + str(self.data)) 
        print("PREV: " + str(self.prev)) 
        print("NEXT: " + str(self.next)) 
        
class DLL(): 
    def __init__(self): 
        self.first = None 
    
    def insertFront(self, data): 
        if self.first == None: 
            self.first = Node(data) 
        else: 
            newNode = Node(data) 
            self.first.prev = newNode
            newNode.next = self.first 
            self.first = newNode
    
    def contains(self, value): 
        if self.first == None: 
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
        if self.first == None: 
            print("The doubly linked list is empty.") 
        else: 
            current = self.first 
            while current != None: 
                current.print() 
                current = current.next 

class Word(str): 
    def __hash__(self): 
        return sum(ord(self[i])*i) for i in range(len(self)) 
    
    def print(self): 
        print(self.upper()) 

class HT(): 
    def __init__(self, size): 
        self.size = size 
        self.array = [DLL() for i in range(size)] 
    
    def insert(self, data): 
        target = Word(data).hash() % self.size 
        self.array[target].insertFront(data) 
    
    def contains(self, data): 
        target = Word(data).hash() % self.size 
        if self.array[target].first == None: 
            return False 
        else: 
            targetDLL = self.array[target]
            current = targetDLL.first 
            while current != None and current.data != data: 
                current = current.next 
            if current == None: 
                return False 
            else: 
                return True 
    
    def print(self): 
        for i in range(self.size): 
            if self.array[i].first != None: 
                self.array[i].print() 

class BSTNode(Node): 
    def __init__(self, key, ht):
        self.data = (key, ht) 
        self.left = self.link1 
        self.right = self.link2 

    def print(self): 
        print("KEY: " + str(self.data[0])) 
        print("BST.DATA: ")
        self.data[1].print() 
        print("LEFT: " + str(self.left.data[0])) 
        print("RIGHT: " + str(self.right.data[0]))  

class BST(): 
    def __init__(self): 
        self.root = None 

    def insert(self, word): 
        targetKey = word[0].upper() 
        current = self.root 
        while current != None and current.data[0] != targetKey: 
            if ord(current.data[0]) < ord(targetKey): 
                current = current.left 
            else: 
                current = current.right 
        if current != None: 
            current.data[1].insert(word)
    
    def contains(self, word): 
        targetKey = word[0].upper() 
        current = self.root 
        while current != None and current.data[0] != targetKey: 
            if ord(current.data[0]) < ord(targetKey): 
                current = current.left 
            else: 
                current = current.right 
        if current == None: 
            return False 
        else: 
            return current.data[1].contains(word) 

    def print(self): 
        