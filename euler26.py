'''Euler 26'''
def recip_cycles():
    ans = 0

    num = 1000
    count = []
    while num > 1 and len(count)-1 < num:
    #A reciprocal can't have more repeating digits than its number
        count = []
        condition = 0
        modulus = 1
        count.append(modulus)

        while condition == 0:
            modulus = (modulus*10) % num

            if modulus == 0:
                condition = 1
                num -= 1
            count.append(modulus)

    #Check if the moduli repeat, and see if it's a record length
            if len(count)>2 and count[-1] in count[:-1]:
                condition = 1
                if len(count) > ans:
                    ans = len(count)-1
                    ansnum = num

                num -= 1


    print('The number with the most repeating digits in its decimal is',ansnum)

recip_cycles()
