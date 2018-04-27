#Euler 3
def largestprime(var):
    maxprime = 1
    num = var
    j = 2
    while j < int(var**.5):
        if num%j == 0:
            num = num/j     #Taking advantage of prime factorization prop.
            maxprime = j
            j = 1
            if num == 1:
                break
        j = j + 1

    print("The largest prime factor of",var,"is:",maxprime)
    return(maxprime)

largestprime(13195)
largestprime(600851475143)
