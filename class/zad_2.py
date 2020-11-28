class Complex(object):
    def __init__(self, re, im=0.0):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re,self.im - other.im)

    def __mul__(self, other):
        return Complex(self.re*other.re - self.im*other.im, self.im*other.re + self.re*other.im)

    def __div__(self, other):
        r = float(other.re**2 + other.im**2)
        return Complex((self.re*other.re+self.im*other.im)/r, (self.im*other.re-self.re*other.im)/r)

    def __str__(self):
        return '%g + %gj' % (self.re, self.im)

    def __repr__(self):
        return 'Complex' + str(self)


x = Complex(2,-3)
y = Complex(4,7)    
u = x * y
print u        