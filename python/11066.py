import sys

T = int(sys.stdin.readline().rstrip())



for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    sum = [0 for _ in range(N+1)]
    dp = [ [ 0 for _ in range(N+1)]   for _ in range(N+1)  ]
    numbers = [0] + list(map(int,input().split()))
    # 누적합 만들어두고
    for i in range(1,N+1):
        sum[i] = sum[i-1] + numbers[i]
    
    for i in range(2,N+1):
        for j in range(1,N+2-i):
            