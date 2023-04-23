import sys


def frontback(str , left , right):
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def pell(str , left , right):
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            front = frontback(str,left+1,right)
            back = frontback(str,left,right-1)
            if front or back :
                return 1
            else:
                return 2
    return 0

n = int(sys.stdin.readline().rstrip("\n"))

i=0

for i in range(n):
    str = sys.stdin.readline().rstrip("\n")
    left = 0
    right = len(str)-1
    flag = pell(str,left,right)
    print(flag)