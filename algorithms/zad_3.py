def scalarProduct(a,b):
	result = 0
	wectorLen = len(a) # = len(b)
	for i in range(0, wectorLen):
		result += a[i] * b[i]
	return result
a = [1, 2, 12, 4]
b = [2, 4, 8, 2]
print(scalarProduct(a,b))
