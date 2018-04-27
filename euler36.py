'''
Euler 36
'''
def binary(direction,number):
    '''
    Put 1 for direction to go from base 10 to binary
    Put 2 for direction to go from binary to base 10
    '''
    if direction == 1:
        digs = []
        answer = ''
        while number > 1:
            remain = number % 2
            number = int(number/2)
            digs.insert(0,remain)
            if number < 2:
                digs.insert(0,number)

        for i in range(len(digs)):
            answer += str(digs[(i)])

        answer = int(answer)

    if direction == 2:
        digs = list(str(number))
        for i in digs:
            i = int(i)

        answer = 0
        for i in range(len(digs)):
            if int(digs[i]) == 1:
                answer += 2**(len(digs)-i-1)

    return answer

#print(binary(1,59))
#print(binary(2,binary(1,59)))

def is_palindrome(number):
    number = str(number)

    answer = True
    for i in range(len(number)):
        #print(number[i],number[-(i+1)])
        if number[i] != number[-(i+1)]:
            answer = False

    return answer

def dbl_palindromes(N):
    palist = [1] #For some reason my algorithm doesn't like 1 so I put it in
                 #manually.
    for i in range(N-1):
        if (N-i)%2 == 1: #Since we can't have leading zeros, the binary
                         #representation must end in 1.
            if is_palindrome(N-i)==True:
                if is_palindrome(binary(1,N-i))==True:
                    palist.append(N-i)
                    #print(N-i,binary(1,N-i))
    print(sum(palist))
dbl_palindromes(10**6)
