
'''Euler 21'''
def amicable(N):

    def divisors(num):
        divs = []
        for i in range(1,num):
            if num%i==0:
                divs.append(i)
        return sum(divs)

    cumsum = 0

    for i in range(1,N):
        a = divisors(i)
        b = divisors(a)
        if a != b and i == b:
            cumsum += a

    print(cumsum)

amicable(10000)
