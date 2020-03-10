##2019 CT computing revision

''' ------------- Worksheet 6 -------------- '''
#Search Algorithm 
#linear search 
def linear_search(L, t): 
	for i in range(len(L)): 
		if L[i] == t: 
			return i 
	return -1 

#binary search 
def binary_search(L, t): 
	start = 0 
	end = len(L)-1 
	while start <= end: 
		mid = (start+end)//2 
		if L[mid] == t: 
			return mid
		elif L[mid] < t:
			start = mid+1
		else: 
			end = mid-1 
	return -1 


''' ------------- Worksheet 7 -------------- '''
#k2d
def k2d(s, k):
	mapping = "0123456789ABCDEFG" 
	result = 0 
	for i in range(len(s)): 
		result += mapping.index(s[i]) * k**(len(s)-i-1) 
	return result 

def d2k(d, k): 
	mapping = "0123456789ABCDEFG" 
	result = "" 
	while d > 0: 
		result = mapping[d%k]
		d //= k 
	return result 

''' ------------- Worksheet 8 -------------- '''
#sort algorithm 
#bubble sort 
def bubbleSort(L): 
	for i in range(len(L)-1): 
		swap = False 
		for j in range(len(L)-i-1): 
			if L[j] > L[j+1]: 
				L[j], L[j+1] = L[j+1], L[j] 
		if not swap: 
			break 
	return L 

#insertion sort 
def insertion sort(L): 
	for i in range(1, len(L)): 
		for j in range(i, 0, -1): 
			if L[j] < L[j-1]: 
				L[j], L[j-1] = L[j-1], L[j] 
	return L 

#quicksort 
def quickSort(L): 
	less = [] 
	more = []
	pivot = L[0]
	for i in range(1, len(L)): 
		if L[i] < pivot: 
			less.append(L[i]) 
		else: 
			more.append(L[i]) 
	return quickSort(less) + [pivot] + quickSort(more) 


''' ------------- Worksheet 9 -------------- '''
#linked list
class Node():
	def __init__(self, data): 
		self.data = data 
		self.prev = None 
		self.next = None 

#singly linked list(SLLL)
class SLLL(): 
	def __init__(self): 
		self.first = None 

	def isEmpty(self): 
		if self.first == None: 
			return True 
		else: 
			return False 

	def insertFront(self, data): 
		newNode = Node(data) 
		newNode.next = self.first 
		self.first = newNode 

	def insertBack(self, data): 
		newNode = Node(data) 
		current = self.first 
		while current.next != None: 
			current = current.next 
		current.next = newNode 

	def exist(self, data): 
		if self.isEmpty(): 
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
		if self.isEmpty(): 
			return False 
		else: 
			if self.first.data == data: 
				self.first = self.first.next 
				return True 
			else: 
				previous = self,first 
				while previous.next != None and previous.next.data != None: 
					previous = previous.next 
				if.next == None: 
					return False 
				else: 
					previous.next previous.next.next 
					return True 

#doubly linked list(DLLL)
class DLLL(SLLL): 
	def insertFront(self, data): 
		newNode = Node(data) 
		if self.first != None: 
			self.first.prev = newNode
		newNode.next = self.first 
		self.first = newNode 

	def insertBack(self, data): 
		newNode = Node(data) 
		if self.isEmpty(): 
			self.first = newNode 
		else: 
			current = self.first 
			while current.next != None: 
				current = current.next 
			current.next = newNode
			newNode.prev = current 

	def delete(self, data): 
		if self.isEmpty(): 
			return False 
		else: 
			previous = self.first 
			while previous.next != None and previous.next.data != data: 
				previous = previous.next
			if previous.next == None: 
				return False 
			else: 
				previous.next = previous.next.next 
				if previous.next != None: 
					prevous.next.prev = previous 
				return True 

#doubly linked circular list(DLCLL)
class DLCLL(DLLL): 
	def insertFront(self, data): 
		newNode = Node(data)
		if self.isEmpty(): 
			self.first = newNode 
			self.first.prev = self.first
			self.first.next = self.first 
		else: 
			newNode.prev = self.first.prev 
			newNode.next = self.first 
			self.first.prev.next = newNode 
			self.first.prev = newNode
			self.first = newNode 

	def insertBack(self, data): 
		newNode = Node(data) 
		if self.isEmpty(): 
			self.first = newNode 
			self.first.prev = self.first
			self.first.next = self.first 
		else: 
			current = self.first.prev 
			newNode.prev = current
			newNode.next = current.next 
			current.next.prev = newNode
			current.next = newNode

	def delete(self, data): 
		if self.isEmpty(): 
			return False 
		else: 
			if self.first.data == data: 
				if self.first.next == self.first: 
					self.first = None 
				else: 
					self.first.prev.next = self.first.next 
					self.first.next.prev self.first.prev 
					self.first = self.first.next 
				return True 
			else: 
				current = self.first 
				if current.next != self.first and current.data != data: 
					current = current.next 
				if current.next == self.first: 
					return False 
				else: 
					current.next.prev = current.prev 
					current.prev.next = current.next 
					return True 

''' ------------- Worksheet 10 -------------- '''
#stack and queue 
#stack
class stack(): 
	def __init__(self, size): 
		self.size = size 
		self.top = -1 
		self.array = [None for i in range(size)] 

	def isFull(self): 
		return self.top == self.size -1 

	def isEmpty(self): 
		return self.top == -1 

	def push(self, data): 
		if self.isFull(): 
			return False 
		else: 
			self.top += 1
			self.array[self.top] = data 
			return True 

	def pop(self): 
		if self.isEmpty(): 
			return False
		else: 
			toPop = self.array[self.top] 
			self.array[self.top] = None 
			self.top -= 1
			return toPop

	def peek(self):
		return self.array[self.top] 

#queue 
class queue(): 
	def __init__(self, size): 
		self.size = size 
		self.head = -1 
		self.tail = 0 
		self.array = [None for i in range(size)] 

	def isFull(self): 
		return self.head == self.tail 

	def isEmpty(self): 
		return self.head = (self.tail+1)%self.size 

	def enqueue(self, data): 
		if self.isFull(): 
			return False 
		else: 
			self.array[self.tail] = data 
			self.tail = (self.tail+1)%self.size 
			if self.head < 0: 
				self.head = 0 
			return True 

	def dequeue(self): 
		if self.isEmpty(): 
			return False 
		else: 
			toDequeue = self.array[self.head]
			self.array[self.head] = None 
			self.head = (self.head+1)%self.size 
			if self.head == self.tail: 
				self.head, self.tail = -1, 0 
			return toDequeue 

	def peek(self): 
		if self.isEmpty(): 
			return False 
		else: 
			return self.array[self.head] 


''' ------------- Worksheet 11 -------------- '''
#binary search tree 
class Node_bst(): 
	def __init__(self, data): 
		self.data = data 
		self.left = None 
		self.right = None 

	def __str__(self): 
		return ("Data: {}".format(self.data))

class BST(): 
	def __init__(self):
		self.root = None 

	def insert(self, data):
		insertRec(data, self.first)

	def insertRec(self, data, current): 
		if current == None: 
			current = Node_bst(data)
		elif current.data > data:
			insertRec(data, current.left)
		else:  
			insertRec(data, current.right) 

	def insertItr(self, data): 
		newNode = Node_bst(data)
		if self.root == None: 
			self.root = newNode
		else: 
			current = self.root 
			while True: 
				if current == None:
					current = newNode
				elif current.data > data: 
					current = current.left 
				else: 
					current = current.right 

	def exist(self, data): 
		current = self.root
		while True: 
			if current.data == data: 
				return True 
			elif current == None: 
				return False 
			elif current.data > data: 
				current = current.left
			else: 
				current = current.right 

	def inOrder(self): 
		inOrderRec(self.first)

	def inOrderRec(self, current): 
		if current != None: 
			inOrderRec(current.left) 
			print(current) 
			inOrderRec(current.right)

	def preOrder(self): 
		preOrderRec(self.first)

	def preOrderRec(self, current): 
		if current != None: 
			print(current)
			preOrderRec(current.left)
			preOrderRec(current.right)

	def postOrder(self): 
		postOrderRec(self.first)

	def postOrderRec(self, current): 
		if current != None: 
			postOrderRec(current.left)
			postOrderRec(current.right) 
			print(current)


''' ------------- Worksheet 12 -------------- '''
#hash table 
#open addressing 
class HashTable(): 
	def __init__(self, size): 
		self.size = size 
		self.array = [None for i in range(size)]

	def hash(self, data): 
		return hash(data)%self.size 

	def isFull(self): 
		for i in range(self.size): 
			if self.array[i] == None: 
				return False 
		return True 

	def isEmpty(self): 
		for i in range(self.size): 
			if self.array[i] != None: 
				return False 
		return True 

	def insert(self, data): 
		if self.isFull(): 
			return False 
		else: 
			target = self.hash(data) 
			while self.array[target] == None: 
				target = (target+1)%self.size 
			self.array[target] = data 
			return True 

	def exist(self, data): 
		if self.isEmpty(): 
			return False 
		else: 
			target = self.hash(data)
			end = target
			while self.array[target] != data: 
				target = (target+1)%self.size 
				if target == end: 
					break 
			if self.array[target] == data: 
				return True 
			else: 
				return False 

	def delete(self, data): 
		if self.isEmpty(): 
			return False 
		else: 
			target = self.hash(data) 
			end = target
			while self.array[target] != data: 
				target = (target+1)%self.size 
				if target == end: 
					return False 
			if self.array[target] == data: 
				self.array[target] = None 
				return True 
			else: 
				return False 


#separate lining using DLLL 
class HashTable2(HashTable): 
	def __init__(self, size): 
		self.size = size 
		self.array = [DLLL() for i in range(size)]

	def isFull(self): 
		for i in range(self.size): 
			if self.array[i].first == None: 
				return False 
		return True 

	def isEmpty(self): 
		for i in range(self.size): 
			if self.array[i].first != None: 
				return False 
		return True 

	def insert(self, data): 
		target = self.hash(data) 
		self.array[target].insertBack(data) 

	def exist(self, data): 
		target = self.hash(data)
		return self.array[target].exist(data)

	def delete(self, data): 
		target = self.hash(data) 
		return self.array[target].delete(data) 

