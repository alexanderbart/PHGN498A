''' Euler 44 '''
import math

pentagols = []

def is_pent(x):
    ans = (math.sqrt(int(24*x)+1)+1)/6
    remain = ans%1
    if remain == 0:
        #print(x)
        return True
    else:
        return False

condition = 1
numj = 0
while condition:
    numj += 1
    #print(numj)
    pentj = numj*(3*numj-1)/2
    for numk in range(1,numj):
        pentk = numk*(3*numk-1)/2
        if is_pent(pentj-pentk) and is_pent(pentj+pentk):
            print('D =',pentj-pentk)
            condition = 0
