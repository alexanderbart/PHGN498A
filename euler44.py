''' Euler 44 '''

pentagols = []

for i in range(1,10**5):
    num = i*(3*i-1)/2
    pentagols.append(int(num))

    n = (math.sqrt((24 * x) + 1) + 1) / 6

for i in range(len(pentagols)):
    print(pentagols[i])
    for k in range(i):
        for j in range(k):

            pent1 = pentagols[k]
            pent2 = pentagols[j]
            pent3 = pentagols[i]

            if pent1 + pent2 == pent3:
                if pent1 - pent2
                print(pent1,pent2,pent1+pent2,pent1-pent2)
