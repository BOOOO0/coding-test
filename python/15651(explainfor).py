import sys

N , M = map(int,sys.stdin.readline().split())

arr = []

# DFS 반복문에서 처음에 (1,) 그리고 재귀호출로 
# 2번쨰 DFS() 에서 (1,1) 3번쨰 DFS()에서 길이 충족으로 print 하고 return
# 그리고 두번째 DFS로 돌아가면 arr.pop() 첫번쨰 DFS로 돌아가면 또 arr.pop()
# 하고나면 for문은 i값 1을 가지고 돌아가서 그다음 2가 arr.append() 그 후 또 새로운 두번쨰 DFS()
# 아래는 설명글
# 이 때, 원래 가지고 있던 i값이 그대로 유지됩니다. 5번 시점에서 i가 2였죠? lst는 [1, 2]고요.
# 그러면 13번 줄에서 lst의 2가 제거된 후 for문은 i를 3으로 만들어줍니다.
# https://www.acmicpc.net/board/view/84354
# 
def DFS():
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return
    for i in range(1,N+1): 
        arr.append(i)
        DFS()
        arr.pop()
            

DFS()
