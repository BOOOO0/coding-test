import sys


N, S = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

stk = []
result = 0


def DFS(idx, sum):
    global result
    if idx >= N:
        return
    sum += arr[idx]
    if sum == S:
        result += 1
    print(sum, "prev")
    DFS(idx + 1, sum - arr[idx])
    print(sum, "next")
    DFS(idx + 1, sum)
    print(sum, "last")


DFS(0, 0)
print(result)


# def DFS():
#     global result
#     if len(stk) > 0 and sum(stk) == S:
#         result += 1
#         print(stk)
#         return
#     for i in range(1, len(arr)):
#         if arr[i] not in stk:
#             stk.append(arr[i])
#             DFS()
#             stk.pop()


# DFS()
# print(result)
