class Node(): 
	def __init__(self, data): 
		self.data = data
		self.left = None
		self.right = None 

	def __str__(self): 
		#print(str(self.data)+str(self.left)+str(self.right))
		return "{0:<10}{1:<10}{2:<10}".format(self.data, self.left, self.right)

class BST(): 
	def __init__(self): 
		self.root = None 

	def insert(self, data): 
		newNode = Node(data)
		if self.root == None: 
			self.root = newNode
		else: 
			current = self.root 
			while True: 
				if current.data > data: 
					if current.left != None: 
						current = current.left
					else: 
						current.left = newNode
						break
				else: 
					if current.right != None: 
						current = current.right
					else: 
						current.right = newNode
						break

	def exists(self, data):
		if self.root == None: 
			return False 
		else: 
			current = self.root
			while current != None: 
				if current.data == data: 
					return True
				elif current.data > data: 
					current = current.left
				elif current.data < data: 
					current = current.right 
			return False


	def print(self): 
		if self.root ==None: 
			print("Empty")
		else: 
			stack = [self.root]
			print("{0:<10}{1:<10}{2:<10}".format("Node.data", "Node.left", "Node.right")) 
			while len(stack) > 0: 
				current = stack.pop()
				print(current)
				if current.left != None: 
					stack.append(current.left)
				if current.right != None: 
					stack.append(current.right)

	def _traversal(self, node, mode): 
		if node != None: 
			print(node.data) if mode == "pr" else print("", end="")
			self._traversal(node.left, mode)
			print(node.data) if mode == "in" else print("", end="")
			self._traversal(node.right, mode) 
			print(node.data) if mode == "po" else print("", end="")

	def preOrderPrint(self): 
		if self.root == None: 
			print("BST Empty")
		else: 
			self._traversal(self.root, "pr")

	def inOrderPrint(self): 
		if self.root == None: 
			print("BST Empty")
		else: 
			self._traversal(self.root, "in")

	def postOrderPrint(self):
		if self.root == None: 
			print("BST Empty") 
		else: 
			self._traversal(self.root, "po")