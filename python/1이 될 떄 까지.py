import sys

N, K = map(int, sys.stdin.readline().split())


result = 0
# N을 K로 나눈 몫 * K 만큼 N에서 빼준 다음
target = (N // K) * K
result += N - target
while True:
    if N < K:
        break
    result += 1
    N //= K
# 마지막 남은 수에 대해서 1씩 빼기
result += N - 1
print(result)


# cnt = 0
# while True:
#     if N == 1:
#         break
#     elif N % K == 0:
#         N //= K
#         cnt += 1
#         continue
#     elif N > 1:
#         N -= 1
#         cnt += 1

# print(cnt)
