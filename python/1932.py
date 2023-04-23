import sys

# 높이가 N인 삼각형을 입력을 받는다
# N x ? 의 리스트를 만든다
# 1번째 줄 부터 전 줄의 최대값과의 합이 자기자신이 된다
# N-1 번째 줄 까지 반복


N = int(sys.stdin.readline().rstrip())


Trinity = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

for i in range(1,N):
    for j in range(len(Trinity[i])):
        if j==0:
            Trinity[i][j] = Trinity[i-1][j] + Trinity[i][j]
        elif j == len(Trinity[i])-1:
            Trinity[i][j] = Trinity[i-1][j-1] + Trinity[i][j]
        else:
            Trinity[i][j] = max(Trinity[i-1][j-1] , Trinity[i-1][j]) + Trinity[i][j]
        
print(max(Trinity[N-1]))