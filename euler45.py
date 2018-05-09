''' Euler 45 '''
import math

'''
Thankfully, all hexagonal numbers are triangular numbers,
making this quite easy.
'''

def is_pent(x):
    ans = (math.sqrt(int(24*x)+1)+1)/6
    remain = ans%1
    if remain == 0:
        return True
    else:
        return False


condition = 1
hexn = 143
while condition:
    hexn += 1
    print(hexn)
    num = hexn*(2*hexn-1)

    if is_pent(num):
        print('Answer is',num)
        condition = 0
