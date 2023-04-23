import sys

a,b,v = map(int, input().split())
'''
day = 1
sum = 0

while True :
    sum += a
    day += 1
    if v > sum :
        sum -= b
    else :
        break
    
print(day)
'''

print((v-b-1)//(a-b) +1)