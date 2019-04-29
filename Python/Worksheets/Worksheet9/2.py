#all attributes should be private 
class Node():
    def __init__(self, data):
        self._data = data
        self._next = None 
        self._prev = None 
    
    def getData(self):
        return self._data 
    
    def getNext(self):
        return self._next 
    
    def setNext(self, data):
        self._next = data
    
    def getPrev(self):
        return self._prev
        
    def setPrev(self, data):
        self._prev = data

class SLLL():
    def __init__(self):
        self._first = None
    
    def getRoot(self):
        return self._first
    
    def setRoot(self, node): 
        self._first = node 
    
    def isEmpty(self):
        if self._first == None: 
            return True 
        else: 
            return False 

    def insertFront(self, data): 
        newNode = Node(data)
        newNode.setNext(self._first)
        self._first = newNode

    def insertBack(self, data): 
        newNode = Node(data) 
        current = self._first 
        while current._next != None:
            current = current.getNext()
        current.setNext(newNode) 

    def delete(self, data): 
        if self._first == None: 
            return False 
        else: 
            previous = self._first 
            if previous.getData() == data: 
                self._first = previous.getNext()
                return True 
            else: 
                while previous.getNext().getData() != data and previous.getNext() != None: 
                    previous = previous.getNext() 
                if previous.getNext().getData() == data: 
                    previous.setNext(previous.getNext().getNext()) 
                    return True
                else: 
                    return False 

    def exist(self, data): 
        if self._first == None: 
            return False 
        else: 
            current = self._first 
            while current.getData() != data and current.getNext() != None: 
                current = current.getNext() 
            if current.getData() == data: 
                return True 
            else: 
                return False 

    def getNode(self, data): 
        if self._first == None: 
            return None 
        else: 
            current = self._first 
            if current.getData() != data and current != None: 
                current = current.getNext()
            if current.getData == data: 
                return current 
            else: 
                return None 

    def print(self):
        result = "" 
        current = self._first 
        while current != None: 
            result += str(current.getData()) + "\n" 
            current = current.getNext() 
        print(result) 

class DLLL(SLLL):
    def insertFront(self, data):
        newNode = Node(data) 
        if self._first == None: 
            self._first = newNode 
        else: 
            self._first.setPrev(newNode)
            newNode.setNext(self._first)
            self._first = newNode
    
    def insertBack(self, data):
        newNode = Node(data)
        if self._first == None: 
            self._first = newNode
        else: 
            current = self._first
            while current.getNext() != None: 
                current = current.getNext()
            current.setNext(newNode)
            newNode.setPrev(current)

    def delete(self, data):
        if self._first == None:
            return False
        else: 
            current = self._first 
            while current.getData() != data and current != None:
                current = current.getNext()
            if current.getData == data: 
                current.getPrev().setNext(current.getNext())
                if current.getNext() != None: 
                    current.getNext().setPrev(current.getPrev())
                return True 
            else: 
                return False 
