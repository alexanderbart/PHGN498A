''' Euler 19 '''

answer = 0
day = 0
for i in range(1901,2001): #number of years

    for j in range(1,13): #number of months

        if j == 2:
            if i%4 == 0: # leap years
                day += 29
                if day%7 == 0:
                    answer += 1
            else:
                day += 28
                if day%7 == 0:
                    answer += 1
        if j==1 or j==3 or j==5 or j==7 or j==8 or j==10 or j==12:
            day += 31
            if day%7 == 0:
                answer += 1
        if j==4 or j==6 or j==9 or j==11:
            day += 30
            if day%7 == 0:
                answer += 1

print('Sundays =',answer+1)
