# DFS와 동일한 로직을 가지고 있으나
# 방문 처리가 STACK에서 POP으로 되느냐 QUEUE에서 SHFIT로 되느냐의 차이

from collections import *

def bfs(graph, start, visited):
    queue = deque([start])
    # 시작 노드 방문 처리
    visited[start] = True

    # queue가 빌 때 까지
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        # SHIFT된 노드와 인접한 노드 중 방문하지 않은 모든 노드 QUEUE에 삽입하는데
        # 그와 동시에 방문 처리를 한다?
        # 편의를 위해 여기서 구현하는 데에 방문 처리를 바로 한 것이지
        # 실제 방문은 SHIFT 되어 출력되는 것이다.
        # 출력시에 방문 처리를 하도록 하면 결과가 다른가? -> O
        # 이 방법이 일반화가 가능한가? -> X 방문이라는 개념을 이해하기 위한 정도로 넘어가자
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)