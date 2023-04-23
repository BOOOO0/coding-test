import sys

def GCD ( N , M ):
    while M > 0:
        N , M = M , N % M
    return N
def GCD_Recursion (N , M):
    if M == 0:
        return N
    return GCD_Recursion(M , N % M)

def LCM ( N , M ):
    result = (N * M) // GCD(N,M)
    return result


N , M = map(int , sys.stdin.readline().split())

factor = GCD(N,M)
multiple = LCM(N,M)

print(factor,multiple)

