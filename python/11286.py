import sys
import heapq

N = int(sys.stdin.readline().rstrip())


hq = []

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num != 0 :
        heapq.heappush(hq,(abs(num),num))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)