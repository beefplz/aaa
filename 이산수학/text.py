
print("정방행렬의 크기를 입력하세요.")
n = int(input())  
print("만들 정방행렬의 크기는 ", n, "*", n, "입니다.\n") 


h = [] 
for i in range(n):
    e = []         
    for j in range(n):
        e.append(0)
    h.append(e)

