from random import randint 
import numpy as np

def matrixDet(mat):
    assert mat.shape[0] == mat.shape[1] #it must be a square matrix
    dim = mat.shape[0]
   
    for x in range(0, dim-1):
       
        for y in range(x+1, dim):
            if mat[y,x] != 0.0:
                temp = mat [y,x]/mat[x,x]
                mat[y,x:dim] = mat[y,x:dim] - temp * mat[x,x:dim]  #the solution is to create 'triangle' from matrix 

    return np.prod(np.diag(mat)) #in this solution determinant is products of diagonal elements


dim = randint(1,8)
m1 = np.random.random((dim,dim))
print("Macierz:\n{}\n".format(m1))
print("Wyznacznik:\n{}".format(matrixDet(m1)))
print ("Wyznacznik - funkcja biblioteczna:\n{}".format(np.linalg.det(m1)))