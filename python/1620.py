import sys

N , M = map(int,sys.stdin.readline().split())

pokemon = {}
number = {}
for i in range(N):
    name = sys.stdin.readline().rstrip()
    pokemon[name] = i+1
    number[str(i+1)] = name


for i in range(M):
    prob = sys.stdin.readline().rstrip()
    if prob.isdigit():
        print(number[prob])
    else:
        print(pokemon[prob])