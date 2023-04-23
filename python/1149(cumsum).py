import sys 


N = int(sys.stdin.readline().rstrip())

#  0 은 R, 1은 G, 2는 B
rgb_cost = []

for i in range(N):
    rgb_cost.append(list(map(int,sys.stdin.readline().split())))
    
for i in range(1,N):
    rgb_cost[i][0] = min(rgb_cost[i-1][1] , rgb_cost[i-1][2]) + rgb_cost[i][0]
    rgb_cost[i][1] = min(rgb_cost[i-1][0] , rgb_cost[i-1][2]) + rgb_cost[i][1]
    rgb_cost[i][2] = min(rgb_cost[i-1][0] , rgb_cost[i-1][1]) + rgb_cost[i][2]

print(min(rgb_cost[N-1][0] , rgb_cost[N-1][1] , rgb_cost[N-1][2]))
