# def DFS(graph, x, visited):
#     visited[x] = True
#     print(x, end=" ")
#     for y in graph[x]:
#         if not visited[y]:
#             DFS(graph, y, visited)


def DFS(graph, x, visited):
    stk = []
    stk.append(x)
    visited[x] = True
    while stk:
        x = stk.pop()
        print(x, end=" ")
        for y in graph[x]:
            if not visited[y]:
                stk.append(y)
                visited[y] = True


graph = [[], [2, 3, 8], [1, 6, 7], [1, 4, 5], [3], [3], [2], [2, 8], [1, 7]]

visitied = [False for _ in range(9)]

print(DFS(graph, 1, visitied))
