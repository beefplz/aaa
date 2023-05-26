A = [[1, 2],[3,4]]
print(A[0])
print(A[1])

print("\n1행 : ", end = '')
for i in range(2):
    print(A[0][i], end=' ')
print("\n2행 : ", end ='')
i=0
for i in range(2):
    print(A[1][i], end = ' ')
print("\n1열:", end= '')
for i in range(2):
    print(A[i][0], end = ' ')
print("\n2열:", end = '')
for i in range(2):
    print(A[i][1], end = ' ')
print("\n")

print("몇행?\n")
a = int(input())
print(A[a-1])

print("몇열?\n")
b = int(input())
print(A[0][b-1], A[1][b-1])

print("\n")

F = [[1, 2],[3, 4]]
K = [[5, 6],[7, 8]]

print(F[0], "+", K[0])
print(F[1], " ", K[1])

print("=")

print(F[0][0]+K[0][0], F[0][1]+K[0][1])
print(F[1][0]+K[0][1], F[1][0]+K[1][1])

