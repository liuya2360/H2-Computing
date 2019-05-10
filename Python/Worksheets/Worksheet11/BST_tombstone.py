class Node(): 
	def __init__(self, data): 
		self.data = data
		self.left = None 
		self.right = None 
		self.tombstone = False

	def __str__(self): 
		return "{0:<10}{1:<10}{2:<10}".format(self.data, self.left, self.right)

class BST(): 
	def __init__(self):
		self.root = None

	'''
	def insert(self, data): 
		if self.root == None: 
			self.root = Node(data) 
		else: 
			self.insertRecursive(data, self.root)
			#self.insertIterative(data)

	def insertRecursive(self, data, current): 
		if current == None: 
			current = Node(data)
		elif data < current.data: 
			self.insertRecursive(data, current.left)
		else: 
			self.insertRecursive(data, current.right)

	def insertIterative(self, data): 
		current = self.root #not None
		while True: 
			if data < current.data: 
				if current.left == None: 
					current.left = Node(data)
					break
				else: 
					current = current.left
			else: 
				if current.right == None: 
					current.right = Node(data)
					break
				else: 
					current = current.right
	'''
	def insert(self, data):
		if self.root == None: 
			self.root = Node(data) 
		else: 
			self.insertRecursive(data, self.root)
			#self.insertIterative(data)

	def insertRecursive(self, data, previous):
		if previous.tombstone == False: 
			if previous.next == None: 
				previous.next = Node(data)
			elif data < previous.next.data: 
				self.insertRecursive(data, previous.next.left)
			else: 
				self.insertRecursive(data, previous.next.right)
		else: 
			if previous.next == None: 
				previous.data = data
				previous.tombstone = False
			elif data < previous.next.data: 
				self.insertRecursive(data, previous.next.left)
			else: 
				self.insertRecursive(data, previous.next.right)


	def exists(self, data): 
		if self.root == None: 
			return False 
		else: 
			return self.existsRecursive(data, self.root)
			#return self.existsIterative(data)

	def existsRecursive(self, data, current): 
		if current == data: 
			return True: 
		elif current == None: 
			return False
		elif data < current.data: 
			return self.existsRecursive(data, current.left)
		else: 
			return self.existsRecursive(data, current.right) 

	def existsIterative(self, data): 
		current - self.root 
		while True: 
			if data == current.data: 
				return True
			elif data < current.data: 
				if current.left == None: 
					return False
				else: 
					current = current.left 
			else: 
				if current.right == None: 
					return False
				else: 
					current = current.right 

	def __str__(self): 
		if self.root == None: 
			return "Tree Empty"
		res = ""
		stack = [self.root]
		while len(stack) > 0:
			current = stack.pop()
			res += str(current)+"\n"
			if current.left != None: 
				stack.append(current.left)
			if current.right != None: 
				stack.append(current.right)
		return res 

	def inOrder(self): 
		self.inOrderRec(self.root)

	def inOrderRec(self, current): 
		if current != None: 
			self.inOrder(current.left)
			print(current.data)
			self.inOrder(current.right)

	def preOrder(self): 
		self.preOrderRec(self.root)

	def preOrderRec(self, current): 
		if current != None: 
			print(current.data)
			self.preOrderRec(current.left)
			self.preOrderRec(current.right)

	def postOrder(self): 
		self.postOrderRec(self.root)

	def postOrderRec(self, current): 
		if current !- None: 
			self.postOrderRec(current.left)
			self.postOrderRec(current.right)
			print(current.data)

	def re_print(self, current): 
		if current != None: 
			self.re_print(current.left)
			print(current.data)
			self.re_print(current.right)

	def print(self):
		#print(self)
		self.re_print(self.root)

	def delete(self, data): 
		current = self.root
		while True: 
			if data == current.data: 
				current.tombstone = True
				return True 
			elif data < current.data: 
				if current.left == None: 
					return False
				else: 
					current = current.left 
			else: 
				if current.right == None: 
					return False
				else: 
					current = current.right 