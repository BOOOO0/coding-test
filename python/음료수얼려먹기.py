import sys

# 왼쪽에서부터 0을 채워나간다
def DFS(x, y):
    print(graph, "\n")
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 0인 노드라면
    if graph[x][y] == 0:
        # 1로 바꾸고
        graph[x][y] = 1
        # 인접한 모든 0인 노드 방문하며 1로 바꾼 다음
        DFS(x, y - 1)
        DFS(x, y + 1)
        DFS(x - 1, y)
        DFS(x + 1, y)
        # True를 반환한다
        return True
    return False


N, M = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

result = 0

for i in range(N):
    for j in range(M):
        if DFS(i, j) == True:
            result += 1

print(result)
