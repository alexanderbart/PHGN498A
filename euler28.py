import numpy as np

'''Euler 28'''
def spiral_diag(N):
    '''
Starting at the middle, we move down the row once, then column once.
Then we go up row twice, up column twice. Then up row thrice, column thrice.
So even numbers of moves increase column and row. Odd numbers of moves
decrease column and row. The final piece of the spiral has the same number
of moves as previous, so I had to account for that.
    '''


    mat = np.zeros((N,N))
    mat[int((N-1)/2),int((N-1)/2)] = 1

    moves = 1
    num = 2
    i = int((N-1)/2)
    j = int((N-1)/2)

    while mat[0,int(N-1)] == 0:

        if moves%2 != 0:
            for k in range(moves):
                j += 1
                mat[i,j] = num
                num += 1
            for k in range(moves):
                i += 1
                mat[i,j] = num
                num += 1

        if moves%2 == 0:
            for k in range(moves):
                j -= 1
                mat[i,j] = num
                num += 1
            for k in range(moves):
                i -= 1
                mat[i,j] = num
                num += 1
        if mat[0,0] != 0:
            for k in range(moves):
                j += 1
                mat[i,j] = num
                num += 1
        moves += 1

    diag_sum = 0

    for i in range(N):
        diag_sum += mat[i,i]
    for i in range(N):
        diag_sum += mat[i,N-1-i]
    diag_sum -= 1           #Accounts for middle being double-counted

    return diag_sum

print('The sum of the diagonals is',spiral_diag(1001))
