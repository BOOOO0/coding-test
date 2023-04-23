import sys


while True:
    lines = list(map(int,sys.stdin.readline().split()))
    long = max(lines)
    lines.remove(long)
    if sum(lines) == 0:
        break
    if (long **2) == (lines[0] ** 2) + (lines[1] **2 ):
        print("right")
    else:
        print("wrong")
