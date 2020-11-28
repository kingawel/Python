import math 

class Complex:
	def __init__(self, re, im):
		self.re = re
		self.im = im

	def write(self):
		if self.im < 0:
			print("{} {}i".format(self.re,self.im))
		else:
			print("{} + {}i".format(self.re,self.im))
			
	def sum(c1,c2):
		return Complex(c1.re + c2.re, c1.im + c2.im)

	def substract(c1,c2):
		return Complex(c1.re - c2.re, c1.im - c2.im)

	def abs(self):
		return math.sqrt(self.re**2 + self.im**2)


c1 = Complex(3,4)
c2 = Complex(3,-5)
c1.write()
Complex.sum(c1,c2).write()
Complex.substract(c1,c2).write()
print(c1.abs())