from random import randint # or it is possible to use random (0-1.0)

def matrixCreate(r,c):  # r-rows, c-columns
	matrix = [0] * r
	for i in range (0,r):
		matrix[i] = [0] * c
	for x in range(0,r):
		for y in range(0,c):
			matrix[x][y] = (randint(-10,10)) 
	return matrix

def matrixMultiply(matrix1,matrix2,matrix3):
	print("Macierz 1: {}".format(matrix1))
	print("Macierz 2: {}".format(matrix2))
	for x in range(0,r):
		for y in range(0,c):
			matrix3[x][y] = 0
			for n in range(0,c):
				matrix3[x][y] += matrix1[x][n] * matrix2[n][y] 	
	return matrix3
r = 3 #in this program both matrixes have the same number of rows and columns
c = 3 #instead of 3x3 use 8x8
m1 = matrixCreate(r,c)
m2 = matrixCreate(r,c)
m3 = matrixCreate(r,c) 
print("Iloczyn:      {}".format(matrixMultiply(m1,m2,m3))) 

