import sys

n = int(sys.stdin.readline().rstrip())

board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

#print(board[0],board[1])
'''
for i in range(n):
    j=i
    for j in range(n):
        if(board[j][0] > board[])
'''

board.sort()

for i in range(n): 
    print(board[i][0],board[i][1])