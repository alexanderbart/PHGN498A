''' Euler 57 '''

'''
Looking at the pattern, at can be seen that the new numerator is the
old numerator times 2 plus the next older numerator.
Same for denominator.  That makes this problem pretty easy.
'''

answer = 0

oldn = 1
oldd = 1

numer = 3
denom = 2
for i in range(10**3):
    if len(str(numer)) > len(str(denom)):
        answer += 1

    numer , oldn = numer*2 + oldn , numer
    denom , oldd = denom*2 + oldd , denom

print(answer)
