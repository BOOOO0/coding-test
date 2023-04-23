import sys

N, K = map(int, sys.stdin.readline().split())

cnt = 0

while bin(N).count("1") > K:
    # 2진수로 만든 N을 거꾸로 뒤집어서
    # 1의 수가 K개 이하로 될때까지 2**idx 더해준다
    idx = bin(N)[::-1].index("1")
    cnt += 2**idx
    N += 2**idx

print(cnt)



