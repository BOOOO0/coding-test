import sys

X , Y , W , H = map(int,sys.stdin.readline().split())

updown = (H - Y)
leftright = (W - X)


# 탈출 방향은 상하 좌우
# 0,0 에서 w,h 까지 직사각형 안에 x,y는
# 좌방향 x 하방향 y 상방향 h-y 우방향 w-x 이기 때문에 x,y도 비교에 넣어야한다
    
print(min([X,Y,updown,leftright]))