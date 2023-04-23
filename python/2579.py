import sys


n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])

'''

N = int(sys.stdin.readline().rstrip())

steps = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

DP = [0 for i in range(N+1)]

for i in range( len(steps)-1 , 0 ,-1):
    if i-1 == 0 :
        DP += steps[i-1]
        break
    elif steps[i-1] > steps[i-2]:
        DP += steps[i-1]
        i -= 2
    else:
        DP += steps[i-2]
        i -= 1
        print(DP)
print(DP)
'''