class Trapezium():
	def __init__(self, top, bottom, side1, side2 ,height):
		self.top = top
		self.bottom = bottom
		self.height = height
		self.side1 = side1
		self.side2 = side2

	def area(self):
		return 0.5*(self.top+self.bottom)*height

	def perimeter(self):
		return self.top+self.bottom+self.side1+self.side2

class Parallelgram():
	def __init__(self, side1, side2, height):
		self.side1 = side1
		self.side2 = side2
		self.height = height

	def area(self):
		return self.side1*self.height

	def perimeter(self):
		return 2*(self.side1+self.side2)

class Kite():
	def __init__(self, diagonal1, diagonal2):
		self.diagonal1 = diagonal1
		self.diagonal2 = diagonal2

	def area(self):
		return 0.5*(self.diagonal1*self.diagonal2)

	def perimeter(self):
		return 2*(self.diagonal1**2+self.diagonal2**2)**0.5

class Rhombus(Kite):
	def __init__(self, diagonal1, diagonal2):
		super().__init__(diagonal1,diagonal2)

class Rectangle(Parallelgram):
	def __init__(self, length, breadth):
		super().__init__(length, length, breadth)

class Square(Rectangle):
	def __init__(self, length):
		super().__init__(length, length)

x = Rectangle(1,1)
print(x.area())
