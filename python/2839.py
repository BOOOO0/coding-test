import sys
'''
n = int(input())
if ((n % 5) % 3 != 0) and n%3 ==0 :
    b3 = n//3
    print(b3)
elif ((n % 5) % 3 != 0) or (n < 3) or (n>3 and n<5):
    print(-1)
else:
    b5 = n // 5
    b3 = (n%5)//3
    print(b5+b3)
    # 반례 11
'''
n = int(input())

cnt = 0

while True:
    if n%5 == 0:
        print(cnt+n//5)
        break
    n-=3
    cnt+=1
    if n==0:
        print(cnt)
        break
    if(n<0):
        print(-1)
        break
