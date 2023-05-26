A=[[0,0],[0,0]]
B=[[0,0],[0,0]]
C=[[0,0],[0,0]]

print("2*2행렬 1 입력")
for i in range(2):
    for j in range(2):
        A[i][j] = int(input())

print("2*2행렬 2 입력")
for i in range(2):
    for j in range(2):
        B[i][j] = int(input())

for i in range(2):
    for j in range(2):
        for n in range(2):
            C[i][j] += A[i][n]* B[n][j]

print("곱셈은")

for i in range(2):
    for j in range(2):
        print(C[i][j], end = ' ')
    print(" ")

for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] + B[i][j]

print("덧셈은")

for i in range(2):
    for j in range(2):
        print(C[i][j], end = ' ')
    print(" ")
