''' Euler 37 '''
import numpy as np
import time as t

'''
Takes a looooong time, but it gets there eventually. I used my old sieve
algorithm to generate a lot of primes, and brute forced it out.
'''

#From Euler 7
def get_primes(var,n):
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
    return primes

primes = get_primes(10,int(10**6))

trunc_primes = 0
trunc_sum = 0
i = 4
while trunc_primes != 11:
    prime = str(primes[i])
    check = 1
    if prime[0] == '9' and prime[-1] == '9': #Shave some time, 9 not prime
        check = 0

    if check:
        for j in range(1,len(prime)):
            if not int(prime[j:]) in primes or not int(prime[:j]) in primes:
                check = 0
                break

    if check:
        print(prime)
        trunc_primes += 1
        trunc_sum += int(prime)

    i += 1

print('Sum is',trunc_sum)
