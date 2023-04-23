import sys
from collections import deque

# 입력 받은 값을 어떻게 나눠서 저장할 지
# 트리의 지름이 의미하는 것이 무엇인지
# 어떻게 구하는 것인지

# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다.

N = int(sys.stdin.readline().rstrip())
graph = [ [] for _ in range(N+1)]

for _ in range(N):
    c = list(map(int, sys.stdin.readline().split()))
    for edge in range(1, len(c)-2, 2):
        #첫번째 숫자가 정짐의 번호이고 
        #그 다음 인덱스 부터 연결된 정점과 그 정점까지의 거리
        #반복문을 2씩 증가시켜서 (정점, 거리) 를 그래프 리스트에 더해지게 만든다        
        graph[c[0]].append( (c[edge], c[edge+1]) )


# 방문하지 않았는지만 체크하고 거리를 더해주면
# 방문기록이 체크되어서 다시 방문하지 않는다
def BFS(start):
    b_check = [ -1 for _ in range(N+1)]
    deq = deque()
    deq.append(start)
    b_check[start] = 0
    max_distance = [0,0]
    
    while deq:
        x = deq.popleft()
        for y , dist in graph[x]:
            if b_check[y] == -1:
                b_check[y] = b_check[x] + dist
                deq.append(y)
                if max_distance[0] < b_check[y]:
                    max_distance = b_check[y] , y
    return max_distance

# 트리의 지름은 아무 노드에서 bfs(dfs도 무관)를 통해 가정 멀리있는 노드를 구한 후 
# 해당 노드에서 bfs를 한번더 진행하여 가장 멀리있는 노드를 구하면 된다.

dis, node = BFS(1)
dis, node = BFS(node)

print(dis)