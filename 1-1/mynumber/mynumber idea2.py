import random
computer_number = random.randint(1, 100)
def is_same(target, number):
    if target == number:
        result="Win"
    elif target > number:
        result="Low"
    else:
        result="High"
    return result
print("안녕.\n난 1부터 100 중 숫자 하나를 골랐어요.")

guess = int(input("뭔지 쓰고 엔터 키를 누르세요."))

higher_or_lower = is_same(computer_number, guess)

counter=1
while higher_or_lower != "Win":
    if higher_or_lower == "Low":
        guess = int(input("그것보다 높습니다. 다시 생각해보세요."))
    else:
        guess = int(input("그것보다 낮습니다. 다시 생각해보세요."))
    counter = counter+1
    higher_or_lower = is_same(computer_number, guess)

print("정답!\n", counter, "번째에 맞췄습니다.\n")
input("잘했어요.\n\n\n마치려면 엔터 키를 누르세요.")

