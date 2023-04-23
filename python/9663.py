import sys

N = int(sys.stdin.readline().rstrip())


# 1번 퀸을 배치했을 때 1번 퀸이 공격할 수 없는 자리 하나에 2번 퀸을 배치한다.
# 2번 퀸도 똑같이 2번 퀸이 공격할 수 없는 자리를 찾는다.
# 더이상 배치할 수 있는 퀸이 없으면 첫번째 DFS 재귀로 돌아간다.
# DFS()는 퀸의 좌표를 한번씩 담으면서 찾고 퀸을 배치할 자리가 더이상 없을 때
# 그 좌표를 담은 리스트의 길이를 리턴하고 돌아와서 list.pop()
# 1. 좌표 (0,0) 부터 시작 (0,0)에서 8방향 체크
# for문 8개가 필요



# 각 열의 인덱스와 할당해주는 값으로 좌표를 처리한다


ans = 0
row = [0] * N

def is_promising(x):
    for i in range(x):
        # row[x] 현재 검사하는 퀸 좌표값
        # row[x] == row[i] 면 같은 열에 있는것
        # abs(row[x] - row[i]) == abs(x - i) 라면 대각선에 위치한 것인데
        # 몇열 차이인지 == 몇행 차이인지 라면 대각선에 있다.
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == N:
        ans += 1
        return
    else:
        for i in range(N):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            # 여기서 False가 나오면 그냥 다음 반복문으로 증가된 i 넣는다
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
sys.stdout.write(str(ans))