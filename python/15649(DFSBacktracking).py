import sys
from itertools import permutations


N , M = map(int,sys.stdin.readline().split())

answer = []
'''
arr = []

def DFS():
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(1,N+1):
        if i not in arr:
            arr.append(i)
            DFS()
            arr.pop()

DFS()
'''
for i in range(N):
    answer.append(i+1)

nPm = list(permutations(answer , M))



for i in range(len(nPm)):
    print(' '.join(map(str,nPm[i])))