#Euler 9
def pythagtrip():
    # Again, no input here because of the specificity.
    a = 1
    b = 2
    c = 3
    condition = 0
    while condition == 0:
        for i in range(1,501):
            if condition == 1: #Want to stop as soon as the conditions are met.
                break
            a = i
            for j in range(1,501):
                if condition == 1:
                    break
                b = j
                c = 1000 - (b+a)    # a+b+c always = 1000
                if (((a**2) + (b**2)) == c**2):
                    condition = 1
    print("The numbers are",a,b,c,"and the product is",a*b*c)
pythagtrip()
