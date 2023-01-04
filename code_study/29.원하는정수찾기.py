import sys

sys.stdin = open('../input_data/29.원하는정수찾기.txt', 'r')

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

M = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))



for i in range(M):
    find = False    
    target = m_list[i]
    start = 0
    end = N-1

    while start <= end:
        idx = int((start + end) / 2) 
        mid = a[idx]

        if target < mid :
            end = idx - 1
        
        elif target > mid :
            start = idx + 1

        else :
            find = True
            break
        
    if find :
        print(1)
    else : 
        print(0)