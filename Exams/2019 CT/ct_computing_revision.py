#2019 CT computing revision

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
		if mid == t: 
			return mid
		elif mid < t: 
			start = mid+1
		else: 
			end = mid-1
	return -1

''' ------------- Worksheet 7 -------------- '''
#k2d
def k2d(s, k):
	mapping = "0123456789ABCDEF"
	result = 0
	for i in range(len(s)): 
		result += mapping.index(s[i]) * k**(len(s)-i-1)
	return result 

def d2k(d, k): 
	mapping = "0123456789ABCDEF"
	result = ""
	while d != 0:
		digit = mapping[d%k]
		d //= k
		result = digit + result 
	return result 

''' ------------- Worksheet 8 -------------- '''
#sort algorithm 
#bubble sort 
def bubbleSort(L): 
	for i in range(len(L)-1): 
		swap = False
		for j in range(len(l)-1-i): 
			if L[j] > L[j+1]:
				L[j], L[j+1] = L[j+1], L[j]
				swap = True
		if swap = False: 
			break 
	return L

#insertion sort 
def insertion sort(L): 
	for i in range(len(L)): 
		for j in range(i, 0, -1): 
			if L[j] < L[j-1]: 
				L[j], L[j-1] = L[j-1], L[j]
	return L 

#quicksort 
def quickSort(L): 
	if len(L) <= 1: 
		return L
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
		self.next = None
		self.prev = None 

#singly linked list(SLLL)
class SLLL(): 
	def __init__(self):
		self.first = None 

	def getRoot(self): 
		return self.first

	def setRoot(self, node): 
		self.first = node 

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
				self.first = self.first.next
				return True  
			else: 
				previous = self.first
				while previous.next != None and previous.next.data != data: 
					previous = previous.next 
				if previous.next == None: 
					return False
				else: 
					previous.next = previous.next.next
					return True


#doubly linked list(DLLL)
class DLLL(SLLL): 
	def insertFront(self, data): 
		newNode = Node(data)
		self.first.prev = newNode
		newNode.next = self.first
		self.first = newNode

	def insertBack(self, data): 
		newNode = Node(data)
		current = self.first
		while current.next != None: 
			current = current.next
		current.next = newNode
		newNode.prev = current

	def delete(self, data): 
		if self.first == None: 
			return False
		else: 
			if self.first.data == data: 
				self.first.next.prev = None  
				self.first = self.first.next 
				return True
			else: 
				current = self.first
				while current != None and current.data != data: 
					current = current.next
				if current == None: 
					return False
				else: 
					current.prev.next = current.next
					if current.next != None: 
						current.next.prev = current.prev
					return True 


#doubly linked circular list(DLCLL)
class DLCLL(DLLL): 
	def setRoot(self, node): 
		self.first = node
		node.prev = node
		node.next = node

	def insertFront(self, data): 
		newNode = Node(data)
		newNode.prev = self.first.prev
		newNode.next = self.first 
		self.first.prev = newNode
		self.first = newNode

	def insertBack(self, data): 
		newNode = Node(data)
		current = self.first
		newNode.next = self.first
		newNode.prev = self.first.prev
		self.first.prev.next = newNode
		self.first.prev = newNode

	def delete(self, data): 
		if self.first == None: 
			return False
		else: 
			current = self.first
			while current.next != self.first and current.data != data: 
				current = current.next
			if current.data == data: 
				current.prev.next = current.next
				current.next.prev = current.prev
				return True 


''' ------------- Worksheet 10 -------------- '''
#stack and queue 
#stack
class stack(): 
	def __init__(self, size): 
		self.top = -1 
		self.size = size 
		self.array = [None for i in range(size)]

	def isFull(self): 
		return self.top == self.size -1 

	def isEmpty(self): 
		return self.top == -1 

	def push(self, data): 
		if self.isFull():
			return False
		else: 
			self.array[self.top] = data
			self.top += 1
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
		self.head = -1
		self.tail = 0
		self.size = size 
		self.array = [None for i in range(size)]

	def isFull(self):
		return self.head == self.tail 

	def isEmpty(self): 
		return self.head == -1

	def enqueue(self, data): 
		if self.isFull(): 
			return False
		else: 
			self.array[self.tail] = data 
			self.tail = (self.tail+1)%self.size 
			return True 

	def dequeue(self): 
		if self.isEmpty():
			return False
		else: 
			toDequeue = self.array[self.head]
			self.head = (self.head+1)%self.size 
			if self.head == self.tail: 
				self.head, self.tail = -1, 0
			return toDequeue

	def peek(self): 
		return self.array[self.head] 


''' ------------- Worksheet 11 -------------- '''
#binary search tree 
class Node_bst(): 
	def __init__(self, data): 
		self.data = data
		self.left = None 
		self.right = None 

class BST(): 
	def __init__(self):
		self.root = None 

	def insert(self, data):
		if self.root == None: 
			self.root = Node_bst(data) 
		else: 
			insertRec(data, self.root)
			#insertItr(data)

	def insertRec(self, data, current): 
		if current == None: 
			current = Node_bst(data)
		elif current.data < data: 
			insertRec(data, current.right)
		else: 
			insertRec(data, current.left) 

	def insertItr(self, data): 
		current = self.root 
		while True: 
			if current == None: 
				current = Node_bst(data)
				break 
			elif current.data < data: 
				current = current.right 
			else: 
				current = current.left 

	def exist(self, data): 
		if self.root == None: 
			return False 
		else: 
			current = self.root
			while current != None and current.data != data: 
				if current.data > data: 
					current = current.left 
				else: 
					current = current.right 
			if current == None: 
				return False 
			else: 
				return True 

	def inOrder(self): 
		if self.root == None: 
			print("BST Empty")
		else: 
			self.inOrderRec(self.root)

	def inOrderRec(self, current): 
		if current != None: 
			inOrderRec(current.left)
			print(current)
			inOrderRec(current.right)

	def preOrder(self): 
		if self.root == None: 
			print("BST Empty")
		else: 
			self.preOrderRec(self.root) 

	def preOrderRec(self, current): 
		if current != None: 
			print(current) 
			preOrderRec(current.left) 
			preOrderRec(current.right) 

	def postOrder(self): 
		if self.root == None: 
			print("BST Empty")
		else: 
			self.postOrderRec(self.root) 

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
		return hash(data) % self.size 

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
			while self.array[target] != None: 
				target = (target+1)%self.size 
			self.array[target] = data 

	def exists(self, data): 
		if self.isEmpty(): 
			return False 
		else: 
			target = self.hash(data) 
			end = target 
			while self.array[target] != data: 
				target = (target+1)%self.size 
				if target == end: 
					return False 
			return True 

	def delete(self, data): 
		if self.isEmpty(): 
			return False
		else: 
			target = self.hash(data) 
			end = target 
			while self.array[targe] != data: 
				target = (target+1)%self.size 
				if target == end: 
					return False 
			self.array[target] = None 
			return True 

#separate lining using DLLL 
class HashTable2(HashTable): 
	def __init__(self, size): 
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


