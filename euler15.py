''' Euler 15 '''

import numpy as np
import time

'''
I found this one tricky. First I use bits for down and right, so 0 corresponds
to down and 1 to right (doesn't matter what you consider to be assigned to what)
Therefore every combination of moves is described by a bit sequence. Moves that
will get you to the bottom right have equal amounts of downs and rights
aka 0s and 1s. So if the sum of bits equals half the number of moves, that's a
path.

This was too slow, but is included at the bottom.
I did some research and found a better method which is
dynamic.
Credit: Jason Hill, "Jason's Code Blog"
'''

gridl = 20
grid = np.zeros((gridl+1,gridl+1)) # Need a data point for number of paths to
                                   # each point

for i in range(gridl+1): #One path to top and left edge points
    grid[i][0] = 1
    grid[0][i] = 1

#print(grid)

'''
Number of paths to each point is the number of paths to the upper point plus
number of paths to the leftward point.
'''

for i in range(1,gridl+1):
    for j in range(1,gridl+1):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

print(grid[-1][-1])


###############################################################################
#
# gridl = 11
# pathl = 2*gridl
#
# strings = []
# for i in range(2**pathl):
#     strings.append('')
#
# '''
# Building all possible paths with appropriate number of moves
# (not necessarily going along grid)
# '''
# t1 = time.time()
#
# ndx = 2**pathl
# step = 0
# cyc = 1
# while ndx != 1:
#     ndx = int(ndx/2)
#
#     for j in range(0,step+1):
#         for i in range(0,ndx):
#             strings[i+2*ndx*(j)] += '0'
#
#         for i in range(0,ndx):
#             strings[i+ndx+2*ndx*(j)] += '1'
#
#         #print(ndx,j,strings)
#     step = 2**cyc - 1
#     cyc += 1
#
# t2 = time.time()
#
# print(t2-t1,len(strings))
#
# print('poop')
# '''
# Finding paths with equal downs and rights...
# Save a little time knowing each path can have opposite moves and end up in
# corner.
# '''
# paths = 0
# for i in strings[:int(len(strings)/2)]:
#     numsum = 0
#     for j in range(pathl):
#         numsum += int(i[j])
#     #print(numsum)
#     if numsum == gridl:
#         paths += 1
# paths *= 2
#
# t3 = time.time()
#
# print('Total paths are',paths)
# print(t3-t2)
#
#
# ''''''





###############################################################################
