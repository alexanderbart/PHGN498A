''' Euler 52 '''

condition = 1
num = 1
while condition:
    multiplier = 1

    while multiplier != 6:
        check = 1 #If check stays at 1, then we know the number is the answer
        multiplier += 1
        newnum = multiplier*num

        if len(str(newnum)) != len(str(num)):
            # If product is longer than number, it won't work
            check = 0
            break

        for i in str(num):
            if not i in str(newnum):
                # Need to have each digit in the product
                check = 0
                break

        if check == 0:
            break

    if check == 1:
        print('answer is',num)
        condition = 0

    num += 1
