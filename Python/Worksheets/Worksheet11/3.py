class Node(): 
	def __init__(self, data):
		self.data = data
		self.LeftP = None 
		self.RightP = None 

class BST():
	def __init__(self): 
		self.thisTree = [Node(None) for i in range(21)] #based on the description, it is 1 index 
		self.root = None
		self.nextFreePosition = 0
		for i in range(20): 
			thisTree[i].LeftP = i+1 

	def addItemToBinaryTree(self, data): 
		if self.root == None: 
			self.root = nextFreePosition
			self.thisTree[self.root] = Node(data)
			self.nextFreePosition = self.thisTree[self.root].LeftP
			self.thisTree[self.root].LeftP = None
		else: 
			#traverse the tree to find the position of the new value 
			currentPosition = self.root
			lastMove = 'X' 
			while currentPosition != 0: 
				