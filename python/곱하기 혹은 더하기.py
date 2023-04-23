# 0이 아니라면 무조건 곱하고 0이면 더한다

import sys


# S = sys.stdin.readline().rstrip()

# S_arr = list(map(str, S))

# result = 0

# result += int(S_arr[0])


# for i in range(1, len(S_arr)):
#     if result == 0 or S_arr[i] == 0:
#         result += int(S_arr[i])
#     else:
#         result = result * int(S_arr[i])


# print(result)

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
