# 노드의 방문 처리를 위한 별도의 리스트를 두는 구현

def dfs(graph, v, visited):
    # 처음 시작 노드의 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 그 노드와 인접한 방문하지 않은 모든 노드를 STACK에 삽입하는 과정
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    # 그 이후 최상단 노드부터 다시 pop 되면서 방문처리되고 그 노드와 인접한 노드를 모두 STACK에 삽입
    # 반복할 것

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

dfs(graph, 1, visited)

