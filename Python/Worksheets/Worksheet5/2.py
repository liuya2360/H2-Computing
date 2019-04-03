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