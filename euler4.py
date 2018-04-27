#Euler 4
def palindromeproduct():
    prod = 0
    maxVal = 0
    for i in range(100,1000):
        for j in range(100,1000):
            prod = i*j
            if str(prod) == str(prod)[::-1]:
                if prod > maxVal:
                    maxVal = prod
    print(maxVal)
palindromeproduct()
