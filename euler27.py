import numpy as np
import time as t

'''Euler 27 (takes about 10 seconds...)'''
# From HW 2
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

# This takes about 10 secs
def quad_primes():
    primes = prime_list(10**5) # Using old prime list code!
    mostprimes = 0

    timei = t.time()
    for aa in range(-100,0):
        if np.abs(aa) in primes: # coefficients must be prime to produce primes
            for bb in range(1000):
                if np.abs(bb) in primes:
                    count = 0
                    condition = 0
                    i = 0
                    # I iterate through different "n"s with the a and b set
                    # and count up how many primes in a row it produces
                    while condition == 0:
                        yy = i**2 + aa*i + bb
                        if yy in primes:
                            count += 1
                            i += 1
                        else:
                            condition = 1
                    if count > mostprimes:
                        mostprimes = count
                        a = aa
                        b = bb
    timef = t.time()

    print("Answer is:",a*b)
    print("Time taken:",timef-timei)

quad_primes()
