import sys

n = int(input())

def fact (n):
    if n==0:
        return 1
    answer = n
    sum = answer * fact(n-1)
    return sum

print(fact(n))