import sys

class stack():
    def __init__(self) :
        self.stack = []
        
    def push(self,item):
        self.stack.append(item)
        
    def pop(self):
        if len(self.stack) != 0:
            print(self.stack.pop())
        else:
            print(-1)
        
    def size(self):
        print(len(self.stack))
        
    def empty(self):
        if len(self.stack) == 0:
            print(1)
        else:
            print(0)
            
    def top(self):
        if len(self.stack) != 0:
            print(self.stack[-1])
        else:
            print(-1)
    

N = int(sys.stdin.readline().rstrip())
    
stk = stack()

for _ in range(N):
    str_num = list(map(str , sys.stdin.readline().split()))
    
    if str_num[0] == "push":
        stk.push(str_num[1])
    if str_num[0] == "pop":
        stk.pop()
    if str_num[0] == "size":
        stk.size()
    if str_num[0] == "empty":
        stk.empty()
    if str_num[0] == "top":
        stk.top()

