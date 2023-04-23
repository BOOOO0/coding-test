import sys



N = int(sys.stdin.readline().rstrip())

rooms = [ list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# https://suri78.tistory.com/26
# 시작시간까지도 오름차순으로 정렬해야 하는 이유 반례 있음

rooms.sort(key = lambda x : (x[1],x[0]))

# 회의는 시간과 관계없이 최소 1개는 열리게 되어있다
cnt = 1

endTime = rooms[0][1]



for i in range(1,N):
    if rooms[i][0] >= endTime:
        cnt+=1
        endTime = rooms[i][1]
        
print(cnt)
