import numpy as np
import time as t

#Takes about a minute
def euler10(num):
    n = 3.5*(10**7)
    arr = np.arange(0,n)
    arr[1]=0
    tick = t.time()
    for i in range(2,int(n**0.5)):
        if arr[i] > 1:
            for j in range(0,(int(n/i))-i):
                arr[(i**2)+(j*i)] = 0   #Erases multiples of the prime

    primes = []
    for i in range(0,len(arr)):
        if not arr[i] == 0:
            primes.append(arr[i])
            #Makes an array of what's left of the old list (primes).
    tock = t.time()
    print("This took {} seconds to find {} primes."\
        .format(tock-tick,len(primes)))

    prsum = 0
    for i in primes:
        if i < num:
            prsum += i

    return prsum
print(euler10(2000000))
