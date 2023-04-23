import sys

n = int(sys.stdin.readline().rstrip())

num_list = list(map(int,sys.stdin.readline().split()))

num_list.sort()

print(num_list[0] * num_list[n-1])