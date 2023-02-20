import sys

sys.stdin = open('../data/최대부분증가수열.txt', 'r')

n = int(sys.stdin.readline())

real_list = list(map(int, sys.stdin.readline().split()))
real_list.insert(0, 0)
l_list = [0]*(n+1)
l_list[1] = 1
res = 0

for i in range(2, n+1):
    max = 0
    for j in range(i-1,0,-1):
        if real_list[j] < real_list[i] and l_list[j] > max :
            max = l_list[j]
        
    l_list[i] = max + 1
    
    if l_list[i] > res:
        res = l_list[i] 

print(res)