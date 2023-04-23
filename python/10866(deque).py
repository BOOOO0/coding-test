import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

deq = deque()

def push_front(deq , num):
    deq.appendleft(num)

def push_back(deq , num):
    deq.append(num)

def pop_front(deq):
    if(len(deq) > 0):
        print(deq.popleft())
    else:
        print(-1)
def pop_back(deq):
    if(len(deq) > 0):
        print(deq.pop())
    else:
        print(-1)
    
def size(deq):
    print(len(deq))
    
def empty(deq):
    if(len(deq) > 0):
        print(0)
    else:
        print(1)

def front(deq):
    if(len(deq) > 0):
        print(deq[0])
    else:
        print(-1)

def back(deq):
    if(len(deq) > 0):
        print(deq[len(deq)-1])
    else:
        print(-1)

for i in range(N):
    str_num = list(map(str,sys.stdin.readline().split()))
    
    
    if str_num[0] == "push_front":
        push_front(deq , str_num[1])
    if str_num[0] == "push_back":
        push_back(deq , str_num[1])
    
    if str_num[0] == "pop_front":
        pop_front(deq)
    if str_num[0] == "pop_back":
        pop_back(deq)
    if str_num[0] == "size":
        size(deq)
    if str_num[0] == "empty":
        empty(deq)
    if str_num[0] == "front":
        front(deq)
    if str_num[0] == "back":
        back(deq)