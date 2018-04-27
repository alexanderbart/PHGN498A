'''Euler 14'''
def collatz(n):
    num = 1
    maxcnt = 1
    while num < n:
        i = num
        count = 1
        while i != 1:
            if i % 2 == 0:
                i = i/2
                count += 1

            else:
                i = 3*i + 1
                count += 1

        if count > maxcnt:
            maxcnt = count
            answer = num

        num += 1

    print(answer)

collatz(1000000)
