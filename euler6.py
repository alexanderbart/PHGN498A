#Euler 6
def euler6(var):
    sumofsqr = 0
    sqrofsum = 0
    for i in range(var+1):
        sumofsqr += i**2
        sqrofsum += i
    sqrofsum = sqrofsum**2
    ans = sqrofsum-sumofsqr
    return ans
print(euler6(100))
