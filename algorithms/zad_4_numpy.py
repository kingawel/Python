import numpy as np

r1 = 4 #use 128x128 instead of 4x4, 
c1 = 4
r2 = 4
c2 = 4
m1 = np.random.random((r1,c1))
m2 = np.random.random((r2,c2))
print("Macierz 1:\n{}".format(m1))
print("Macierz 2:\n{}".format(m2)) 
print("Suma:\n{}".format(m1+m2)) 

