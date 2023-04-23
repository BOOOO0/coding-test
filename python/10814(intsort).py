import sys

n = int(sys.stdin.readline().rstrip())

nai = []

for i in range(n):
    n_n = str(sys.stdin.readline().rstrip())
    n_n = n_n.split()
    n_n[0] = int(n_n[0])
    n_n.append(int(i))
    nai.append(n_n)
    
nai.sort(key= lambda x : (x[0],x[2]))

for i in range(n):
    sys.stdout.write(str(nai[i][0]) + " " +str(nai[i][1]) + "\n")

# string 정렬과 int정렬을 좀 다릅니다. 20 이 9보다 앞에 오는 이런 상황이 발생하기 때문

