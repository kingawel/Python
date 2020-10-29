from random import randint # or it is possible to use random (0-1.0)

def matrixCreate(n,m):  # n-rows, m-columns
	matrix = [0] * n
	for i in range (0,n):
		matrix[i] = [0] * m
	for x in range(0,n):
		for y in range(0,m):
			matrix[x][y] = (randint(-10,10)) 
	return matrix

def matrixSum(matrix1,matrix2,matrix3):
	print("Macierz 1: {}".format(matrix1))
	print("Macierz 2: {}".format(matrix2))
	for x in range(0,r):
		for y in range(0,c):
			matrix3[x][y] = matrix1[x][y] + matrix2[x][y]
	return matrix3
r = 4 #in this program both matrixes have the same number of rows and columns
c = 4 #nstead of 4x4 use 128x128 
m1 = matrixCreate(r,c)
m2 = matrixCreate(r,c)
m3 = matrixCreate(r,c) 
print("Suma:      {}".format(matrixSum(m1,m2,m3)))  

