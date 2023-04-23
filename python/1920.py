import sys

def binarySearch (list , check):
    first = 0 
    last = len(list)-1
    
    flag = 0
    while(first <= last):
        mid = (first + last) // 2
        if list[mid] == check:
            flag = 1
            break
        else:
            if check < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if flag == 0:
        print(0)
    else:
        print(1)

N = int(sys.stdin.readline().rstrip())

n_numbers = list(sys.stdin.readline().rstrip().split())

M = int(sys.stdin.readline().rstrip())

m_numbers = list(sys.stdin.readline().rstrip().split())


n_numbers.sort()


for m in m_numbers:
    binarySearch(n_numbers  , m)

