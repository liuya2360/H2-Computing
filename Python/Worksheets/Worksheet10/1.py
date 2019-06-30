def stack(): 
	def __init__(self, size): 
		self.top = -1 
		self.size = size
		self.array = [None for i in range(size)]

	def isFull(self): 
		return self.size -1 == self.top 

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