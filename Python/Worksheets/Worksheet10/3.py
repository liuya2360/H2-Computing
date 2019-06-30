def queue(): 
	def __init__(self, size): 
		self.head = -1 
		self.tail = 0
		self.size = size
		self.array = [None for i in range(size)]

	def isEmpty(self): 
		return self.head < 0

	def isFull(self): 
		return self.head == self.tail 

	def enqueue(self, data): 
		if self.isFull():
			return False 
		else: 
			self.array[self.tail] = data
			self.tail = (self.tail+1)%self.size
			if self.head == -1:
				self.head = 0 
			return True 

	def dequeue(self): 
		if self.isEmpty(): 
			return False
		else: 
			toDequeue = self.array[self.head] 
			self.head = (self.head+1)%self.size 
			if self.head == self.tail: 
				self.head = -1 
				self.tail = 0
			return toDequeue

	def peek(self): 
		return self.array[self.head]