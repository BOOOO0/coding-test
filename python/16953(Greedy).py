import sys

A, B = map(int, sys.stdin.readline().split())


count = 1
while True:
    if A == B:
        break
    elif A > B:
        count = -1
        break
    elif (B % 10) == 1:
        B = B // 10
        count += 1
    elif (B % 2) == 0:
        B = B // 2
        count += 1
    # 위 까지가 이전 풀이에서 만든 조건들
    # 그 외에 식에서 벗어나는 숫자들도 -1이 출력되게 해야했음
    else:
        count = -1
        break

print(count)
