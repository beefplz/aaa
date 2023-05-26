A = [[1,2,3],[3,2,1],[2,3,1]]
B = [[4,5,6],[6,4,5],[5,6,4]]
C = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j]+B[i][j]

for i in range(3):
    for j in range(3):
        print(C[i][j], end = ' ')
    print()
