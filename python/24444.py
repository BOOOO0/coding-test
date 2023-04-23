import sys
from collections import deque

N , M , R = map(int,sys.stdin.readline().split())

edge = [[] for _ in range(N+1)]
b_check = [False for _ in range(N+1)]
edge_count = [0 for _ in range(N+1)]

for _ in range(M):
    v1 , v2 = map(int,sys.stdin.readline().rstrip().split())
    edge[v1].append(v2)
    edge[v2].append(v1)

for e in edge:
    e.sort()
que = deque()
que.append(R)

# 시간단축요소
# b_check 를 True로 바꾸는 과정없이
# 바로 첫번째 시작정점의 간선들을 deque에 append 시킨다음
# popleft로 이어진 정점들을 너비우선으로 탐색하면서 
# cnt를 더해준다 
# 그리고 더 빠른 탐색을 위해서 시작정점의 이동 횟수 카운트에
# 1을 미리 넣어주고
# cnt는 2부터 시작하면서 추가해준다

edge_count[R] = 1
cnt = 2

while que:
    x = que.popleft()
    
    for e in edge[x]:
        if edge_count[e] == 0:
            que.append(e)
            edge_count[e] = cnt
            cnt += 1
            
for c in edge_count[1:]:
    print(c)
        