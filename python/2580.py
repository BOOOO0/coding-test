

import sys


# 시간단축요소
# exit()
# 재귀함수를 사용할 때
# 재귀 호출을 계속 하다보면 스택에 함수가 쌓인다
# 이 문제는 9줄의 출력이 끝나면 완료가 된다 
# 그런데 9줄의 출력이 다 끝나고 나서도 앞에 쌓인 함수들을 마무리하기 위해서
# 다시 돌아가야 하는데
# exit()를 사용해서 마지막 함수 실행으로 9번째 줄을 출력했을 때
# 그대로 종료되게 하면서 시간을 단축시킬 수 있었다

board = [list(map(int , sys.stdin.readline().split())) for _ in range(9)]

check_board = [(i,j) for i in range(9) for j in range(9) if board[i][j] == 0 ]

def select(x , y):
    
    numbers = [1,2,3,4,5,6,7,8,9]
    
    for n in range(9):
        if board[x][n] in numbers:
            numbers.remove(board[x][n])
        if board[n][y] in numbers:
            numbers.remove(board[n][y])
            
    y = y//3
    x = x//3
    
    for i in range(x*3 , (x+1)*3):
        for j in range(y*3 , (y+1)*3):
            if board[i][j] in numbers:
                numbers.remove(board[i][j])
    return numbers

def DFS(count ):
    if count == len(check_board):
        for i in range(9):
            sys.stdout.write(" ".join(map(str, board[i])) + "\n")
        exit()
    (i,j) = check_board[count]
    selected = select(i,j)
    for sel in selected:
        board[i][j] = sel
        DFS(count+1)
        board[i][j] = 0

DFS(0)


'''

# 지금까지 가장 빠른 코드

import sys


def check(x, y):
    key = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):  # 가로세로 검사
        if game[x][i] in key:
            key.remove(game[x][i])
        if game[i][y] in key:
            key.remove(game[i][y])

    x1 = x // 3
    y1 = y // 3

    for i in range(x1 * 3, x1 * 3 + 3):  # 3곱3 검사
        for j in range(y1 * 3, y1 * 3 + 3):
            if game[i][j] in key:
                key.remove(game[i][j])

    return key


def solve(n, count):

    if n == count:
        for i in range(9):
            sys.stdout.write(" ".join(map(str, game[i])) + "\n")
        exit()

    i, j = tosolve[n]
    for item in check(i, j):
        game[i][j] = item
        solve(n + 1, count)
        game[i][j] = 0


game = []

for i in range(9):
    game.append(list(map(int, sys.stdin.readline().split())))

tosolve = [(i, j) for i in range(9) for j in range(9) if game[i][j] == 0]

solve(0, len(tosolve))
'''