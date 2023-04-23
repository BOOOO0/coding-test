import sys
# readline을 사용하면 rstrip을 쓸 수 없어서 엔터가 들어간다
sick = input().split('-')
num = []

# 더해지는 숫자들을 다 괄호로 묶어서 합친 다음에
# 빼게 만들면 식의 최솟값을 만들 수 있다

for s in sick:
    cnt = 0
    add = s.split('+')
    for a in add:
        cnt += int(a)
    num.append(cnt)
# 더해지는 애들은 이미 다 더해져서 num에 들어간다
# 빼져야 하는 숫자들은 빼기 전에 num에 들어간다
# 각각을 순서대로 다 빼지게 만들면
# 최솟값이 나온다
n = num[0]
for i in range(1,len(num)):
    n -= num[i]
print(n)