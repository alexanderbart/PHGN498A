''' Euler 97 '''

'''
The exponent is huge, so I did research and was led to
https://en.wikipedia.org/wiki/Exponentiation_by_squaring
Still takes a while, but it works!
'''
def exp_by_sqr(x,n):
    if n == 1:
        return x
    elif n%2 == 0:
        return exp_by_sqr(x*x,int(n/2))
    else:
        return x*exp_by_sqr(x*x,int((n-1)/2))

exponent = exp_by_sqr(2,7830457)
answer = 28433*exponent+1
print(str(answer)[-10:])
