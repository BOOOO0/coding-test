import sys

N = int(sys.stdin.readline().rstrip())

DP = [0] * 101
DP[1] = 1
DP[2] = 1
DP[3] = 1

def wave (P):
    if P > 3:
        for i in range(4,P+1):
            DP[i] = DP[i-2] + DP[i-3]
    return DP[P]

for i in range(N):
    P = int(sys.stdin.readline().rstrip())
    print(wave(P))