import sys

pell_list = []  

n = int(input())   


for i in range(n):  
    data = sys.stdin.readline().rstrip()    
    pell_list.append(data)                 

def pell (list):
    front = False
    back = False
    for str in list:
        ax = len(str) // 2
        i=0
        for i in range(ax):
            j=0
            if str[i] != str[len(str)-1]:
                for j in range(ax-i)
            else :
    
    
    
print(pell(pell_list))     
