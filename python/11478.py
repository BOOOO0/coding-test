import sys

str = sys.stdin.readline().rstrip()

answer = set()

for i in range(len(str)):
    for j in range(i,len(str)):
        answer.add(str[i:j+1])

print(len(answer))