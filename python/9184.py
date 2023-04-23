import sys

# 000 100 010 001 110 011 은 1번 조건에 따라서 1을 return
# 이것을 사용해서 DP 알고리즘 수행
# ex) 111 은 1 + 1 + 1 -1 로 2를 출력
DP = [[[0]*(21) for _ in range(21)] for _ in range(21)]


def W (a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return W(20,20,20)
    # 값이 이미 존재한다면 바로 리턴한다
    # 큰값 처리 시간단축요소
    # if list[index] : 는 값이 0이 아니라면 조건문을 수행한다
    if DP[a][b][c]:
        return DP[a][b][c]
    if a<b and b<c:
        DP[a][b][c] = W(a,b,c-1) + W(a,b-1,c-1) - W(a,b-1,c)
        return DP[a][b][c]
    DP[a][b][c] = W(a-1,b,c) + W(a-1,b-1,c) + W(a-1,b,c-1) - W(a-1,b-1,c-1)
    return DP[a][b][c]    

while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {W(a,b,c)}')
    


