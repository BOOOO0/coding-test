import sys



N = int(sys.stdin.readline().rstrip())

card = list(sys.stdin.readline().split())

M = int(sys.stdin.readline().rstrip())

check = list(sys.stdin.readline().split())

card.sort()

count = {}

for c in card:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

def Binary_Search(check, card, first, last):
    if first > last :
        return 0
    
    mid = (first + last) // 2
    
    if card[mid] == check:
        return count.get(check)
    elif card[mid] > check:
        return Binary_Search(check , card , first , mid -1)
    else:
        return Binary_Search(check , card , mid + 1 , last)
    
for chec in check:
    print(Binary_Search(chec , card , 0 , len(card)-1), end= ' ')