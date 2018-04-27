import time as t
import numpy as np

'''
Problem 2: Euler 39
'''
def int_right_triangles(perimeter):
    print('This takes aboot 11 seconds')
    max_sols = 0
    p = perimeter
    t1 = t.time()
    while p != 11:
        if p%2 == 0: #Perimeter must be even
            num_sols = 0
            for i in range(1,int(p/3)):
                a = i
                if a%2 == 1: #a and b can't both be odd.
                    for j in range(i,int(p/2)):
                        if j%2 == 0:
                            b = j
                            if p - (a+b) > b:
                                if p - (a+b) == (a**2 + b**2)**0.5:
                                    num_sols += 1
                if a%2 == 0:
                    for j in range(i,int(p/2)):
                        b = j
                        if p - (a+b) > b:
                            if p - (a+b) == (a**2 + b**2)**0.5:
                                num_sols += 1

            if num_sols > max_sols:
                max_sols = num_sols
                answer = p
        p -= 1
        t2 = t.time()
    print("A perimeter of {} has {} solutions. This took {} secs."\
    .format(answer,max_sols,t2-t1))
int_right_triangles(1000)
