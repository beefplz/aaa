how_far = int(input("몇 단의 구구단을 원하시나요?\n"))
num = int(input("몇까지 구할까요?\n"))
n=1
while n <= how_far:
    print(n, "x", num, "=", n*num)
    n=n+1
