''' Euler 41 '''

import numpy as np

def prime_list(n):
    arr = np.arange(0,n)
    arr[1]=0

    for i in range(2,int(n**0.5)):
        if arr[i] > 1:
            for j in range(0,(int(n/i))-i):
                arr[(i**2)+(j*i)] = 0   #Erases multiples of the prime

    primes = []
    for i in range(0,len(arr)):
        if not arr[i] == 0:
            primes.append(arr[i])
            #Makes an array of what's left of the old list (primes).
    return primes

primes = prime_list(10**7)
answer = 0
for i in primes:
    count = 0

    #print(len(str(i)))
    for j in range(1,len(str(i))+1):
        if str(j) in str(i):
            count += 1
        if count == len(str(i)) and i > answer:
            answer = i

print(answer)
