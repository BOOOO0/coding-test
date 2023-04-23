from collections import deque
import sys
'''
이 문제는 한번씩 방문을 하면 끝나는 문제이기 때문에
한번의 DFS나 BFS를 수행하고 나면 끝나도 괜찮다
그렇기 때문에 시작점을 기점으로 한번의 탐색으로 끝나는 것

간선 리스트를 도는 반복문은 뻗을 수 있는 모든 자식 노드에 대해서 탐색한다 라는 의미라고 볼 수 있다

'''




N , M , start = map(int,sys.stdin.readline().split())
# N + 1 인 이유는 시작이 1이지 0은 아니여서? 0번째를 비워두려고?

edge = [[] for _ in range(N + 1)]
 
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    # 각각의 간선 방향을 서로 다 저장
    edge[v1].append(v2)
    edge[v2].append(v1)

# 순차적으로 돌기 위해서 정렬
for e in edge:
    e.sort()
    
d_check = [False for _ in range(N + 1)]

def dfs(x):
    d_check[x] = True
    print(x, end = ' ')
    # 뻗을 수 있는 모든 자식 노드에 대해서
    for y in edge[x]:
        if d_check[y] == False:
            dfs(y)

def bfs():
    # deque 생성 시엔 deque([list]) 여야한다 start지점부터 찾아야하니 start 넣어줌
    queue = deque([start])
    b_check = [False for _ in range(N + 1)]
    b_check[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        
        # 해당 정점의 간선방향을 가진 edge 리스트로 가서
        # 반복문을 이용해서 순차적으로 탐색
        # 뻗을 수 있는 모든 자식 노드에 대해서
        for i in edge[v]:
            if not b_check[i]:
                b_check[i] = True
                queue.append(i)


dfs(start)
print()
bfs()
print()