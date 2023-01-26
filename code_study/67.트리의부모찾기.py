import sys

sys.stdin = open('../input_data/67.트리의부모찾기.txt', 'r')

n = int(sys.stdin.readline())

g = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = [False] * (n+1)

for _ in range(n-1):
    s, e = map(int, sys.stdin.readline().split())

    g[s].append(e)
    g[e].append(s)

def dfs(x):
    visited[x] = True

    for i in g[x]:
        if not visited[i]: 
            answer[i] = x
            dfs(i)

dfs(1)

for i in range(1, n):
    print(answer[i+1])