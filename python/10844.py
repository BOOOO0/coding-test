import sys

N = int(sys.stdin.readline().rstrip())

dp = [ [0 for _ in range(10)] for _ in range(N+1)]

# 일의 자리수들은 해당 인덱스 수가 맨 뒤에 올 수 있는 일의 자리수의 갯수가 1개이다
# 그래서 첫번째 자리수인 dp[i][] 들을 1로 초기화해준다
for i in range(1,10):
        dp[1][i] = 1
if N == 1:
        print(sum(dp[N]))
else:
    for i in range(2,N+1):
        for j in range(10):
            if j == 0:
                # 0이 가질 수 있는 계단 수는 이전 자릿수의 1이 가지는 계단수의 갯수와 같다
                # 좌우 대각선 중에 오른쪽 대각선만 있다
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                # 9가 가질 수 있는 계단 수도 이전 자릿수의 8이 가지는 계단수의 갯수와 같다
                # 좌우 대각선 중에 왼쪽 대각선만 있다
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[N]) % 1000000000) 
            