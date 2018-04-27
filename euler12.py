#Euler 12
def euler12(num):
    condition = 0
    jj = 2

    tris = []
    tris.append(1)
    t1 = t.time()
    while condition == 0:
        tris.append(tris[-1] + jj)
        #nums = np.linspace(1,tris[-1],tris[-1])
        facts = []
        for i in range(1,int(tris[-1]**0.5)):
            if tris[-1]%i == 0:
                facts.append(i)
                facts.append(tris[-1]/i)

        if len(facts) > num:
            condition = 1
        jj += 1

    t2 = t.time()
    print(t2-t1)
    return tris[-1]

print(euler12(500))
