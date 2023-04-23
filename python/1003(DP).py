# DP 동적 프로그래밍
# 메모리를 늘려서 시간을 단축시키는 알고리즘
# 미리 0, 1, 2 의 0 호출 수 1 호출 수를 리스트로 만들어 둔다
# 그 다음 3의 호출 수 부터 계산을 시작해서 N 까지의 호출 수를 계산한다
# 미리 테스트를 할 리스트를 생성하는 것이 계산 시간 단축을 만드는 듯하다

'''

가장 기본적인 DP 예시

d = [0] * 100

d[1] = 1 # 첫 번째 항
d[2] = 1 # 두 번째 항
N = 99   # 피보나치 수열의 99번째 숫자는?

for i in range(3, N+1):
    d[i] = d[i-1] + d[i-2]

print(d[N])
'''
import sys
  
  
  
n = int(sys.stdin.readline().rstrip())


zero = [1,0,1]
one = [0,1,1]




def pbo_cal (N):
    if len(zero) <= N:
        # 입력 숫자가 3일때 부터
        # 그러니까 3의 피보나치 수열을 구할 때 부터
        # 이 조건문이 동작을 시작하는데 len(zero)가 3 이기 때문에
        # 조건문 동작 횟수를 생각해보면 
        # N+1 을 해야 3을 구할 때 한번 반복문 수행하고 답 출력
        # 이런 조건으로 짠 코드이다
        for i in range(len(zero), N+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    sys.stdout.write(str(zero[N]) + " " + str(one[N]) + "\n")
    
for i in range(n):
    k = int(sys.stdin.readline().rstrip())
    pbo_cal(k)