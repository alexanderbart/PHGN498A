''' Euler 24 '''
import numpy as np
import math

index = 999999 #Millionth starting with 0
nums = [0,1,2,3,4,5,6,7,8,9]
digits = 10

answer = ''

while digits != 1:

    #Build a grid with each column having permutations of each possible starting
    #number
    print('\n Grid is {} rows by {} columns'\
    .format(math.factorial(digits-1),digits))

    numrows = math.factorial(digits-1)

    column = int(index/numrows)
    print('column is',column)

    answer += str(nums[column])
    nums.remove(nums[column])
    print(nums)

    index = index%numrows
    digits -= 1

answer += str(nums[0])
print(answer)

















#############################################################################
