import sys

class stack():
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()

N = int(sys.stdin.readline().rstrip())

stk = stack()

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        stk.pop()
    else:
        stk.push(num)
        
print(sum(stk.stack))