''' Euler 40 '''

'''
I decided to record the index that corresponded to each number that gets
concecated...
'''

index = 0
number = 0
exponent = 0
decimals = []
while exponent <= 6:
    index += 1

    number += len(str(index))
    #print(number,index)
    if number >= 10**exponent:
        decimals.append([index,number])
        exponent += 1

print(decimals)

'''
Then I use the index and corresponding number to work backwards to the correct
decimal
'''

answer = 1
for i in range(len(decimals)):
    difference = 10**i-decimals[i][1]-1
    answer *= int(str(decimals[i][0])[difference])
print('The answer is',answer)
