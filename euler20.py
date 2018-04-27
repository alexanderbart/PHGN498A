'''Euler 20'''
def fact_digit_sum(var):
    factsum = 0
    fact = 1
    num = var
    #Do the factorial
    while num != 1:
        fact *= num
        num -= 1
    #Do the sum of the digits
    for i in str(fact):
        factsum += float(i)

    print("The sum of the digits of {}! is {}".format(var,factsum))
fact_digit_sum(100)
