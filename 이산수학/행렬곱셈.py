A = [[1,2],
     [3,4]]
B = [[5,6],
     [3,4]]
C=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        for n in range(2):
            C[i][j] += A[i][n]*B[n][j]

for i in range(2):
    for j in range(2):
        print(C[i][j],end=' ')
    print()

