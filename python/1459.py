import sys

X , Y , W , S = map(int , sys.stdin.readline().split())



distance = X + Y

maxx = max(X,Y) 

minn = min(X,Y)

way1 = distance * W

if distance % 2 == 0:
    way2 = maxx * S
else:
    way2 = (maxx-1) * S + W 
    
way3 = (minn * S) + ( (maxx - minn) * W )

answer = min(min(way1,way2),way3)

print(answer)
            
