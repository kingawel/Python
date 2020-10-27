import math
try:
        a = float(input("Set a "))
        b = float(input("Set b "))
        c = float(input("Set c "))
except IOError:
        print("Set only numbers!") #you can only put numbers
delta = b * b - 4 * a * c
if delta < 0:
	print("There is no solution")
elif delta == 0:
	x1 = (-b) / (2 * a)
	print ("There is one solution x = {}".format(x1))
else:
	s_delta = math.sqrt(delta)
	x1 = (-b + s_delta) / (2 * a)
	x2 = (-b - s_delta) / (2 * a)
	print ("There are two solutions: x1 = {} and x2 = {}".format(x1,x2))