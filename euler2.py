import numpy as np
import time as t

#Euler 2
def fibbmax():
    var1 = 1
    var2 = 2
    var3 = 0
    sumVar = 2
    while var3 <= 4000000:
        var3 = var2 + var1
        var1 = var2
        var2 = var3
        if var3 % 2 == 0:
            sumVar = sumVar + var3
    print(sumVar)
fibbmax()
