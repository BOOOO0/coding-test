import sys

N = int(sys.stdin.readline().rstrip())

times = list(map(int,sys.stdin.readline().split()))

times.sort()
sum = 0
for i in range(N):
    sum += times[i]
    for j in range(i):
        sum += times[j]
        
print(sum)