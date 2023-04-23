import sys

n = int(input())


# 1번 행의 분수 1 2 4 7 11 (1 2 3 4)

# 분자 분모의 합 2 3 4 5 6
# 에서 분자는 1씩 커지고 분모는 합 - 분자
cha = 1
num = 0
level = 1

while n > num:
    num += (level - 1)*cha +1
    level += 1  

num = num - ((level -2)*cha +1)

rest = n - num 

if (level - 2) % 2 == 0:
    a = level -1
    b = 1
    for i in range(rest-1):
        a -= 1
        b += 1
else:
    a = 1
    b = level -1
    for i in range(rest-1):
        a+=1
        b-=1
    
print("{}/{}".format(a,b))
