''' Euler 92 '''

'''
Quite slow, but works
'''

def digitsqr(num):
    num = str(num)
    ans = 0
    for i in num:
        ans += int(i)**2
    return ans

count = 0
for i in range(1,10**7):
    condition = 1
    num = i
    while condition:

        if num == 1:
            print(1,i)
            condition = 0
        if num == 89:
            print(89,i)
            count += 1
            condition = 0
        num = digitsqr(num)
print(count)
