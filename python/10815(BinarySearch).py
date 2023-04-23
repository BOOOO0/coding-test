import sys



def Binary_Search(check , cardN):
    first,last = 0,len(cardN)-1
    print_what = False   
    
    while first <= last:
        mid = (first + last) // 2
        if cardN[mid] == check:
            print_what = True
            break
        elif cardN[mid] > check:
            last = mid -1 
        elif cardN[mid] < check:
            first = mid +1
    if print_what == True:
        sys.stdout.write("1 ")
    else:
        sys.stdout.write("0 ")


N = int(sys.stdin.readline().rstrip())

cardNumber = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())

check = list(map(int,sys.stdin.readline().split()))

cardNumber.sort()

for i in range(len(check)):
    Binary_Search(check[i],cardNumber)


'''
answer = [0] * M

idx = 0

for whichN in whichNumber:
    if whichN in cardNumber:
        answer[idx] = 1
    idx+=1
        
        
for i in range(M):
    sys.stdout.write(str(answer[i])+" ")
'''