import sys

# 아래 주석도 딱히 이해 안됐을 때 쓴거
# 이분탐색 알고리즘으로 입력되는 숫자들 802 743 457 539 들을
# 차례로 이분탐색 하다보면 
# 최적의 랜선 길이가 나온다 그리고 그게 end값이고
# 이분탐색 응용의 대표적인 문제이다 알아두자

K , N = map(int, sys.stdin.readline().split())

numbers = [ int(sys.stdin.readline().rstrip()) for _ in range(K)]

start , end = 1 , max(numbers)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    # 처음에 첫번쨰 mid로 랜선길이들을 한번씩 다 나눠본다
    # 그런데 자른 갯수가 N보다 많으면 이분탐색 start = mid + 1 
    # 숫자가 더 커져야 자르는 수가 적어지니까
    # 반대의 경우엔 반대로
    # 반복해서 최적의 길이 출력
    for num in numbers:
        cnt += num // mid
        
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
    print(end)
        
print(end)