import sys
from collections import deque

sys.stdin = open('../input_data/26.DFS와BFS.txt', 'r')

N, M, V = map(int, sys.stdin.readline().split())

dfs_list = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    f, e = map(int, sys.stdin.readline().split())

    dfs_list[f].append(e)
    dfs_list[e].append(f)

# 정렬
for i in dfs_list:
    i.sort()

def dfs(idx):

    print(idx, end=' ')
    visited[idx] = True

    for i in dfs_list[idx]:        
        if not visited[i]:
            dfs(i)

print()
dfs(3)



visited = [False] * (N+1)
q = deque()
q.append(3)

while q:
    temp = q.popleft()
    
    print(temp, end = ' ')
    visited[temp] = True

    for i in dfs_list[temp]:
        if not visited[i]:
            visited[i] = True
            q.append(i)    

