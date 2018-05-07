''' Euler 56 '''

def digitsum(num):
    ans = 0
    for i in str(num):
        ans += int(i)
    return ans

answer = 1
for i in range(1,100):
    for j in range(1,100):
        bignum = i**j
        bigsum = digitsum(bignum)
        if bigsum > answer:
            answer = bigsum

print(answer)
