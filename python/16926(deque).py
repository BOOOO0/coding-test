import sys
from collections import deque


N , M , R = map(int , sys.stdin.readline().split())

board = [list(map(int , sys.stdin.readline().split())) for _ in range(N)]

def rotate (y,x,height,width):
    global board
    q = deque()
    # 한 depth 씩 board의 원소들을 deque에 삽입
    
    for i in range(x, x+width):
        q.append(board[y][i])
    
    for i in range(y+1, y+height):
        q.append(board[i][x+width-1])
    
    for i in range(x+width-2, x, -1):
        q.append(board[y+height-1][i])
    
    for i in range(y+height-1, y, -1):
        q.append(board[i][x])
    
    # 한줄로 입력받은 board의 원소들을 deque.rotate() 시킨다
    
    q.rotate(-R)
    for i in range(x, x+width):
        board[y][i] = q.popleft()
    
    for i in range(y+1, y+height):
        board[i][x+width-1] = q.popleft()
    
    for i in range(x+width-2, x, -1):
        board[y+height-1][i] = q.popleft()
    
    for i in range(y+height-1, y, -1):
        board[i][x] = q.popleft()
    
height = N
width = M
y , x = 0 , 0
   
while True:
    if height == 0 or width == 0: break

    rotate(y, x, height, width)
    y += 1
    x += 1
    height -= 2
    width -= 2

for i in board:
    print(*i)