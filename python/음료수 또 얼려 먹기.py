def dfs(x, y):
    # board의 범위 밖으로 나간다면 False를 반환
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x , y + 1)
        return True
    return False

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

result = 0

# 내 기억에 이 부분이 일반화가 어려운 부분이였고
# 일반적으로 dx, dy 리스트를 생성해 상하좌우 좌표 이동을 하던 것을
# 재귀로 사용하는 부분이 배워갈만한 내용이었다.
# 저부분도 일반화는 어려웠던 걸로 기억
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)