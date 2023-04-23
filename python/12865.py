import sys


# knapsack 알고리즘


N , K = map(int,sys.stdin.readline().split())


stuff = [[0,0]]

# 물건 무게 x 물건 개수
# knapsack[stuff][weight]
knapsack = [ [0 for _ in range(K+1)] for _ in range(N+1) ]

for _ in range(N):
    stuff.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,N+1):
    for j in range(1,K+1):
        weight = stuff[i][0]
        value = stuff[i][1]
        
        if j < weight:
            # 메모이제이션?
            # 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다
            knapsack[i][j] = knapsack[i-1][j]
        else:
            # 설명 블로그에 나오는 표를 만들기 위함인데 그 표가 어떻게 이 문제를 해결하는 알고리즘인가
            # 배낭에 물건의 가치를 비교하면서 가치가 최대이면서 배낭 무게에 맞는 물건들을 고르게 한다
            # 현재 넣을 물건의 무게만큼 배낭에서 뺀다 그리고 현재 물건을 넣는다
            # or
            # 현재 물건을 넣지않고 이전 배낭 그대로 가지고 간다
            # j-weight가 최종적으로 가방 무게에서 그 물건을 넣기 전 가치 value를 더하면 넣은 후 가치
            # 그것과 그 물건을 고려하기 전 knapsack[i-1][j] 의 가치와 비교해서
            # 마지막 N번째 물건을 가방 무게 j 까지 비교해보고 나온 결론이 답
            knapsack[i][j] = max( value + knapsack[i-1][j-weight] , knapsack[i-1][j] )
            
print(knapsack[N][K])