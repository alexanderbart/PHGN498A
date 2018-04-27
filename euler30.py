'''Euler 30'''
def digit_powers(dig):

    '''
    TBH I didn't know how far to check numbers, but 10**7 took really long,
    and 10**6 gave me the right answer.
    '''
    print("Euler 30:")
    numbers = []
    goodones = []
    for i in range(2,10**(dig+1)):
        numbers.append(i)
    for j in numbers:
        sumofpower = []
        for i in range(len(str(j))):
            sumofpower.append(int(str(j)[i])**dig)
        if sum(sumofpower) == j:
            goodones.append(j)
            #print(goodones)

    return sum(goodones)

print('The sum of numbers that can be written as the sum of their \
5th power digits is',digit_powers(5))
