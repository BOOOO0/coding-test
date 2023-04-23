import sys


N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    # 이 문제에서는 readline을 쓰는 것보다 input을 썼을 때
    # 더 효율적이다
    # 왜냐면 letters라는 하나의 변수에 저장을 받은 다음에
    # 그것을 사용하려 하기 때문에
    # input을 사용하여 ()이 입력되도 ( 과 )으로 나뉘게 한다
    letters = list(input())
    is_empty = False
    stk = []
    for letter in letters:
        if letter == '(':
            stk.append(letter)
        else:
            if not stk:
                is_empty = True
                break
            else:
                stk.pop()
    if not stk and not is_empty == True:
        print("YES")
    else:
        print("NO")

    