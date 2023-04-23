from collections import deque


def BFS(graph, start, visited):
    deq = deque([start])
    visited[start] = True
    while deq:
        x = deq.popleft()
        print(x, end=" ")
        for y in graph[x]:
            if not visited[y]:
                deq.append(y)
                visited[y] = True


graph = [[], [2, 3, 8], [1, 6, 7], [1, 4, 5], [3], [3], [2], [2, 8], [1, 7]]

visitied = [False for _ in range(9)]

BFS(graph, 1, visitied)
