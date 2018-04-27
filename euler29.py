'''Euler 29'''
def distinct_powers(n):
    powers = []
    powcnt = 0
    for i in range(2,n+1):
        for j in range(2,n+1):
            if i**j not in powers:
                powers.append(i**j)
                powcnt += 1

    print(powcnt)

distinct_powers(100)
