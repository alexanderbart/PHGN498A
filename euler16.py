'''Euler 16'''
def power_digit_sum(var):
    digitsum = 0
    for i in str(var):
        digitsum += float(i)
    print("The sum of the digits is {}".format(digitsum))

power_digit_sum(2**1000)
