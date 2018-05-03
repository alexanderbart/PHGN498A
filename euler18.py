''' Euler 18 '''
import numpy as np


triangle = \
'75\
95 64\
17 47 82\
18 35 87 10\
20 04 82 47 65\
19 01 23 75 03 34\
88 02 77 73 07 63 67\
99 65 04 28 06 16 70 92\
41 41 26 56 83 40 80 70 33\
41 48 72 33 47 32 37 16 94 29\
53 71 44 65 25 43 91 52 97 51 14\
70 11 33 28 77 73 17 78 39 68 17 57\
91 71 52 38 17 14 91 43 58 50 27 29 48\
63 66 04 68 89 53 67 30 73 16 69 87 40 31\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

'''
Remove spaces so python can seperate all the numbers
'''
while ' ' in triangle:
    triangle = triangle.replace(' ','')
#print(triangle)


rows = 15
thisrow = 1
index = 0
nums = []
while thisrow <= rows:
    for i in range(thisrow):
        nums.append(triangle[index:index+2])
        index += 2

    thisrow += 1

thisrow = 1
numindex = 1
trinum = []
while thisrow <= rows:
    rowarr = np.zeros(thisrow)
    for i in range(thisrow):
        rowarr[i] = int(nums[i+numindex-1])
    trinum.append(rowarr)
    thisrow += 1
    numindex += thisrow-1

'''
Now all the rows have their own array.

David Wolfe helped me understand how to work from the bottom up!
Starting at the bottom, you replace each number in the row above with the
highest possible sum from the two numbers below it, and keep going up!
'''
thisrow = 15
while thisrow > 1:
    lowrow = trinum[thisrow-1]
    abvrow = trinum[thisrow-2]

    for i in range(len(abvrow)):
        if lowrow[i] > lowrow[i+1]:
            abvrow[i] += lowrow[i]
        else:
            abvrow[i] += lowrow[i+1]
    #print(abvrow)

    trinum[thisrow-2] = abvrow

    thisrow -= 1

print('The max sum is',trinum[0][0])




















##############################################################################
