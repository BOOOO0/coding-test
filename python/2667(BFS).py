import sys
from collections import deque

def BFS(board , a , b):
    n = len(board)
    deq = deque()
    deq.append((a,b))
    board[a][b] = 0
    count = 1
    
    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                deq.append((nx,ny))
                count += 1
    return count


N = int(sys.stdin.readline().rstrip())

board = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip())))

cnt = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            cnt.append(BFS(board , i , j))

cnt.sort()
print(len(cnt))
for c in cnt:
    print(c)