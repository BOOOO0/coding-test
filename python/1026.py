from posixpath import split

# A배열의 최솟값 x B배열의 최댓값 B배열의 최솟값 x A배열의 최댓값
# 나머지는 그냥 계산

import sys

N = int(sys.stdin.readline().rstrip())

A = list(map(int, sys.stdin.readline().split()))

B = list(map(int, sys.stdin.readline().split()))


B.sort()
A.sort(reverse=True)

S = 0
for i in range(N):
    S += A[i] * B[i]
print(S)
