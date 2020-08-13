#linked list 
#insert front, insert back, exist, delete, print, insert in order 
class Node(): 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
        self.prev = None 

class SLLL(): 
    def __init__(self): 
        self.first = None 

    def insertFront(self, data): 
        newNode = Node(data) 
        if self.first == None: 
            self.first = newNode
        else: 
            newNode.next = self.first 
            self.first = newNode 
    
    def insertBack(self, data): 
        newNode = Node(data)
        if self.first == None: 
            self.first = newNode 
        else: 
            current = self.first 
            if current.next != None: 
                current = current.next 
            current.next = newNode 

    def exist(self, data): 
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

    def delete(self, data): 
    	if self.first == None: 
    		return False 
    	else: 
    		if self.first.data == data: 
    			self.first = self.first 
    		previous = self.first 
    		if previous.next != None and previous.next.data != data: 
    			previous = previous.next 
    		if previous.next == None: 
    			return False 
    		else: 
    			previous.next = previous.next.next 

    def print(self): 
    	if self.first == None: 
    		print("Empty")
    	else: 
    		current = self.first 
    		while current != None: 
    			print(current.data) 
    			current = current.next 

    def insertInOrder(self, target, data): 
    	newNode = Node(data)
    	if self.first == None: 
    		self.first = newNode 
    	else: 
    		current = self.first 
    		while current != None and current.data != data: 
    			current = current.next 
    		if current == None: 
    			return False 
    		else: 
    			newNode.next = current.next
    			current.next = newNode 
    			return True 


class DLLL(): 
	def __init__(self):
		self.first = None 

	def insertFront(self, data): 
		newNode = Node(data)
		newNode.next = self.first
		if self.first != None: 
			self.first.prev = newNode
		self.first = newNode 

	def insertBack(self, data): 
		newNode = Node(data) 
		if self.first == None: 
			self.first = newNode 
		else: 
			current = self.first
			while current.next != None: 
				current = current.next 
			current.next = newNode
			newNode.prev = current 

	def exist(self, data): 
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

	def print(self): 
		if self.first == None: 
			print("Empty") 
		else: 
			current = self.first 
			while current != None: 
				print(current.data) 
				current = current.next 

	def insertInOrder(self, target, data): 
		newNode = Node(data) 
		if self.first == None: 
			self.first = newNode 
			return True  
		else: 
			current = self.first 
			while current != None and current.data != target: 
				current = current.next 
			if current == None: 
				return False 
			else: 
				newNode.next = current.next 
				newNode.prev = current 
				current.next = newNode
				if newNode.next != None: 
					newNode.next.prev = newNode 
				return True 
