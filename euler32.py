import time as t
import numpy as np

'''Euler 32'''
def pandigital():
    '''
    Got help from Julie Bosley on this one.
    We just need to check values of a number between 1 and 98 for the smaller
    digit mulitpliers, and 123 to 9876 for the larger "multiplicands."
    This takes care of some of our double counted products too.
    '''
    print('\nEuler 32:')
    target = sorted('123456789')

    prods = []
    multipliers = np.linspace(1,98,98,dtype = int)

    multiplands = np.linspace(123,9876,(9876-123)+1,dtype = int)

    timei = t.time()

    for i in multipliers:
        for j in multiplands:
            if not '0' in (str(i) or str(j)):
                prod = i * j
                n1 = str(i)
                n2 = str(j)
                n3 = str(prod)
                strtest = n1+n2+n3
                #print(strtest,sorted(strtest))
                if sorted(strtest) == target and (int(n3) not in prods):
                    prods.append(int(n3))
                    print('One pandigital combo is {} times {} equals {}'\
                    .format(n1,n2,n3))

    #print(prods)
    timef = t.time()
    #print(timef - timei)
    return sum(prods)

print('The sum of products of pandigital combos is',pandigital())
