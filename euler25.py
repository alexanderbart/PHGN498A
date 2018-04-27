import time as t

'''Euler 25'''
def fib_list(power):
    fibs = [1,1]
    condition = 0

    start = t.time()

    while condition == 0:
        fibs.append(fibs[-1]+fibs[-2])
        if fibs[-1] >= (10**(10**power-1)):
            condition = 1
    #print(fibs[-1])
    #print(fibs)
    finish = t.time()
    print("Index {} in the Fib sequence has 10^{} digits."\
    .format(len(fibs),power))
    print("This took {} secs.".format(finish-start))
fib_list(3)
