#all attributes are public

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class SLLL():
    def __init__(self):
        self.first = None 
    
    def insertBack(self, data):
        newNode = Node(data)
        if self.first == None:
            self.first = newNode
        else: 
            current = self.first 
            while current.next != None: 
                current = current.next 
            current.next = newNode 
        
    def insertFront(self, data):
        newNode = Node(data)
        newNode.next = self.first 
        self.first = newNode 
    
    def delete(self, data): 
        if self.first == None: 
            return False 
        else: 
            if self.first == data: 
                self.first = self.first.next 
                return False
            else: 
                previous = self.first 
                while previous != None and previous.next.data != data:
                    previous = previous.next 
                if previous.next.data == data: 
                    previous.next = previous.next.next
                    return True 
                else: 
                    return False 

    def exist(self, data):
        if self.first == None:
            return False:
        else:
            current = self.first
            while current.data != data and current.next != None:
                current = current.next 
            if current.data == data:
                return True 
            else: 
                return False 
            
    def __str__(self):
        if self.first == None:
            return "Empty"
        else: 
            res = ""
            current = self.first
            while current != None:
                res += str(current) + "\n"
                current = current.next 
            return res 

def DLLL():
    def __init__(self):
        self.first = None
     
    def insertBack(self, data):
        newNode = Node(data)
        if self.first == None:
            self.first = newNode
        else: 
            current = self.first 
            while current.next != None: 
                current = current.next 
            current.next = newNode 
            current.next.prev = current
        
    def insertFront(self, data):
        newNode = Node(data)
        newNode.next = self.first 
        self.first = newNode 
        self.first.next.prev = self.first 

    def delete(self, data):
        if self.first == None: 
            return False 
        else: 
            current self.first 
            #must check if current is none or not or the code will throw an error when trying to check current.data
            while current != None and current.data != data: 
                current = current.next
            if current == None: 
                return False 
            else: 
                if current is self.first: 
                    self.first = self.first.next 
                    if self.first != None: 
                        self.first.prev = None 
                else: 
                    current.prev.next = current.next 
                    if current.next != None:
                        current.next.prev = current.prev
                return True 
    
    def delete_prev(self, data): 
        if self.first == None: 
            return False 
        else: 
            if self.first == data: 
                self.first = self.first.next 
                if self.first != None: 
                    self.first.prev = None
                return False
            else: 
                previous = self.first 
                while previous.next != None and previous.next.data != data:
                    previous = previous.next 
                if prevous.next == None: 
                    return False
                else: 
                    previous.next = previous.next.next
                    if previous.next.next != None: 
                        previous.next.next.previous = previous 
                    return True 

    def exist(self, data):
        if self.first == None:
            return False:
        else:
            current = self.first
            while current.data != data and current.next != None:
                current = current.next 
            if current.data == data:
                return True 
            else: 
                return False 
            
    def __str__(self):
        if self.first == None:
            return "Empty"
        else: 
            res = ""
            current = self.first
            while current != None:
                res += str(current) + "\n"
                current = current.next 
            return res 