A = [[1,2,3],
     [2,1,3],
     [3,1,2]]

B = [[2,3,1],
     [3,2,1],
     [3,2,2]]

C = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(3):
    for j in range(3):
        for n in range(3):
            C[i][j] += A[i][n]*B[n][j]

for i in range(3):
    for j in range(3):
        print(C[i][j],end=' ')
    print()

