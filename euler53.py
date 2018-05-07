''' Euler 53 '''
import math
answer = 0

def combinatoric(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

for i in range(1,101):
    for j in range(1,i+1):
        if combinatoric(i,j) > 10**6:
            answer += 1

print(answer)
