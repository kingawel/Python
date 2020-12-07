import matplotlib.pyplot as plt
from multiprocessing.pool import Pool
from random import randint 
import math 

def Calculation(number):
    #some random calculation
    r_num = randint(1,30000)
    for i in range(300):
        num = math.sqrt(r_num)
        num *= (i%number+0.245/r_num)
        num /=10
    return num
    

if __name__ == "__main__":
    p = Pool(processes=4)
    tab = [12, 65, 8, 5, 20]
    calc = p.map(Calculation, tab)
    print('Calculations: \n {0}'.format(calc))
    p.close()
    p.join()
    plt.hist(calc, bins=16)
    plt.show()

