''' Euler 55 '''

def palindrome(mystr):
    mystr = str(mystr)
    palin = True
    for i in range(0,int(len(mystr)/2)):
        if not(mystr[i] == mystr[(len(mystr)-1-i)]):
            palin = False

    return palin

def reverse(mystr):
    mystr = str(mystr)
    palin = ''
    for i in range(len(mystr)-1,-1,-1):
        palin += mystr[i]

    return palin

lych = 0

for i in range(1,10**4):
    check = 1 #If check stays at 1: after 50 iterations no palindrome
    newnum = i + int(reverse(i))
    for j in range(50):
        if palindrome(newnum) == True:
            check = 0
            break
        newnum += int(reverse(newnum))

    if check == 1:
        lych += 1

print(lych)
