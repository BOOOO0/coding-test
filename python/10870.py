n = int(input())

def pbo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    answer = n
    sum = pbo(n-1) + pbo(n-2)
    return sum

print(pbo(n))