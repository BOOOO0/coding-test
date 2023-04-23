import sys
from collections import deque

# 뒤집는 횟수가 홀수번 일떄만 뒤집는다
# 두번 뒤집어야 하는 상황은 그대로인 것과 같기 때문에
# 시간초과를 피하기 위해서 홀수번만 뒤집는다

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    str = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    deq = deque(arr)

    rev, front, back = 0, 0, len(deq) - 1
    # 네번쨰 테스트케이스

    flag = 0

    if n == 0:
        deq = []
        front = 0
        back = 0

    for s in str:
        if s == "R":
            rev += 1
        elif s == "D":
            if len(deq) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    deq.popleft()
                else:
                    deq.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(deq) + "]")
        else:
            deq.reverse()
            print("[" + ",".join(deq) + "]")
