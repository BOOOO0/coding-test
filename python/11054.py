import sys

N = int(sys.stdin.readline().rstrip())

dpFront = [0 for _ in range(N)]
dpBack = [0 for _ in range(N)]
dpSum = [0 for _ in range(N)]

nums = list(map(int , sys.stdin.readline().split()))

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j] and dpFront[i] < dpFront[j] :
            dpFront[i] = dpFront[j]
    dpFront[i]+=1

for i in range(N-1 , -1 , -1):
    for j in range(N-1 , i , -1):
        if nums[i] > nums[j] and dpBack[i] < dpBack[j] :
            dpBack[i] = dpBack[j]
    dpBack[i]+=1
    
for i in range(N):
    dpSum[i] = dpFront[i] + dpBack[i] -1

print(max(dpSum))