import sys

def GCD ( A , B ):
    if B == 0:
        return A
    return(GCD(B,A%B))

def LCM ( A , B ):
    answer = (A * B) // GCD(A,B)
    return answer


T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N , M = map(int,sys.stdin.readline().split())
    print(LCM(N,M))