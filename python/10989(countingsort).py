import sys

n = int(sys.stdin.readline().rstrip())



arr=[int(sys.stdin.readline().rstrip()) for i in range(int(input()))]

count = [0] * (10001)

for num in arr:
    count[num] += 1
    
for i in range(1, len(count)):
    count[i] += count[i-1]

result = [0] * (len(arr))

for num in arr:
    idx = count[num]
    result[idx - 1] = num
    count[num] -= 1

print(result)