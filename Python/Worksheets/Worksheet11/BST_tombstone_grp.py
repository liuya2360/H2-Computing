class Node(): 
	def __init__(self, data): 
		self.data = data
		self.left = None 
		self.right = None 
		self.tombstone = False 

	def __str__(self): 
		return "{0:<10}{1:<10}{2:<10}".format(str(self.left),str(self.data)+"(T)" if self.tombstone else "", str(self.right))

class BST():
	def __init__(self): 
		self.root = None 

	def print(self): 
		if not self.root: 
			print("Empty")
		else: 
			stack = [self.root]
			while len(stack) > 0:
				current = stack.pop()
				print(current)
				if current.left: 
					stack.append(current.left)
				if current.right: 
					stack.append(current.right)

	def insert(self, data): 
		if not self.root: 
			self.root = Node(data) 
		else: 
			current = self.root
			while True: 
				if current.tombstone and\
				(self.maxInSubTree(current.left) == None or self.maxInSubTree(current.left) < data) and \
				(self.minInSubTree(current.right) == None or self.minInSubTree(current.right) >= data): 
					current.data = data
					current.tombstone = False
					break
				elif data < current.data: 
					if not current.left: 
						current.left = Node(data)
						break
					else: 
						current = current.left
				else: 
					if not current.right: 
						current.right = Node(data)
						break 
					else: 
						current = current.right 

	def findTarget(self, data): 
		if not self.root: 
			return None
		else: 
			current = self.root
			while True: 
				if data == current.data and not current.tombstone: 
					#current.tombstone = True #this line shouldn't be here
					return current 
				elif data < current.data: 
					if not current.left:
						return None
					else:  
						current = current.left
				else: 
					if not current.right: 
						return None 
					else: 
						current = current.right 

	def exists(self, data): 
		return self.findTarget(data) != None

	def delete(self, data): 
		target = self.findTarget(data)
		if target: 
			target.tombstone = True
			return True
		return False 

	def minInSubTree(self, node): 
		if not node: 
			return None
		else: 
			res = node.data 
			leftMin = self.minInSubTree(node.left)
			rightMin = self.minInSubTree(node.right)
			if leftMin: #remove not
				res = min(res, leftMin)
			if rightMin: #remove not
				res = min(res, rightMin)
			return res

	def maxInSubTree(self, node): 
		if not node: 
			return None
		else: 
			res = node.data
			leftMax = self.maxInSubTree(node.left)
			rightMax = self.maxInSubTree(node.right)
			if leftMax: #remove not
				res = max(res, leftMax)
			if rightMax: #remove not
				res = msx(res, rightMax)
			return res

tree = BST()
l = [50, 25, 75, 0, 35, 65, 100]
for i in range(len(l)): 
	tree.insert(l[i])
tree.print()
tree.delete(25)
tree.insert(20)
tree.print()