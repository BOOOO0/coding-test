import sys
from collections import deque

M , N = map(int,sys.stdin.readline().split())

board = []
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
deq = deque()
answer = 0
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
    
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            deq.append((i,j))

def BFS():
    while deq:
        x,y = deq.popleft()  
        
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                deq.append((nx,ny))
                
BFS()

for i in board:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    answer = max(answer,max(i))
print(answer -1 )