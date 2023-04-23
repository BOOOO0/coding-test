import sys
from queue import PriorityQueue
import heapq

N = int(sys.stdin.readline().rstrip())


hq = []

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num > 0:
        heapq.heappush(hq,(-num))
    else:
        if hq :
            print(-1 * heapq.heappop(hq))
        else:
            print(0)

'''
que = PriorityQueue()

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num > 0:    
        que.put(num)
    else:
        # 파이썬 PriorityQueue 에 대해서 더 알아봐야겠다
        # 리스트를 활용하듯이 NULL이면 수행하게 조건문이 안되고
        # len으로 길이를 알수도없다
        if que :
            print(que.get())
        else:
            print(0)
'''