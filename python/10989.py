import sys

n = int(sys.stdin.readline().rstrip())

count = [0] * (10001)

for i in range(n):
    count[int(sys.stdin.readline().rstrip())] +=1

#count list의 최대값까지가 인덱스의 범위라고 생각
#count list의 idx가 arr의 원소 num이고 count list의 원소는 해당 idx(arr의 num)의 갯수이다 

#for문에 대한 설명
#작은 수부터 큰 수 까지의 첫번째 포문
#두번째 포문은 그 해당 수의 갯수 만큼의 출력
for idx in range(10001):    
    for num in range(count[idx]):
        print(idx)