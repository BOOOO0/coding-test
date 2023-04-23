import sys

N , M , R = map(int , sys.stdin.readline().split())


arr = [list(map(int , sys.stdin.readline().split())) for _ in range(N)]

for _ in range(R):
    # 바깥 포문은 안쪽으로 한 층씩 들어가면서 한 층씩 돌리기 위한 것
    for i in range(min(N ,M) // 2):
        x, y = i, i
        value = arr[x][y]
        
        for j in range(i + 1 , N - i):
            x = j 
            prev_value = arr[x][y]
            arr[x][y] = value
            value = prev_value
        
        for j in range(i + 1 , M - i):
            y = j
            prev_value = arr[x][y]
            arr[x][y] = value
            value = prev_value
            
        for j in range(i + 1 , N - i):
            x = N - j - 1
            prev_value = arr[x][y]
            arr[x][y] = value
            value = prev_value
            
        for j in range(i + 1 , M - i):
            y = M - j - 1
            prev_value = arr[x][y]
            arr[x][y] = value
            value = prev_value
            
for i in arr:
    print(*i)