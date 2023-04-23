import sys


N = int(sys.stdin.readline().rstrip())

numbers = list(map(int,sys.stdin.readline().split()))
stk = []
answer = [-1 for _ in range(N)]


stk.append(0)

for i in range(1,N):
    while stk and numbers[stk[-1]] < numbers[i]:
        answer[stk.pop()] = numbers[i]
    stk.append(i)

print(*answer)
'''
for i in range(N):
    max = numbers[i]
    for j in range(N-i-1):
        pop = numbers.pop()
        print(numbers)
        if pop > max:
            stk.append(pop)
    for _ in range(len(stk)):
        clear = stk.pop()
        numbers.append(clear)
        
    answer.append(clear)
    
print(answer)
'''