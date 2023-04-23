import sys

    
N , M , R = map(int,sys.stdin.readline().rstrip().split())

edge = [[] for _ in range(N+1)]
d_check = [False for _ in range(N + 1)]

edge_count = [0 for _ in range(N+1)]

for _ in range(M):
    v1 , v2 = map(int,sys.stdin.readline().rstrip().split())
    edge[v1].append(v2)
    edge[v2].append(v1)
    
for e in edge:
    e.sort()
    
cnt = 1

stk = []
stk.append(R)

while stk:
    x = stk.pop()
    d_check[x] = True
    if edge_count[x] == 0:
        edge_count[x] = cnt
        cnt+=1
    
    for y in edge[x]:
        if not d_check[y]:
            stk.append(y)

for c in edge_count[1:]:
    print(c)