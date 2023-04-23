import sys

def fact (n):
    if n==0:
        return 1
    return n * fact(n-1)


N , K = map(int , sys.stdin.readline().split())

# 0< N < 10 0< K <N

print( (fact(N)) // ((fact(K) * fact(N-K))) )