''' Euler 48 '''
'''
Super straightforward...
'''

answer = 0
for i in range(1,10**3+1):
    answer += i**i

print(int(str(answer)[-10:]))
