import numpy as np

r1 = 4 #use 8x8 instead of 4x4, 
c1 = 4
r2 = 4
c2 = 4
def matrixMultiply(m1,m2):
	if c1 == r2:
		m3 = np.empty((r1,c2))
		for x in range(0,r1):
			for y in range(0,c2):
				m3[x][y] = 0
				for n in range(0,c2):
					m3[x][y] += m1[x][n] * m2[n][y] 	
	else:
		m3 = ("Nie mozna mnozyc macierzy o takich wymiarach")
	return m3

m1 = np.random.random((r1,c1))
m2 = np.random.random((r2,c2))
print("Macierz 1:\n{}".format(m1))
print("Macierz 2:\n{}".format(m2))
print("Iloczyn:\n{}".format(matrixMultiply(m1,m2)))  

print("Iloczyn obliczony z funckji wbudowanej:\n{}".format(m1.dot(m2)))