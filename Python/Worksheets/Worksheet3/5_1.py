class wordFreq():
	def __init__(self):
		sekf,freqs = {}

	def addWord(self, word):
		if word in self.freqs.keys():
			self.freqs[word] += 1
		else: 
			self.freqs[word] = 1

		def displayFreqs(self):
			for key in self.freqs.keys():
				print("{0:<20}{1:<10}".format(key,str[self.freqs[key]]))