import sys
from collections import deque
# N이 1일수도 있기 때문에 deque를 사용한 pop,popleft 로 처음과 끝값 가지기는 힘들듯

N = int(sys.stdin.readline().rstrip())

nums = list(map(int,sys.stdin.readline().split()))

sums = [nums[0]]

for i in range(N-1):
    # sums는 i+1번쨰 까지의 누적합을 가지면서 인덱스가 증가한다고 볼 수 있다
    # 그런데 그 누적합보다 nums의 i+1번째 숫자가 크다면 nums의 숫자를 sums 리스트에 추가한다
    # 연속된 숫자의 합과 입력받은 숫자들 중 큰값을 모아 저장한 리스트의 최대값이 문제에서 원하는 답이다
    sums.append( max(sums[i] + nums[i+1] , nums[i+1] ) ) 


print(max(sums))