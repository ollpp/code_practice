import sys
from collections import deque

sys.stdin = open('../input_data/28.트리지름구하기.txt', 'r')

n = int(sys.stdin.readline())

# 그래프 정보
A = [[] for _ in range(n+1)]

# bfs를 위한 q
# q = deque()

# visit 정보
visited = [False] * (n+1)
len_list = [0] * (n+1)

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    idx = 0
    head = data[idx]
    idx += 1
    while True:
        if data[idx] == -1:
            break
        # else : 
        v = data[idx+1]
        A[head].append((data[idx], v))
        idx+=2

# for i in range(n):
#     q.append(i)
print(A)



def bfs(x):
    
    q = deque()
    q.append(x)
    visited[x] = True
    
    while q:        
        now_node = q.popleft()
        for i in A[now_node]:

            if not visited[i[0]]:
                visited[i[0]] = True   
                q.append(i[0])
                len_list[i[0]] = len_list[now_node] + i[1]


bfs(1)
max = 1
for i in range(2, n+1):
    if len_list[max] < len_list[i]:
        max = i


visited = [False] * (n+1)
len_list = [0] * (n+1)
bfs(max)
len_list.sort()
print(len_list)
print(len_list[n])
