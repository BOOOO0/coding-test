import sys
import heapq

N = int(sys.stdin.readline().rstrip())

leftheap = []
rightheap = []

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap,(-num,num))
    else:
        heapq.heappush(rightheap,(num,num))
    
    if rightheap and leftheap[0][1] > rightheap[0][1]:
        rightMin = heapq.heappop(rightheap)[1]
        leftMax = heapq.heappop(leftheap)[1]
        heapq.heappush(leftheap,(-rightMin,rightMin))
        heapq.heappush(rightheap,(leftMax,leftMax))
        
    print(leftheap[0][1])