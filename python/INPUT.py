import sys

"""
"""
# input()사용
"""
#공백으로 구분 된 데이터를 리스트로 받을 때

data = list(map(int , input().split()));

#공백으로 구분 된 데이터를 각각 받을 때

a,b,c = map(int , input().split());

"""
# readline() 사용
"""



# 공백없는걸 하나씩 나눠서 저장하려면 그냥 rstrip으로 한줄을 그대로 받아서 map하면 된다
# split을 하면 오히려 나눠지지 않는다
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]








# 입력으로 딕셔너리 만들기 ( 전부다 문자열 이기 때문에 숫자쓰려면 맵핑 필요 )
n = int(sys.stdin.readline().rstrip())

dict = {}

for i in range(n):
    k_v = str(sys.stdin.readline().rstrip())
    k_v = k_v.split()
    key = k_v[0]
    value = k_v[1]
    dict[key] = value

print(dict)

# set 입력받기

A = set(map(int,sys.stdin.readline().split()))

#set 한줄씩 입력받아서 넣기
S = set()

for i in range(N):
    S.add(sys.stdin.readline().rstrip())

#공백으로 구분 된 숫자 리스트 입력 받기
arr = list(map(int,sys.stdin.readline().split()))

#공백으로 구분 된 2개 숫자 입력 받기
N, M = map(int,sys.stdin.readline().split())

#2차원 리스트 N x N 입력 받기 (List comprehension) N x N 아니여도 됨 각 행마다 리스트 길이 자유
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

#문자열 입력 받기 (끝에 엔터 지우기?)
data = sys.stdin.readline().rstrip()

#2751번 빠른 입력 한 줄 씩 숫자 입력받아 리스트에 넣기

for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

# 동일 문제 list_comprehension 사용 출력까지 stdout 빠른 출력

array=[int(sys.stdin.readline().rstrip()) for i in range(int(input()))]

for i in array:
    sys.stdout.write(str(i)+'\n')
    
# stdout 은 자동 개행 없음 자료형도 정해줘야함

"""
