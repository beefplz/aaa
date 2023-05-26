A=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
B=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
C=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]

print("3*4행렬 1 입력")
for i in range(3):
    for j in range(4):
        A[i][j] = int(input())

print("3*4행렬 2 입력")
for i in range(3):
    for j in range(4):
        B[i][j] = int(input())

for i in range(3):
    for j in range(4):
        C[i][j] = A[i][j] + B[i][j]

if(len(A)==len(B), len(A[1])==len(B[1])):
    if(len(A[1])==len(B[1])):
        print("덧셈가능")
        for i in range(len(A)):
            for j in range(len(A[1])):
                print(C[i][j], end = ' ')
            print(" ")
else:
    print("덧셈불가능")
