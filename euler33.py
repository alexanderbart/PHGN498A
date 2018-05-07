''' Euler 33 '''
import numpy as np

numers = []
denoms = []
for i in range(10,100):
    for j in range(10,100):
        if i>j:
            numers.append(j)
            denoms.append(i)

print(len(numers))
print(len(denoms))
fracs = len(numers)

ansnum = 1
ansden = 1
count = 0

for i in range(fracs):
    newnum = 0
    newden = 0
    if str(numers[i])[0] == str(denoms[i])[0]:
        newnum = int(str(numers[i])[1])
        newden = int(str(denoms[i])[1])

    if str(numers[i])[1] in str(denoms[i])[1]:
        newnum = int(str(numers[i])[0])
        newden = int(str(denoms[i])[0])

    if str(numers[i])[0] in str(denoms[i])[1]:
        newnum = int(str(numers[i])[1])
        newden = int(str(denoms[i])[0])

    if str(numers[i])[1] in str(denoms[i])[0]:
        newnum = int(str(numers[i])[0])
        newden = int(str(denoms[i])[1])


    if newden != 0 and denoms[i] != newden*10:
        if numers[i]/denoms[i] == newnum/newden:
            ansnum *= numers[i]
            ansden *= denoms[i]

print("The product of numerators divided by the product of denominators is",\
ansnum/ansden)
print("So the reduced denominator is 100")

#print(ansnum,np.product(ansnum))















###############################################################################
