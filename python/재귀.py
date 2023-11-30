from collections import *

# [5, 4, 3, 2, 1]로 콜 스택에 담겨있다.
# 1일 경우 return 1 이므로 1이 반환된다.
# 2는 1의 결과 1과 자기 자신을 곱한 2x1을 반환한다.
# 3은 2의 결과 2x1과 자기 자신을 곱한 3을 반환한다.
# 결국 마지막 n은 1부터 n-1까지를 곱한 값과 자기 자신을 곱한 값을 반환하므로
# 팩토리얼 완성

def factorial (n):
    print(n)
    if n <= 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))