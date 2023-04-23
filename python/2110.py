import sys

N , C = map(int,sys.stdin.readline().split())

houses = [ int(sys.stdin.readline().rstrip()) for _ in range(N)]

houses.sort()

first = 1
last = houses[-1] - houses[0]

# 집 간 거리를 이용하고 그리고 그것을 구하는 문제이다
answer = 0
while first <= last :
    mid = (first + last) // 2
    cnt = 1
    current = houses[0]
    
    for i in range(1,len(houses)):        
        if houses[i] >= current + mid:
            cnt += 1
            current = houses[i]
    
    if cnt >= C:        
        first = mid + 1
        answer = mid
    else:
        last = mid -1
        
print(answer)