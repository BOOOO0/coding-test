# 공포도가 1 2 3 2 2 라면
# 공포도 3인 모험가는 3명이상의 그룹에
# 공포도가 2인 모함가는 2인 이상인 그룹에 들어가야한다
# 그렇다면 몇개의 그룹을 만들 수 있는가?

import sys

N = int(sys.stdin.readline().rstrip())

fear = list(map(int, sys.stdin.readline().split()))
fear.sort()

result = 0
cnt = 0

# 정렬이 되어있기 때문에 i가 현재 공포도의 크기이다
# 그래서 현재 공포도보다 그룹에 포함된 모험가 수가 더 많다면
# 그룹으로 출발시킬 수 있기 때문에 그룹의 수 result를 증가시킨다
# (1,2,3) (2,2)로 묶으면서 그룹을 만들어 수를 구하는 것은 아니지만
# 결과적으로는 그룹의 수를 구할 수 있는 알고리즘이다
for i in fear:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)
