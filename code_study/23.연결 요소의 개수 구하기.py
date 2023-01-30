# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6

import sys
# sys.stdin = open('../input_data/14.절대값 힙 구현.txt', 'r')
sys.stdin = open('../input_data/23.연결요소개수구하기.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

# print(n, m)

node_list = [[] for _ in range(n)]

for i in range(m):
    s, e = map(int, sys.stdin.readline().split()) 
    node_list[s-1].append(e-1)

chk_list = [False] * n

# print(chk_list)

def dfs(v):
    chk_list[v] = True
    
    for i in node_list[v]:
        if not chk_list[i]:
            dfs(i)

cnt = 0
for i in range(n):
    if chk_list[i] == False:
        dfs(i)
        cnt += 1
    
print(cnt)