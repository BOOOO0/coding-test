import sys

N , M = map(int,sys.stdin.readline().split())

trees = list(map(int,sys.stdin.readline().split()))

first , last = 1 , max(trees)

while first <= last :
    mid = (first + last) // 2
    cnt = 0
    for tree in trees:
        if tree >= mid:

            cnt += tree - mid
        # 시간 단축 요소
        # cnt가 M 이상이라면
        # 나머지 나무들은 잘라보지 않고
        # 바로 다음 이분탐색으로 넘어가게 해준다
        # ex) 10을 4번 잘라보지 않고 10 한번 잘라보고 바로 다음 15 잘라보기로 넘어감
        if cnt > M:
            break
    if cnt >= M:
        first = mid + 1
    else:
        last = mid - 1
    
print(last)
        
        