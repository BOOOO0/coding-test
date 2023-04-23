import sys

N = int(sys.stdin.readline().rstrip())

wines = [0]

for _ in range(N):
    wines.append(int(sys.stdin.readline().rstrip()))
    
# 0 은 0
dp = [0]
# 1 은 wines[1]
dp.append(wines[1])
# 2 는 wines[1] + wines[2]
if N > 1:
    dp.append(wines[1] + wines[2])
# 3 부터는 계단 오르기와 동일한 점화식
# 바로 이전 까지의 dp 와 비교가 들어간 이유는
# 시작점이 정해져있지 않기 때문?
# 자기 자리를 패스할 때 더 큰 경우를 고려하기 위해서?
# 바로 이전 dp와의 비교를 넣지 않았을 때의
# 반례가 1 1 0 0 1 1 이 있다 4가 나와야 하는데 3이 나옴

# 계단오르기 문제와 다른 이유 
# 계단오르기에서는 마지막 계단을 반드시 지나야 하기 때문에
# 자기 자신을 패스하는 dp[i-1]과의 비교가 빠진 것이고
# 이 문제는 마지막 잔을 지나치고 가도 되기 때문에 
# 만약 N-2,N-1을 연달아 마시는 경우의 값이 더 크다면 패스할 수 있다는 전제를 넣어서
# dp[i-1] 즉 바로 이전 dp의 값도 비교의 대상이 된다

for i in range(3,N+1):
    dp.append( max(dp[i-1], dp[i-3] + wines[i-1] + wines[i] , dp[i-2] + wines[i] ) )

print(dp[N])

