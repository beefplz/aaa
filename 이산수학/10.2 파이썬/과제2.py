A=[[0,0,0],[0,0,0]]
B=[[0,0],[0,0],[0,0]]
C=[[0,0],[0,0]]

print("2*3행렬 입력")
for i in range(2):
    for j in range(3):
        A[i][j] = int(input())

print("3*2행렬 입력")
for i in range(3):
    for j in range(2):
        B[i][j] = int(input())

for i in range(2):
    for j in range(2):
        for n in range(3):
            C[i][j] += A[i][n]* B[n][j]

if(len(A)==len(B[1])):
    for i in range(2):
        for j in range(2):
            print(C[i][j], end = ' ')
        print(" ")
else:
    print("행렬 곱셈 불가")
