''' Euler 24 '''
import numpy as np

digit = 2
combos = 2
string = ['01','10']

while digit < 11:

    # string = np.zeros(combos,dtype = str)
    # print(string)

    # for i in range(combos):
    #     for j in range(digit):
    #         string[i] += str(digit)

    digit += 1
    combos *= digit
    print(combos)
