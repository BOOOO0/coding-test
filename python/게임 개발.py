import sys
# 갈 수 있는 땅은 0이고 갈 수 없는 땅은 1이다.
# 처음 바라보는 방향이 주어지고 그 방향 기준으로 왼쪽으로 이동한다.
# 그렇다면 0일 때는 y값 -1, 1일 때는 x 값 -1, 2일 때는 y값 +1, 3일 때는 x값 + 1
# 그 다음 이동한 방향 기준으로 또 왼쪽으로 회전하고 갈 수 있으면 이동한다.
# 근데 가본 곳이면 생략해야 하는데 이것을 방문 후 갈 수 없는 땅으로 1로 변경
# 긴 설명 필요 없이 일반적인 dx, dy 사용하는 문제
# 코드로 보는 것이 나음

n , m = map(int, sys.stdin.readline().split())



a, b, d = map(int, sys.stdin.readline().split())

board = []

for i in range(n):  
    board.append(list(map(int, input().split()))) 
move_steps = [(-1, 0), (0, -1), (1, 0), (0, 1)] 

result = 1
count = 0
board[a][b] = 2 

while True:  
    d = d - 1  
    if d == -1:    
        d = 3  
    next_a = a + move_steps[d][0]  
    next_b = b + move_steps[d][1]  
    if board[next_a][next_b] == 0:    
        a = next_a   
        b = next_b  
        result += 1   
        board[a][b] = 2   
        count = 0  
    else:   
        count += 1   
        if count == 4:      
            next_a = a + move_steps[d-2][0]   
            next_b = b + move_steps[d-2][1]   
            if board[next_a][next_b] == 1:      
                break     
            else:       
                a = next_a    
                b = next_b    
                count = 0
print(result)

