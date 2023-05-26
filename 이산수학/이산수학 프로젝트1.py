# 1.사용자로부터 정방행렬의 크기를 입력받는다.
print("정방행렬의 크기를 입력하세요.")
n = int(input())  #n은 정방행렬 크기
print("만들 정방행렬의 크기는 ", n, "*", n, "입니다.\n") 

# 2.입력받은 크기만큼의 영행렬인 정방행렬을 만든다.
h = []       # h는 행렬의 이름
for i in range(n):
    e = []      
    for j in range(n):
        e.append(0)
    h.append(e)

# 3. 만들어진 영행렬안에 행렬식 계산을 할 수를 입력한다.
for i in range(n):
    for j in range(n):
        print(i+1, "행", j+1, "열에 들어갈 수를 입력하세요\n")
        h[i][j] = int(input())

print("행렬식 계산을 할 행렬입니다\n.")
for i in range(n):
    for j in range(n):
        print(h[i][j], end='  ')
    print()

# 4. 사루스 공식을 이용한 행렬식 계산
# 4.1 왼쪽위에서 오른쪽 아래로 이어지는 플러스가 되는 대각선
hPlus=[]    # hPlus배열에  플러스가 되는 대각선을 모음
k=1
for i in range(len(h)):
    for l,o in zip(range(len(h)), range(len(h)-i)):
        k *= h[l][o+i]
        if(o+i == len(h)-1):
            for j in range(len(h)-l-1):
                k *= h[l+j+1][j]
    hPlus.append(k)                 #곱셈이 끝날때마다 hPlus에 저장
    k=1
# 4.2 오른쪽 위에서 왼쪽 아래로 이어지는 마이너스가 되는 대각선
hMinus=[]    # hMinus배열에 마이너스가 되는 대각선을 모음
k=1
for i in range(len(h)):
    for o,l in zip(range(len(h)-i), range(len(h)-i-1,-1, -1)):
        k *= h[o][l]
        if(l==0):
            for j, v in zip(range(o+1, len(h)+1, +1), range(len(h)-1, o, -1)):
                k *=h[j][v]
    hMinus.append(k)                      #곱셈이 끝날때마다 hMinus에 저장
    k=1
# 4.3 hPlus에서 hMinus를 빼서 답을 구한다
print("행렬식 계산 결과는 : ")
Answer=0
for i in range(len(h)):
    Answer += hPlus[i] - hMinus[i]
print(Answer)
