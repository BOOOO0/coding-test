import sys

str = sys.stdin.readline().rstrip()

croatian = ['c=', 'c-' , 'dz=' , 'd-' , 'lj' , 'nj' , 's=' , 'z=']

i=0
cnt = 0
for i in range(8):
    if str.find(croatian[i]) != -1:
        cnt +=1
        str = str.replace(croatian[i],'.')

print(len(str))