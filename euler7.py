import numpy as np
import time as t

#Euler 7
def tenthousandthprime(var,n):
    print("This will take about 30 seconds, please be patient.")
    #n = 1.8*(10**7)     #This number gives over 1M primes from trial and error.
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
    print("The 10,001st prime number is",primes[10000])
    #print("The {} prime number is {}".format(var,primes[var-1]))
tenthousandthprime(10,int(10**5.1))
