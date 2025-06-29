class operands:
	def __init__(self, var1, var2):
		self.x = var1
		self.y = var2
	def print_val(self):
		return self.x, self.y
	def div(self):
		if not self.y:
			return "Zero Division Error"
		return self.x/self.y
	def mul(self):
		return self.x*self.y
	def add(self):
		return self.x+self.y
	def sub(self):
		return self.x-self.y

i,j = [int(i) for i in input("Enyter numbers: ").split(sep=',')]
x = operands(i,j)
print("\nValues:", x.print_val())
print("addition:", x.add())
print("substarct:",x.sub())
print("multiply:", x.mul())
print("div:", x.div())
