import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
'''
for _ in range(T):
    N , M = map(int, sys.stdin.readline().split())
    deq = deque(input().split())
    zero = deq[0]
    cnt = 0
    order =deque()
    for _ in range(N):
        order.append(0)
    order[M] = 1
    while True:
        if zero < max(deq):
            deq.rotate(-1)
            order.rotate(-1)
            zero = deq[0]
            cnt += 1
        if zero == max(deq) :
            if order[0] == 1:
                print(cnt)
                break
            else:
                deq.rotate(-1)
                order.rotate(-1)
                    
'''

for _ in range(T):
    N , M = map(int, sys.stdin.readline().split())
    queue = list(map(int,input().split()))
    idx = [0 for i in range(N)]
    idx[M] = 1
    
    order = 0
    
    for q in queue:
        if q == max(queue):
            order += 1
            
            if idx[0] == 1:
                print(order)
                break
            else:
                queue.pop(0)
                idx.pop(0)
        else:
            queue.append(queue.pop())
            idx.append(idx.pop())



