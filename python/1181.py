import sys

n = int(sys.stdin.readline().rstrip())

words=[]

for i in range(n):
    words.append(str(sys.stdin.readline().rstrip()))

#set으로 만들면 중복 삭제
words = list(set(words))

words.sort(key= lambda x : (len(x),x))



for i in range(len(words)):
    sys.stdout.write(str(words[i])+'\n')