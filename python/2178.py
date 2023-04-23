import sys
from collections import deque

N , M = map(int,sys.stdin.readline().split())

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

board = []

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip())))



def BFS(x , y):
    deq = deque()
    deq.append((x,y))
    
    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 0:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                deq.append((nx,ny))

    return board[N-1][M-1]

print(BFS(0, 0))
