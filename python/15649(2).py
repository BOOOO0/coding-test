import sys

N, M = map(int, sys.stdin.readline().split())

stk = []


def DFS():
    # 스택의 길이가 M과 같다면
    if len(stk) == M:
        # 완성된 조합을 출력하고 return해서 이전에 호출된 함수로 돌아간다
        print(" ".join(map(str, stk)))
        return
    for i in range(1, N + 1):
        if i not in stk:
            stk.append(i)
            # 다음 depth로
            DFS()
            # 다음 depth로 갔으나 유망성이 없는 경우 뒤로 돌아가거나 더 나아갈 depth가
            # 없을때 돌아오기 위해서 stk.pop()
            stk.pop()
