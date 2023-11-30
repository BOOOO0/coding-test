# BFS로 1을 찾아 이동하면서 이전 값에 1씩 더하고
# 마지막에 도달했을 때 총 이동 거리가 저장되므로
# board[n][m]이 답이 되는 문제
# 방문 가능한 모든 부분을 방문하면서 더하는 문제에 응용이 되었던 걸로 기억
# 그런데 이것도 어느 정도 난이도가 넘어가면 일반화는 되지 않았던 걸로 기억

from collections import deque


def bfs(a, b):
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] == 0:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))

    return board[n - 1][m - 1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

board = []

for i in range(n):
    board.append(list(map(int, input())))

print(bfs(0, 0))

for i in board:
    print(i)
