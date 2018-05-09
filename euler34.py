''' Euler 34 '''

'''
This is a pretty straightforward problem. I didn't know how long to check for
these numbers, and an upper bound is pretty important.  I did some research and
got the upper bound from
https://www.mathblog.dk/project-euler-34-factorial-digits/
'''
def factorial(x):
    ans = 1
    if x == 0:
        return 1
    if x == 1:
        return 1
    else:
        for i in range(1,x+1):
            ans *= i
        return ans

answer = 0

number = 10
while number < 2540160:
    number = str(number)
    factsum = 0
    for i in number:
        factsum += factorial(int(i))
    number = int(number)
    if factsum == number:
        answer += number

    number += 1

print('Sum of factorial digit sums is',answer)
