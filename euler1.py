import numpy as np
import time as t

'''Euler 1'''
def threeandfive(var):
    ans = 0
    for i in range(1,var):
        if i%3==0:
            ans = i + ans
        if i%5==0:
            ans = i + ans
        if i%15==0: #Takes care of cases where i is divisible by three AND five.
            ans = ans - i
    print("\nThe sum of factors of three and five under",var,"is:",ans)
    return(ans)
print(threeandfive(1000))
