import sys


'''
이 문제는 backtracking 문제를 DFS에 비유하면서 이해하기 위해서 주석을 달았음
'''
N , M = map(int,sys.stdin.readline().split())

arr = []

def DFS(start):
    # DFS에서의 True 체크하는 느낌인데 조건을 달아서 조건을 만족하면 출력
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        # 재귀함수 반복을 위한 return
        return
    #간선 리스트 탐색과 비슷
    for i in range(start,N+1):
        #아직 방문하지 않아서 False라면 
        if i not in arr:
            arr.append(i)
            DFS(i+1)
            arr.pop()

DFS(1)
