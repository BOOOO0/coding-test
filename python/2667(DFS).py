import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
board = []
num = []
count = 0
result = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip())))

def DFS(x , y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if board[x][y] == 1:
        global count
        count += 1
        board[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx,ny)
        return True
    return count



for i in range(N):
    for j in range(N):
        if DFS(i,j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for n in num:
    print(n)

