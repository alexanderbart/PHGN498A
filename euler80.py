''' Euler 80 '''
import math
from decimal import *

def digitsum(num):
    num = str(num)
    ans = 0
    for i in num:
        ans += int(i)
    return ans

answer = 0
for i in range(1,101):

    getcontext().prec = 103
    number = Decimal(i)**Decimal(0.5)
    decimal = str(number)[2:101]+str(number)[0]

    if decimal[2:6] != '0000':
        answer += digitsum(decimal)
print('sum is',answer)
