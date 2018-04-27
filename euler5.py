#Euler 5
def smallestmultiple():
    #No input here because the problem is so specific
    ans = 2520
    num = 10

    while num != 21:
        if ans%num != 0:
            num = 10
            ans = ans + 2520 #know it must be multiple of first 10 numbers
        num = num + 1
    print("The smallest multiple of all numbers 1 to 20 is",ans)

smallestmultiple()
