import sys

# 열은 a~h
# 행은 1~8
# 입력으로 열과 행이 주어지고
# 그 엔트리 포인트를 기점으로 이동할 수 있는 경우의 수를 구한다.
# 나이트는 행과 열이 -2, -1 | -2, +1 | -1, -2 | -1, +2 | +1, -2 | +1, +2 | +2, -1 | +2, +1 | 움직일 수 있다.
# 행이 < 1이 아니고 열이 < a가 아니고 행이 > 8이 아니고 열이 > h가 아니게 되는 경우의 수를 구하면 되는 문제

row_col = list(map(str, sys.stdin.readline().rstrip()))

answer = 0

row = int(row_col[1])
# 미리 아스키코드 값을 뽑아서 a가 1이 되는 것을 기준으로 만든다
col = ord(row_col[0]) - 96

tup = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))

for t in tup:
    if(t[0] + row < 1 or t[1] + col < 1 or t[0] + row > 8 or t[1] + col > 8):
        continue
    else:
        answer += 1

print(answer)