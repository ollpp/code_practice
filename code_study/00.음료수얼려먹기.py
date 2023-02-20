import sys
from collections import deque


sys.stdin = open('../input_data/00.음료수얼려먹기.txt', 'r')


n, m = map(int, sys.stdin.readline().split())

A = []

for i in range(n):
    tmp = list(map(int, input()))
    A.append(tmp)
    
visited = [[False]*m for _ in range(n)]

def dfs(x, y):
    if visited[x][y]:
        return False
    else:
        if x>=0, y>=0, x<n, y<m:
            visited[x][y] = True
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            return True


