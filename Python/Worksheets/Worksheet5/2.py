class LongInt():
	def __init__(self, l):
		if l[0] == "-":
			self.sign = -1
			self.value = l[1:]
		else:
			self.sign = 1
			self.value = l

	def getValue(self):
		out = ""
		if self.sign == -1:
			out += "-"
		out += self.value 

	def setValue(self, l):
		if l[0] == "-":
			self.sign = -1
			self.value = l[1:]
		else:
			self.sign = 1
			self.value = l

	def add(self, b): 
		if len(self.value) >= len(b.value):
			max_num = self
			min_num = b
		else:
			max_num = b
			min_num = self
		for i in range(len(min_num.value)):
			j = i
			while True:
				j -= 1
				if int(max_num.value[j]) + int(min_num.value[j]) > 10:
					max_num.value[]
				else:
					max_num.value = max_num.value[:j] + str(int(max_num.value[j+1]) + int(min_num.value[j+1])) = max_num.value[j+2:]
					break
		for i in range(len(max_num.value), -1, -1):
			if int(max_num.value[i] > 9):
				if i != 0:
					max_num.value = max_num.value[:i-2] + str(int(max_num.value[i-1]) + 1) + max_num.value[i:]
				else:
					max_num.value = "1" + max_num.value
		if max_num.value[0] == 

	def subtract(self, b):

