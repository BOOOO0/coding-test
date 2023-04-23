import sys

N = int(sys.stdin.readline().rstrip())

DP = [0] * (N+1)
if N == 1:
    DP[1] = 1
else:
    DP[1] = 1
    DP[2] = 2

def Binary(N):
    if N >= 3:
        for i in range(3,N+1):
            # 계속 나머지 연산을 해야 메모리 초과가 아니라는데
            # int max 를 벗어나는 값이 나오기 때문이라고 한다
            DP[i] = (DP[i-2] + DP[i-1])  % 15746
    return DP[N] 

print(Binary(N))